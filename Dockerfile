FROM python:3.7

RUN pip install fastapi uvicorn names

COPY tec_api /api/tec_api

ENV PYTHONPATH=/api
WORKDIR /api/tec_api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0", "--reload"]