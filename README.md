# Stock Price Prediction

This project focuses on predicting Google stock price on real time data. I used past 10 years worth of historical Google (GOOGL) stock data for training and built an effective model for predicting stock prices and displayed the predictions on webpage using Flask, Kafka and Highcharts.

![GitHub repo size](https://img.shields.io/github/repo-size/Wolvarun9295/StockMarketPredictionProject?color=2188FC&label=Repo%20Size&style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Wolvarun9295/StockMarketPredictionProject?color=BE33FF&label=Code%20Size&style=plastic)
![GitHub issues](https://img.shields.io/github/issues/Wolvarun9295/StockMarketPredictionProject?color=FF3D37&label=Issues&style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/Wolvarun9295/StockMarketPredictionProject?color=5DFF00&label=Last%20Commit&style=plastic)
[![GitHub license](https://img.shields.io/github/license/Wolvarun9295/StockMarketPredictionProject?color=FF9B23&label=License&style=plastic)](https://github.com/Wolvarun9295/StockMarketPredictionProject/blob/master/LICENSE)

#

## Prerequisites:

- Python3
```
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
```
- [JDK 8 ](https://jdk.java.net/) - [Read this to install Java](https://github.com/Wolvarun9295/InstallationDocuments/blob/master/JAVA.txt)
- [Apache Zookeeper](https://zookeeper.apache.org/releases.html) - [Read this to install Zookeeper](https://github.com/Wolvarun9295/InstallationDocuments/blob/master/ZOOKEEPER.txt)
- [Apache Kafka](https://kafka.apache.org/downloads) – [Read this to run Kafka](https://kafka.apache.org/quickstart)
- [Amazon AWS Account](https://aws.amazon.com/)
- [Google Historical Data](https://in.finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch), download CSV file selecting the range
- [Requirements.txt](Requirements.txt)

Use the following command to install the .txt file:

```
$ sudo pip3 install -r Requirements.txt
```

**NOTE:** This project has been created using Jetbrains PyCharm Community Edition and Visual Studio Code. You can install both from [Snap Store](https://snapcraft.io/)

```
$ sudo apt update
$ sudo apt install snapd
$ sudo snap install pycharm-community –classic
$ sudo snap install code --classic
```
#

## What the project does and how it was made?
- This project has been built using Python3 to help predict the future stock close prices of Google stock with the help of Machine Learning and Data Visualization in real time.
- To start, I created an AWS account and created a user with all access.
- Downloaded the Amazon CLI on my system and then added the AWS access keys to be accessed globally.
- Next I started creating python script to create a bucket and upload the downloaded CSV file onto the AWS bucket. To do this, I needed to install the boto3.

#### ***What is boto3?***
***Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.***

#### ***What is Amazon S3 Bucket?***
***An Amazon S3 bucket is a public cloud storage resource available in Amazon Web Services' (AWS) Simple Storage Service (S3), an object storage offering. Amazon S3 buckets, which are similar to file folders, store objects, which consist of data and its descriptive metadata.***

- After creating and uploading my CSV file, I fetched the file from my S3 bucket with the help of Pandas.
- Since no data is clean and has missing values, it needs to be cleaned.
- Now after the data has been cleaned, we can now built a model using Machine Learning. Keep in mind, the less data we use the higher chances of underfitting occur and the more data we use, the higher chances of overfitting occur. So we need to choose the data not more, not less.
- The model building process has been done using PySpark’s mlib Library.

#### ***What is PySpark?***
***Apache Spark is written in Scala programming language. To support Python with Spark, Apache Spark community released a tool, PySpark. Using PySpark, you can work with RDDs in Python programming language also. It is because of a library called Py4j that they are able to achieve this.***

- I used Linear Regression to train the model and used the Regression Evaluator to give the accuracy of my model.
- After the successfull buliding of my model, I needed to check if it works on real data. For that I registered on a website called AlphaVantage and generated the key to access the live data from their site.

#### ***What is AlphaVantage?***
***Alpha Vantage Inc. is a company that provides realtime and historical stock APIs as well as forex (FX) and digital/crypto currency data feeds.***

- Now comes the fun part of testing the model using Data Visualization.
- For this, firstly I had to install Apache Zookeeper and Apache Kafka.

#### ***What is Apache Zookeeper?***
***ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications. Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable. Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them, which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations of these services lead to management complexity when the applications are deployed.***

#### ***What is Apache Kafka?***
***Apache Kafka is a distributed publish-subscribe messaging system and a robust queue that can handle a high volume of data and enables you to pass messages from one end-point to another. Kafka is suitable for both offline and online message consumption. Kafka messages are persisted on the disk and replicated within the cluster to prevent data loss. Kafka is built on top of the ZooKeeper synchronization service. It integrates very well with Apache Storm and Spark for real-time streaming data analysis.***

- To display the prediction in real time, we first need to start the Zookeeper server and then start the Kafka server.
- I created the Producer and Consumer scripts in Python3 and ran them through Flask app.

#### ***What is Flask?***
***Flask is a web application framework written in Python. Flask is based on the Werkzeug WSGI
toolkit and Jinja2 template engine. The Flask framework uses Werkzeug as one of its bases. Werkzeug is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building a web framework on top of it. Web Server Gateway Interface (WSGI ) is a specification for a universal interface between the web server and the web applications. It has been adopted as a standard for Python web application development. Jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages.***

- Finally, to display the graph I used Highcharts JS in my HTML file and styled it through CSS.

#

## Setup to run the project
### Step 1:
- Create an AWS account. (free for 1 year)
- Login after the account has been successfully created.
- Now go to **IAM** in **Identity and Access Management** services and setup a user with programming access and give full access to the user.
- After the setup, note down the **Public Access Key** and **Secret Access Key**. **(Highly Important)**

### Step 2:
- Install the Amazon CLI (Command Line Interface) on your local machine. (requires curl)
```
$ sudo apt-get install curl
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
$ aws –version
```
- On your local machine, make a folder **.aws** in root folder and touch two files in the folder: **config** and **credentials**. (to make the aws keys globally accessible)
- Add the following lines in **config**:
```
[default]
region=region of your choice
```
- Add the following lines in **credentials**:
```
[default]
aws_access_key_id=your access key
aws_secret_access_key=your secret access key
```
- Now run the following commands to check if the keys are configured and set respectively:
```
$ aws configure
$ aws configure list
```

### Step 3:
In this step we will run all the python scripts in the following order. Note that you can make changes wherever necessary according to your settings.
- Run the **createBucket.py** file. This will create the bucket in the AWS S3.
- Run the **uploadFile.py** file. This will upload the CSV file in your bucket.
- Run the **fetchFile.py** file. This will fetch the CSV file from your bucket.
- Run the **dataCleaner.py** file. This is clean the data in CSV file.
- Run the **modelBuilder.py** file. This will build the model based on the data and save the model. It will be saved in the project folder named **GoogleStockModel**.

**NOTE: Running the modelBuilder.py can also run all the above files sequentially. If you want to test each code, run each one individually.**

### Step 4:
- After building the model, on terminal start the Zookeeper and Kafka servers.
```
$ cd zookeeper
$ ./bin/zkServer.sh start ./conf/zoo.cfg

$ cd kafka
$ ./bin/kafka-server-start.sh ./config/server-properties
```
- Create a **key.txt** file in the project and add your AlphaVantage key in it so that the **Producer.py** file can access it.
- Now run the **Producer.py** file. This will start the Producer that will serve the messages by creating the topic called **GoogleStock**.
- Now run **app.py** file. This will run the **Consumer.py** file and start receiving the messages published by **Producer.py**.
- The **app.py** is the flask application which calls the HTML template in the templates folder which uses the CSS and JS files in the static folder.
- Open the browser to see the graph displayed on **127.0.0.1:5000** shown in the below screeenshot.
<img src=Screenshots/graph.gif height=”100”>

**NOTE:** The graph needs to be kept running for at least 30 mins before it starts giving near accurate predictions, and for over an hour or full market hours to activate the hour and day filters respectively.

#

## Solving error while running project
- ***Two kinds of errors that we face is while running PySpark code: one is py4j error which is solved by installing py4j package. The other is PySpark worker is running in Python2.7 error.***
- To solve the **PYSPARK_PYTHON** and **PYSPARK_DRIVER_PYTHON** error while running PySpark in PyCharm, do the following in files wherever required:
- Click on the **Edit Configurations** besides the Run button.
<img src=Screenshots/edit.png height=”100” >

- In **Environmental Variables**, click on the small page button.
<img src=Screenshots/environmentalVars.png height=”100” >

- And add the following variables in it and click on **OK**  and then **Apply**.
<img src=Screenshots/addingVars.png height=”100” >

#

## Deployment Process
- First create an EC2 instance, download the **filename.pem** file which is available at the time of instance creation.

#### ***What is Amazon EC2?***
***Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction. It provides you with complete control of your computing resources and lets you run on Amazon’s proven computing environment.***

- Now before logging in to the instance, make sure you assign an elastic IP to your instance. For this refer the 7th video of **[this](https://youtu.be/CIVI-DIzCFk)** link first before going forward. This will ensure that your IP address doesn’t change when you stop or reboot the instance and will also save some usage charges.

#### ***What is Amazon Elastic IP address?***
***An Elastic IP address is a reserved public IP address that you can assign to any EC2 instance in a particular region, until you choose to release it. When you associate an Elastic IP address with an EC2 instance, it replaces the default public IP address. If an external hostname was allocated to the instance from your launch settings, it will also replace this hostname; otherwise, it will create one for the instance. The Elastic IP address remains in place through events that normally cause the address to change, such as stopping or restarting the instance.***

- Open the terminal on your local machine and make your filename.pem file readable to avoid permission issues during logging in the instance.
```
$ chmod 400 filename.pem
```
- Now login to the instance using the .pem file and instance address.
```
$ ssh -i filename.pem ubuntu@your.elastic.IP
```
- After successfully logging in your instance, do the following as a good practice:
```
$ sudo apt-get update
$ python3 -V
$ sudo apt-get install python3-pip
```
- Install Java. Refer **[this](#Prerequisites)**
- Next clone your project using git on the instance.
- To ensure everything required package is available on the instance, follow the **[Prerequisites](#Prerequisites)** mentioned above.
- For running the flask app on AWS, we need two additional packages: **nginx** and **gunicorn3** (since project is running on Python3)
```
$ sudo apt-get install nginx
$ sudo apt-get install gunicorn3
```
#### ***What is NGINX?***
***NGINX is open source software for web serving, reverse proxying, caching, load balancing, media streaming, and more. It started out as a web server designed for maximum performance and stability. In addition to its HTTP server capabilities, NGINX can also function as a proxy server for email (IMAP, POP3, and SMTP) and a reverse proxy and load balancer for HTTP, TCP, and UDP servers.***

#### ***What is Gunicorn?***
***Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.***

- Now go in the **sites-enabled** folder inside nginx and do the following:
```
$ cd /etc/nginx/sites-enabled/
$ sudo nano flaskapp
```
- Inside the flaskapp file add the following:
```
server{
	listen : 80;
	server_name : your.elastic.IP;
	location / {
		proxy_pass http://127.0.0.1:8000;
	}
}
```
- Save the above file and restart the nginx service.
```
$ sudo service nginx restart
```
- Follow the videos from **[1–6](https://www.youtube.com/playlist?list=PL5KTLzN85O4KTCYzsWZPTP0BfRj6I_yUP)** for reference.
- Finally start your Zookeeper and Kafka servers on the current terminal as usual.
- Now open two additional terminals and login to the same instance from them and run the **Producer.py** and **app.py** files on each terminals as follows:
```
$ python3 Producer.py
$ gunicorn3 app:app
```
- Now after successfull execution of the flask app, enter **your.elastic.IP** (No port number necessary) in your browser and voila, the flask app is up and running.

#

## Job Scheduling on AWS
- To perform job scheduling on AWS, we need to make four bash executable files: **zookeeper.sh, kafka.sh, ProducerJob.sh and AppJob.sh** and store them in the project directory.
```
# In zookeeper.sh add the following:
/home/ubuntu/zookeeper/bin/zkServer.sh start /home/ubuntu/zookeeper/conf/zoo.cfg

# In kafka.sh add the following:
/home/ubuntu/kafka/bin/kafka-server-start.sh /home/ubuntu/kafka/config/server.properties

# In ProducerJob.sh add the following:
python3 Producer.py

# In AppJob.sh add the following:
gunicorn3 app:app

```
- Save the above four files and make them executable using the following commands:
```
$ chmod u+x zookeeper.sh
$ chmod u+x kafka.sh
$ chmod u+x ProducerJob.sh
$ chmod u+x AppJob.sh
```
- Now check if there are any cron jobs running:
```
$ crontab -l
```
#### ***What is Cron and Crontab?***
***Cron is a scheduling daemon that executes tasks at specified intervals. These tasks are called cron jobs and are mostly used to automate system maintenance or administration.
For example, you could set a cron job to automate repetitive tasks such as backing up databases or data, updating the system with the latest security patches, checking the disk space usage, sending emails, and so on.
The cron jobs can be scheduled to run by a minute, hour, day of the month, month, day of the week, or any combination of these.***
```
* * * * * command(s)
- - - - -
| | | | |
| | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
| | | ------- Month (1 - 12)
| | --------- Day of month (1 - 31)
| ----------- Hour (0 - 23)
------------- Minute (0 - 59)
```
- Now edit the crontab file and add the following:
```
$ crontab -e

# Select nano option

# Add the following in the file (Ex: I want to start my project everyday at 10:30 AM):
30 10 * * * /bin/sh /home/ubuntu/StockMarketPredictionProject/zookeeper.sh
35 10 * * * /bin/sh /home/ubuntu/StockMarketPredictionProject/kafka.sh
40 10 * * * /bin/sh /home/ubuntu/StockMarketPredictionProject/ProducerJob.sh
45 10 * * * /bin/sh /home/ubuntu/StockMarketPredictionProject/AppJob.sh
```
- Save and exit.
- Since we have given 5 minutes interval between all the four files, we need to wait 20 minutes.
- To check if all cron jobs are running as intended, do the following:
```
$ ps -ef | grep filename.sh

# or

$ ps -ef | grep taskname
```
- Now check the output on the browser using **your.elastic.IP**.

#

## References
- [Keith, The Coder – First 3 videos for AWS bucket operations](https://www.youtube.com/playlist?list=PLlQ1p0CY-uJVOXeu6laL4Dqq-Ocabuqbn)
- [Avery Makes Games – AlphaVantage key generating and pulling live stock data](https://youtu.be/339AfkUQ67o)
- [Srce Cde – First 7 videos for deploying flask app on AWS](https://www.youtube.com/playlist?list=PL5KTLzN85O4KTCYzsWZPTP0BfRj6I_yUP)
- [Linux Help – Scheduling the Cron Job on AWS](https://youtu.be/CIVI-DIzCFk)

#

## License and Copyright

© Varun I. Nagrare

Licensed under the [MIT License](LICENSE)
