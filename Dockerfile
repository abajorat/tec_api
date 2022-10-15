FROM python:3.8

RUN pip install fastapi uvicorn names

COPY src /api

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["tec_api.main:app", "--host", "0.0.0.0", "--reload"]