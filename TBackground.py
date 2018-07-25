import tweepy
from platform import node
from time import sleep
import os
from random import shuffle
from time import localtime, strftime
import ConfigParser


def get_config(key):
    return parser.get("TBackgroundBot_Config", key)


parser = ConfigParser.RawConfigParser()
parser.read(r"config.txt")
consumer_key = get_config("consumer_key")
consumer_secret = get_config("consumer_secret")
access_token = get_config("access_token")
access_token_secret = get_config("access_token_secret")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

name = node()

directory = get_config("backgrounds_path")

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
    removed_file = None
    while i < len(name_list):
        if removed_file is not None:
            name_list.remove(removed_file)
            removed_file = None
        break_and_continue = False
        while True:
            try:
                api.update_profile_banner(name_list[i])
            except tweepy.error.RateLimitError:
                print "Rate limited exceeded. Trying again in ten minutes."
                sleep(600)
                continue
            except tweepy.error.TweepError as e:
                if "The system cannot find the file specified" in str(e):
                    print "The photo with name \"" + str(name_list[i]).split("/")[-1] + "\" has been deleted. Removing from list.\n"
                    removed_file = name_list[i]
                    break_and_continue = True
                    break
                else:
                    print "Something went wrong when uploading banner photo:"
                    print e
                    print "Trying again in 10 seconds.\n"
                    sleep(10)
                    continue
            break
        if break_and_continue:
            continue
        print "Finished uploading pic number " + str(i+1) + "/" + str(len(name_list)) + " at " + strftime("%I:%M:%S %p on %m/%d.", localtime())
        print "It has a filename of \"" + str(name_list[i]).split("/")[-1] + "\". Going again in 1 minute.\n"
        i += 1
        sleep(60)

    print "Restarting cycle.\n\n\n"
