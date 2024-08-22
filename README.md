# How to run

## 1. Run local

- First make python environment and activate it. Then run:
    ```
    pip install -r ./requirements.txt
    ```
- Set NLLB model in .env file. (It's default is nllb-distilled-1.3B)
- Run Script to download Models before running API:
    ```
    python ./download_models_script.py
    ```
- Start server:
    ```
    uvicorn main:app --reload --timeout-keep-alive 10000
    ```
- Access docs and API endpoints from:
    http://localhost:8000/docs

## 2. Run with Docker Compose
```
docker compose up -d
```
<mark>This App needs to download 8GB models! Consider having good internet with no limitation.</mark>
