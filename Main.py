import nltk;
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer


# Clean Words 
clean_tweets = ['book','amazing', 'contents', 'contained', 'book', 'blows', 'mind', 'amazing', 'great', 'curiosity']


# Instance of Porter Stemmer
stemmer = PorterStemmer(); 
stemOutput = [stemmer.stem(tweet) for tweet in clean_tweets]
print(f"Porter Stemmer Output: {stemOutput}")


#Instance of Snowball Stemmer
stemmer = SnowballStemmer("english"); 
stemOutput = [stemmer.stem(tweet) for tweet in clean_tweets]
print(f"Snowball Stemmer Output: {stemOutput}")

#Instance of Lancaster Stemmer
stemmer = LancasterStemmer(); 
stemOutput = [stemmer.stem(tweet) for tweet in clean_tweets]
print(f"Lancaster Stemmer Output: {stemOutput}")