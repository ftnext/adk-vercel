# adk-vercel
EXPERIMENTAL

## Deploy to Vercel

1. Fork this repository: <https://github.com/ftnext/adk-vercel>
2. [Connect the forked repository to Vercel](https://vercel.com/docs/git).
3. Set `GOOGLE_API_KEY` as an [environment variable](https://vercel.com/docs/environment-variables) for the Production environment.
4. **Create Deployment**

## Example request

This is the example used in the YouTube video:

```shell
curl https://adk-vercel-experiment.vercel.app/run \
  --json '{"appName": "blogger", "userId": "user", "sessionId": "s01", "newMessage": {"role": "user", "parts": [{"text": "Top 3 use cases for AI agents"}]}}'
```

I recommend that the deployment was deleted after its behavior was verified.
