from typing import List

from pydantic import BaseModel


class Macro(BaseModel):
    hotkey: List
    many_times: int
    interval_between_hotkeys: int
    sleep_time: int
