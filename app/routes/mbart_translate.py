from fastapi import APIRouter, Query
from app.models.mbart_lang import LanguageDropdownOptions, languages

from app.utils.mbart import translation



router = APIRouter()


@router.get("/translate/")
async def read_items(
    text: str = "We’ve been painting all afternoon; let’s call it a day and continue tomorrow.",
    source_lang: LanguageDropdownOptions = Query(..., description="Source Language"),
    target_lang: LanguageDropdownOptions = Query(..., description="Target Language"),
):
    result = translation(source=languages[source_lang],target=languages[target_lang],text=text)
    return result
