# SL? Are you DTL?

This is a Discord bot that mercilessly pings people when playing League of
Legends.

## Developing Locally

1. Install [Poetry](https://python-poetry.org/).
2. Install dependencies. `poetry install`
3. Put secrets in `.env`.
4. Run the server. `poetry run python -m dtl.bot`
5. If you want to make commits, please install the precommit hooks.
   `poetry run pre-commit install`

## Deploying on Heroku

1. Make a new app.
2. Enable worker dynos.
3. Add the buildpacks here: https://github.com/moneymeets/python-poetry-buildpack
4. Add `BOT_TOKEN` in the config vars.
5. Link the app with the repo.
6. To check logs, you can use Heroku's CLI: `heroku logs -a your-app-name-here -t`
