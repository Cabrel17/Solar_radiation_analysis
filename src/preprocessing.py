def loading_dataset(filepath):
    """
    This function return a dataframe after creating a new column within of it
    """
    import pandas as pd

    df = pd.read_csv(filepath, index_col=0, parse_dates=True) # definition of Timestamp column as index

    df['Country'] = filepath.split('/')[2].split('-')[0].capitalize() # Creation of a new column

    return df


def outliers(df, colname):
    """
    This function return the list of outliers present in a column of a dataframe
    """
    import pandas as pd

    Q1 = df[colname].quantile(0.25)
    Q3 = df[colname].quantile(0.75)
    IQR = Q3 - Q1

    outliers = df[colname][((df[colname] < (Q1 - 1.5 * IQR)) | (df[colname] > (Q3 + 1.5 * IQR)))]

    return outliers
