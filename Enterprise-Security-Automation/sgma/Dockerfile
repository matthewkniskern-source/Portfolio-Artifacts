FROM python:3.13-slim
WORKDIR /app
COPY sgma/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && useradd --create-home --uid 10001 sgma
COPY governance/ governance/
COPY security/ security/
COPY sgma/ sgma/
USER 10001
ENV SGMA_MODE=local SGMA_CONTAINER_LOCAL=1 PYTHONDONTWRITEBYTECODE=1
EXPOSE 8765
CMD ["python","sgma/app.py","serve"]
