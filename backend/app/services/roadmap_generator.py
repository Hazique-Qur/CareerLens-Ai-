import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY
import json

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

ROLE_BASED_FALLBACKS = {
    "Data Scientist": {
        "projects": ["Churn Prediction Model", "Customer Segmentation Analysis", "Sales Forecasting Dashboard"],
        "roadmap": [
            {"topic": "Statistical Modeling", "description": "Learn regression and hypothesis testing.", "difficulty": "Intermediate", "resource_url": "https://www.khanacademy.org/math/statistics-probability"},
            {"topic": "Machine Learning with Scikit-Learn", "description": "Build classification and clustering models.", "difficulty": "Intermediate", "resource_url": "https://scikit-learn.org/"},
            {"topic": "Data Viz with Tableau", "description": "Create professional business dashboards.", "difficulty": "Beginner", "resource_url": "https://www.tableau.com/learn"}
        ]
    },
    "Frontend Developer": {
        "projects": ["Responsive Portfolio Site", "Task Management App (React)", "Weather Dashboard with API"],
        "roadmap": [
            {"topic": "React Hooks & State", "description": "Master useEffect and custom hooks.", "difficulty": "Intermediate", "resource_url": "https://react.dev/"},
            {"topic": "Tailwind CSS Mastery", "description": "Build modern layouts without writing raw CSS.", "difficulty": "Beginner", "resource_url": "https://tailwindcss.com/"},
            {"topic": "Next.js & SSR", "description": "Learn server-side rendering and routing.", "difficulty": "Advanced", "resource_url": "https://nextjs.org/"}
        ]
    },
    "Backend Engineer": {
        "projects": ["LMS Backend with Django", "Inventory API with FastAPI", "Auth System with JWT"],
        "roadmap": [
            {"topic": "RESTful API Design", "description": "Learn best practices for endpoint structure.", "difficulty": "Intermediate", "resource_url": "https://restfulapi.net/"},
            {"topic": "Database Optimization", "description": "Master indexing and query optimization.", "difficulty": "Advanced", "resource_url": "https://use-the-index-luke.com/"},
            {"topic": "Docker & Containerization", "description": "Learn to containerize Python apps.", "difficulty": "Intermediate", "resource_url": "https://www.docker.com/"}
        ]
    },
    "Cybersecurity Analyst": {
        "projects": ["Network Intrusion Detector", "Password Strength Analyzer", "Security Audit Script"],
        "roadmap": [
            {"topic": "CompTIA Security+ Prep", "description": "Learn core security principles.", "difficulty": "Beginner", "resource_url": "https://www.comptia.org/"},
            {"topic": "Ethical Hacking (Kali Linux)", "description": "Learn penetration testing basics.", "difficulty": "Intermediate", "resource_url": "https://www.kali.org/"},
            {"topic": "Cloud Security (AWS)", "description": "Secure IAM and VPC configurations.", "difficulty": "Advanced", "resource_url": "https://aws.amazon.com/security/"}
        ]
    },
    "AI/ML Engineer": {
        "projects": ["Object Detection with YOLO", "Sentiment Analysis for Finance", "Generative AI Chatbot"],
        "roadmap": [
            {"topic": "Deep Learning (PyTorch)", "description": "Build neural networks from scratch.", "difficulty": "Advanced", "resource_url": "https://pytorch.org/tutorials/"},
            {"topic": "MLOps & Engineering", "description": "Deploy models using Flask and Docker.", "difficulty": "Advanced", "resource_url": "https://ml-ops.org/"},
            {"topic": "Computer Vision Basics", "description": "Learn OpenCV and image processing.", "difficulty": "Intermediate", "resource_url": "https://opencv.org/"}
        ]
    },
    "DevOps Engineer": {
        "projects": ["Automated CI/CD Pipeline", "K8s Microservices Cluster", "Infrastructure as Code (Terraform)"],
        "roadmap": [
            {"topic": "Kubernetes (CKA)", "description": "Master container orchestration.", "difficulty": "Advanced", "resource_url": "https://kubernetes.io/docs/home/"},
            {"topic": "Terraform Mastery", "description": "Learn to manage AWS with HCL.", "difficulty": "Intermediate", "resource_url": "https://developer.hashicorp.com/terraform"},
            {"topic": "Linux Systems Admin", "description": "Shell scripting and system hardening.", "difficulty": "Beginner", "resource_url": "https://linuxjourney.com/"}
        ]
    },
    "Mobile Developer": {
        "projects": ["Social Media App (Flutter)", "Health Tracker (React Native)", "Native iOS Music Player"],
        "roadmap": [
            {"topic": "Native UI Design", "description": "Learn Swift UI or Jetpack Compose.", "difficulty": "Intermediate", "resource_url": "https://developer.apple.com/xcode/swiftui/"},
            {"topic": "Cross-Platform Frameworks", "description": "Master Flutter or React Native.", "difficulty": "Intermediate", "resource_url": "https://flutter.dev/"},
            {"topic": "Mobile Backend (Firebase)", "description": "Real-time DB and Auth for apps.", "difficulty": "Beginner", "resource_url": "https://firebase.google.com/"}
        ]
    },
    "Cloud Architect": {
        "projects": ["Serverless Blog Platform", "Multi-region AWS Infrastructure", "Cloud Migration Strategy"],
        "roadmap": [
            {"topic": "AWS Solutions Architect", "description": "High-level system design in cloud.", "difficulty": "Advanced", "resource_url": "https://aws.amazon.com/certification/certified-solutions-architect-associate/"},
            {"topic": "Serverless (AWS Lambda)", "description": "Build event-driven architectures.", "difficulty": "Intermediate", "resource_url": "https://aws.amazon.com/lambda/"},
            {"topic": "Cost Optimization", "description": "Manage cloud budgets and reserved instances.", "difficulty": "Advanced", "resource_url": "https://aws.amazon.com/aws-cost-management/"}
        ]
    },
    "UX Designer": {
        "projects": ["Accessible E-commerce App", "Travel Booking UI/UX", "Design System for SaaS"],
        "roadmap": [
            {"topic": "Interaction Design", "description": "Learn Figma and prototyping.", "difficulty": "Intermediate", "resource_url": "https://www.figma.com/resource-library/design-basics/"},
            {"topic": "User Research Methods", "description": "Master interviews and usability testing.", "difficulty": "Intermediate", "resource_url": "https://www.nngroup.com/articles/user-research-methods-basics/"},
            {"topic": "Accessibility (WCAG)", "description": "Build inclusive digital products.", "difficulty": "Advanced", "resource_url": "https://www.w3.org/WAI/fundamentals/accessibility-intro/"}
        ]
    },
    "Product Manager": {
        "projects": ["Product Requirement Doc (PRD)", "Market Competitor Analysis", "Product Roadmap Strategy"],
        "roadmap": [
            {"topic": "Agile & Scrum", "description": "Master sprint planning and backlogs.", "difficulty": "Beginner", "resource_url": "https://www.atlassian.com/agile"},
            {"topic": "Data-Driven Decisions", "description": "Learn A/B testing and analytics.", "difficulty": "Intermediate", "resource_url": "https://www.google.com/analytics/"},
            {"topic": "Stakeholder Management", "description": "Learn to manage cross-functional teams.", "difficulty": "Advanced", "resource_url": "https://www.mindtheproduct.com/"}
        ]
    },
    "Data Analyst": {
        "projects": ["Financial Performance Dashboard", "Customer Churn SQL Analysis", "E-commerce Sales Report"],
        "roadmap": [
            {"topic": "SQL for Data Analysis", "description": "Master complex joins and window functions.", "difficulty": "Intermediate", "resource_url": "https://mode.com/sql-tutorial/"},
            {"topic": "Excel Power BI", "description": "Build automated business reports.", "difficulty": "Intermediate", "resource_url": "https://powerbi.microsoft.com/en-us/learning/"},
            {"topic": "Python for Data Analysis", "description": "Learn Pandas and Matplotlib.", "difficulty": "Beginner", "resource_url": "https://pandas.pydata.org/docs/getting_started/"}
        ]
    },
    "QA Engineer": {
        "projects": ["Automated UI Testing Suite", "REST API Testing Framework", "Load Testing for Web Apps"],
        "roadmap": [
            {"topic": "Selenium WebDriver", "description": "Automate browser testing.", "difficulty": "Intermediate", "resource_url": "https://www.selenium.dev/"},
            {"topic": "Postman API Testing", "description": "Master automated API validation.", "difficulty": "Intermediate", "resource_url": "https://learning.postman.com/"},
            {"topic": "Test Strategy & Planning", "description": "Learn to design comprehensive test plans.", "difficulty": "Beginner", "resource_url": "https://www.ministryoftesting.com/"}
        ]
    },
    "Embedded Systems": {
        "projects": ["IoT Smart Thermostat", "Embedded RTOS Kernel", "Sensor Fusion Dashboard"],
        "roadmap": [
            {"topic": "Embedded C Mastery", "description": "Low-level memory management.", "difficulty": "Advanced", "resource_url": "https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard"},
            {"topic": "RTOS Principles", "description": "Learn FreeRTOS and task scheduling.", "difficulty": "Advanced", "resource_url": "https://www.freertos.org/"},
            {"topic": "Hardware Communication", "description": "Master I2C, SPI, and UART protocols.", "difficulty": "Intermediate", "resource_url": "https://learn.sparkfun.com/tutorials/i2c"}
        ]
    },
    "Fullstack Developer": {
        "projects": ["Fullstack E-commerce Site", "Blogging Engine (MERN)", "Real-time Collaboration Tool"],
        "roadmap": [
            {"topic": "Fullstack Architecture", "description": "Learn to connect React with Express.", "difficulty": "Intermediate", "resource_url": "https://fullstackopen.com/"},
            {"topic": "Database Design & Auth", "description": "Secure user auth and DB schema design.", "difficulty": "Intermediate", "resource_url": "https://auth0.com/blog/"},
            {"topic": "Deployment & DevOps", "description": "Learn to deploy fullstack apps to Vercel/Render.", "difficulty": "Beginner", "resource_url": "https://vercel.com/docs"}
        ]
    }
}

