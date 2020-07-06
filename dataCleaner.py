import fetchFile

print("\nFetching file from AWS Bucket:")
df = fetchFile.fetcher()

try:
    del df['Adj Close']
    print("\nConverting columns to list:")
    print(df.columns.tolist())

    df = df.rename(columns={df.columns[1]: 'Open'})
    df = df.rename(columns={df.columns[2]: 'High'})
    df = df.rename(columns={df.columns[3]: 'Low'})
    df = df.rename(columns={df.columns[4]: 'Close'})

    # The followiong code can be used when there are unwanted characters like $ sign
    # print("\nRemoving characters:")
    # df['Close'] = df['Close'].str.replace(',', '').astype('float')
    # df['Open'] = df['Open'].str.replace(',', '').astype('float')
    # df['High'] = df['High'].str.replace(',', '').astype('float')
    # df['Low'] = df['Low'].str.replace(',', '').astype('float')
    # .str.replace('$', '').astype('float')
    print(df.head())

    print("\nChecking the data types:")
    print(df.dtypes)

    print("\nChecking for null values:")
    print(df.isnull().sum())

except Exception:
    print("Error! Something went wrong!")
