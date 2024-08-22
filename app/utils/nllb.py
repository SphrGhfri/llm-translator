from app.models.ai_models import nllb_models_dict

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import time



def load_model(model_name):
    print("\tLoading model: %s" % model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(nllb_models_dict[model_name])
    tokenizer = AutoTokenizer.from_pretrained(nllb_models_dict[model_name])

    return (model, tokenizer)


def translation(source, target, text, model_name="nllb-distilled-1.3B"):
    start_time = time.time()
    (model, tokenizer) = load_model(model_name)

    translator = pipeline(
        "translation",
        model=model,
        tokenizer=tokenizer,
        src_lang=source,
        tgt_lang=target,
    )
    output = translator(text, max_length=400)

    end_time = time.time()

    output = output[0]["translation_text"]
    result = {
        "model_name":model_name,
        "inference_time": end_time - start_time,
        "source": source,
        "target": target,
        "result": output,
    }
    return result
