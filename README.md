# Twilio Computer Vision App
A simple computer vision app that can detect a chair, and which sends a text message letting the user know when a chair has been detected.

## Requirements
- [alwaysAI account](https://alwaysai.co/auth?register=true)
- [alwaysAI CLI tools](https://dashboard.alwaysai.co/docs/getting_started/development_computer_setup.html)
- Create a [Twilio account](https://www.twilio.com/docs/sms/quickstart/node#install-nodejs-and-the-twilio-module) and get a Twilio phone number and an auth token

## Running
See [this page](https://alwaysai.co/docs/getting_started/working_with_projects.html) for documentation on setting up projects in the dashboard. See [this page](https://alwaysai.co/blog/building-and-deploying-apps-on-alwaysai) for details on building and running applications.

## Output
Once your alwaysAI application detects a chair, it should send you a text.

## Troubleshooting
- If you are having trouble connecting to your edge device, use the CLI configure command to reset the device. Please see [this page](https://alwaysai.co/docs/reference/cli_commands.html) for more details.
- Make sure you are logged in to the CLI. Verify with ```aai user show``` and log in with ```aai user login``` if not. 

## Support
Docs: https://dashboard.alwaysai.co/docs/getting_started/introduction.html
Community Discord: https://discord.gg/rjDdRPT
Email: support@alwaysai.co