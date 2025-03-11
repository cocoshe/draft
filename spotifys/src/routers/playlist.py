import os
from typing import Annotated
from fastapi import Depends
from fastapi.responses import JSONResponse
from services.utils import get_spotify_client
from services.spotify import SpotifyClient

from fastapi import APIRouter

router = APIRouter()

# Route: /playlist

@router.get("/playlist")
async def get_playlist(spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)]):
    playlists = spotify_client.get_all_playlist()
    return playlists

@router.get("/playlist/{name}")
async def get_playlist(name: str, spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)]):
    playlist = spotify_client.find_playlist(name)
    if playlist is None:
        return JSONResponse(status_code=404, content={"message": "Playlist not found"})
    else:
        return playlist

@router.post("/playlist")
async def create_playlist(name: str, public: bool, spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)]):
    playlist_id = spotify_client.create_playlist(name, public)
    return { "playlist_id": playlist_id }
