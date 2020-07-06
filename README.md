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
- [Google Historical Data](https://in.finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch), dowload CSV file selecting the range
- Requirements.txt

Use the following command to install the .txt file:

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
region=ap-south-1 (This can be the region of your choice)
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

### Step 3:

