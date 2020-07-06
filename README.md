# Stock Price Prediction

This project focuses on predicting Google stock price on real time data. I used past 10 years worth of historical Google (GOOGL) stock data for training and built an effective model for predicting stock prices and displayed the predictions on webpage using Flask, Kafka and Highcharts.

## Prerequisites:

- Python3
```
sudo apt-get install python3
sudo apt-get install python3-pip
```
- [JDK 8 ](https://jdk.java.net/)
- [Apache Zookeeper](https://zookeeper.apache.org/)
- [Apache Kafka](https://kafka.apache.org/downloads)
- [Amazon AWS Account](https://aws.amazon.com/)
- [Google Historical Data](https://in.finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch), download CSV file selecting the range
- Requirements.txt

Use the following command to install the .txt file:

```
sudo pip3 install -r Requirements.txt
```

**NOTE:** This project has been created using Jetbrains PyCharm Community Edition and Visual Studio Code. You can install both from [Snap Store](https://snapcraft.io/)

```
sudo apt update
sudo apt install snapd
sudo snap install pycharm-community –classic
sudo snap install code --classic
```
## 

## What the project does and how it was made?
- This project has been built using Python3 to help predict the future stock close prices of Google stock with the help of Machine Learning and Data Visualization in real time.
- To start, I created an AWS account and created a user with all access.
- Downloaded the Amazon CLI on my system and then added the AWS access keys to be accessed globally.
- Next I started creating python script to create a bucket and upload the downloaded CSV file onto the AWS bucket. To do this, I needed to install the boto3.

### What is boto3?
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.

### What is Amazon S3 Bucket?
An Amazon S3 bucket is a public cloud storage resource available in Amazon Web Services' (AWS) Simple Storage Service (S3), an object storage offering. Amazon S3 buckets, which are similar to file folders, store objects, which consist of data and its descriptive metadata.

- After creating and uploading my CSV file, I fetched the file from my S3 bucket with the help of PySpark.



## Setup to run the project
### Step 1:
- Create an AWS account. (free for 1 year)
- Login after the account has been successfully created.
- Now go to **IAM** in **Identity and Access Management** services and setup a user with programming access and give full access to the user.
- After the setup, note down the **Public Access Key** and **Secret Access Key**. (**Highly Important**)

### Step 2:
- Install the Amazon CLI (Command Line Interface) on your local machine. (requires curl)
```
sudo apt-get install curl
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws –version
```
- On your local machine, make a folder **.aws** in root folder and touch two files in the folder: **config** and **credentials**. (to make the aws keys globally accessible)
- Add the following lines in config:
```
[default]
region=region of your choice
```
- Add the following lines in credentials:
```
[default]
aws_access_key_id=your access key
aws_secret_access_key=your secret access key
```
- Now run the following commands to check if the keys are configured and set respectively:
```
aws configure
aws configure list
```


