"""All portfolio content lives here. Edit this file; the templates do the rest."""

PROFILE = {
    "name": "Emmanuel James L. Mape",
    "role": "Vibe-coder",
    "tagline": "AI integration is the future.",
    "email": "emmanueljames.mape@sorsu.edu.ph",
    "links": [("GitHub", "https://github.com/saikyo-debug"), ("LinkedIn", "https://www.linkedin.com/")],
    "about": [
        "Hey I am Emmanuel James L. Mape, a student vibe coder who loves to build fast and flow hard."
        "I focus on bringing ideas to life through high-level design, "
        "creative problem-solving, and AI-assisted workflows.",
    ],
}

SKILLS = {
    "Languages": ["Python", "JavaScript", "SQL", "HTML & CSS"],
    "Frameworks": ["Flask", "Django", "Bootstrap"],
    "Data & tools": ["PostgreSQL", "Git & GitHub", "VS Code", "Pandas"],
    "Working style": ["Clear communication", "Documentation", "Problem solving", "Teamwork"],
}

PROJECTS = [
    {"title": "Personal Web Portfolio", "link": "https://github.com/saikyo-debug/personal-web-portfolio",
     "summary": "a unique online personal portfolio.",
     "tags": ["Python", "Flask", "SQLite"]},
    {"title": "Project name two", "link": "https://github.com/",
     "summary": "Describe the problem you solved and your specific contribution.",
     "tags": ["JavaScript", "API", "Responsive design"]},
    {"title": "Project name three", "link": "",
     "summary": "A data or automation project works well here too.",
     "tags": ["Python", "Pandas"]},
]

EXPERIENCE = [
    {"title": "Job or internship title", "org": "Company name", "period": "2025 to present",
     "points": ["What you were responsible for.", "A result you can measure or describe."]},
    {"title": "Previous role", "org": "Organization", "period": "2024 to 2025",
     "points": ["Responsibility or achievement."]},
]

FIELD_WORK = [
    {"title": "On-the-job training / practicum", "org": "Host organization", "period": "Summer 2025",
     "points": ["What you did in the field.", "What you learned or delivered."]},
    {"title": "Community or research fieldwork", "org": "Site or partner", "period": "2024",
     "points": ["Your role and the outcome."]},
]

EDUCATION = [
    {"title": "Degree or program", "org": "University or school", "period": "2022 to 2026", "points": []},
    {"title": "Certification", "org": "Issuer", "period": "2025", "points": []},
]

CONTENT = dict(p=PROFILE, skills=SKILLS, projects=PROJECTS, experience=EXPERIENCE,
               fieldwork=FIELD_WORK, education=EDUCATION)
