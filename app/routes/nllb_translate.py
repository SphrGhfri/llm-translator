from fastapi import APIRouter, Query
from app.models.nllb_lang import LanguageDropdownOptions, languages
from app.utils.nllb import translation
from dotenv import load_dotenv
import os

load_dotenv()

nllb_model_name = os.environ.get("NLLB_MODEL")


router = APIRouter()


@router.get("/translate/")
async def read_items(
    text: str = "We’ve been painting all afternoon; let’s call it a day and continue tomorrow.",
    source_lang: LanguageDropdownOptions = Query(..., description="Source Language"),
    target_lang: LanguageDropdownOptions = Query(..., description="Target Language"),
):
    result = translation(
        languages[source_lang], languages[target_lang], text, nllb_model_name
    )
    return result
