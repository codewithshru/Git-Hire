"""Matching/AI background tasks (executed on the ai_heavy queue).

Implementations are deferred — tasks are registered so the worker, queues,
and beat schedule can be verified before feature development begins.
"""

import logging

from app.workers.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(name="app.workers.tasks.matching_tasks.recompute_stale_scores")
def recompute_stale_scores() -> str:
    """Recompute Job Ready Scores / matches older than the freshness window."""
    logger.info("recompute_stale_scores: no-op (matching engine not yet implemented)")
    return "noop"
