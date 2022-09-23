from fastapi import FastAPI, HTTPException


KEY_VALUE_STORE = {}

app = FastAPI()
NAME_NOT_FOUND = HTTPException(status_code=400, detail="Name not found.")


@app.post("/nickname")
def create_path(name: str, nickname: str):
    KEY_VALUE_STORE[name] = nickname
    return {"status": "success"}


@app.post("/nickname/name/{name}/nickname/{nickname}")
def create_query(name: str, nickname: str):
    KEY_VALUE_STORE[name] = nickname
    return {"status": "success"}


@app.get("/nickname")
def get_path(name: str):
    if name not in KEY_VALUE_STORE:
        raise NAME_NOT_FOUND
    return {"nickname": KEY_VALUE_STORE[name]}


@app.get("/nickname/name/{name}")
def get_query(name: str):
    if name not in KEY_VALUE_STORE:
        raise NAME_NOT_FOUND
    return {"nickname": KEY_VALUE_STORE[name]}


@app.put("/nickname")
def update_path(name: str, nickname: str):
    if name not in KEY_VALUE_STORE:
        raise NAME_NOT_FOUND
    KEY_VALUE_STORE[name] = nickname
    return {"status": "success"}


@app.put("/nickname/name/{name}/nickname/{nickname}")
def update_query(name: str, nickname: str):
    if name not in KEY_VALUE_STORE:
        raise NAME_NOT_FOUND
    KEY_VALUE_STORE[name] = nickname
    return {"status": "success"}


@app.delete("/nickname")
def delete_path(name: str):
    if name not in KEY_VALUE_STORE:
        raise NAME_NOT_FOUND
    del KEY_VALUE_STORE[name]
    return {"status": "success"}


@app.delete("/nickname/name/{name}")
def delete_query(name: str):
    if name not in KEY_VALUE_STORE:
        raise NAME_NOT_FOUND
    del KEY_VALUE_STORE[name]
    return {"status": "success"}
