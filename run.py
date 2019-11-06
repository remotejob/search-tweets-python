import pandas as pd
import csv
import uuid
import time
from searchtweets import collect_results,  gen_rule_payload, load_credentials

#FULL 2 words
#words =['enemman','sinne']

#week 10 words maybe 11 
words =['tätä','viestissä','missä','miehet','jota','toinen','voisi','muuten','jotta','ihminen','kansan']
#words =['','','','','','','','','','']
#words =['','','','','','','','','','']
#words =['','','','','','','','','','']
#words =['','','','','','','','','','']
#words =['','','','','','','','','','']







#words =['herralle']


for word in words:
    print(word)

    premium_search_args = load_credentials(".twitter_keys.yaml",yaml_key="search_tweets_api",env_overwrite=False)
    rule = gen_rule_payload(word+" lang:fi",results_per_call=100)

    print(rule)

    tweets = collect_results(rule, max_results=2500, result_stream_args=premium_search_args)

    df = pd.DataFrame(tweets,columns = ['id_str','in_reply_to_status_id_str','truncated','lang','text'])

    uniqfilename = 'data/'+str(uuid.uuid4()) +'.csv'

    print(uniqfilename)

    df.to_csv(uniqfilename,sep='\t',index=False,header=False, quoting=csv.QUOTE_ALL)
    time.sleep(60)


#cat data/*.csv >data/tweets.csv
