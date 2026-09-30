"""GitHub analysis background tasks (ai_heavy queue) — registered as stubs."""

import logging

from app.workers.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(name="app.workers.tasks.github_tasks.analyze_candidate_repos")
def analyze_candidate_repos(candidate_id: str) -> str:
    """Fetch and analyze a candidate's public GitHub repos (via adapter)."""
    logger.info("analyze_candidate_repos(%s): no-op (adapter integration pending)", candidate_id)
    return "noop"
