# Dockerfile Repair Lab (DevOps Foundation)

`incident-api` is a small Flask service. **The Python code is correct.** The Docker packaging is broken: the image does not build, and after you get it building, the container still does not start.

Your job: repair the packaging in three tasks, prove the API answers, and explain it in a video of at most 3 minutes. Full instructions are in the assignment on the platform.

## What the service should do

| Request | Expected response |
|---|---|
| `GET /health` | `200` with `{"status":"ok"}` |
| `GET /incidents` | `200` with a JSON list of 2 incidents and `"open":1` |

The app listens on `0.0.0.0:8080` inside the container.

## Rules

- Change only `Dockerfile` and `.dockerignore`. Do not edit `app.py`, `src/` or `requirements.txt`.
- Keep the base image family `python:3.12-slim`.
- Use Docker on your own machine. No cloud account, no paid tool.

## Start

```bash
# 1. Fork this repo on GitHub, then clone YOUR fork
git clone https://github.com/<your-username>/dockerfile-repair-lab-v2.git
cd dockerfile-repair-lab-v2
git switch -c fix/dockerfile-build

# 2. Reproduce the first failure
docker build -t incident-api:dev .
```

## Run and check (after your repairs)

```bash
docker rm -f incident-api 2>/dev/null
docker run -d --name incident-api -p 8080:8080 incident-api:dev
docker ps -a --filter "name=^incident-api$"
docker logs incident-api
curl -i http://localhost:8080/health
curl http://localhost:8080/incidents
```

Windows PowerShell: use `curl.exe` instead of `curl`, and skip `2>/dev/null` (run `docker rm -f incident-api` on its own; an error saying the container does not exist is fine).

## Clean up

```bash
docker rm -f incident-api
```
