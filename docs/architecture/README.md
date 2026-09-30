# Architecture

The approved GitHire architecture (modular monolith) is the source of truth:

- **Frontend:** one React SPA, three role experiences (`/candidate`, `/recruiter`, `/creator`), each lazy-loaded and theme-scoped.
- **Backend:** FastAPI modular monolith — 13 modules under `backend/app/modules/`, each shaped `router / schemas / models / repository / service`.
- **Rule:** modules communicate **only through service functions** — never another module's models or repositories. This is what makes future service extraction a refactor instead of a rewrite.
- **External systems** (GitHub, AI, S3, email) are reached only via `backend/app/adapters/`.
- **Slow work** (parsing, embeddings, GitHub analysis) runs on Celery queues: `default` + `ai_heavy`.

Major decisions will be recorded here as ADRs as feature work begins.
