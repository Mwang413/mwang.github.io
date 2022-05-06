###
# Muduo Wang
# Jan 2022
# Crypto Analysis Machine

# Comments: wanted to make production grade but it's unfortunately not optimal 
     # because the response of the API needs to be cleaned for model training
     # will still try to use as many functions as possible to save memory for ML training
###

### imports
from asyncio import WriteTransport
from asyncore import file_dispatcher, loop
from gc import get_referents
import async_timeout
from pyparsing import OnlyOnce
import requests, json, subprocess, os

from pprint import pprint

from struct import iter_unpack

from time import sleep
from time import time

from json import dumps, loads

from scipy.fft import dct
import kafka
from kafka import KafkaConsumer, KafkaProducer, TopicPartition
from kafka.vendor.six import Module_six_moves_urllib

from pyspark.context import SparkContext
from pyspark.sql import SparkSession

from pymongo import MongoClient

import tensorflow
from tensorflow import keras

from numpy import array, min_scalar_type

def inits():
     ### init MongoDB
     # connect to MongoDB,
     client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
     db=client.admin
     # Issue the serverStatus command and print the results
     # creating a table name
     db = client.crypto

     # init Kafka
     consumer = KafkaConsumer(
                    bootstrap_servers=['localhost:9092'],
                    auto_offset_reset='earliest',
                    enable_auto_commit=True,
                    group_id='1',
                    value_deserializer=lambda x: loads(x.decode('utf-8')))
     # tracking consumer for end
     topic = "2damoon"
     tp = TopicPartition(topic,0)
     consumer.assign([TopicPartition(topic, 0)])
     consumer.seek_to_end()
     consumer_position = consumer.position(tp)


     ### init api
     with open("/Users/muduo/GitHub/Metanauts_BD/key", "r") as f:
          for line in f:
               key = line

     # init Kafka
     kafka_path = "~/opt/kafka_2.13-3.0.0"
     os.system(kafka_path+"/bin/kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic 2damoon --bootstrap-server localhost:9092")
     producer = KafkaProducer(
          bootstrap_servers=['localhost:9092'],
          value_serializer=lambda x: 
          dumps(x).encode('utf-8')
          )

     os.chdir("/Users/muduo/GitHub/Metanauts_BD/Pipeline2:Crypto/")
     from historical_model_training import make_model
     # make_model(coin_list)
     return producer, consumer_position, tp, key

producer, consumer_position,tp, key = inits()

# Streaming
coin_list = ["BTC"]
def stream_and_process(coin_list = coin_list):
     prices = {}
     for n, coin in enumerate(coin_list): 
          
          # init real-time api
          url = "https://alpha-vantage.p.rapidapi.com/query"

          querystring = {"from_currency":coin,"function":"CURRENCY_EXCHANGE_RATE","to_currency":"USD"}

          headers = {
          'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
          'x-rapidapi-key': key
          }
          
          # pull api
          response = requests.request("GET", url, headers=headers, params=querystring).text
          prices[coin] = {}
          prices[coin]["cur_price"]=float(json.loads(response)["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

          model = keras.models.load_model(f"/Users/muduo/GitHub/Metanauts_BD/Pipeline2:Crypto/{coin}_model")
          prediction = model.predict(array(prices[coin]["cur_price"]).reshape(1,1,1))
          prices[coin]["pred_next"] = float(prediction)
          producer.send("2damoon", json.dumps(prices))

while True:
     if 'aT' not in globals():  # if exists, starting variables here, this will only be ran once
          aT = time()
     else:
          aT = time()
          stream_and_process()
          while True:
               if (time()-aT)  > 20.0: # time passed
                    aT = time()
                    stream_and_process()
                    sleep(5)
                    continue
               else:
                    sleep(5) # prevent crash