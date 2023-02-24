[![Tests Status](https://github.com/{name}/{repository}/actions/workflows/ci.yml/badge.svg?branch={branch})](https://github.com/{name}/{repository}/actions/workflows/ci.yml)

- add docker ci in github actions
- update `Makefile`
- add docker wasm

## Starting

1. rename `pyproject-example.toml` to `pyproject.toml` and edit it.
2. delete `vscode` if you dont need it or compare it with `.vscode`.
3. delete `github` folder or rename it to `.github`.
4. remove or replace LICENSE.
5. create `.venv` by using `poetry shell` or `poetry env use 3.11` commands.
6. exec `poetry update`, `poetry install`, `poetry lock` commands.
7. install pre-commits by `pre-commit install` command.
8. copy `.env.example` file and rename it to `.env`.
9. throw your data into `.env` file.
10. create `master` branch.
11. start `docker compose -f docker-compose.yml up -d --build db`.
12. write your models to `src/bot/models.py`.
13. run `cd src` and make `alembic revision --autogenerate -m "Initial migration"`.
14. run `cd ..` and start `docker compose -f docker-compose.yml up -d --build`.
15. now, remove all containers by `docker compose down -v`.

Done! Also edit this readme file, particularly "Tests Status" in first line!
