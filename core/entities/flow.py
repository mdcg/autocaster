from typing import List

from pydantic import BaseModel

from core.entities.macro import Macro


class Flow(BaseModel):
    macros: List[Macro]
