from fastapi.responses import JSONResponse
from fastapi import status


def Ok(response = None):
    res = {"status": "ok"}
    if response is None:
        return JSONResponse(content = res, status_code = status.HTTP_200_OK)
    else:
        res = {"status": "ok", "message": response}
        return JSONResponse(content = res, status_code = status.HTTP_200_OK)

def OkBut(response = None):
    res = {"status": "ok", "message": []}
    if response is None:
        return JSONResponse(content = res, status_code = status.HTTP_200_OK)
    else:
        res = {"status": "ok", "message": response}
        return JSONResponse(content = res, status_code = status.HTTP_200_OK)

def Created(response = None):
    res = {"status": "ok"}
    if response is None:
        return JSONResponse(content = res, status_code = status.HTTP_201_CREATED)
    else:
        res = {"status": "ok", "message": response}
        return JSONResponse(content = res, status_code = status.HTTP_201_CREATED)
    
def Error(response = None):
    res = {"status": "error"}
    if response is None:
        return JSONResponse(content = res, status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        res = {"status": "error", "message": response}
        return JSONResponse(content = res, status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

def ValidationError():
    res = {
        "status": "error",
        "message": "Invalid data"
        }
    return JSONResponse(content = res, status_code = status.HTTP_400_BAD_REQUEST)