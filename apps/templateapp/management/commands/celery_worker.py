import os
import shlex
import subprocess
from typing import Any, Dict

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery() -> None:
    queue_name = os.getenv("CELERY_QUEUE", "default_queue")
    worker_name = f"worker_{queue_name}"
    subprocess.call(shlex.split('pkill -f "celery worker"'))
    subprocess.call(
        shlex.split(f"celery -A templateproject worker -Q {queue_name} -c 2 -l INFO -n {worker_name}")
    )


class Command(BaseCommand):
    def handle(self, *args: Any, **kwargs: Dict[str, Any]) -> None:
        print("Starting celery worker with autoreload...")
        autoreload.run_with_reloader(restart_celery)
