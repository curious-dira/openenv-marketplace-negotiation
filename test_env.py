import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from env.env import MarketplaceEnv
from env.models import Action

env = MarketplaceEnv()

obs = env.reset()
print("Observation:", obs)

action = Action(action_type="accept")

result = env.step(action)

print("Result:", result)