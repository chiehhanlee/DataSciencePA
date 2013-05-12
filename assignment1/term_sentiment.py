import sys
import json

ITERATION = 5

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def main():
    sent_file = open(sys.argv[1])
    #Load Score
    n_scores = {} #native score
    for line in sent_file:
        term, score  = line.split("\t") 
        term = term.decode('utf-8')
        n_scores[term] = int(score)  
    
    #Load Tweets
    tweet_file = open(sys.argv[2])

    d_scores = {} #deductive score
    d_cnt   = {}

    for iTimes in xrange(ITERATION):
        for line in tweet_file:
            line = line.decode('utf-8')
            tweets = json.loads(line)
            score = 0
            score_nr = 0
            if 'text' in tweets.keys():
                sentence = tweets['text'].split()
                for word in sentence:
                    if word in n_scores.keys():
                        score += n_scores[word]
                        score_nr +=1
                    if word in d_scores.keys():
                        score += d_scores[word]
                        score_nr +=1

                if score_nr == 0:
                    continue
                for word in sentence:
                    if not word in n_scores:
                        if word in d_cnt:
                            a , b = d_cnt[word]
                            d_cnt[word] = (a+score, b+score_nr)
                        else:
                            d_cnt[word]=(score,score_nr)
        for word in d_cnt.keys():
            score, nr = d_cnt[word]
            d_scores[word] = float(score)/nr

#    for word in n_scores.keys():
#        if is_ascii(word):
#            #print unicode(word,'utf-8'), n_scores[word]
#            print word, n_scores[word]


    for word in d_scores.keys():
        if is_ascii(word):
            #print unicode(word,'utf-8'), d_scores[word]
            print word, d_scores[word]

if __name__ == '__main__':
    main()
