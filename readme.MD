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
- [x] Develop basic algorithm that can predict prices with a reasonable margin of error
- [x] Add instructions to readme
- [x] Fix output formatting in instructions
- [ ] Research converting generated models to .pb files for serving
- [ ] Fix the serving script and Docker file
- [ ] Figure out how to run on the server (intensive)
- [ ] Develop user interface to interact with POST endpoints in TensorServe
- [ ] Deploy algorithm and UI to web
- [ ] Obtain data weekly/monthly to retrain model
- [ ] Add Sentiment analysis
- [ ] Add Blockchain monitoring

## Instructions
### Pre-requisites
  1. Have Python 3.3 installed and available.
      * Should able to access python from your command-line
  1. Install all dependencies *(Look in the .py file or follow errors in terminal at run)*
### Install and Run
> This process will be evolving over the course of the project. Expected to be complete at each phase.
  1. **From the Command Line** install necessary packages, if you haven't already.
      ```
      pip3 install --upgrade tensorflow
      pip3 install pandas
      pip3 install sklearn
      ```
  1. Run the script
      ```
      python3 cryptornn.py
      ```
### Models and Data
  > In order to see the data models that have been generated, please use the **serveTensorboard .sh** script. This will serve on [localhost:6006](localhost:6006)