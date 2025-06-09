import { Probot } from "probot";
import axios from "axios";

interface FixIssuePayload {
  title: string;
  description: string;
  repo_url?: string;
}

export default (app: Probot) => {
  app.on("issues.opened", async (context) => {
    // Repo Information
    const owner = context.payload.repository.owner.login;
    const repo = context.payload.repository.name;
    const branch = "main";
    const installationId = context.payload.installation?.id;

    // Instatiate octokit with additional authentication
    const octokit = await app.auth(installationId);

    // Pull Request information
    const issue = context.payload.issue;
    const issue_number = issue.number;
    const pullrequest_title = issue.title + " - Kaizen Solution.";

    // Generate unique branch name
    const fileSafe = new Date()
      .toISOString()
      .slice(0, 16)
      .replace(/[-:T]/g, "_")
      .replace(/(\d{8})(\d{4})/, "$1_$2");
    const new_branch = "kaizen_fix_" + fileSafe;

    // Check if Kaizen label is present
    const Kaizen_tag = issue.labels?.some((label) => label.name === "Kaizen");

    if (Kaizen_tag) {
      //Call API
      const payload: FixIssuePayload = {
        title: issue.title,
        description: issue.body ?? "",
        repo_url: issue.repository_url,
      };

      try {
        const response = await axios.post(
          "http://127.0.0.1:5000/fix_issue",
          payload
        );
        console.log("Response:", response.data);

        const diff = response.data;

        // Context Received from API

        const file_path = diff.path_code?.split("/").at(-1);

        // file_content has to be encoded with base64
        const file_content = Buffer.from(diff.fixed_code, "utf-8").toString(
          "base64"
        );

        const pullrequest_body = "Testing PR" + "\n Fixes #" + issue_number;
        const commit_message = "";

        try {
          //1. Get the latest commit SHA of the main branch
          const { data: refData } = await octokit.git.getRef({
            owner,
            repo,
            ref: `heads/${branch}`,
          });

          const baseSha = refData.object.sha;

          // 2. Create a new branch from main
          await octokit.git.createRef({
            owner,
            repo,
            ref: `refs/heads/${new_branch}`,
            sha: baseSha,
          });

          // 3. Get the current file content and SHA
          const response = await octokit.repos.getContent({
            owner,
            repo,
            path: file_path,
            ref: branch,
          });

          var fileSha = "";

          if (!Array.isArray(response.data)) {
            fileSha = response.data.sha;
          }

          // 4. Update the file on the new branch
          await octokit.repos.createOrUpdateFileContents({
            owner,
            repo,
            path: file_path,
            message: commit_message,
            content: file_content,
            sha: fileSha,
            branch: new_branch,
          });

          // 5. Create a pull request
          const { data: pr } = await octokit.pulls.create({
            owner,
            repo,
            title: pullrequest_title,
            head: new_branch,
            base: branch,
            body: pullrequest_body,
          });

          console.log("Pull request created:", pr.html_url);
        } catch (error) {
          console.error("Error creating PR:", error);
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          console.error("Axios error:", error.response?.data || error.message);
        } else {
          console.error("Unexpected error:", error);
        }
      }
    }
  });
};
