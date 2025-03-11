import os
from typing import Annotated
from fastapi import Depends
from fastapi.responses import JSONResponse
from services.utils import get_spotify_client
from services.spotify import SpotifyClient

from fastapi import APIRouter

router = APIRouter()

# Route: /top/{type}

@router.get("/top/tracks")
async def get_playlist(spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)]):
    top_tracks = spotify_client.get_top_tracks()
    return top_tracks

@router.get("/top/artists")
async def get_playlist(spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)]):
    top_artists = spotify_client.get_top_artists()
    return top_artists


@router.get("/recently-played")
async def get_recently_played(spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)]):
    recently_played = spotify_client.get_recently_played()
    return recently_played



