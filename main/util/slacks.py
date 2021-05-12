# https://pypi.org/project/slackclient/
# pip install slackclient
from slack import WebClient
from slack.errors import SlackApiError

def send_slack_message(channel, message):
    client = WebClient(token="{token}")

    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(f"Got an error: {e.response['error']}")
if __name__ == '__main__':
    send_slack_message()