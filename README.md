# Property Email Notifier

A lightweight microservice that sends styled email notifications when property listing profiles are matched. Built with FastAPI and AWS SES.

## How It Works

A client POSTs property profile data (location, price, summary, URL, and description) to the REST API. The service composes a formatted HTML email and delivers it via AWS Simple Email Service.

```
Client → POST /api/v1/profiles → FastAPI → AWS SES → Inbox
```

## Running

```bash
# Install dependencies
poetry install

# Run locally
poetry run fastapi run rm_email_notifier/main.py

# Or with Docker
docker build -f docker/Dockerfile -t property-email-notifier .
docker run -p 8080:8080 \
  -e AWS_REGION=eu-west-1 \
  -e AWS_SES_IDENTITY_ARN=arn:aws:ses:... \
  -e SOURCE_EMAIL=notifications@example.com \
  -e DESTINATION_EMAIL=user@example.com \
  property-email-notifier
```

## Development

```bash
poetry install --with=dev
poetry run pytest
poetry run mypy .
poetry run flake8 --ignore=E501
```

## License

MIT
