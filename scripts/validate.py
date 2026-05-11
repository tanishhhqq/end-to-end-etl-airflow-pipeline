def validate_data(df):

    if df.empty:
        raise Exception("DataFrame is empty")

    if df.isnull().sum().sum() > 0:
        raise Exception("Null values found")

    print("Validation successful")