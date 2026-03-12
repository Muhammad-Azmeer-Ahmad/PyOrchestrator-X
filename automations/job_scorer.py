from automations.config import KEYWORDS, ROLES


def score_job(text: str) -> int:
    """
    Calculate relevance score for a job posting
    based on keywords and role matching.
    """

    score = 0
    text = text.lower()

    # Keyword relevance
    for kw in KEYWORDS:
        if kw.lower() in text:
            score += 2

    # Role importance
    for role in ROLES:
        if role.lower() in text:
            score += 3

    return score


def classify_job(score: int) -> str:
    """
    Classify job based on score.
    """

    if score >= 10:
        return "HIGH"
    elif score >= 5:
        return "MEDIUM"
    else:
        return "LOW"