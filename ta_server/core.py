from typing import Union

import numpy as np
import talib
from talib import abstract

from ta_server.model import TAFunction


def run_ta_function(
    *,
    func_name: str,
    open_: Union[np.ndarray, None] = None,
    high: Union[np.ndarray, None] = None,
    low: Union[np.ndarray, None] = None,
    close: Union[np.ndarray, None] = None,
    volume: Union[np.ndarray, None] = None,
    **kwargs,
):
    """Run TA function.

    :param func_name: TA function name.
    :param open_: Open price.
    :param high: High price.
    :param low: Low price.
    :param close: Close price.
    :param volume: Volume.
    :param kwargs: TA function arguments.
    :return: TA function result.
    """
    ta_function = abstract.Function(func_name)
    return ta_function(
        {
            'open': open_,
            'high': high,
            'low': low,
            'close': close,
            'volume': volume,
        },
        **kwargs,
    ).tolist()


def list_ta_functions() -> list[TAFunction]:
    """List TA functions.

    :return: List of TA functions.
    """
    functions = []
    for group, names in talib.get_function_groups().items():
        for name in names:
            functions.append(TAFunction(name=name, group=group))
    return functions
