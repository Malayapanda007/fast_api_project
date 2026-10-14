from app.cache.redis_cache import get_cache_prediction, set_cache_prediction
from app.models.utils import get_prediction
from app.service.utils import convert_into_hash


def prediction(data: dict) -> int:
    key = convert_into_hash(data)

    cached = get_cache_prediction(key)
    if cached is not None:        # not `if cached:`, because 0 is a valid prediction
        return cached

    result = int(get_prediction(data))
    set_cache_prediction(key, result)
    return result