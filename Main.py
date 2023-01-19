# Day 1

# Imports
import re

# Function for cleaning Tweet with hastag expressions, hyperlinks and Retweets
def TweetCleaner(tweet):
    return (re.sub("^RT[\s]+", "", (re.sub("https?:\/\/.*[\r\n]*", "", (re.sub("#", "", tweet))))))


# Main Function Call
if __name__ == "__main__":
    initialTweet = "This book was amazing, as the contents contained in the book blows my mind. :) #amazing #great #curiosity https:///thinam.c...g"
    print(f"Initial Tweet:  {initialTweet}")

    finalTweet = TweetCleaner(initialTweet)
    print(f"Final Tweet: {finalTweet}")
