"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float|int]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    rounded_scores = []

    for score in student_scores:
        rounded_score = round(score)
        rounded_scores.append(rounded_score)

    return rounded_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    others = list()

    for score in student_scores:
        if score <= 40:
            others.append(score)

    return len(others)
