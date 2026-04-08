import json
import hashlib
from typing import Optional
import valkey.asynchronous as valkey # Prioritizing Valkey as requested

class SemanticCache:
    def __init__(self, host='localhost', port=6379, db=0):
        # Configuration is loaded via host parameter, typically from ENV
        self.client = valkey.Valkey(host=host, port=port, db=db, decode_responses=True)

    def _generate_hash(self, prompt: str, model: str) -> str:
        # Generates a unique ID based on the prompt and model
        return hashlib.sha256(f"{model}:{prompt}".encode()).hexdigest()

    async def get_cache(self, prompt: str, model: str) -> Optional[dict]:
        cache_key = self._generate_hash(prompt, model)
        data = await self.client.get(cache_key)
        return json.loads(data) if data else None

    async def set_cache(self, prompt: str, model: str, response: dict, expire: int = 3600):
        cache_key = self._generate_hash(prompt, model)
        await self.client.set(cache_key, json.dumps(response), ex=expire)
