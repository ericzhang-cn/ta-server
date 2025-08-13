import numpy as np
from fastapi import FastAPI

from ta_server.core import list_ta_functions, run_ta_function
from ta_server.model import CalculateRequest

app = FastAPI()


@app.get('/functions/')
def show_functions():
    """Show TA functions."""
    return list_ta_functions()


@app.post('/calculate/')
def run_function(req: CalculateRequest):
    """Run TA function."""
    result = run_ta_function(
        func_name=req.func_name,
        open_=np.array(req.open),
        high=np.array(req.high),
        low=np.array(req.low),
        close=np.array(req.close),
        volume=np.array(req.volume),
        **req.params,
    )
    if isinstance(result, np.ndarray):
        if len(req.output_labels) > 0:
            output_label = req.output_labels[0]
        else:
            output_label = 'output_0'
        return {
            output_label: [
                x if (not np.isnan(x) and not np.isinf(x)) else None
                for x in result
            ]
        }
    elif isinstance(result, list):
        if len(req.output_labels) >= len(result):
            output_labels = req.output_labels
        else:
            output_labels = [f'output_{i}' for i in range(len(result))]
        return {
            output_labels[i]: [
                x if (not np.isnan(x) and not np.isinf(x)) else None for x in y
            ]
            for i, y in enumerate(result)
        }
