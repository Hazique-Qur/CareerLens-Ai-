ROLE_SKILLS_DB = {
    "Data Scientist": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "Statistics",
        "Pandas",
        "NumPy",
        "Data Visualization",
        "Scikit-learn",
        "TensorFlow"
    ],
    "UX Designer": [
        "Figma",
        "User Research",
        "Wireframing",
        "Prototyping",
        "Usability Testing",
        "Design Systems",
        "Interaction Design"
    ],
    "Frontend Developer": [
        "JavaScript",
        "React",
        "HTML",
        "CSS",
        "Next.js",
        "Tailwind",
        "REST APIs"
    ]
}

def get_role_skills(role: str):
    # Dynamic Role Matching
    role_map = {
        "data-scientist": "Data Scientist",
        "ux-designer": "UX Designer",
        "frontend": "Frontend Developer",
        "product-manager": "Product Manager",
        "backend": "Backend Engineer"
    }
    
    # Normalize input
    target_role = role_map.get(role.lower(), role)
    
    # Add new role if missing but common
    if target_role not in ROLE_SKILLS_DB and target_role == "Backend Engineer":
        ROLE_SKILLS_DB["Backend Engineer"] = ["Python", "SQL", "Docker", "REST APIs", "FastAPI", "PostgreSQL", "Unit Testing"]
    
    if target_role not in ROLE_SKILLS_DB and target_role == "Product Manager":
        ROLE_SKILLS_DB["Product Manager"] = ["Agile", "User Stories", "Roadmapping", "Market Research", "Jira", "A/B Testing"]

    # Default fallback for unknown roles
    return ROLE_SKILLS_DB.get(target_role, ["Communication", "Problem Solving", "Teamwork", "Adaptability", "Critical Thinking"])
