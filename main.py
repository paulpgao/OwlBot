import praw
from youtube2 import youtube_search
from spotify2 import search_track
import urllib.request
import image
import numpy as np
import scipy
from scipy import ndimage
import glob
import pickle

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
    if commentIDs.find(comment.id) == -1:
        if 'owlbot play ' in text.lower():
            search = text[text.lower().index('owlbot play ') + len('owlbot play '):]
            video = youtube_search(search)
            youtube_message = ("Now Playing: [%s](https://youtube.com/watch?v=%s)." % (video["snippet"]["title"], video["id"]["videoId"])).format(author)
            spotify_message = search_track(search)
            comment.reply(youtube_message + " " + spotify_message)
            f1 = open('comments.txt', 'a+')
            f1.write(comment.id + " ")
            f1.close()

        if ("owlbot, is this an owl?" in text.lower()) and 'https://' in text.lower():
            search = text[text.index("https://") : text.index("]")]
            print (search)
            urllib.request.urlretrieve(search, "imgtest.jpg")
            imgtest = glob.glob("F:/Paul Gao/Documents/randombot/*.jpg")[0]
            imgtest = np.array(ndimage.imread(imgtest, flatten=False))
            imgtest = scipy.misc.imresize(imgtest, size=(64, 64)).reshape((1, 64 * 64 * 3)).T

            pred = open('pred.pckl', 'rb')
            d = pickle.load(pred)
            pred.close()

            mypred = image.predict_nonlogical(d["w"], d["b"], imgtest)

            print (mypred)

            if mypred > 0.5:
                # comment.reply("I am " + str(mypred * 100)[2:-2] + "% sure this is an owl! If you like owls, have you heard of Rice University?")
                comment.reply("I am thinking this is an owl! If you like owls, have you heard of Rice University?")
            else:
                # comment.reply("Hmm, I am " + str((1 - mypred) * 100)[2:-2] + "% sure this is not an owl. What do you think it is?")
                comment.reply("Hmm, I don't think this is an owl. What do you think it is?")
            f1 = open('comments.txt', 'a+')
            f1.write(comment.id + " ")
            f1.close()



