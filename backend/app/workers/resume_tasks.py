"""Resume parsing background tasks (ai_heavy queue) — registered as stubs."""

import logging

from app.workers.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(name="app.workers.resume_tasks.parse_resume")
def parse_resume(resume_id: str) -> str:
    """Extract skills/experience from an uploaded resume."""
    logger.info("parse_resume(%s): no-op (parser not yet implemented)", resume_id)
    return "noop"
