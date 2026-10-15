import uvicorn
from fastapi import FastAPI,Depends
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import route_auth,route_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exception import register_exception_handlers
from app.core.dependencies import get_current_user  # use whatever your token-verify dependency is called

app=FastAPI()

app.add_middleware(LoggingMiddleware)


app.include_router(route_auth.router,tags=['Auth'])
app.include_router(route_predict.routes,tags=['Prediction'])

Instrumentator().instrument(app).expose(app,dependencies=[Depends(get_current_user),])

register_exception_handlers(app)


if __name__ =='__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)