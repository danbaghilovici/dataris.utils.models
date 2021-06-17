from __future__ import annotations
from typing import TypedDict,Union,List

class IUNCTIOCompositionOperation(TypedDict):
    result:any
    time:Union[int,float]
    iteration:int
    name:any
    done:bool
    errors:List[Union[Exception]]
    warnings:List[any]