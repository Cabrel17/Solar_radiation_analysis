def trend_viz(df, col, country,sampling, year):
    """
    This function plot a trend plot of a variable over time.

    Parameters:
    df (dataframe): dataframe
    col (str): variable of interest
    country (str): define the country
    sampling (str): 'Y' for year, 'M' for mean, 'D' for day ...

    Returns:
    A plot

    """
    import matplotlib.pyplot as plt

    ctr = df[col][df['Country']==country].resample(sampling).agg(['mean','min','max'])
    ctr['mean'][year].plot(label='mean per month')
    plt.fill_between(ctr.index, ctr['max'], ctr['min'], alpha=0.2, label='min_max per month')
    plt.legend()
    plt.title(f'country:{country}, variable:{col}, year:{year}')
    plt.show()
    