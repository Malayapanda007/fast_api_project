from datetime import datetime,timedelta,timezone
from authlib.jose import JoseError,jwt
from fastapi import HTTPException
from app.core.config import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data:dict):
    header={'alg':ALGORITHM}
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload=data.copy()
    payload.update({'exp':expire})
    return jwt.encode(header,payload,SECRET_KEY).decode('utf-8')

def verify_access_token(token:str):
    try:
        claims=jwt.decode(token,SECRET_KEY)
        claims.validate()
        username=claims.get('sub')
        if username is None:
            raise HTTPException(status_code=401)
        return username
    except JoseError:
        raise HTTPException(status_code=401,detail="invalid token")