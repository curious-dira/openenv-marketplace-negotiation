from env.env import MarketEnv
from tasks import ALL_TASKS
from env.models import Action

def simple_agent(obs):
    if obs.buyer_offer > 0.9 * obs.listed_price:
        return Action(action_type="accept")
    elif obs.buyer_offer > 0.5 * obs.listed_price:
        return Action(action_type="counter")
    else:
        return Action(action_type="reject")


def run():
    total_score = 0

    for task in ALL_TASKS:
        env = MarketEnv(task)
        obs = env.reset()

        action = simple_agent(obs)

        _, reward, _, _ = env.step(action)

        print(f"{task['name']} → {reward.score}")

        total_score += reward.score

    print("\nFinal Score:", total_score)


if __name__ == "__main__":
    run()
