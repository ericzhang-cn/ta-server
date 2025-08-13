from typing import Union, Any

from pydantic import BaseModel


class TAFunction(BaseModel):
    """TA function model."""

    name: str
    group: str


class CalculateRequest(BaseModel):
    """Calculate request model."""

    func_name: str
    open: Union[list[float], None] = None
    high: Union[list[float], None] = None
    low: Union[list[float], None] = None
    close: Union[list[float], None] = None
    volume: Union[list[float], None] = None
    params: dict[str, Any] = {}
    output_labels: list[str] = []
