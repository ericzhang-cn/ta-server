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
    result = [None if np.isnan(x) or np.isinf(x) else x for x in result]
    return result
