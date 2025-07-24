from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"

print("Loading model on CPU...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype = torch.float32,
    device_map = "cpu"
)

text_generator = pipeline(
    "text-generation",
    model = model,
    tokenizer = tokenizer,
    device = -1
)

def generate_response(prompt: str, max_new_tokens: int = 150) -> str:
    output = text_generator(
        prompt,
        max_new_tokens = max_new_tokens,
        temperature = 0.7,
        top_k = 50,
        top_p = 0.95,
        do_sample = True,
        repetition_penalty = 1.1
    )
    return output[0]['generated_text']