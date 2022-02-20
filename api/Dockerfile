FROM python:3.8-slim
WORKDIR /api
ENV API_HOME=/api
RUN adduser -u 5678 --disabled-password --gecos "" ml && chown -R ml .
USER ml
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.cfg app.cfg
COPY app app
COPY model model
EXPOSE 8000
ENV MODEL_VERSION=1.0.0
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]