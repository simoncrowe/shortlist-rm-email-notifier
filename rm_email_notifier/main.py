import fastapi

from rm_email_notifier import email, models

app = fastapi.FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/v1/profiles", status_code=201)
def email_profile(profile: models.Profile):
    email.send(profile)
