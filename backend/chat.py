from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
try:
    mname = 'facebook/blenderbot-400M-distill'
    model = BlenderbotForConditionalGeneration.from_pretrained(mname)
    tokenizer = BlenderbotTokenizer.from_pretrained(mname)
except:
    print("No internet")
    pass
def chat(query):
    inputs = tokenizer([query], return_tensors='pt')
    reply_ids = model.generate(**inputs)
    return tokenizer.batch_decode(reply_ids,skip_special_tokens=True)[0]

