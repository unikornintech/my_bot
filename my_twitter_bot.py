import tweepy
import time

print('this is my twitter bot')

CONSUMER_KEY = 'QPor5JXMfHv3fqzUUgOb8aFGD'
CONSUMER_SECRET = 'tFdVHPAqCsB9A03JFQzFtyV1zr390ZMthAGJTfUuyaRzGwRpHn'
ACCESS_KEY = '1147500042229616640-nLpQ6oHKiWbQq4qSGfvLsEdvKp491b'
ACCESS_SECRET = 'PbBSBlbwVGjf8UqYsNTutEXWcNEFMne85UtBygqIXN8A4'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print('retrieving and replying to tweets...')


# DEV NOTE: use 1152916698162520064 for testing.
last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
for mention in reversed(mentions):
    print(str(mention.id) + ' - ' + mention.full_text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '#codenewbie' in mention.full_text.lower():
        print('found #codenewbie!')
        print('responding back...')
        api.update_status('@' + mention.user.screen_name +
                          '#codenewbie back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
