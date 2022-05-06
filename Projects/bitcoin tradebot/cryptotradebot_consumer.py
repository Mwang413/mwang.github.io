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
from gc import get_referents
import requests, json, subprocess, os

from pprint import pprint

from struct import iter_unpack

from time import sleep, time

from json import dumps, loads

from scipy.fft import dct
import kafka
from kafka import KafkaConsumer, KafkaProducer, TopicPartition
from kafka.vendor.six import Module_six_moves_urllib

from pyspark.context import SparkContext
from pyspark.sql import SparkSession

from pymongo import MongoClient

from tensorflow import keras

### init MongoDB
# connect to MongoDB,
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(str(serverStatusResult)[0:100]) if len(str(serverStatusResult))>50 else None
# creating a table name
db = client.cryptobets
serverStatusResult=db.command("serverStatus")
# print first 150 characters
pprint(str(serverStatusResult)[0:100]) if len(str(serverStatusResult))>50 else None

### init api
with open("/Users/muduo/GitHub/Metanauts_BD/key", "r") as f:
     for line in f:
          key = line

import os
os.chdir("/Users/muduo/GitHub/Metanauts_BD/Pipeline2:Crypto/")

# init kafka
from cryptotradebot_producer import consumer_position, tp, coin_list
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
consumer.seek(tp, consumer_position)

for message in consumer:
     message = message.value
     prices = json.loads(message)   
     for n, coin in enumerate(coin_list):
          prediction = prices[coin]["pred_next"]
          
          current_price = float(prices[coin]["cur_price"])
          
          if (prediction - current_price)/current_price >= 1.05: # 5 percent profit
               # buy coin
               continue

          # cached for later use, update cache each loop
          global cached_pred
          if "cached_pred" not in globals(): # creates var at the beginning of the iterations
               cached_pred = {}
          cached_pred[coin] = prediction
          print("\n"*10, cached_pred)

          if n >= 1:
               # we will only consider "going long" on coins
               # check if our previous prediction was good or bad
               # conditional trigger model update

               model = keras.models.load_model(f"/Users/muduo/GitHub/Metanauts_BD/Pipeline2:Crypto/{coin}_model")
               cur_price = prices[coin]["cur_price"]
               if (cur_price/cached_pred[coin])>1.1 or (cur_price/cached_pred[coin])<0.99: # if loss > 1% or if profit > 10%
                    num_epochs = int(10000+len(prices)/50) # reweight/discipline our model 2% of total observations (we started with around 10000 observations)
                    
                    model.fit(cached_pred[coin], cur_price, epochs=num_epochs)
                    model.save(f"/Users/muduo/GitHub/Metanauts_BD/Pipeline2:Crypto/{coin}_model")
          
          # problem is that if we our model keeps performing really well, the data will not be maintained properly
          '''
          Implement Maintenance of Database here: deleting oldest archived record per interval
          Other types of model maintenance
          '''
     # Insert file into MongoDB at the end of interval
     result = db.cryptobets.insert_one(prices)
     print(f'Stored as {result.inserted_id}')
     for x in db.cryptobets.find():
          print(x)
     del cached_pred # reset this value at the end of the interval

