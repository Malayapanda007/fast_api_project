import logging
from app.cache.redis_cache import get_cache_prediction, set_cache_prediction
from app.models.utils import get_prediction
from app.service.utils import convert_into_hash
logger = logging.getLogger(__name__)

def prediction(data: dict) -> int:
    key = convert_into_hash(data)

    cached = get_cache_prediction(key)
    if cached is not None:  
        logger.info("forecast cache hit %s", key)      # not `if cached:`, because 0 is a valid prediction
        return cached

    logger.info("calling the model for forecast output %s", key)
    result = int(get_prediction(data))
    set_cache_prediction(key, result)
    return result