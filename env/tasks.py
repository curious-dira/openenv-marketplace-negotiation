from graders import grade_easy, grade_medium, grade_hard

task_easy = {
    "name": "high_offer",
    "data": {"listed_price": 1000, "buyer_offer": 950},
    "grader": grade_easy
}

task_medium = {
    "name": "low_offer",
    "data": {"listed_price": 1000, "buyer_offer": 600},
    "grader": grade_medium
}

task_hard = {
    "name": "very_low_offer",
    "data": {"listed_price": 1000, "buyer_offer": 300},
    "grader": grade_hard
}

ALL_TASKS = [task_easy, task_medium, task_hard]
