from pandas import Series, DataFrame
from statsmodels.tsa.stattools import adfuller


def series_train_test_split(series: Series, split=0.7) -> Series:
    train_size = int(len(series) * split)
    train, test = series[0:train_size], series[train_size:]
    return train, test


def moving_average_smoothing(series: Series, window_size: int) -> Series:
    """ Moving average smoothing for cleaning noisy signal """
    return series.rolling(window=window_size).mean()


def series_differentiation(series: Series, order: int) -> Series:
    """
    Timeseries differentiation.Usefull for detrend series
    """
    if order == 1:
        return series.diff()
    if order == 2:
        return series.diff().diff()
    else:
        print("It doesn't have sense ")


def baseline_predictions(train: list, test: list) -> list:
    '''
    Return baseline predictions for naive model
    '''
    history = [x for x in train]
    predictions = list()

    for i in range(len(test)):
        yhat = history[-1]
        predictions.append(yhat)
        # observation
        obs = test[i]
        history.append(obs)
        print('>Predicted=%.3f, Expected=%3.f' % (yhat, obs))

    return predictions


def unit_root_test(series: Series) -> bool:
    "Unit root stationarity test = Adfuller "
    result = adfuller(series.values)
    p_value = result[0]

    if p_value > 0.05:
        print(f"Series is non-stationary, p_value = {p_value}  ")
        return False

    else:
        print(f"Series is stationary, p_value = {p_value}")
        return True


def get_outliers_iqr(df: DataFrame, iqr_mul=3) -> DataFrame:
    """
    Return upper and lower bound of outliers from pandas dataframe based on IQR indicator.
    :param df: Pandas dataFrame
    :param IQR_mul : IQR_mult > 1.5 - normal outliers and extreme outliers, IQR_mul > 3 - extreme outliers
    :return lower_outliers, upper outlliers :
    """
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1

    lower_outliers = df < (Q1 - iqr_mul * IQR)
    upper_outliers = df > (Q3 + iqr_mul * IQR)

    return lower_outliers, upper_outliers
