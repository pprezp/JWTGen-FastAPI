from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def read_users():
    return [{"username": "user"}, {"username": "user2"}]

@router.post("/")
async def create_user(user: dict):
    return {"username": user.get("username"), "status": "created"}


@router.post("/put")
async def update_user(user: dict):
    return {"username": user.get("username"), "status": "updated"}