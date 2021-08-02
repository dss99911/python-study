# https://pypi.org/project/slackclient/
# pip install slack_sdk
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_message(channel, message):
    client = WebClient(token='{token}')

    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(f"Got an error: {e.response['error']}")

def send_slack_file(channel, filename, content):
    client = WebClient(token='xoxb-342485334516-SHfa8toTlNBTgqlfzdfmaIPA')

    try:
        return client.files_upload(
            content=content,
            filename=filename,
            channels=channel
            )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(f"Got an error: {e.response['error']}")