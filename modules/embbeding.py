from transformers import AutoTokenizer, AutoModel
import torch

def text_to_embedding(mebox, text):
    tokenizer = mebox.embeddingTokenizer
    model = mebox.embeddingModel

    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1)
    return embedding