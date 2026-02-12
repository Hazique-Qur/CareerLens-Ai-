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
        # Calculate raw match
        raw_match = (len(matched) / len(required_skills)) * 100
        
        # provide a baseline score if we found any technical skills at all
        # this avoids the demoralizing "0%" for valid resumes
        if len(matched) > 0:
            match_score = max(20, raw_match)
        elif len(user_skills) > 0:
            match_score = 15 # Baseline for "some effort"
        else:
            match_score = 5 # Minimum for uploading a file

    return {
        "match_score": min(95, round(match_score, 2)), # Cap slightly below 100 for modesty
        "matched_skills": matched,
        "missing_skills": missing
    }
