import pandas as pd
import json
from pyspark import SparkContext
from pyspark.sql import SQLContext
from kafka import KafkaConsumer
from pyspark.ml.regression import LinearRegressionModel
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import functions


def StockPricePrediction(LoadModel):
    try:
        for message in Consumer:
            res = json.loads(message.value.decode('utf-8'))
            dlist = list(res.values())
            df = pd.DataFrame([dlist], columns=['Open', 'Close', 'Volume', 'High', 'Low'])
            df = df.astype(float)
            spark_df = sqlContext.createDataFrame(df)
            vectorAssembler = VectorAssembler(inputCols=['Open', 'High', 'Low'], outputCol='Features')
            df_vect = vectorAssembler.transform(spark_df)
            df_vect_features = df_vect.select(['Features', 'Close'])
            predictions = LoadModel.transform(df_vect_features)
            predictions.select("prediction", "Close", "Features").show()
            predict_value = predictions.select(functions.round(predictions["prediction"], 2).alias("prediction")).collect()[0].__getitem__("prediction")
            close_value = predictions.select('Close').collect()[0].__getitem__('Close')
            print(message.key)
            date_time = message.key.decode('utf-8')
            return predict_value, close_value, date_time
    except:
        print("Invalid Column Exception")


sc = SparkContext()
sqlContext = SQLContext(sc)

try:
    ModelPath = "GoogleStockModel"
    LoadModel = LinearRegressionModel.load(ModelPath)
except Exception:
    print("Model NOT Found!")

try:
    Consumer = KafkaConsumer('GoogleStock', bootstrap_servers=['localhost:9092'])
except:
    print('Connection Error!')

# StockPricePrediction(LoadModel)
