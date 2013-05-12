from collections import Counter
import sys
import json

def is_in_us(obj):
    if type(obj) != dict:
        return False
    if not 'place' in obj:
        return False
    if type(obj['place']) != dict:
        return False
    if not 'country_code' in obj['place']:
        return False
    if obj['place']['country_code']=='US':
        return True
    return False

def get_state_name_by_place(obj):
    if type(obj) != dict:
        return False
    if not 'place' in obj:
        return False
    if type(obj['place']) != dict:
        return False
    if not 'full_name' in obj['place']:
        return False
    fullname , abname = obj['place']['full_name'].split(',')
    return abname

def get_state_name_by_usr(obj):
    return False
    if type(obj) != dict:
        return False
    if not 'user' in obj:
        return False
    if type(obj['user']) != dict:
        return False
    if not 'location' in obj['user']:
        return False
    fullname , abname = obj['user']['location'].split(',')
    return abname

def main():
    sent_file = open(sys.argv[1])

    #Load Score
    scores = {} 

    stateScore = Counter()
    stateCnt = Counter()

    for line in sent_file:
        term, score  = line.split("\t") 
        scores[term] = int(score)  
    
    #Load Tweets
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweets = json.loads(line)
        score = 0

        state = False

        if is_in_us(tweets):
            state = get_state_name_by_place(tweets)
        #else:
        #    state = get_state_name_by_usr(tweets)
        #state = get_state_name_by_usr(tweets)
        if state == False:
            continue

        if 'text' in tweets.keys():
            sentence = tweets['text'].split()
            for word in sentence:
                if word in scores:
                    score += scores[word]
            stateScore[state] += score
            stateCnt[state] +=1

    maxArg = None
    maxScr = None

    for sta in stateScore.keys():
        score = float(stateScore[sta])/stateCnt[sta]
        if score > maxScr:
            maxScr = score
            maxArg = sta
    print sta

if __name__ == '__main__':
    main()
