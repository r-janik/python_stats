from pandas import Series
from statsmodels.tsa.stattools import adfuller


def series_train_test_split(series: Series, split=0.7) -> Series:
    train_size = int(len(series) * split)
    train, test = series[0:train_size], series[train_size:]
    return train, test


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
