from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/mbart-large-50-many-to-many-mmt"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Loaded successfully!")


hindi_text ="एक हिंदी लेखक के जीवन की सुबह सूचनाओं से और रात उपन्यास से होती है। वह दुपहर से शाम तक ख़राब सिनेमा के असर में रहता है। इस असर में बाहर धूल और भीतर पन्ने उड़ते रहते हैं। यह उड़ान ही है कि महानगर जीवन क"

inputs = tokenizer(
    hindi_text,

    return_tensors="pt",
    max_length=1024,
    truncation=True
)

summary_ids = model.generate(
    **inputs,
    forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"],
    max_length=60,
    min_length=30,
    num_beams=4,
    early_stopping=True
)

summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)

print(summary)