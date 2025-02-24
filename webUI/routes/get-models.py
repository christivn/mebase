from flask import request, session, render_template, redirect, jsonify
from server import app
import requests

authorsUrls = {
    "openai": "https://www.openai.com",
    "mistralai": "https://www.mistral.ai",
    "google": "https://ai.google",
    "anthropic": "https://www.anthropic.com",
    "meta-llama": "https://ai.facebook.com",
    "qwen": "https://chat.qwenlm.ai",
    "deepseek": "https://chat.deepseek.com",
    "cohere": "https://cohere.ai",
    "perplexity": "https://www.perplexity.ai",
    "microsoft": "https://www.microsoft.com/en-us/ai",
    "neversleep": "https://huggingface.co",
    "sao10k": "https://huggingface.co",
    "nousresearch": "https://nousresearch.com",
    "x-ai": "https://x.ai",
    "cognitivecomputations": "https://huggingface.co",
    "undi95": "https://huggingface.co",
    "amazon": "https://www.amazon.com/ai",
    "eva-unit-01": "https://huggingface.co",
    "liquid": "https://www.liquid.ai",
    "aion-labs": "https://aionlabs.com",
    "ai21": "https://www.ai21.com",
    "openchat": "https://huggingface.co",
    "sophosympatheia": "https://huggingface.co",
    "nvidia": "https://www.nvidia.com/en-us/ai",
    "thedrummer": "https://huggingface.co",
    "anthracite-org": "https://huggingface.co",
    "inflection": "https://www.inflection.ai",
    "gryphe": "https://www.gryphe.com",
    "alpindale": "https://huggingface.co",
    "xwin-lm": "https://huggingface.co",
    "mancer": "https://mancer.tech",
    "jondurbin": "https://huggingface.co",
    "pygmalionai": "https://www.pygmalion.ai",
    "infermatic": "https://infermatic.ai",
    "nothingiisreal": "https://huggingface.co",
    "minimax": "https://minimaxi.com",
    "openrouter": "https://www.openrouter.ai",
    "databricks": "https://www.databricks.com",
    "teknium": "https://huggingface.co",
    "aetherwiing": "https://huggingface.co",
    "huggingfaceh4": "https://huggingface.co",
    "raifle": "https://huggingface.co",
    "01-ai": "https://www.01.ai",
    "allenai": "https://www.allenai.org"
}

@app.route("/update-models/<privateToken>", methods=['GET'])
def update_models(privateToken):
    if(privateToken=="7d423aced265f1bb4f1d9b690233d9bb"):
        response = requests.get("https://openrouter.ai/api/v1/models")
        if response.status_code == 200:
            models = response.json()["data"]
        else:
            print(f"Error 'get-model' {response.status_code}: {response.text}")

        # Upload to supabase
        meboxModels = []
        for model in models:
            data = {
                "model": model["id"],
                "display_name": model["name"],
                "author": model["id"].split("/")[0],
                "description": model["description"],
                "context": model["context_length"],
                "input_token_pricing": model["pricing"]["prompt"],
                "output_token_pricing": model["pricing"]["completion"],
                "create_at": model["created"],
                "author_website": authorsUrls.get(model["id"].split("/")[0]),
                "modality": model["architecture"]["modality"],
                "active": True
            }
            if model["id"].split("/")[0]!="openrouter":
                try:
                    app.config['supabase'].table("models").insert(data).execute()
                except:
                    try:
                        app.config['supabase'].from_("models").update(data).eq("model", model["id"]).execute()
                    except Exception as e:
                        print("ERROR 'update_model': "+str(e))

        return {"status": "complete"}
    else:
        return {"status": "invalid-token"}

# Example
'''
{
    "architecture": {
    "instruct_type": null,
    "modality": "text->text",
    "tokenizer": "DeepSeek"
    },
    "context_length": 128000,
    "created": 1740004929,
    "description": "Note: As this model does not return <think> tags, thoughts will be streamed by default directly to the `content` field.\n\nR1 1776 is a version of DeepSeek-R1 that has been post-trained to remove censorship constraints related to topics restricted by the Chinese government. The model retains its original reasoning capabilities while providing direct responses to a wider range of queries. R1 1776 is an offline chat model that does not use the perplexity search subsystem.\n\nThe model was tested on a multilingual dataset of over 1,000 examples covering sensitive topics to measure its likelihood of refusal or overly filtered responses. [Evaluation Results](https://cdn-uploads.huggingface.co/production/uploads/675c8332d01f593dc90817f5/GiN2VqC5hawUgAGJ6oHla.png) Its performance on math and reasoning benchmarks remains similar to the base R1 model. [Reasoning Performance](https://cdn-uploads.huggingface.co/production/uploads/675c8332d01f593dc90817f5/n4Z9Byqp2S7sKUvCvI40R.png)\n\nRead more on the [Blog Post](https://perplexity.ai/hub/blog/open-sourcing-r1-1776)",
    "id": "perplexity/r1-1776",
    "name": "Perplexity: R1 1776",
    "per_request_limits": null,
    "pricing": {
    "completion": "0.000008",
    "image": "0",
    "prompt": "0.000002",
    "request": "0"
    },
    "top_provider": {
    "context_length": 128000,
    "is_moderated": false,
    "max_completion_tokens": null
    }
}
'''

@app.route("/get-models", methods=['GET'])
def get_models():
    try:
        response = app.config['supabase'].table("models").select("*").order("create_at", desc=True).execute()

        # Formatear valores de punto flotante
        formatted_data = []
        for model in response.data:
            if "input_token_pricing" in model and isinstance(model["input_token_pricing"], float):
                model["input_token_pricing"] = format(model["input_token_pricing"], ".10f")
            if "output_token_pricing" in model and isinstance(model["output_token_pricing"], float):
                model["output_token_pricing"] = format(model["output_token_pricing"], ".10f")
            
            formatted_data.append(model)

        return formatted_data
    except Exception as e:
        print("Error fetching models:", e)
        return None