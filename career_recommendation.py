print("CAREER RECOMMENDATIO SYSTEM")
career_data={
    "ai":{
        "beginner":
        {
            "career":"Machine Learning Engineer",
            "skills":["Python , NumPy , Pandas , Scikit-Learn"]
        },
        "intermediate":
        {
            "career":"AI Developer",
            "skills":["DeepLearning,PyTorch,TensorFlow,Computer Vision"]
        },
        "advanced":
        {
            "career":"AI Research Scientist",
            "skills":["Neural Networks,NLP,Research papers,Advanced Mathematics"]
        }
    },
    "web development": {
        "beginner": {
            "career": "Frontend Developer",
            "skills": [
                "HTML",
                "CSS",
                "JavaScript",
                "Bootstrap"
            ]
        },
        "intermediate": {
            "career": "Full Stack Developer",
            "skills": [
                "React",
                "Node.js",
                "MongoDB",
                "REST APIs"
            ]
        },
        "advanced": {
            "career": "Software Architect",
            "skills": [
                "System Design",
                "Cloud Computing",
                "Microservices",
                "DevOps"
            ]
        }
    },

    "mobile development": {
        "beginner": {
            "career": "Flutter Developer",
            "skills": [
                "Dart",
                "Flutter Widgets",
                "Firebase",
                "Git"
            ]
        },
        "intermediate": {
            "career": "Mobile Application Developer",
            "skills": [
                "State Management",
                "API Integration",
                "Firebase",
                "UI/UX"
            ]
        },
        "advanced": {
            "career": "Mobile Solutions Architect",
            "skills": [
                "App Security",
                "Architecture Design",
                "Performance Optimization",
                "Cloud Services"
            ]
        }
    },

    "cybersecurity": {
        "beginner": {
            "career": "Security Analyst",
            "skills": [
                "Networking",
                "Linux",
                "Cybersecurity Basics",
                "Ethical Hacking"
            ]
        },
        "intermediate": {
            "career": "Penetration Tester",
            "skills": [
                "Vulnerability Assessment",
                "Kali Linux",
                "Web Security",
                "OWASP"
            ]
        },
        "advanced": {
            "career": "Cybersecurity Engineer",
            "skills": [
                "Incident Response",
                "Cloud Security",
                "Digital Forensics",
                "Threat Intelligence"
            ]
        }
    }
}

print("\n Available Interests:")
print("- AI")
print("- Web Development")
print("- Mobile Development")
print("- Cybersecurity")
interest = input("\nEnter your interest: ").strip().lower()
print("\nSkill Levels:")
print("- Beginner")
print("- Intermediate")
print("- Advanced")
skill_level = input("Enter your skill level: ").strip().lower()

if interest in career_data:

    if skill_level in career_data[interest]:

        recommendation = career_data[interest][skill_level]

        print("\n" + "=" * 50)
        print("      RECOMMENDATION RESULT")
        print("=" * 50)

        print(f"\nInterest      : {interest.title()}")
        print(f"Skill Level   : {skill_level.title()}")

        print("\nRecommended Career:")
        print(f"→ {recommendation['career']}")

        print("\nRecommended Skills To Learn:")

        for skill in recommendation["skills"]:
            print(f"✓ {skill}")

        print("\nKeep learning and building projects!")
        

    else:
        print("\nInvalid Skill Level.")

else:
    print("\nInterest not found.")
