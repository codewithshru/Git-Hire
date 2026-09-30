"""Notification dispatch tasks (default queue) — registered as stubs."""

import logging

from app.workers.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(name="app.workers.notification_tasks.send_notification")
def send_notification(user_id: str, message: str) -> str:
    """Deliver an in-app/email notification."""
    logger.info("send_notification(%s): no-op", user_id)
    return "noop"
