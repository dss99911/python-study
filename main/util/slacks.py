# https://pypi.org/project/slackclient/
# pip install slack_sdk


def send_slack_message(channel, message):
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    client = WebClient(token='{token}')

    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(f"Got an error: {e.response['error']}")


def send_slack_message_to_url(text, url="https://hooks.slack.com/services/00000/000000"):
    import requests
    payload = {
        "text": text
    }
    requests.post(url, json=payload)


def send_slack_file(channel, filename, content):
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    client = WebClient(token='{token}')

    try:
        return client.files_upload(
            content=content,
            filename=filename,
            channels=channel
            )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        print(f"Got an error: {e.response['error']}")