import os
from typing import Annotated
from fastapi import Depends
from fastapi.responses import PlainTextResponse
from dtos.api import TrackTitles, TrackURIs
from services.utils import get_spotify_client
from services.spotify import SpotifyClient


from fastapi import APIRouter

router = APIRouter()

# Route: /playlist/{playlist_id}/tracks

@router.get("/playlist/{playlist_id}/tracks")
async def get_playlist_tracks(playlist_id: str, spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)]):
    tracks = spotify_client.get_tracks_from_playlist(playlist_id)
    return tracks

@router.post("/playlist/{playlist_id}/tracks")
async def add_tracks_to_playlist(playlist_id: str, track_titles: TrackTitles, spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)]): 
    spotify_client.add_tracks_to_playlist(playlist_id, track_titles)
    return PlainTextResponse(status_code=200)

@router.delete("/playlist/{playlist_id}/tracks")
async def remove_tracks_from_playlist(playlist_id: str, track_uris: TrackURIs, spotify_client: Annotated[SpotifyClient, Depends(get_spotify_client)]):
    spotify_client.remove_tracks_from_playlist(playlist_id, track_uris)
    return PlainTextResponse(status_code=200)