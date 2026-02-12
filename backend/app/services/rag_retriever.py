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
        "JavaScript", "JS", "React", "React.js", "HTML", "CSS", "HTML5", "CSS3", "Next.js", "Tailwind", "REST APIs", "Frontend", "Web Development", "UI", "UX", "Responsive Design"
    ],
    "Mobile Developer": [
        "Swift", "Kotlin", "React Native", "Flutter", "iOS Development", "Android Development", "Mobile Design", "Firebase", "App Store", "Play Store"
    ],
    "Backend Engineer": [
        "Python", "Node.js", "Java", "Go", "SQL", "PostgreSQL", "MongoDB", "Redis", "REST APIs", "GraphQL", "Microservices", "Docker", "FastAPI", "Backend", "APIs", "Database Design", "Unit Testing"
    ],
    "Product Manager": [
        "Agile", "User Stories", "Roadmapping", "Market Research", "Jira", "A/B Testing", "Product Strategy", "Stakeholder Management", "UX Research"
    ],
    "DevOps Engineer": [
        "CI/CD", "Kubernetes", "K8s", "Docker", "AWS", "Azure", "GCP", "Terraform", "Jenkins", "Linux", "Monitoring", "Cloud", "Automation", "Git", "SRE"
    ],
    "Fullstack Developer": [
        "JavaScript", "React", "Node.js", "Python", "SQL", "HTML", "CSS", "Next.js", "REST APIs", "Fullstack", "Web Architecture"
    ],
    "Cybersecurity Analyst": [
        "Security", "Cybersecurity", "Network Security", "Penetration Testing", "Pentesting", "Risk Assessment", "Encryption", "SOC", "Vulnerability", "Compliance", "Firewall", "Identity Management"
    ],
    "AI/ML Engineer": [
        "Python", "Deep Learning", "NLP", "Computer Vision", "PyTorch", "TensorFlow", "Model Deployment", "MLOps", "Data Engineering"
    ],
    "Data Analyst": [
        "SQL", "Excel", "Tableau", "Power BI", "Python", "Statistics", "Data Cleaning", "Reporting", "A/B Testing"
    ],
    "Cloud Architect": [
        "AWS", "Azure", "Google Cloud", "Cloud Security", "Serverless", "Networking", "Microservices", "Infrastructure as Code", "Cost Optimization"
    ],
    "QA Engineer": [
        "Selenium", "Automation Testing", "Unit Testing", "Jira", "Regression Testing", "Postman", "API Testing", "CI/CD"
    ],
    "Embedded Systems Engineer": [
        "C", "C++", "RTOS", "Microcontrollers", "Embedded C", "Microprocessors", "I2C/SPI", "Hardware Debugging"
    ],
    "Data Engineer": [
        "ETL", "Spark", "Hadoop", "SQL", "Python", "Data Warehousing", "Airflow", "NoSQL", "Snowflake", "Data Pipelines"
    ],
    "Game Developer": [
        "Unity", "C#", "C++", "Unreal Engine", "Game Design", "Shaders", "Physics Engines", "3D Math", "Game Mechanics"
    ],
    "Blockchain Engineer": [
        "Solidity", "Ethereum", "Smart Contracts", "Cryptography", "Web3.js", "Hardhat", "Rust", "Hyperledger", "DeFi"
    ],
    "Technical Writer": [
        "Documentation", "Markdown", "API Documentation", "DITA", "MadCap Flare", "Copywriting", "Instructional Design", "Software Documentation"
    ],
    "Security Consultant": [
        "Risk Assessment", "Compliance", "Security Auditing", "ISO 27001", "Threat Modeling", "Incident Response", "Identity Management"
    ],
    "Systems Architect": [
        "Distributed Systems", "System Design", "Microservices", "Cloud Architecture", "Scalability", "Reliability Engineering", "Network Protocols"
    ]
}

def get_role_skills(role: str):
    # Dynamic Role Matching
    role_map = {
        "data-scientist": "Data Scientist",
        "ux-designer": "UX Designer",
        "frontend": "Frontend Developer",
        "product-manager": "Product Manager",
        "backend": "Backend Engineer",
        "mobile": "Mobile Developer",
        "devops": "DevOps Engineer",
        "fullstack": "Fullstack Developer",
        "security": "Cybersecurity Analyst",
        "ai-ml": "AI/ML Engineer",
        "data-analyst": "Data Analyst",
        "cloud-architect": "Cloud Architect",
        "qa-engineer": "QA Engineer",
        "embedded": "Embedded Systems Engineer",
        "data-engineer": "Data Engineer",
        "game-dev": "Game Developer",
        "blockchain": "Blockchain Engineer",
        "technical-writer": "Technical Writer",
        "security-consultant": "Security Consultant",
        "architect": "Systems Architect"
    }
    
    # Normalize input
    target_role = role_map.get(role.lower(), role)
    
    # Default fallback for unknown roles - include common tech/soft skills
    default_skills = [
        "Communication", "Problem Solving", "Teamwork", "Adaptability", 
        "Technical Documentation", "Software Principles", "Project Management", 
        "Critical Thinking", "Professionalism"
    ]
    return ROLE_SKILLS_DB.get(target_role, default_skills)
