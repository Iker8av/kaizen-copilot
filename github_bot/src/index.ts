import { Probot } from "probot";

export default (app: Probot) => {
  app.on("issues.opened", async (context) => {
    const issue = context.payload.issue;
    // const repo = context.payload.repository;

    // Example: log issue title and body
    app.log.info(`New issue opened: ${issue.title}`);
    app.log.info(`Issue body: ${issue.body}`);
    issue.labels &&
      issue.labels?.length > 0 &&
      app.log.info(`Issue labels: ${issue.labels[0].name}`);
    // const issueComment = context.issue({
    //   body: "Thanks for opening this issue!",
    // });
    // await context.octokit.issues.createComment(issueComment);
  });
  // For more information on building apps:
  // https://probot.github.io/docs/

  // To get your app running against GitHub, see:
  // https://probot.github.io/docs/development/
};
