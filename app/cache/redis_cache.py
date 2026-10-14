import json
import logging

import redis

from app.core.config import REDIS_URL

logger = logging.getLogger(__name__)

# REDIS_URL example: redis://localhost:6379/0
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

CACHE_PREFIX = "pred:v1:"   # bump v1 when you retrain or change the model


def get_cache_prediction(key: str):
    try:
        value = redis_client.get(CACHE_PREFIX + key)
    except redis.RedisError as e:
        logger.warning("Redis read failed: %s", e)
        return None
    return json.loads(value) if value is not None else None


def set_cache_prediction(key: str, result, ttl: int = 3600) -> None:
    try:
        redis_client.setex(CACHE_PREFIX + key, ttl, json.dumps(result))
    except redis.RedisError as e:
        logger.warning("Redis write failed: %s", e)