from CreationPhase import fetchFile

print("\nFetching file from AWS Bucket:")
df = fetchFile.fetcher()

try:
    print("\nConverting columns to list:")
    print(df.columns.tolist())

    df = df.rename(columns={df.columns[1]: 'Close'})
    df = df.rename(columns={df.columns[2]: 'Volume'})
    df = df.rename(columns={df.columns[3]: 'Open'})
    df = df.rename(columns={df.columns[4]: 'High'})
    df = df.rename(columns={df.columns[5]: 'Low'})

    print("\nRemoving characters:")
    df['Close'] = df['Close'].str.replace(',', '').str.replace('$', '').astype('float')
    df['Open'] = df['Open'].str.replace(',', '').str.replace('$', '').astype('float')
    df['High'] = df['High'].str.replace(',', '').str.replace('$', '').astype('float')
    df['Low'] = df['Low'].str.replace(',', '').str.replace('$', '').astype('float')
    print(df.head())

    print("\nChecking the data types:")
    print(df.dtypes)

    print("\nChecking for null values:")
    print(df.isnull().sum())

except Exception:
    print("Error! Something went wrong!")
