from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyC8Lr1783Le0ZFz_rJ_wFTLzJlTdQXpxYM"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(q, max_results=50, order="relevance", token=None, location=None, location_radius=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=q,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",
        maxResults=max_results,
        location=location,
        locationRadius=location_radius

    ).execute()
    return (search_response['items'][0]['id']['videoId'])


def geo_query(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet, recordingDetails, statistics'

    ).execute()

    return video_response
