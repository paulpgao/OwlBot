import praw


alexabot = praw.Reddit(user_agent = 'alexa_play_bot_2',
                  client_id = 'obgVOv3lTA0JbQ',
                  client_secret = 'sKCI6fZm9pHLy6WVUBNNuOIwV_8',
                  username = 'alexa_play_bot',
                  password = '990610Alexa')

subreddit = alexabot.subreddit('testingground4bots')

comments = subreddit.stream.comments()
# posts = subreddit.stream.submissions()

for comment in comments:
    text = comment.body
    author = comment.author
    if 'alexa play' in text.lower():
        message = "Now Playing: ".format(author)
        comment.reply(message)

# for post in posts:
#     text = post.title
#     author = post.author
#     if 'alexa play' in post.title.lower():
#         message = "sorry dude despacito sucks".format(author)
#         post.reply(message)