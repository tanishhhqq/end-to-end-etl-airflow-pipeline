def transform_data(df):

    # lowercase columns
    df.columns = [
        col.lower().replace(' ', '_')
        for col in df.columns
    ]

    # remove null values
    df = df.dropna()

    # convert sales to float
    if 'sales' in df.columns:
        df['sales'] = df['sales'].astype(float)

    print("Transformation completed")

    return df