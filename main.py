import praw
from youtube2 import youtube_search
from spotify2 import search_track
import posixpath
import urllib.parse
import requests
from imgurpython import ImgurClient

alexabot = praw.Reddit(user_agent = 'alexa_play_bot_2',
                  client_id = 'obgVOv3lTA0JbQ',
                  client_secret = 'sKCI6fZm9pHLy6WVUBNNuOIwV_8',
                  username = 'alexa_play_bot',
                  password = '990610Alexa')

client = ImgurClient(client_id = 'dd33db2d7391c65',
                     client_secret = '7e473c05de42a24de086f965fc126fd8ce7c9c6f')


subreddit = alexabot.subreddit('testingground4bots')

comments = subreddit.stream.comments()
print("Running Owlbot")

for comment in comments:
    f = open('comments.txt', 'r+')
    commentIDs = f.read()
    f.close()
    if len(commentIDs) > 1000:
        open('comments.txt', 'w')
    text = comment.body
    author = comment.author
    text = text.lower()
    if commentIDs.find(comment.id) == -1:
        if 'owlbot play ' in text:
            search = text[text.index('owlbot play ') + len('owlbot play '):]
            video = youtube_search(search)
            youtube_message = ("Now Playing: [%s](https://youtube.com/watch?v=%s)." % (video["snippet"]["title"], video["id"]["videoId"])).format(author)
            spotify_message = search_track(search)
            comment.reply(youtube_message + " " + spotify_message)
            f1 = open('comments.txt', 'a+')
            f1.write(comment.id + " ")
            f1.close()
        if 'owlbot check' in text and 'imgur.com/' in text:
            search = text[text.index('imgur.com') + len('imgur.com'):]
            image = client.get_image(search)
