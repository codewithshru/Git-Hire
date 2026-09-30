"""Celery application.

Two queues keep fast tasks responsive when AI work spikes:
- default:   emails, notifications, light parsing
- ai_heavy:  LLM calls, embeddings, GitHub repo analysis

Celery Beat drives scheduled score/match recomputation.
"""

from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "githire",
    broker=settings.redis_url,
    backend=settings.redis_url,
    include=[
        "app.workers.github_tasks",
        "app.workers.resume_tasks",
        "app.workers.matching_tasks",
        "app.workers.notification_tasks",
    ],
)

celery_app.conf.update(
    task_default_queue="default",
    task_queues={
        "default": {"exchange": "default", "routing_key": "default"},
        "ai_heavy": {"exchange": "ai_heavy", "routing_key": "ai_heavy"},
    },
    task_routes={
        "app.workers.matching_tasks.*": {"queue": "ai_heavy"},
        "app.workers.github_tasks.*": {"queue": "ai_heavy"},
        "app.workers.resume_tasks.*": {"queue": "ai_heavy"},
    },
    beat_schedule={
        "recompute-stale-match-scores": {
            "task": "app.workers.matching_tasks.recompute_stale_scores",
            "schedule": 3600.0,  # hourly
        },
    },
    task_track_started=True,
    broker_connection_retry_on_startup=True,
)
