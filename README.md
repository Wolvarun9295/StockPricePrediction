# Stock Price Prediction

This project focuses on predicting Google stock price on real time data. I used past 10 years worth of historical Google (GOOGL) stock data for training and built an effective model for predicting stock prices and displayed the predictions on webpage using Flask, Kafka and Highcharts. Then deployed my project on AWS EC2 instance.

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
- Requirements.txt

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:

```
sudo pip3 install -r Requirements.txt
```

NOTE: This project has been created using Jetbrains PyCharm Community Edition and Visual Studio Code. You can install both from [Snap Store](https://snapcraft.io/)

```
sudo apt update
sudo apt install snapd
sudo snap install pycharm-community –classic
sudo snap install code --classic
```

## Usage
## Step 1:
- Create an AWS account (Free for 1 year)
- Login after the account has been successfully created
- Now go to IAM in Identity and Access Management services and setup a user with programming access.
- After the setup, note down the Public Access Key and Secret Access Key (Highly Important)
