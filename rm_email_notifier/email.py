import os

import boto3

from rm_email_notifier import models


def send(profile: models.Profile):
    ses_identity_arn = os.environ["AWS_SES_IDENTITY_ARN"]
    source_email = os.environ["SOURCE_EMAIL"]
    destination_email = os.environ["DESTINATION_EMAIL"]

    ses = boto3.client("ses")

    subject = f"Property Profile Matched: {profile.metadata.summary}"

    profile_data = profile.metadata.dict()
    profile_data["body"] = profile.text
    body_plain = "\n".join(
        f"{key.upper()}: {value}"
        for key, value in profile_data.items()
    )

    html_lines = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "  <head>"
        f"    <title>{profile.metadata.summary}</title>"
        "    <meta charset='utf-8'>"
        "  </head>"
        "  <body>"
        f" <a href=\"{profile.metadata.url}\">{profile.metadata.summary}</a>",
        "  <dl>",
        f"    <dt>Location</dt><dd>{profile.metadata.location}</dd>",
        f"    <dt>Price</dt><dd>{profile.metadata.price}</dd>",
        "  </dl>",
        "\n".join(f"  <p>{paragraph}</p>"
                  for paragraph in profile.text.split("\n")),
        "  </body>"
        "</html>"
    ]
    body_html = "\n".join(html_lines)

    ses.send_email(
        SourceArn=ses_identity_arn,
        Source=source_email,
        Destination={"ToAddresses": [destination_email]},
        Message={
            "Subject": {
                "Data": subject,
                "Charset": "utf-8",
            },
            "Body": {
                "Text": {
                    "Data": body_plain,
                    "Charset": "utf-8",
                },
                "Html": {
                    "Data": body_html,
                    "Charset": "utf-8",
                },
            }

        }
    )
