import pandas as pd

SEQ_LEN = 60  # how long of a preceeding sequence to collect for RNN
FUTURE_PERIOD_PREDICT = 3  # how far into the future are we trying to predict?
RATIO_TO_PREDICT = "XRP-USD"

main_df = pd.DataFrame() # begin empty

ratios = ["BTC-USD", "LTC-USD", "XRP-USD", "ETH-USD"] # the 4 ratios we want to consider

for ratio in ratios:  # begin iteration
    print(ratio)
    dataset = f'./data/{ratio}.csv'  # get the full path to the file.
    df = pd.read_csv(dataset, names=['time', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'vol_usd'])  # read in specific file

    # rename volume and close to include the ticker so we can still which close/volume is which:
    df.rename(columns={"close": f"{ratio}_close", "volume": f"{ratio}_volume"}, inplace=True)

    df.set_index("time", inplace=True)  # set time as index so we can join them on this shared time
    df = df[[f"{ratio}_close", f"{ratio}_volume"]]  # ignore the other columns besides price and volume

    if len(main_df)==0:  # if the dataframe is empty
        main_df = df  # then it's just the current df
    else:  # otherwise, join this data to the main one
        main_df = main_df.join(df)

main_df.fillna(method="ffill", inplace=True)  # if there are gaps in data, use previously known values
main_df.dropna(inplace=True)

def classify(current, future):
    if float(future) > float(current):
        return 1
    else:
        return 0

main_df['future'] = main_df[f'{RATIO_TO_PREDICT}_close'].shift(-FUTURE_PERIOD_PREDICT)
main_df['target'] = list(map(classify, main_df[f'{RATIO_TO_PREDICT}_close'], main_df['future']))

print(main_df.head())