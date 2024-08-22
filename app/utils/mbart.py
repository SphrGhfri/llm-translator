from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import time



def load_model():
    print("Loading model: mbart-large-50-many-to-many-mmt")
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

    return (model, tokenizer)


def translation(source="en_XX", target="de_DE", text='Hello World!'):
    start_time = time.time()
    (model, tokenizer) = load_model()

    tokenizer.src_lang = source
    encoded_hi = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_hi,
        forced_bos_token_id=tokenizer.lang_code_to_id[target]
    )
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    

    end_time = time.time()

    result = {
        "inference_time": end_time - start_time,
        "source": source,
        "target": target,
        "result": translated_text,
    }
    return result
