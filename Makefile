# GitHire development commands
.PHONY: help api worker beat dev migrate lint lint-backend lint-frontend typecheck test
.DEFAULT_GOAL := help

help: ## Show available commands
	@echo "GitHire dev commands:"
	@echo "  make api          Start backend API (localhost:8000)"
	@echo "  make worker       Start Celery worker (default + ai_heavy queues)"
	@echo "  make beat         Start Celery Beat scheduler"
	@echo "  make dev          Start frontend dev server (localhost:5173)"
	@echo "  make migrate      Run Alembic migrations"
	@echo "  make lint         Lint backend + frontend"
	@echo "  make typecheck    TypeScript check frontend"
	@echo "  make test         Backend pytest suite"

api: ## Start FastAPI backend
	cd backend && ./.venv/Scripts/python.exe -m uvicorn app.main:app --reload --port 8000

worker: ## Start Celery worker
	cd backend && ./.venv/Scripts/python.exe -m celery -A app.workers.celery_app.celery_app worker -Q default,ai_heavy -l info

beat: ## Start Celery Beat scheduler
	cd backend && ./.venv/Scripts/python.exe -m celery -A app.workers.celery_app.celery_app beat -l info

dev: ## Start frontend dev server
	cd frontend && npm run dev

migrate: ## Run Alembic migrations
	cd backend && ./.venv/Scripts/python.exe -m alembic upgrade head

lint: lint-backend lint-frontend ## Lint everything

lint-backend: ## Ruff + mypy on backend
	cd backend && ./.venv/Scripts/python.exe -m ruff check app tests
	cd backend && ./.venv/Scripts/python.exe -m mypy app

lint-frontend: ## ESLint on frontend
	cd frontend && npm run lint

typecheck: ## tsc on frontend
	cd frontend && npx tsc -b --noEmit

test: ## Backend pytest suite
	cd backend && ./.venv/Scripts/python.exe -m pytest -q
