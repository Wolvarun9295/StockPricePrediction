from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from CleaningPhase import dataCleaner
import pickle


def modelSaver():
    try:
        X = input("\nDo you want to save the model? Type (Y)es or (N)o: ")
        if X.lower() == "y":
            LRModel.save("GoogleStockModel")
            return print("\nModel saved successfully!")
        elif X.lower() == "n":
            return print("\nModel not saved!")
    except:
        print("Invalid Input! Try Again!")


try:
    print('\nStarting PySpark...')
    pdDataFrame = dataCleaner.df
    sc = SparkContext()
    sparkSession = SparkSession(sc)

    print('\nConverting Pandas DataFrame to PySpark DataFrame:')
    stockData = sparkSession.createDataFrame(pdDataFrame)
    print(stockData)

    print('\nPrinting Schema of PySpark DataFrame:')
    print(stockData.printSchema())

    print("\nPerforming Descriptive Analytics Operations:")
    print(stockData.describe().toPandas().transpose())

    print("\nSeperating the Open, High and Low:")
    featureAssembler = VectorAssembler(inputCols=["Open", "High", "Low"], outputCol="Independent Columns")
    output = featureAssembler.transform(stockData)
    print(output.show())

    print("\nChecking the Vectorized Feature:")
    print(output.select("Independent Columns").show())

    print("\nListing Columns:")
    print(output.columns)

    print("\nGetting Column Sorted:")
    finalData = output.select("Independent Columns", "Close")
    print(finalData.show())

    print("\nDividing Data for Training and Testing:")
    trainData, testData = finalData.randomSplit([0.75, 0.25])

    print("\nBuilding the Model:")
    regressor = LinearRegression(featuresCol='Independent Columns', labelCol='Close')
    regressor = regressor.fit(trainData)

    LR = LinearRegression(featuresCol='Independent Columns', labelCol='Close', maxIter=10, regParam=0.3,
                          elasticNetParam=0.8)
    LRModel = LR.fit(trainData)
    print("Coefficients: " + str(LRModel.coefficients))
    print("Intercept: " + str(LRModel.intercept))

    print("\nTesting the Model:")
    LRPredictions = LRModel.transform(testData)
    print(LRPredictions.select("Close", "Independent Columns", "Prediction").show(5))

    print("\nEvaluating the Model:")
    LREvaluator = RegressionEvaluator(predictionCol="prediction", labelCol="Close", metricName="r2")
    print(f"R Squared (R2) on test data = {LREvaluator.evaluate(LRPredictions)}")

    modelSaver()

    print("\nUsing Pickle:")
    PKLFilename = "PickleLRModel.pkl"
    with open(PKLFilename, 'wb') as file:
        pickle.dump(LRModel, file)

except Exception:
    print("\nSomething went wrong!")
