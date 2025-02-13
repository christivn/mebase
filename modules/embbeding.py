from transformers import AutoTokenizer, AutoModel
import torch

def text_to_embedding(oFile, text):
    tokenizer = AutoTokenizer.from_pretrained(oFile.embeddingModel)
    model = AutoModel.from_pretrained(oFile.embeddingModel)

    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1)
    return embedding