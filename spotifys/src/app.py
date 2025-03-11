from fastapi import FastAPI
from routers.playlist import router as playlist_router
from routers.track import router as track_router
from auth.auth import router as auth_router
from routers.personal import router as personal_router
app = FastAPI()
# port = 8080

app.include_router(playlist_router)
app.include_router(track_router)
app.include_router(auth_router)
app.include_router(personal_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}








