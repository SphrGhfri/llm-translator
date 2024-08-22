from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from app.routes.nllb_translate import router as nllb_translate_router
from app.routes.mbart_translate import router as mbart_translate_router


app = FastAPI(title="Clean Code Challenge", version="1.0.0")

# CORS middleware configuration
origins = [
    os.getenv("CLIENT_ORIGIN", "http://localhost")  # Default to localhost if not set
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# translate routes
app.include_router(nllb_translate_router, tags=["Facebook NLLB 200 Models"], prefix="/nllb")
app.include_router(mbart_translate_router, tags=["Facebook mBART-50 many to many multilingual translation"], prefix="/mbart")

