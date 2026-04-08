from fastapi import FastAPI, HTTPException
from litellm import acompletion
from .core.cache import SemanticCache
import os

# SS360-CORE-FRAMEWORK: Standardized Gateway Entrance
app = FastAPI(title="SS360 AI Gateway")
cache = SemanticCache(host=os.getenv("VALKEY_HOST", "localhost"))

@app.post("/v1/chat/comprehensive")
async def chat_completion(prompt: str, model: str = "claude-3-5-sonnet-20240620"):
    # 1. Check Semantic Cache (Valkey)
    cached_res = await cache.get_cache(prompt, model)
    if cached_res:
        return {"source": "cache", "data": cached_res}

    try:
        # 2. Async call via LiteLLM
        # Credentials should be set via environment variable LITELM_API_KEY
        response = await acompletion(
            model=model,
            messages=[{"content": prompt, "role": "user"}],
            temperature=0.2
        )
        
        # 3. Persist in Valkey for future reuse
        await cache.set_cache(prompt, model, response)
        
        return {"source": "api", "data": response}
    
    except Exception as e:
        # Standardized Error Handling
        raise HTTPException(status_code=500, detail=str(e))
