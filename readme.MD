# Crypto Price Prediction Algorithm

## Description
> The goal is to create an algorithm for machine learning platform Tensorflow to utilize, which can accurately predict price changes in crypto currency 3 - 4 hours ahead of changes at first. We will utilize a few methodologies to create an accurate learning algorithm.
  1. Past historical data
      * API data sources
      * Live scraping utilizing tools such as Pupateer
  1. Sentiment analysis from multiple source
      * Twitter
      * World news
  1. Monitoring the Blockchain for large transactions in each block


## To-Do
- [ ] Develop basic algorithm that can predict prices with a reasonable margin of error
- [ ] Add instructions to readme
- [ ] Fix output formatting in instructions
- [ ] Research deploying in a Docker/Docker Swarm to improve efficiency
- [ ] Add automatic scrape/addition of data to models daily/hourly/minute
- [ ] Develop user interface to monitor and obtain data as needed
- [ ] Deploy algorithm and UI to web
- [ ] Add Sentiment analysis
- [ ] Add Blockchain monitoring

## Instructions
### Pre-requisites
  1. Have Python 3.3 installed and available.
      * Should able to access python from your command-line
### Install and Run
> This process will be evolving over the course of the project. Expected to be complete at each phase.
  1. **From the Command Line** install necessary packages, if you haven't already.
      ```
      pip install --upgrade tensorflow
      pip install pandas
      ```
  1. Run the script
      ```
      py ./
  >
    *Output should look something like this (sorry for poor formatting...will fix later*
      BTC-USD
      LTC-USD
      XRP-USD
      ETH-USD
      time BTC-USD_close  BTC-USD_volume  LTC-USD_close  LTC-USD_volume  XRP-USD_close  XRP-USD_volume  ETH-USD_close  ETH-USD_volume  future target 2019-05-05 04-PM        5700.62          131.13          75.20         1787.95         0.2971       265583.95         159.78         1899.32  0.2975       1 2019-05-05 3-PM        5711.94          159.90          75.60          320.52         0.2977       218459.12         161.27          571.99  0.2975       0 2019-05-05 02-PM        5721.98          254.09          75.40          627.63         0.2968       216799.99         161.12         1538.07  0.2971       1 2019-05-05 01-PM        5734.00          308.44          75.85         1403.48         0.2975       239693.49         162.06          889.21  0.2982       1 2019-05-05 04-AM        5717.04          355.96          75.59          616.15         0.2989       259390.81         162.08          158.58  0.2993       1