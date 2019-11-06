python tools/search_tweets.py --credential-file .twitter_keys.yaml --config-file apifinbot.yaml


python tools/search_tweets.py --credential-file .twitter_keys.yaml --config-file apifinbot.yaml  --filter-rule "video lang:fi"


cd data

cat *.csv > tweets.csv
