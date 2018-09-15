import praw
import gdata.youtube
import gdata.youtube.service
yt_service = gdata.youtube.service.YouTubeService()

yt_service.developer_key = 'AIzaSyB4npSjJ7nlyDpIyjC2eiDGVHnomLP_bNs'
yt_service.client_id = '992095518153-ucsohpb3emcu3glri3ojn62e8fdkvi8g.apps.googleusercontent.com'


alexabot = praw.Reddit(user_agent = 'alexa_play_bot_2',
                  client_id = 'obgVOv3lTA0JbQ',
                  client_secret = 'sKCI6fZm9pHLy6WVUBNNuOIwV_8',
                  username = 'alexa_play_bot',
                  password = '990610Alexa')

subreddit = alexabot.subreddit('testingground4bots')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body
    author = comment.author
    if 'alexa play' in text.lower():
        message = "Now Playing: ".format(author)
        comment.reply(message)
