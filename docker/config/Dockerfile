# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
COPY src ./src
COPY docker ./docker

# Install pip requirements
RUN python -m pip install -r requirements.txt


ENV PYTHONPATH "${PYTHONPATH}:/src:/local"

CMD ["sh", "./docker/scripts/entrypoint.sh"]