# import praw
# import spotify
#
#
# alexabot = praw.Reddit(user_agent = 'alexa_play_bot_2',
#                   client_id = 'obgVOv3lTA0JbQ',
#                   client_secret = 'sKCI6fZm9pHLy6WVUBNNuOIwV_8',
#                   username = 'alexa_play_bot',
#                   password = '990610Alexa')
#
# subreddit = alexabot.subreddit('testingground4bots')
#
# comments = subreddit.stream.comments()
#
# for comment in comments:
#     text = comment.body
#     author = comment.author
#     if ('alexa play' in text.lower()) & (len(text) > 11):
#         print (text)
#         print (text.index('alexa play') + len('alexa play '))
#         songtitle = text[text.index('alexa play ') + len('alexa play '):-1].split('.')[0]
#         # songtitle = text[0:3]
#         message = spotify.search_track(songtitle).format(author)
#         comment.reply(message)

import praw
from youtube2 import youtube_search

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
    text = text.lower()

    if 'owlbot play ' in text:
        search = text[text.index('owlbot play ') + len('owlbot play '):] #text.replace('alexa play', '')
        test = youtube_search(search)
        s = "https://www.youtube.com/watch?v=" + test
        message = ("Now Playing: " + s).format(author)
        comment.reply(message)