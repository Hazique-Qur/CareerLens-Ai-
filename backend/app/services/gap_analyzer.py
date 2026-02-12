def analyze_skill_gap(user_skills: list, required_skills: list):

    user_skills_lower = [skill.lower() for skill in user_skills]
    required_skills_lower = [skill.lower() for skill in required_skills]

    matched = []
    missing = []

    for skill in required_skills_lower:
        if any(skill in user_skill for user_skill in user_skills_lower):
            matched.append(skill)
        else:
            missing.append(skill)

    match_score = 0
    if required_skills:
        match_score = (len(matched) / len(required_skills)) * 100

    return {
        "match_score": round(match_score, 2),
        "matched_skills": matched,
        "missing_skills": missing
    }
