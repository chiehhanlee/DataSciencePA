import sys
import json

def main():
    sent_file = open(sys.argv[1])

    #Load Score
    scores = {} 
    for line in sent_file:
        term, score  = line.split("\t") 
        scores[term] = int(score)  
    
    #Load Tweets
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweets = json.loads(line)
        score = 0
        if 'text' in tweets.keys():
            sentence = tweets['text'].split()
            for word in sentence:
                if word in scores:
                    score += scores[word]
        print score 


if __name__ == '__main__':
    main()
