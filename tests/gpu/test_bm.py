from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import time

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

inputs = tokenizer("This is a test sentence for benchmarking.", return_tensors="pt")
start_time = time.time()
for _ in range(100):  # Repeat inference 100 times
    with torch.no_grad():
        outputs = model(**inputs)
end_time = time.time()

print(f"Average Inference Time: {(end_time - start_time) / 100:.4f} seconds")
