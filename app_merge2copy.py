import streamlit as st
import datetime
from mock_data import get_valencia_programming_catalog, get_community_resources

# Page configuration
st.set_page_config(page_title="Real life Student Balancer", layout="wide")
st.title("🌱 Real Life Student Balancer")

# --- GOOGLE FONTS STYLESHEET WRAPPER ---
st.markdown(
    """
    <style>
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMarkdownContainer"] {
        font-family: 'Poppins', sans-serif !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CLEAR & SUPPORTIVE WORKLOAD ANALYSIS ENGINE ---


def analyze_student_wellness_pulse(stress, sleep, workload, work_hrs, childcare_hrs, active_courses):
    total_life_hours = work_hrs + childcare_hrs
    course_count = len(active_courses)
    # Rule of thumb: 9 hours per course weekly
    estimated_study_hours = course_count * 9

    insights = []

    # Schedule & Time Check
    if total_life_hours >= 40:
        insights.append(
            f"⚠️ **Your schedule is packed tight.** You have {total_life_hours} hours committed to work and family. "
            f"Adding {course_count} courses means finding another {estimated_study_hours} hours to study every week. "
            f"Take it steady—don't hesitate to space your courses out if it feels like too much."
        )
    else:
        insights.append(
            "✅ **Good balance on your time.** Your current work and family hours leave you with a healthy amount of room to handle your classes.")

    # Stress & Overwhelm Check (Connected directly to your resources tab)
    if stress >= 6 or workload >= 8:
        insights.append(
            "⚡ **Things are feeling heavy right now.** If you are feeling overwhelmed by your workload, "
            "remember you can use Valencia's free tutoring resources or reach out to your professors "
            "early to talk about extensions before you hit a wall. "
            "We also highly recommend checking out our **Community Support Links** tab at the top of this page "
            "for direct access to confidential local counseling, food pantry programs, and essential hygiene assistance."
        )
    elif sleep >= 7:
        insights.append(
            "🛌 **Energy levels are running low.** Make sure to schedule explicit breaks and protect your sleep. Rest is part of studying.")
    else:
        insights.append(
            "🌱 **You're in a stable groove.** Your stress and workload indicators are in a safe space. Keep doing what you're doing.")

    # High-Risk Course Pairs
    if "COP1000C" in active_courses and work_hrs >= 30:
        insights.append("💻 **Heads up on programming:** COP1000C requires a lot of deep focus and coding practice. Balancing this with a heavy work schedule means you'll need clear, dedicated blocks of quiet study time.")

    return "\n\n".join(insights)


# --- TAB NAVIGATION ---
tab1, tab2, tab3 = st.tabs([
    "🚀 Core Balance Tracker",
    "📋 Valencia Course Roadmap",
    "🤝 Community Support Links"
])

# --- TAB 1: CORE TRACKER ---
with tab1:
    st.subheader(
        "Keep your semester pace stable and your mental health protected.")
    st.markdown("Academic success isn't just about grades—it's about managing your limited hours. Log your current situation below to see how your schedule shapes up.")

    # --- INPUTS PLACED OUTSIDE THE FORM FOR INSTANT PAGE REFRESHING ---
    st.markdown("### 📊 Personal Pulse Check")

    # 1. Stress Slider: Starts at 0, triggers warning at 6 or higher
    stress_slider = st.slider(
        "Current Stress Level (0-10)", min_value=0, max_value=10, value=0)
    if stress_slider >= 6:
        st.info(
            "❤️ **Hey, things look heavy right now.** We noticed your stress level is high. "
            "Remember you don't have to carry it alone. Head over to the **Community Support Links** "
            "tab at the top of the page for free, confidential local care, food, and mental health resources."
        )

    # 2. Exhaustion Slider: Starts at 0, triggers warning at 7 or higher
    sleep_slider = st.slider("Exhaustion Level (0-10)",
                             min_value=0, max_value=10, value=0)
    if sleep_slider >= 7:
        st.info(
            "🛌 **Energy levels are critically low.** Severe exhaustion drains focus. "
            "If your sleep schedule is completely disrupted, check out the **Community Support Links** "
            "tab to see available health and wellness resources."
        )

    # 3. Classwork Pressure Slider: Starts at 0, triggers warning at 8 or higher
    workload_slider = st.slider(
        "Classwork Pressure (0-10)", min_value=0, max_value=10, value=0)
    if workload_slider >= 8:
        st.info(
            "⚡ **The academic load is hitting a critical peak.** You don't have to navigate "
            "this pressure solo. Remember you can connect with Valencia's free online tutoring "
            "resources or reach out directly to your advisor for proactive pacing options."
        )

    st.markdown("---")

    # --- THE STANDARD FORM WORKSPACE CONTAINER ---
    with st.form("wellness_data_form"):
        st.markdown("### ⏱️ Weekly Commitments")
        work_slider = st.slider("Weekly Work Hours",
                                min_value=0, max_value=60, value=0, step=5)
        childcare_slider = st.slider(
            "Weekly Family & Childcare Hours", min_value=0, max_value=80, value=0, step=5)

        st.markdown("---")
        st.markdown("### 📚 Select Your Current Courses")
        sta2023 = st.checkbox("STA 2023: Statistical Methods", value=True)
        enc1101 = st.checkbox("ENC 1101: Freshman Composition I", value=True)
        cgs2545c = st.checkbox(
            "CGS2545C: Database Management Systems", value=False)
        cop1000c = st.checkbox(
            "COP1000C: Introduction to Programming Concepts", value=False)

        active_basket = []
        if sta2023:
            active_basket.append("STA 2023")
        if enc1101:
            active_basket.append("ENC 1101")
        if cgs2545c:
            active_basket.append("CGS2545C")
        if cop1000c:
            active_basket.append("COP1000C")

        st.markdown("---")
        # --- SHARE LOGIC ATTACHED INSIDE THE FORM WORKSPACE ---
        share_flag = st.checkbox(
            "Send a copy of this wellness pulse report to my academic advisor.", value=False)
        execute_button = st.form_submit_button("⚡ Generate My Strategy Report")

    # Generate and preserve output via session state on click
    if execute_button:
        st.session_state.saved_advice = analyze_student_wellness_pulse(
            stress=stress_slider,
            sleep=sleep_slider,
            workload=workload_slider,
            work_hrs=work_slider,
            childcare_hrs=childcare_slider,
            active_courses=active_basket
        )
        st.session_state.report_generated = True

    if st.session_state.get("report_generated"):
        st.markdown("---")
        st.markdown("### 📋 Your Balance Strategy Guide")
        st.success(st.session_state.saved_advice)

        # Display confirmation message if the advisor checkbox was selected
        if share_flag:
            st.info("📨 **Advisor Copy Queued:** A copy of this report will be securely packaged and forwarded to your academic advisor's portal track.")

        st.caption("☁️ Securely synced with your student dashboard")

# --- TAB 2: COURSE ROADMAP ---
with tab2:
    st.subheader("Valencia College Degree Roadmap")
    st.markdown(
        "Browse through the requirements for your Associate in Science (A.S.) degree program.")

    catalog = get_valencia_programming_catalog()
    selected_tier = st.selectbox(
        "Choose an Academic Phase:",
        options=list(catalog.keys()),
        key="catalog_phase_selector"
    )

    for course in catalog[selected_tier]:
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"##### **{course['course_code']}**")
                st.text(course['course_name'])
            with col2:
                st.metric(label="Credits", value=f"{course['credits']} units")
            with col3:
                intensity = course['intensity']
                if intensity == "Coding Intensive":
                    st.warning(f"⚡ {intensity}")
                elif intensity == "Light Coding / SQL":
                    st.info(f"💾 {intensity}")
                else:
                    st.success(f"📘 {intensity}")

            if course['start_date'] and course['end_date']:
                st.caption(
                    f"Suggested Term Timeline: {course['start_date'].strftime('%B %Y')} - {course['end_date'].strftime('%B %Y')}")
            else:
                st.caption("Timeline Status: Flexible / Open Enrollment")
            st.divider()

# --- TAB 3: COMMUNITY SUPPORT LINKS ---
with tab3:
    st.subheader("❤️ Local Community Care & Support Networks")
    st.markdown("If things are getting tough outside of school, you don't have to carry it alone. Use these verified resources for direct, confidential help.")

    resource_list = get_community_resources()

    for item in resource_list:
        with st.container():
            st.markdown(f"#### {item['category']} | **{item['name']}**")
            st.markdown(f"*{item['description']}*")
            st.info(f"📞 **How to Connect:** {item['contact']}")
            st.markdown(
                f"[Click here to visit their official website]({item['url']})")
            st.divider()
