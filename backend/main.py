from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer
from auth import authenticate, get_user_from_token

app = FastAPI()

security = HTTPBearer()


@app.post("/login")
def login(data: dict):

    token = authenticate(data["email"], data["password"])

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"token": token}


@app.get("/me")
def me(credentials=Depends(security)):

    user = get_user_from_token(credentials.credentials)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"]
    }