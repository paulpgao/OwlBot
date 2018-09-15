import praw
from youtube2 import youtube_search
from spotify2 import search_track
import weather

alexabot = praw.Reddit(user_agent = 'alexa_play_bot_2',
                  client_id = 'obgVOv3lTA0JbQ',
                  client_secret = 'sKCI6fZm9pHLy6WVUBNNuOIwV_8',
                  username = 'alexa_play_bot',
                  password = '990610Alexa')

subreddit = alexabot.subreddit('testingground4bots')

comments = subreddit.stream.comments()
print("Running Owlbot")

for comment in comments:
    f = open('comments.txt', 'r+')
    commentIDs = f.read()
    f.close()
    if len(commentIDs) > 100:
        open('comments.txt', 'w')
    text = comment.body
    author = comment.author
    text = text.lower()
    if commentIDs.find(comment.id) == -1:
        if 'owlbot play ' in text:
            search = text[text.index('owlbot play ') + len('owlbot play '):]
            video = youtube_search(search)
            youtube_message = ("Now Playing on Youtube: [%s](https://youtube.com/watch?v=%s)." % (video["snippet"]["title"], video["id"]["videoId"])).format(author)
            spotify_message = search_track(search)
            comment.reply(youtube_message + '\n' + spotify_message)
            f1 = open('comments.txt', 'a+')
            f1.write(comment.id + " ")
            f1.close()
        if 'owlbot what is the weather like in ' in text:
            search = text[text.index('owlbot what is the weather like in ') + len('owlbot what is the weather like in '):]
            city = search.split(',')[0]
            state = search.split(',')[1]
            zip = weather.get_zip(city, state)
            weather_message = weather.get_weather(zip, city)
            comment.reply(weather_message)
            f1 = open('comments.txt', 'a+')
            f1.write(comment.id + " ")
            f1.close()

