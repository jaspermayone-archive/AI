import tensorflow as tf
from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

def story(sentence,char=100):
    input_ids = tokenizer.encode(sentence, return_tensors='pt')
    output = model.generate(input_ids, max_length=char, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
    text = tokenizer.decode(output[0], skip_special_tokens=True)
    return text