import json
import random
from typing import Tuple, Dict, Any

from .models import Observation, Action, Reward


class MarketplaceEnv:
    def __init__(self, scenario_path: str = "tasks/scenarios.json"):
        self.scenario_path = scenario_path
        self.scenarios = self._load_scenarios()
        self.current_state: Observation = None

    def _load_scenarios(self):
        with open(self.scenario_path, "r") as f:
            data = json.load(f)
        return data

    def reset(self) -> Observation:
        scenario = random.choice(self.scenarios)

        self.current_state = Observation(
            item_price=scenario["item_price"],
            buyer_offer=scenario["buyer_offer"],
            seller_min_price=scenario["seller_min_price"]
        )

        return self.current_state

    def step(self, action: Action) -> Tuple[Observation, Reward, bool, Dict[str, Any]]:
        if self.current_state is None:
            raise ValueError("Call reset() before step()")
        
        obs = self.current_state

        reward = self._calculate_reward(obs, action)

        done = True

        info = {"action_taken": action.action_type}

        return obs, reward, done, info

    def state(self) -> Observation:
        return self.current_state

    def _calculate_reward(self, obs: Observation, action: Action) -> Reward:

        if action.action_type == "accept":
            if obs.buyer_offer >= obs.seller_min_price:
                return Reward(score=1.0, feedback="Accepted good deal")
            else:
                return Reward(score=0.2, feedback="Accepted bad deal")

        elif action.action_type == "reject":
            if obs.buyer_offer < obs.seller_min_price:
                return Reward(score=0.8, feedback="Correct rejection")
            else:
                return Reward(score=0.3, feedback="Rejected good deal")

        elif action.action_type == "counter":
            if action.counter_offer is None:
                return Reward(score=0.0, feedback="No counter offer")

            if obs.seller_min_price <= action.counter_offer <= obs.item_price:
                return Reward(score=0.9, feedback="Good counter")
            else:
                return Reward(score=0.4, feedback="Bad counter")

        else:
            return Reward(score=0.0, feedback="Invalid action")