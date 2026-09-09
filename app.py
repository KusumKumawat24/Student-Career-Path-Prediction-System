import streamlit as st
import pandas as pd
import joblib

# -------------------- PAGE --------------------

st.set_page_config(
    page_title="Career Prediction System",
    layout="wide"
)

st.title("Students Career Path Prediction System")
st.write("Fill all the details and click Predict Career")

# -------------------- LOAD MODEL --------------------

model = joblib.load("career_model.pkl")

book_encoder = joblib.load("book_encoder.pkl")
cert_encoder = joblib.load("cert_encoder.pkl")
workshop_encoder = joblib.load("workshop_encoder.pkl")
subject_encoder = joblib.load("subject_encoder.pkl")
career_encoder = joblib.load("career_encoder.pkl")
company_encoder = joblib.load("company_encoder.pkl")
job_encoder = joblib.load("job_encoder.pkl")

# -------------------- MAPPINGS --------------------

yes_no = {
    "yes":1,
    "no":0
}

management_map = {
    "Management":0,
    "Technical":1
}

worker_map = {
    "hard worker":0,
    "smart worker":1
}

# -------------------- USER INPUT --------------------

col1,col2 = st.columns(2)

with col1:

    self_learning = st.selectbox(
        "Self Learning Capability",
        ["yes","no"]
    )

    extra_courses = st.selectbox(
        "Extra Courses",
        ["yes","no"]
    )

    senior = st.selectbox(
        "Taken Inputs From Seniors",
        ["yes","no"]
    )

    management = st.selectbox(
        "Management or Technical",
        ["Management","Technical"]
    )

    worker = st.selectbox(
        "Hard / Smart Worker",
        ["hard worker","smart worker"]
    )

    teamwork = st.selectbox(
        "Worked In Teams",
        ["yes","no"]
    )

    introvert = st.selectbox(
        "Introvert",
        ["yes","no"]
    )

with col2:

    technical = st.slider("Technical Score",0,100,50)

    communication = st.slider("Communication Score",0,100,50)

    learning = st.slider("Learning Score",0,100,50)

    professional = st.slider("Professional Score",0,100,50)

    leadership = st.slider("Leadership Score",0,100,50)

    personality = st.slider("Personality Score",0,100,50)

    career_ready = st.slider("Career Readiness",0,100,50)

st.divider()

st.subheader("Interest Information")

book = st.selectbox(
    "Book Category",
    [
        "Creative",
        "Entertainment",
        "Leadership",
        "Business / Leadership",
        "Religious",
        "Technical",
        "Others"
    ]
)

certificate = st.selectbox(
    "Certification Category",
    [
        "Programming",
        "Data Science",
        "Cyber Security",
        "Data Engineering",
        "System Administration"
    ]
)

workshop = st.selectbox(
    "Workshop Category",
    [
        "Cyber Security",
        "Data & AI",
        "Software Development",
        "Software Engineering"
    ]
)

subject = st.selectbox(
    "Subject Category",
    [
        "Software Development",
        "Data & AI",
        "Cyber Security & Networks",
        "Emerging Technologies",
        "Management"
    ]
)

career_area = st.selectbox(
    "Career Area",
    [
        "Software Development",
        "Cyber Security",
        "Business & Management",
        "Infrastructure & Cloud"
    ]
)

company = st.selectbox(
    "Company Category",
    [
        "Business Services",
        "Cloud & SaaS",
        "IT Support & QA",
        "Product Company",
        "Service Company"
    ]
)

# -------------------- ENCODERS --------------------

book = book_encoder.transform([book])[0]
certificate = cert_encoder.transform([certificate])[0]
workshop = workshop_encoder.transform([workshop])[0]
subject = subject_encoder.transform([subject])[0]
career_area = career_encoder.transform([career_area])[0]
company = company_encoder.transform([company])[0]

# -------------------- PREDICT BUTTON --------------------

if st.button("Predict Career"):

    input_df = pd.DataFrame([{

        "self-learning capability?": yes_no[self_learning],
        "Extra-courses did": yes_no[extra_courses],
        "Taken inputs from seniors or elders": yes_no[senior],
        "Management or Technical": management_map[management],
        "hard/smart worker": worker_map[worker],
        "worked in teams ever?": yes_no[teamwork],
        "Introvert": yes_no[introvert],

        "Technical Score": technical,
        "Communication Score": communication,
        "Learning Score": learning,
        "Professional Score": professional,
        "Leadership Score": leadership,
        "Personality Score": personality,
        "Career Readiness": career_ready,

        "Book_Category": book,
        "Certification_Category": certificate,
        "Workshop_Category": workshop,
        "Subject_Category": subject,
        "Career_Area": career_area,
        "Company_Category": company

    }])

    prediction = model.predict(input_df)

    career = job_encoder.inverse_transform(prediction)[0]

    st.success(f"Recommended Career : {career}")

    # ---------------- COURSES ----------------

    course_recommendations = {

        "Software Development":[
            "Python Programming",
            "Data Structures & Algorithms",
            "Java Programming",
            "Web Development",
            "Git & GitHub"
        ],

        "Cyber Security":[
            "Ethical Hacking",
            "Network Security",
            "Linux",
            "Penetration Testing",
            "CEH"
        ],

        "QA & Support":[
            "Manual Testing",
            "Automation Testing",
            "Selenium",
            "JIRA",
            "SQL"
        ],

        "Database & Data Engineering":[
            "SQL",
            "MySQL",
            "MongoDB",
            "Hadoop",
            "Data Engineering"
        ]

    }

    st.subheader("Recommended Courses")

    for course in course_recommendations.get(career, []):
        st.write(course)

    # ---------------- SKILLS ----------------

    skills = {

        "Software Development":[
            "Python",
            "Java",
            "DSA",
            "Git",
            "Problem Solving"
        ],

        "Cyber Security":[
            "Networking",
            "Linux",
            "Security",
            "Firewalls",
            "Cryptography"
        ],

        "QA & Support":[
            "Testing",
            "Bug Reporting",
            "SQL",
            "Automation",
            "Documentation"
        ],

        "Database & Data Engineering":[
            "SQL",
            "Python",
            "ETL",
            "Big Data",
            "Cloud"
        ]

    }

    st.subheader("Required Skills")

    for skill in skills.get(career, []):
        st.write(skill)

   

    # ---------------- CAREER ROADMAP ----------------

    roadmap = {

        "Software Development":[
            "Learn Programming",
            "Master Data Structures",
            "Build Projects",
            "Learn Git & GitHub",
            "Prepare for Interviews"
        ],

        "Cyber Security":[
            "Learn Networking",
            "Master Linux",
            "Practice Ethical Hacking",
            "Get CEH Certification",
            "Apply for Jobs"
        ],

        "QA & Support":[
            "Manual Testing",
            "Automation Testing",
            "Learn Selenium",
            "Build Testing Projects",
            "Apply for QA Jobs"
        ],

        "Database & Data Engineering":[
            "Learn SQL",
            "Learn Python",
            "Study ETL",
            "Practice Cloud Platforms",
            "Build Data Projects"
        ]
    }

    st.subheader(" Career Roadmap")

    for step in roadmap.get(career, []):
        st.write("➡", step)


    # ---------------- DOWNLOAD REPORT ----------------

    report = f"""
Career Prediction Report

Recommended Career: {career}

"""

    st.download_button(
        " Download Report",
        report,
        file_name="Career_Report.txt"
    )

    st.balloons()

    st.success(" Career Prediction Completed Successfully!")

# Run the code in terminal (python -m streamlit run app.py)
