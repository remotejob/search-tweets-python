import pandas as pd
import csv
from searchtweets import collect_results,  gen_rule_payload, load_credentials


premium_search_args = load_credentials(".twitter_keys.yaml",yaml_key="search_tweets_api",env_overwrite=False)

# rule = gen_rule_payload("seksi lang:fi",
#                         from_date="2007-01-01", #UTC 2017-09-01 00:00
#                         to_date="2019-01-01",#UTC 2017-10-30 00:00
#                         results_per_call=100)
rule = gen_rule_payload("pornoa lang:fi",results_per_call=100)

print(rule)

tweets = collect_results(rule, max_results=2000, result_stream_args=premium_search_args)


# print(tweets)

# with open('tweets.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     [employee_writer.writerow([tweet.id,tweet.in_reply_to_status_id,tweet.generator.get("truncated"),tweet.all_text]) for tweet in tweets]


df = pd.DataFrame(tweets,columns = ['id_str','in_reply_to_status_id_str','truncated','lang','text'])

df.to_csv('data/tweets.csv',sep='\t',index=False,header=False, quoting=csv.QUOTE_ALL)


[print(tweet, end='\n') for tweet in tweets]