# Pull base image
FROM ubuntu:22.04

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install packages
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
    python3.10 \
    python3-pip \
    python3.10-venv \
    python3.10-dev \
    build-essential \
    libpq-dev \
    gcc \
    wget \
    autoconf \
    automake \
    pkg-config \
    libtool \
    procps

# Install dependencies
COPY ./requirements/dev.txt /requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY ./compose/production/templateproject/backend/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/production/templateproject/backend/start /start
RUN chmod +x /start

COPY ./compose/production/templateproject/celery/worker/start /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/production/templateproject/celery/beat/start /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/production/templateproject/celery/flower/start /start-flower
RUN chmod +x /start-flower

# Expose port
EXPOSE 8000

# Set working directory
WORKDIR /opt/templateproject

ENTRYPOINT [ "/entrypoint" ]