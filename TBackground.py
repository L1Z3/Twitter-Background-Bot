import tweepy
from platform import node
from time import sleep
import os
from random import shuffle
from time import gmtime, strftime

consumer_key = "KCiLZRUT9CDU22lw5610r9Jru"
consumer_secret = "aWrISWCnzXM6LKTlwV5w4w7VVbNHJfm7CZ8b2k4Cq9nVq7f0rM"
access_token = "1483234068-iZ1sprqjCu76jYWWYaVXIriwjpbdkwCtRAvoKmR"
access_token_secret = "mVbPdSb4iiwNI34isar16wzidWlajGm8RPVSTP9BRKIkp"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

name = node()
# print name
if name == "William-Laptop-2":
    directory = "C:/Users/wcjon/Desktop/Covers"
elif name == "WillBox3000":
    directory = "C:/Users/wcjon/Desktop/Covers"
else:
    directory = "C:/Users/William/Desktop/Programs/Twitter Background Bot/Covers"
# exit(0)
print "Starting header photo cycle."
while True:
    name_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            file = directory + "/" + filename
            name_list.append(file)

            continue
        else:
            continue
    shuffle(name_list)
    i = 0
    for file in name_list:
        i += 1
        while True:
            try:
                api.update_profile_banner(file)
            except tweepy.error.RateLimitError:
                print "Rate limited exceeded. Trying again in ten minutes."
                sleep(600)
                continue
            except tweepy.error.TweepError as e:
                print "Something went wrong when uploading banner photo. Trying again in 10 seconds."
                print e
                sleep(10)

            break

        print "Finished uploading pic number " + str(i) + "/" + str(len(name_list)) + " at " + strftime("%H:%M:%S on %m/%d", gmtime()) + "."
        print "It has a filename of \"" + str(file).split("/")[-1] + "\". Going again in 1 minute.\n"
        sleep(60)

    print "Restarting cycle.\n\n\n"
