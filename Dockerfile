FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
        build-essential ffmpeg libsm6 libxext6 wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Download the latest installer, install it and then remove it
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

# Set up the UV environment path correctly
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY ./pyproject.toml .

RUN uv sync && uv cache clean && chmod -R 755 /root

COPY ./template_files /opt/template_files
# The following secrets are available during build time
RUN useradd --create-home appuser
USER appuser


COPY ./SmartscopeAI SmartscopeAI 


# Set up environment variables for production
ENV PATH="/app/.venv/bin:$PATH"
ENV TEMPLATE_FILES="/opt/template_files/"

# Start the application with Uvicorn in production mode, using environment variable references
CMD ["celery", "-A", "SmartscopeAI.interfaces.celery.app", "worker", "--loglevel=DEBUG", "--pool=solo"]