---
title: deep_research
app_file: app.py
sdk: gradio
sdk_version: 6.14.0
---

# Deep Research Agent

An AI-powered research assistant that takes a topic, plans a set of targeted web searches, runs them, and synthesizes the findings into a written report — then optionally emails it to you.

## How it works

1. **Plan** — a planner agent breaks your query into multiple targeted search terms
2. **Search** — a search agent runs each query and summarizes the results
3. **Write** — a writer agent synthesizes all findings into a structured report
4. **Deliver** — an email agent sends the final report to your inbox

Built with the OpenAI Agents SDK, orchestrating four specialized agents that hand off work to each other.

## Tech Stack

- Python, `openai-agents` SDK
- Gradio for the UI
- SMTP for email delivery

## Running locally

```bash
pip install -r requirements.txt
python app.py
```

Set the following environment variables (e.g. in a `.env` file):

- `OPENAI_API_KEY`
- `EMAIL_ADDRESS`, `EMAIL_SMTP_SERVER`, `EMAIL_APP_PASSWORD` (for report delivery)
- `HOW_MANY_SEARCHES` (optional, defaults to 5)
- `DEFAULT_MODEL_NAME` (optional, defaults to `gpt-5.4-mini`)
