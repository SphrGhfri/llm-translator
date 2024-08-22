FROM python:3.10.5-slim
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/api
WORKDIR /api
COPY ./requirements.txt /api/requirements.txt

RUN pip install -r requirements.txt

COPY . /api

# download models before running api
RUN python ./download_models_script.py

## program run methods
CMD ["uvicorn", "main:app", "--host" , "0.0.0.0" , "--port" , "8000" , "--reload", "--timeout-keep-alive", "10000"]
