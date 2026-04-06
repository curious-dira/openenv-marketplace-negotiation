from env.models import Reward

def grade_easy(result):
    if result["action"] == "accept":
        return Reward(score=1.0, feedback="Correct")
    return Reward(score=0.0, feedback="Should accept high offer")


def grade_medium(result):
    if result["action"] == "counter":
        return Reward(score=1.0, feedback="Good negotiation")
    elif result["action"] == "accept":
        return Reward(score=0.5, feedback="Okay but not optimal")
    return Reward(score=0.0, feedback="Bad decision")


def grade_hard(result):
    if result["action"] == "reject":
        return Reward(score=1.0, feedback="Correct rejection")
    elif result["action"] == "counter":
        return Reward(score=0.5, feedback="Acceptable")
    return Reward(score=0.0, feedback="Loss-making decision")
