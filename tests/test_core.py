import numpy as np

from ta_server.core import run_ta_function, list_ta_functions


def test_run_ta_function():
    open_ = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    high = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    low = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    close = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    volume = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    result = run_ta_function(
        func_name='SMA',
        open_=open_,
        high=high,
        low=low,
        close=close,
        volume=volume,
        timeperiod=2,
    )
    assert result is not None
    assert len(result) == 5
    assert np.allclose(
        result,
        np.array(
            [
                np.nan,
                0.15,
                0.25,
                0.35,
                0.45,
            ]
        ),
        equal_nan=True,
    )


def test_list_ta_functions():
    functions = list_ta_functions()
    assert len(functions) > 0
