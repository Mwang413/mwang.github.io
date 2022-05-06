from urllib import response
import requests
import json
import tensorflow as tf
import datetime, time
from tensorflow import keras
from numpy import array

def make_model(coins = ["BTC"]):

     for coin in coins:
          coin = "BTC"
          url = f'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_{coin}_USD/history?period_id=5MIN&time_start=2021-12-20T00:00:00&limit=10000'
          headers = {'X-CoinAPI-Key' : 'D2FE03D2-98FB-4DB9-BD04-3DB57D7F02F6'}
          response = requests.get(url, headers=headers)
          response = response.text
          dumps = json.dumps(response.text)

          json.loads(response)
          out_dict = {}
          for n,i in enumerate(json.loads(response)):
               out_dict[n] = i

          with open ("/Users/muduo/GitHub/Metanauts_BD/Pipeline 2: Crypto/api_response.json","w") as f:
               json.dump(fp = f, obj = out_dict)

          data = json.load(open("/Users/muduo/GitHub/Metanauts_BD/Pipeline 2: Crypto/api_response.json"))
          prices = [i["price_high"] for i in list(data.values())]
          timex = [i["time_period_start"] for i in list(data.values())]
          timex = [timex[i].replace("T","-")[:-12] for i, _ in enumerate(timex)]
          timex = [time.mktime(datetime.datetime.strptime(timex[i], "%Y-%m-%d-%H:%M").timetuple()) for i,_ in enumerate(timex)]

          timex = array(timex)
          timex = timex.reshape((len(timex), 1))

          # get next interval
          next_prices = [prices[n+1] for n,i in enumerate(prices[:-1])]
          prices = prices[:-1] # remove the end
          timex = timex[:-1]

          pcArr = array(prices)
          pcArr=pcArr.reshape((len(prices),1,1))
          pcArr.shape
          len(next_prices)

          from tensorflow.keras import metrics

          model = keras.models.Sequential()
          model.add(keras.layers.LSTM(128, input_shape=(1,1), return_sequences = True))
          model.add(keras.layers.Dropout(0.2))
          model.add(keras.layers.Dense(64))
          model.add(keras.layers.Dense(8))
          model.add(keras.layers.Dense(1))
          model.compile(loss='mse', optimizer='adam', metrics=["mape",'mae','mse'])
          model.build()
          history = model.fit(pcArr, array(next_prices), verbose = 1, epochs = 250, batch_size=32, validation_split=0.2)

          import matplotlib.pyplot as plt
          plt.plot(history.history["loss"])
          plt.plot(history.history["mae"])
          plt.legend(["loss","mae"])
          plt.show()

          model.save(f"/Users/muduo/GitHub/Metanauts_BD/Pipeline 2: Crypto/{coin}_model")