from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

def register_exception_handlers(app:FastAPI):
    @app.exception_handler(Exception)
    async def general_exception(request:Request,exception:Exception):
        return JSONResponse(status_code=500,content={'details':str(exception)})