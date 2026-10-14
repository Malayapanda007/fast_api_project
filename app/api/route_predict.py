
from app.core.dependencies import get_current_user
from app.service.model_service import prediction
from fastapi import APIRouter,Depends,HTTPException
from pydantic import BaseModel,EmailStr,Field
from typing import Annotated,Optional,Literal

class Input_Data(BaseModel):
    pclass: Annotated[int, Field(ge=1, le=3)]
    sex: Literal["male", "female"]
    age: Annotated[int, Field(gt=10, lt=80)]
    alone: bool


routes=APIRouter()

@routes.post('/prediction')
def model_prediction(data: Input_Data,current_user: Annotated[str, Depends(get_current_user)]):
    predict= prediction(data.model_dump())
    return {'prediction':predict}
    

