from pandas import Series
from statsmodels.tsa.stattools import adfuller

def series_train_test_split(series : Series,split = 0.7) -> Series :
    train_size = int(len(series)*split)
    train,test = series[0:train_size], series[train_size:]
    return train,test





def unit_root_test(series : Series) -> bool:
    "Unit root stationarity test = Adfuller "
    result = adfuller(series.values)
    p_value = result[0]

    if p_value > 0.05:
        print(f"Series is non-stationary, p_value = {p_value}  ")
        return False

    else:
        print(f"Series is stationary, p_value = {p_value}")
        return True


