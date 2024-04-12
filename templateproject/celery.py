import logging
import os
from typing import Any

from celery import Celery
from django.conf import settings

# Setting the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateproject.settings")

app = Celery("templateproject")

# Configuring Celery with settings from the Django settings.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Define the Celery beat schedule if any.
app.conf.beat_schedule = {}

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


@app.task(bind=True)
def debug_task(self: Any) -> None:
    logger.info(f"Request: {self.request!r}")
