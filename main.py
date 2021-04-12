import statistics
import tweepy

# Twitter API keys
APIKey = "mQkNBlcW2XEmRFKUJJVVqysCK"
APISecretKey = "yPLHGwwEO94ymqsZ4CO3jA6hBkeazWRHUO03m9I19CSaCejFws"

bearerToken = "AAAAAAAAAAAAAAAAAAAAAF7ZOQEAAAAARik3%2B7JyPgoAzyw0h44TCqJhTqs" \
              "%3DHbtIWwJBjSMvpJhRgJ0boc9AHKsZuOUsaUggy3QLCvqX64y6ez "

accessToken = "888393487405559808-NNUksYquOW9UHeo5NofigI1VBTP9wir"
accessTokenSecret = "41shbKk8eu6TKus8GXVqPfWMPPoP2J2yyPYmThYMwZk63"

# Tweepy Authentication
auth = tweepy.OAuthHandler(APIKey, APISecretKey)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

option = input(
    "Choose from the following options: \na. Search Twitter for a key term and perform analysis on the corresponding "
    "data received\nb. Grab Tweets from \"tweets.txt\" and perform analysis\n>> ")


# Search for tweets and adds it to the text file
def twitter_search(search):
    f_write = open('tweets.txt', 'w')
    public_tweets = api.search(search)
    for tweet_twitter in public_tweets:
        f_write.write(tweet_twitter.text)
    f_write.close()


# Takes place if user selects 1st option
if option == "a":
    s = input("Enter search term: ")
    twitter_search(s)

# Opens text files
f = open('tweets.txt', 'r')
f2 = open("uniqueWords.txt", 'w')
f3 = open("median.txt", "w")

# Reads, converts to lowercase and stores contents of the text file to the text variable
# It's converted to lowercase to avoid case-sensitive issues
text_file = f.read().lower()

# Separates the text by comma (,) and stores in tweets list
tweets = text_file.split(",")

# Initializing lists and dictionary
words = []
final_words = []
unique_words = []
word_count = {}
# num_count = []

# For loop that splits each tweets variable into its own lists and adds it to the words list
for tweet in tweets:
    words.append(tweet.split())

# For loop that splits up each smaller list within the words list into words and adds it to the words list
for lists in words:
    final_words = final_words + lists

print(final_words)

# For loop that checks how many times a word appears in the list and adds the corresponding info to a dictionary
for word in final_words:
    num = final_words.count(word)
    word_count[word] = num
    num_count = list(word_count.values())
    if num == 1:
        unique_words.append(word)

print(word_count)

# Sorts the num_count and unique_words list
num_count.sort()
unique_words.sort()

# Finds the median using statistics library
median = statistics.median(num_count)

# Writes unique words to text file
f2.write("Unique Words: ")
for word in unique_words:
    f2.write(word + ", ")

# Writes median to text file
f3.write("Median: " + str(median))

# Closes all open file readers
f.close()
f2.close()
f3.close()
