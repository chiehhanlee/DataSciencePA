import sys
import json
from collections import Counter

def is_entity_exist(obj):
    if u'entities' in obj.keys():
        return True
    return False

def is_hashtag_exit(obj):
    if u'hashtags' in obj.keys():
        return True
    return False

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def main():
    tagCnt = Counter()
    
    #Load Tweets
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        tweets = json.loads(line)

        if not is_entity_exist(tweets):
            continue
        if not is_hashtag_exit(tweets[u'entities']):
            continue
        for tag in tweets['entities']['hashtags']:
            if 'text' in tag.keys():
                if is_ascii(tag['text']):
                    tagCnt[tag['text']] +=1

    tagl = []
    for key in  tagCnt.keys():
        tagl.append((key,tagCnt[key]))

    tagl.sort(key = lambda tup : tup[1], reverse=True)

    for i in xrange(10):
        key , cnt = tagl[i]
        print key , float(cnt)


if __name__ == '__main__':
    main()
