__author__ = "Muduo Wang"
__version__ = "1.0"
__status__ = "Development"
__date__ = "2022-02-04"
__project__ = "Twitter Trends Streaming Analysis"

# Imports
from pyspark.sql.session import SparkSession
import requests
import os
import json
from struct import iter_unpack
from kafka.vendor.six import Module_six_moves_urllib
from time import sleep
from time import time
from kafka import KafkaConsumer, KafkaProducer, TopicPartition
from json import dumps, loads
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark import HiveContext
import subprocess

# Setting authorization
with open ("/Users/muduo/Documents/keys.json")as f:
    for line in f:
        keys = json.loads(line)

keys = keys["Twitter"]
consumer_key= keys["API key"]
consumer_secret= keys["API secret key"]
access_token_key= keys["Access Token"]
access_token_secret= keys["Token Secret"]
bearer_token = keys["Bearer Token"]
search_url = "https://api.twitter.com/2/tweets/search/recent"
keywords = ["cats"]

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

# Initializing Kafka
kafka_path = "~/opt/kafka_2.13-3.0.0"
os.system(kafka_path+"/bin/kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic twitter --bootstrap-server localhost:9092")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                    value_serializer=lambda x: 
                    dumps(x).encode('utf-8'))

query_params = {'query': "cats"}

# This gets exported to consumer in order to configure exiting strategy
topic = "twt_txt"
consumer = KafkaConsumer(
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='1',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

tp = TopicPartition(topic,0)
consumer.assign([TopicPartition('twt_txt', 0)])
consumer.seek_to_end()
consumer.position(tp)
last = consumer.end_offsets([tp])[tp]
with open ("/Users/muduo/GitHub/Metanauts_BD/Capstone/last",'w') as f:
    f.write(str(last))

def query_send():
    json_response = connect_to_endpoint(search_url, query_params)
    msgs = json_response["data"]
    topic = "twt_txt"
    for msg in msgs:
        sleep(0.05)
        producer.send(topic, msg["text"])


while True:
     if 'aT' not in globals():  # create if not exist
          aT = time()
     else:
          aT = time()
          query_send()
          while True:
               if (time()-aT) > 10.0: # time passed
                    aT = time()
                    query_send()
                    sleep(2)
                    continue
               else:
                    sleep(2) # prevent crash