import os
from dotenv import load_dotenv

from app.models.ai_models import nllb_models_dict
from transformers import AutoModelForSeq2SeqLM, MBartForConditionalGeneration

load_dotenv()

nllb_model_name = os.environ.get("NLLB_MODEL")

print(f"\nDOWNLOADING {nllb_model_name} MODEL")
temp_model = AutoModelForSeq2SeqLM.from_pretrained(nllb_models_dict[nllb_model_name])
del temp_model

print(f"\n{nllb_model_name} MODEL COMPLETED")


print("\nDOWNLOADING: mbart-large-50-many-to-many-mmt MODEL")
temp_model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
del temp_model
print("\nmbart-large-50-many-to-many-mmt MODEL COMPLETED")
