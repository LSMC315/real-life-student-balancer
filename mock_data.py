# mock_data.py
import datetime


def get_valencia_programming_catalog():
    """
    Returns the official Valencia College A.S. Computer Programming & Analysis
    course tracks with relative date structures for schedule simulations.
    """
    today = datetime.date.today()

    # Relative operational milestones for testing semester splits
    term_1_start = today + datetime.timedelta(days=60)    # e.g., Next term
    term_1_end = today + datetime.timedelta(days=180)

    term_2_start = today + datetime.timedelta(days=240)   # e.g., Future term
    term_2_end = today + datetime.timedelta(days=360)

    return {
        "Foundation": [
            {
                "course_code": "COP 1000C",
                "course_name": "Introduction to Programming Concepts",
                "credits": 3,
                "intensity": "Coding Intensive",
                "start_date": term_1_start,
                "end_date": term_1_end,
                "min_grade_required": "C"
            },
            {
                "course_code": "CGS 2545C",
                "course_name": "Database Management Systems",
                "credits": 3,
                "intensity": "Light Coding / SQL",
                "start_date": term_1_start,
                "end_date": term_1_end,
                "min_grade_required": "C"
            },
            {
                "course_code": "CGS 2100C",
                "course_name": "Computer Fundamentals and Applications",
                "credits": 3,
                "intensity": "Zero-Coding",
                "start_date": term_1_start,
                "end_date": term_1_end,
                "min_grade_required": "C"
            },
            {
                "course_code": "CGS 2091C",
                "course_name": "Social, Legal and Ethical Issues in IT",
                "credits": 3,
                "intensity": "Zero-Coding",
                "start_date": term_1_start,
                "end_date": term_1_end,
                "min_grade_required": "C"
            },
            {
                "course_code": "COP 2822C",
                "course_name": "Web Development I",
                "credits": 3,
                "intensity": "Coding Intensive",
                "start_date": term_1_start,
                "end_date": term_1_end,
                "min_grade_required": "C"
            },
            {
                "course_code": "ENC 1101",
                "course_name": "Freshman Composition I",
                "credits": 3,
                "intensity": "Low Reading/Writing",
                "start_date": term_1_start,
                "end_date": term_1_end,
                "min_grade_required": "C"
            }
        ],
        "Intermediate": [
            {
                "course_code": "COP 2800C",
                "course_name": "Java Programming",
                "credits": 3,
                "intensity": "Coding Intensive",
                "start_date": term_2_start,
                "end_date": term_2_end,
                "min_grade_required": "C"
            },
            {
                "course_code": "COP 2047C",
                "course_name": "Python Programming",
                "credits": 3,
                "intensity": "Coding Intensive",
                "start_date": term_2_start,
                "end_date": term_2_end,
                "min_grade_required": "C"
            },
            {
                "course_code": "CTS 1142C",
                "course_name": "Information Technology Project Management",
                "credits": 3,
                "intensity": "Zero-Coding",
                "start_date": term_2_start,
                "end_date": term_2_end,
                "min_grade_required": "C"
            }
        ],
        "Advanced": [
            {
                "course_code": "COP 2830C",
                "course_name": "Scripting Languages",
                "credits": 3,
                "intensity": "Coding Intensive",
                "start_date": None,  # Test parsing open schedules
                "end_date": None,
                "min_grade_required": "C"
            },
            {
                "course_code": "CIS 2910C",
                "course_name": "IT Capstone",
                "credits": 3,
                "intensity": "Project Intensive",
                "start_date": None,
                "end_date": None,
                "min_grade_required": "C"
            }
        ]
    }


def get_community_resources():
    """
    Returns verified community outreach resources and crisis lifelines
    for immediate student support.
    """
    return [
        {
            "name": "Heart of Florida 211 Network",
            "category": "🧠 Mental Health & Crisis Support",
            "description": "Free, confidential 24/7 access to local crisis counseling, housing placement, and utility bill assistance.",
            "contact": "Dial 2-1-1 or Text your Zip Code to 898211",
            "url": "https://hfuw.org"
        },
        {
            "name": "Second Harvest Food Bank",
            "category": "🍎 Food Assistance",
            "description": "Find local emergency food pantries, community kitchens, and mobile grocery distribution sites near you.",
            "contact": "Call (407) 295-1066",
            "url": "https://feedhopenow.org"
        },
        {
            "name": "Valencia College Student Care Hubs",
            "category": "🧼 Hygiene, Clothing & Basics",
            "description": "Access campus resources like Pookie's Pantry for free food staples, personal hygiene hygiene kits, and emergency resource connections.",
            "contact": "Visit Student Assistance Services on Campus",
            "url": "https://valenciacollege.edu"
        }
    ]
