FROM python:3.7

RUN pip install fastapi uvicorn names

COPY app /api/app

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0", "--reload"]