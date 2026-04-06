from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    item_price: float
    buyer_offer: float
    seller_min_price: float


class Action(BaseModel):
    action_type: str  # "accept", "reject", "counter"
    counter_offer: Optional[float] = None


class Reward(BaseModel):
    score: float
    feedback: str