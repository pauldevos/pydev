from dataclasses import dataclass
from datetime import datetime


@dataclass
class Game:
    game_id: int
    game_date: datetime.now().date()
    

@dataclass(slots=True) # match_args, kw_only, slots
class Player:
    play_id: int
    first_name: str
    last_name: str
    jersey_num: int
    position: str
    height_in: int
    weight: int
    

