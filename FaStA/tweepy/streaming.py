from tweepy.streaming import StreamListener
from tweepy import Stream
from oauth import login

class StdOutListener(StreamListener):
    """ This listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout."""

    def on_data(self, data):
        print(data['text'])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = login()[0]
    set_auth = login()[1]

    stream = Stream(auth, l)
    stream.filter(track=['basketball']).text
