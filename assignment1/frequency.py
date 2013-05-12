from collections import Counter

import sys
import json

def main():
    
    #Load Tweets
    tweet_file = open(sys.argv[1])

    tkCnt = Counter()
    totalCnt =0
    for line in tweet_file:
        tweets = json.loads(line)
        score = 0
        if 'text' in tweets.keys():
            sentence = tweets['text'].split()
            for word in sentence:
                tkCnt[word] +=1
                totalCnt +=1
  
    for terms in tkCnt.keys():
        print terms , float(tkCnt[terms])/totalCnt

if __name__ == '__main__':
    main()