def generate_roadmap(target_role: str, missing_skills: list):
    # Determine the normalized role for matching fallbacks
    normalized_role = target_role
    role_lower = target_role.lower()
    if "frontend" in role_lower: normalized_role = "Frontend Developer"
    elif "backend" in role_lower: normalized_role = "Backend Engineer"
    elif "data scientist" in role_lower: normalized_role = "Data Scientist"
    elif "security" in role_lower or "cyber" in role_lower: normalized_role = "Cybersecurity Analyst"
    elif "ai" in role_lower or "machine learning" in role_lower: normalized_role = "AI/ML Engineer"
    elif "devops" in role_lower: normalized_role = "DevOps Engineer"
    elif "mobile" in role_lower or "android" in role_lower or "ios" in role_lower: normalized_role = "Mobile Developer"
    elif "cloud" in role_lower or "architect" in role_lower: normalized_role = "Cloud Architect"
    elif "ux" in role_lower or "design" in role_lower: normalized_role = "UX Designer"
    elif "product" in role_lower: normalized_role = "Product Manager"
    elif "data analyst" in role_lower: normalized_role = "Data Analyst"
    elif "qa" in role_lower or "test" in role_lower: normalized_role = "QA Engineer"
    elif "embedded" in role_lower: normalized_role = "Embedded Systems"
    elif "fullstack" in role_lower: normalized_role = "Fullstack Developer"
    
    fallback = ROLE_BASED_FALLBACKS.get(normalized_role, {
        "projects": [
            "Real-time Chat Application with WebSocket and Redis",
            "E-commerce Microservices Backend with Docker",
            "AI-powered Personal Finance Tracker"
        ],
        "roadmap": [
            {"topic": "Advanced Data Structures", "description": "Master trees and graphs.", "difficulty": "Advanced", "resource_url": "https://neetcode.io/"},
            {"topic": "System Design Patterns", "description": "Learn to scale applications.", "difficulty": "Intermediate", "resource_url": "https://github.com/donnemartin/system-design-primer"},
            {"topic": "Cloud Infrastructure", "description": "Deploy to AWS/Azure.", "difficulty": "Intermediate", "resource_url": "https://aws.amazon.com/"}
        ]
    })

    if not GEMINI_API_KEY:
        return {
            "is_demo_mode": True,
            "error": "Demo Mode: API Key missing.",
            "learning_roadmap": fallback["roadmap"],
            "project_suggestions": fallback["projects"],
            "interview_questions": [
                f"Explain the most critical skills for a {target_role}.",
                "Describe a project you built using these technologies.",
                "How do you stay updated with industry trends?",
                "Give an example of a difficult technical challenge you solved.",
                "Why are you the best fit for this role?"
            ]
        }

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    # ... rest of the logic remains similar but with fallback update
    prompt = f"""
    A candidate wants to become a {target_role}.
    They are missing these skills: {missing_skills}
    Generate a 3-step learning roadmap, 3 project ideas, and 5 interview questions.
    Return strictly in JSON format.
    """

    try:
        response = model.generate_content(prompt)
        text_response = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text_response)
    except Exception as e:
        print(f"Roadmap Gemini Error: {str(e)}")
        return {
            "is_demo_mode": True,
            "api_error": str(e),
            "learning_roadmap": fallback["roadmap"],
            "project_suggestions": fallback["projects"],
            "interview_questions": [
                f"How would you master {missing_skills[0] if missing_skills else 'new skills'}?",
                "Explain the architecture of your most recent project.",
                "What are your strategies for debugging complex code?",
                "How do you handle team conflict under pressure?",
                "Where do you see yourself in 5 years in this career?"
            ]
        }
