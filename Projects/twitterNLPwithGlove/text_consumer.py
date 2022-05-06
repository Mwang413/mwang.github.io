# Imports
from ast import Break
from math import dist
from pendulum import HOURS_PER_DAY
from pyspark.sql.session import SparkSession
import requests
import os
import json
from struct import iter_unpack
from kafka.vendor.six import Module_six_moves_urllib
from time import sleep
from time import time
from kafka import ConsumerRebalanceListener, KafkaConsumer, KafkaProducer, TopicPartition
from json import dumps, loads
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark import RDD, HiveContext
import subprocess
import gensim
from gensim.test.utils import common_texts
from gensim.models import Word2Vec, KeyedVectors
import matplotlib.pyplot as plt

# for storage into Hive
spark = SparkSession.builder.enableHiveSupport().getOrCreate()

# load consumer position
with open ("/Users/muduo/GitHub/Metanauts_BD/Capstone/last",'r') as f:
    last = f.read()

consumer = KafkaConsumer(
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='1',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

topic = "twt_txt"
tp = TopicPartition(topic,0)
consumer.assign([TopicPartition(topic, 0)])
consumer.position(tp)

consumer.end_offsets([tp])[tp]

# clean text function
def txt_2_feature(msg):
    import string
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    
    # split into words by white space
    words = msg.split()
   
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    words = [word.lower() for word in stripped]

    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    
    return words

# load NLP model
# import gensim.downloader
# glove_vectors = gensim.downloader.load('glove-twitter-200')
# glove_vectors.save("/Users/muduo/GitHub/Metanauts_BD/Capstone/word2vec.model")
glove_vectors = KeyedVectors.load("/Users/muduo/GitHub/Metanauts_BD/Capstone/word2vec.model")

all_tops = {}

try:
    spark.sql("drop table Twittertable")
except:
    print('')

for msg in consumer:
    msg = msg.value
    msg = txt_2_feature(msg)
    print(msg)

    # building a theory:
        # each word has a high-dimensional vectoral representation
        # by adding all the vectors of words in sentence together
        # and finding the closest 3
        # returns the 3 most similar words in the sentence
        # this may represent the sentiment of the sentence
        # and thus its most important words

    msg = [word for word in msg if word in glove_vectors]

    # take Euclidean Distance of words to sentence
    # sentence's hypothetical mul-D vector
    hypo = sum([glove_vectors[word] for word in msg])

    # vector squared
    words_vecs = [glove_vectors[word] for word in msg]

    len(words_vecs)
    # take Euclidean Distance
    dists = []
    for i in words_vecs:
        dists.append(abs((hypo**2 - i**2))**0.5) #sqrt

    # low-D representation of distance
    lst = []
    for i in dists:
        lst.append(sum(i))
    low_dists = list(lst)

    # retrieve most similar vectors' index
    lowests = list(sorted(low_dists)[:3])
    most_sim_ws = []
    for n in range(3):
        for n1, i2 in enumerate(low_dists):
            try:
                if low_dists[n1] == lowests[n]:
                    most_sim_ws.append(n1)
            except IndexError:
                continue
    
    tops = []
    for i in most_sim_ws:
        tops.append(msg[i])

    for i in tops:
        if i not in all_tops.keys():
            all_tops[i] = 1
        else:
            all_tops[i] +=1

    try:
        df = zip(tops,[1 for i in range(len(tops))])
        df = spark.createDataFrame(df)
        df = df.withColumnRenamed("_1","current_tops").withColumnRenamed("_2","count")

        df2 = spark.createDataFrame(zip(all_tops.keys(),all_tops.values()))
        df2 = df2.withColumnRenamed("_1","overall").withColumnRenamed("_2","total_count")

        combined = df.join(df2)
        try:
            combined.write.format("orc").saveAsTable("TwitterTable")

        except:
            combined.write.format("orc").mode("append").saveAsTable("TwitterTable")
   
    except:
        continue
    
    plt.plot(all_tops.keys(),all_tops.values())
    plt.plot(tops, [1 for i in range(len(tops))])
    plt.show()
    input("Press Enter to continue...")

    # if consumer.position(tp) == last: #requires a bit more tuning for smoother exits
    #     print("finished extraction")
    #     break


# spark.sql("select * from Twittertable").show()