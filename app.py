import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Shaik Shariya | AI/ML Portfolio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for stunning design with navigation
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Smooth Scrolling */
    html {
        scroll-behavior: smooth;
    }
    
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        background-attachment: fixed;
    }
    
    /* Fixed Navigation Bar */
    .nav-bar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: rgba(26, 26, 46, 0.95);
        backdrop-filter: blur(10px);
        padding: 20px 50px;
        z-index: 1000;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
    }
    
    .nav-container {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    align-items: center;
}

.nav-logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: #00d4ff;
    letter-spacing: 1px;
    white-space: nowrap;
    flex-shrink: 0;
}

.nav-links {
    display: flex;
    gap: 40px;
    margin-left: auto;   /* pushes nav links to the right */
    align-items: center;
}

    
    .nav-link {
        color: #e0e0e0;
        text-decoration: none;
        font-size: 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
        padding: 8px 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    
    .nav-link:hover {
        color: #00d4ff;
        background: rgba(0, 212, 255, 0.1);
    }
    
    /* Main Content Spacing */
    .main-content {
        margin-top: 10px;
        padding: 0 50px;
    }
    
    /* Section Spacing */
    .section {
        padding: 80px 0;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Hero Section */
    .hero-section {
        min-height: 90vh;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 60px;
        align-items: center;
        padding: 100px 20px;
    }
    
    .hero-image-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .hero-image {
        width: 400px;
        height: 400px;
        border-radius: 50%;
        object-fit: cover;
        border: 5px solid #00d4ff;
        box-shadow: 0 20px 60px rgba(0, 212, 255, 0.4);
        transition: all 0.3s ease;
    }
    
    .hero-image:hover {
        transform: scale(1.05);
        box-shadow: 0 25px 80px rgba(0, 212, 255, 0.6);
    }
    
    .hero-content {
        text-align: left;
    }
    
    @media (max-width: 968px) {
        .hero-section {
            grid-template-columns: 1fr;
            text-align: center;
        }
        .hero-content {
            text-align: center;
        }
    }
    
    .hero-title {
        font-size: 5rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 20px;
        letter-spacing: -2px;
        animation: fadeInDown 1s ease;
    }
    
    .hero-subtitle {
        font-size: 2rem;
        color: #00d4ff;
        margin-bottom: 20px;
        font-weight: 600;
        animation: fadeInUp 1s ease;
    }
    
    .hero-description {
        font-size: 1.2rem;
        color: #b0b0b0;
        max-width: 800px;
        margin: 0 auto 40px;
        line-height: 1.8;
    }
    
    /* CTA Buttons */
    .cta-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 30px;
    }
    
    .cta-button {
        display: inline-block;
        padding: 15px 35px;
        background: transparent;
        color: #00d4ff;
        text-decoration: none;
        border: 2px solid #00d4ff;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .cta-button:hover {
        background: #00d4ff;
        color: #1a1a2e;
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.4);
    }
    
    .cta-button-primary {
        background: #00d4ff;
        color: #1a1a2e;
        border: 2px solid #00d4ff;
    }
    
    .cta-button-primary:hover {
        background: transparent;
        color: #00d4ff;
    }
    
    /* Section Heading */
    .section-heading {
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 50px;
        text-align: center;
        position: relative;
        padding-bottom: 20px;
    }
    
    .section-heading::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: #00d4ff;
        border-radius: 2px;
    }
    
    /* Stats Cards */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 30px;
        margin: 60px 0;
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 40px 30px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-10px);
        border-color: #00d4ff;
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.2);
    }
    
    .stat-number {
        font-size: 3.5rem;
        font-weight: 800;
        color: #00d4ff;
        margin-bottom: 10px;
        line-height: 1;
    }
    
    .stat-label {
        font-size: 1.1rem;
        color: #b0b0b0;
        font-weight: 500;
    }
    
    /* Content Cards */
    .content-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 35px;
        margin-bottom: 30px;
        transition: all 0.3s ease;
    }
    
    .content-card:hover {
        transform: translateY(-5px);
        border-color: #00d4ff;
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.15);
    }
    
    .card-title {
        font-size: 1.8rem;
        color: #00d4ff;
        font-weight: 700;
        margin-bottom: 12px;
    }
    
    .card-subtitle {
        font-size: 1.3rem;
        color: #e0e0e0;
        margin-bottom: 8px;
        font-weight: 600;
    }
    
    .card-date {
        font-size: 1rem;
        color: #808080;
        margin-bottom: 20px;
    }
    
    .card-description {
        color: #b0b0b0;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    
    /* Lists */
    ul {
        color: #b0b0b0;
        line-height: 2;
        padding-left: 20px;
    }
    
    li {
        margin-bottom: 10px;
    }
    
    /* Skills Section */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
        margin-top: 40px;
    }
    
    .skill-category {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 25px;
        transition: all 0.3s ease;
    }
    
    .skill-category:hover {
        border-color: #00d4ff;
        transform: translateY(-3px);
    }
    
    .skill-category-title {
        font-size: 1.3rem;
        color: #00d4ff;
        font-weight: 600;
        margin-bottom: 15px;
    }
    
    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    
    .skill-tag {
        background: rgba(0, 212, 255, 0.1);
        color: #00d4ff;
        padding: 8px 16px;
        border-radius: 6px;
        font-size: 0.95rem;
        font-weight: 500;
        border: 1px solid rgba(0, 212, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .skill-tag:hover {
        background: rgba(0, 212, 255, 0.2);
        border-color: #00d4ff;
        transform: scale(1.05);
    }
    
    /* Projects Grid */
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 30px;
        margin-top: 40px;
    }
    
    /* Contact Section */
    .contact-container {
        text-align: center;
        max-width: 800px;
        margin: 0 auto;
    }
    
    .contact-info {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 50px;
        margin-top: 40px;
    }
    
    .contact-links {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
        margin: 30px 0;
    }
    
    .contact-link {
        display: inline-block;
        padding: 12px 30px;
        background: transparent;
        color: #00d4ff;
        text-decoration: none;
        border: 2px solid #00d4ff;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .contact-link:hover {
        background: #00d4ff;
        color: #1a1a2e;
        transform: translateY(-2px);
    }
    
    /* Certifications */
    .cert-item {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-left: 4px solid #00d4ff;
        padding: 20px 25px;
        margin-bottom: 20px;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .cert-item:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateX(10px);
    }
    
    .cert-name {
        font-size: 1.2rem;
        color: #e0e0e0;
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .cert-year {
        display: inline-block;
        background: #00d4ff;
        color: #1a1a2e;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.9rem;
        font-weight: 600; 
        margin-top: 5px;
    }
    .main .block-container { padding-top: 0px; }
    .main-content { margin-top: 0px; }
    .hero-section { padding: 10px 16px; }

    /* Achievements */
    .achievement-item {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(0, 212, 255, 0.05) 100%);
        border: 1px solid rgba(0, 212, 255, 0.3);
        padding: 25px 30px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: #e0e0e0;
        font-size: 1.15rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .achievement-item:hover {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.15) 0%, rgba(0, 212, 255, 0.08) 100%);
        transform: scale(1.02);
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 40px 20px;
        color: #808080;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 80px;
    }
</style>

<script>
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        const yOffset = -100;
        const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({top: y, behavior: 'smooth'});
    }
}

</script>

""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<style>
/* Reduce page top padding */
.main .block-container { padding-top: 0rem; }

/* Slim header */
.header-wrap { padding: 6px 0; margin: 0 0 6px 0; }

/* Tight typography */
.header-title { font-size: 24px; line-height: 1.1; margin: 0; }
.header-subtitle { font-size: 14px; line-height: 1.2; margin: 2px 0 0 0; }

/* Headings default margin trim */
h1, h2, h3 { margin-top: 0.4rem; margin-bottom: 0.4rem; }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="nav-bar">
    <div class="nav-container">
        <div class="nav-logo">SHAIK SHARIYA</div>
        <div class="nav-links">
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#about" onclick="scrollToSection('about'); return false;">About</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#education" onclick="scrollToSection('education'); return false;">Education</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#experience" onclick="scrollToSection('experience'); return false;">Experience</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#projects" onclick="scrollToSection('projects'); return false;">Projects</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#skills" onclick="scrollToSection('skills'); return false;">Skills</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#certifications" onclick="scrollToSection('certifications'); return false;">Certifications</a>
            <a class="nav-link" style="text-decoration:none;color:pink;" href="#contact" onclick="scrollToSection('contact'); return false;">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
  /* 1) Make nav a bit shorter */
  .nav-bar { padding: 12px 32px; }         /* was 20px 50px */

  /* 2) Remove extra offset under fixed nav */
  .main-content { margin-top: 0px; }      /* was 100px; adjust to your nav height */

  /* 3) Make hero section compact */
  .hero-section { 
    min-height: auto;                      /* was 90vh */
    padding: 10px 16px;                    /* was 100px 20px */
    gap: 36px;                             /* was 60px */
  }

  /* 4) Tighten headline block */
  .hero-title { font-size: 3.2rem; margin-bottom: 8px; }   /* was 5rem and 20px */
  .hero-subtitle { font-size: 1.2rem; margin-bottom: 8px; }
  .hero-description { margin: 6px 0 16px; }

  /* 5) Slightly smaller image so row height is smaller */
  .hero-image { width: 260px; height: 300px; }             /* was 400x400 */
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div id="about" class="main-content">
  <section class="hero-section">
    <div class="hero-image-container">
      <img src="https://raw.githubusercontent.com/ShariyaShaik/portfolio/refs/heads/main/image.jpeg" alt="Shaik Shariya" class="hero-image">
    </div>
    <div class="hero-content">
      <h1 class="hero-title">Shaik Shariya</h1>
      <p class="hero-subtitle">Software Engineer | Problem Solver | Full Stack Developer</p>
      <p class="hero-description">
        Final-year Computer Science Engineering student (AIML specialization) with hands-on experience in Java,
        python programming and database-driven applications. Skilled in Data Structures and Algorithms, debugging and testing with a keen interest
        in software engineering. Recognized for strong problem-solving, teamwork, and adaptability while
        contributing to engineering projects.
      </p>
    </div>
    
  </section>
</div>
""", unsafe_allow_html=True)


# Stats

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""<div style="align:center" class="cta-container" style="justify-content: flex-start;">
        <a style="text-decoration:none" href="#contact" onclick="scrollToSection('contact'); return false;" class="cta-button">Get In Touch</a>
        <a style="text-decoration:none" href="https://drive.google.com/file/d/1fIFsWWEp7RFNmpUcVpPkSmyk8lvAfGad/view?usp=drive_link" target="_blank" class="cta-button">Check Out My Resume</a>
        <a style="text-decoration:none" href="https://github.com/ShariyaShaik" target="_blank" class="cta-button">View GitHub</a>
        <a style="text-decoration:none" href="https://www.linkedin.com/in/shariya-shaik-13677a268/" target="_blank" class="cta-button">LinkedIn Profile</a>
      </div>""",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">9.74</div>
        <div class="stat-label">CGPA</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a style="text-decoration:none" href="https://leetcode.com/u/Shariya123/"><div class="stat-card">
        <div class="stat-number">230+</div>
        <div class="stat-label">LeetCode Problems</div>
    </div></a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a style="text-decoration:none" href="#certifications" onclick="scrollToSection('certifications'); return false;">
        <div class="stat-card">
            <div class="stat-number">5+</div>
            <div class="stat-label">Certifications</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a style="text-decoration:none" href="https://www.hackerrank.com/profile/shaikshariya2825">
    <div class="stat-card">
        <div class="stat-number"style="font-size: 2rem;">Hackerrank</div>
        <div class="stat-label">5★ in Python</div>
        <div class="stat-label">4★ in Java</div>
        <div class="stat-label">4★ in SQL</div>
    </div>
    </a>
    """, unsafe_allow_html=True)




# Education Section
st.markdown('<div id="education" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Education</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="content-card">
    <h3 class="card-title">B.Tech in Artificial Intelligence and Machine Learning</h3>
    <p class="card-subtitle">Mohan Babu University, Tirupati</p>
    <p class="card-date">2022 - 2026</p>
    <p class="card-description" style="color: #00d4ff; font-size: 1.3rem; font-weight: 700; margin-top: 15px;">
        CGPA: 9.74/10
    </p>
</div>
<div class="content-card">
    <h3 class="card-title">Intermediate in MPC</h3>
    <p class="card-subtitle">Sri Chaitanya Junior College, Tirupati</p>
    <p class="card-date">2020 - 2022</p>
    <p class="card-description" style="color: #00d4ff; font-size: 1.3rem; font-weight: 700; margin-top: 15px;">
        Marks: 978/1000
    </p>
</div>
""", unsafe_allow_html=True)


# Professional Experience Section
st.markdown('<div id="experience" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Experience</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="content-card">
    <h3 class="card-title">Java Full Stack Developer Intern</h3>
    <p class="card-subtitle">NETWORX</p>
    <p class="card-date">June 2025 - August 2025</p>
    <div class="card-description">
        <ul>
            <li>Developed Banking System Simulator using Java (OOP + DSA) and Spring Boot</li>
            <li>Integrated JDBC and SQLite3 for efficient data storage and manipulation</li>
            <li>Designed front-end interface using HTML and CSS</li>
            <li>Enhanced skills in JDBC and database handling</li>
        </ul>
        <a href="https://drive.google.com/file/d/10xDFC4LgZH4aTTQg5HHcfw4j_qIY08aV/view?usp=sharing" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 10px; display: inline-block;">View Certificate →</a>
    </div>
</div>
<div class="content-card">
    <h3 class="card-title">AIML Intern</h3>
    <p class="card-subtitle">AICTE (Eduskills)</p>
    <p class="card-date">October 2024 - December 2024</p>
    <div class="card-description">
        <ul>
            <li>Gained practical experience in developing machine learning models</li>
            <li>Experimented with ML models and learned model training based on specific requirements</li>
            <li>Enhanced skills in model evaluation, data pre-processing, and deployment strategies</li>
        </ul>
        <a href="https://drive.google.com/file/d/1lB2__47Lx96UpDOvDrf6YZe2f0FUegX_/view" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 10px; display: inline-block;">View Certificate →</a>
    </div>
</div>


""", unsafe_allow_html=True)


# Projects Section
st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Projects</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="content-card">
        <h3 class="card-title">Banking System Simulator</h3>
        <p class="card-description">
            Comprehensive banking application built with Java, Spring Boot, and database integration for managing financial operations.
        </p>
        <p style="color: #e0e0e0; font-weight: 600; margin: 20px 0 10px 0;">Key Features:</p>
        <ul>
            <li>Object-oriented programming with Java (OOP + DSA)</li>
            <li>JDBC and SQLite3 integration for data persistence</li>
            <li>Clean and responsive front-end using HTML and CSS</li>
            <li>Complete banking operations management</li>
        </ul>
        <div style="margin-top: 20px;">
            <span class="skill-tag">Java</span>
            <span class="skill-tag">Spring Boot</span>
            <span class="skill-tag">JDBC</span>
            <span class="skill-tag">SQLite3</span>
        </div>
        <a href="https://github.com/ShariyaShaik/Banking-system" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 15px; display: inline-block;">View on GitHub →</a>
    </div>
    
    <div class="content-card">
        <h3 class="card-title">Educational Organization - ServiceNow</h3>
        <p class="card-description">
            Comprehensive educational system built on ServiceNow platform with complete administrative features.
        </p>
        <p style="color: #e0e0e0; font-weight: 600; margin: 20px 0 10px 0;">Key Features:</p>
        <ul>
            <li>Business rules and client scripts implementation</li>
            <li>Flow designers for custom tables</li>
            <li>Complete admission, grades, and fee management system</li>
        </ul>
        <div style="margin-top: 20px;">
            <span class="skill-tag">ServiceNow</span>
            <span class="skill-tag">Flow Designer</span>
            <span class="skill-tag">Business Rules</span>
        </div>
        <a href="" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 15px; display: inline-block;">In Progress</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="content-card">
        <h3 class="card-title">Electricity Bill Management System</h3>
        <p class="card-description">
            ServiceNow-based system for managing electricity bill operations with AI-powered virtual agent.
        </p>
        <p style="color: #e0e0e0; font-weight: 600; margin: 20px 0 10px 0;">Key Features:</p>
        <ul>
            <li>Consumer and bill details management</li>
            <li>Receipt generation and tracking</li>
            <li>Virtual agent integration for seamless interaction</li>
        </ul>
        <div style="margin-top: 20px;">
            <span class="skill-tag">ServiceNow</span>
            <span class="skill-tag">Virtual Agent</span>
            <span class="skill-tag">Integration</span>
        </div>
        <a href="https://www.linkedin.com/posts/shariya-shaik-13677a268_servicenow-virtualagent-automation-activity-7370366782080999424-40di?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEGcDzoBwJGtScFFKVwyEfzazxRp9b-3ffA" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 15px; display: inline-block;">View on LinkedIn →</a>
    </div>
    
    <div class="content-card">
        <h3 class="card-title">Fantasy Cricket Application</h3>
        <p class="card-description">
            GUI-based desktop application for cricket enthusiasts to create and manage fantasy teams.
        </p>
        <p style="color: #e0e0e0; font-weight: 600; margin: 20px 0 10px 0;">Key Features:</p>
        <ul>
            <li>Interactive team creation interface</li>
            <li>Player addition/removal functionality</li>
            <li>Automated score calculation based on player performance</li>
            <li>SQL database for persistent data storage</li>
        </ul>
        <div style="margin-top: 20px;">
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Qt Designer</span>
            <span class="skill-tag">SQL</span>
        </div>
        <a href="https://www.linkedin.com/posts/shariya-shaik-13677a268_excited-to-share-my-latest-project-a-fantasy-activity-7211810547988668416-audU?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEGcDzoBwJGtScFFKVwyEfzazxRp9b-3ffA" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-top: 15px; display: inline-block;">View on LinkedIn →</a>
    </div>
    """, unsafe_allow_html=True)


# Skills Section
st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Technical Skills</h2>', unsafe_allow_html=True)

skills_data = {
    "Programming Languages": ["Python", "Java", "SQL", "DSA"],
    "Frameworks": ["Qt Designer", "JDBC"],
    "Web Technologies": ["HTML", "CSS", "JavaScript"],
    "Databases": ["MySQL", "SQLite3"],
    "ServiceNow": ["System Administration", "Application Development", "Incident Management", 
                   "Problem Management", "Change Management", "Service Catalog", 
                   "User and Role Management", "Access Control", "Business Rules", 
                   "UI Policies", "Client Scripts"],
    "Tools & Technologies": ["VS Code", "Google Colab", "Jupyter Notebook", "Replit", "Servicenow"]  
}

cols = st.columns(2)
items = list(skills_data.items())
for idx, (category, skills) in enumerate(items):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class="skill-category">
            <h3 class="skill-category-title">{category}</h3>
            <div class="skill-tags">
                {''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills])}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<h3 style="color: #00d4ff; font-size: 2rem; margin-top: 60px; margin-bottom: 30px; text-align: center;">Soft Skills</h3>', unsafe_allow_html=True)

soft_skills = [
    "Strong Collaboration & Teamwork",
    "Adaptable in Dynamic Environments",
    "Client Relationship Management",
    "Problem-Solving Mindset",
    "Quick Learner"
]

cols = st.columns(3)
for idx, skill in enumerate(soft_skills):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="skill-category" style="text-align: center;">
            <p style="color: #e0e0e0; font-size: 1.05rem; margin: 0;">{skill}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Certifications Section
st.markdown('<div id="certifications" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Certifications</h2>', unsafe_allow_html=True)

certifications = [
    ("Certified System Administrator - ServiceNow", "2025", "https://drive.google.com/file/d/19dzrKbxLPYuuutpk4JHwcxnSbND_kd4u/view?usp=drive_link"),
    ("Certified Application Developer - ServiceNow", "2025", "https://drive.google.com/file/d/1v6VWEnQ97pgYowZoVpFquzEdPtGctu4X/view?usp=drive_link"),
    ("Programming, Data Structures and Algorithms using Python - NPTEL", "2024", "https://archive.nptel.ac.in/content/noc/NOC24/SEM1/Ecertificates/106/noc24-cs45/Course/NPTEL24CS45S64250053230164497.pdf"),
    ("Google AI Essentials - Google, Coursera", "2024", "https://www.coursera.org/account/accomplishments/verify/WSAJV9GWAGNA"),
    ("Java (Basic) Certificate - HackerRank", "2025", "https://www.hackerrank.com/certificates/afa9a9f6a485"),
    ("Python (Basic) Certificate - HackerRank", "2025", "https://www.hackerrank.com/certificates/54665ee9596d"),
    ("SQL (Basic) Certificate - HackerRank", "2025", "https://www.hackerrank.com/certificates/0d4c4ae63d0a")
]

for cert, year, link in certifications:
    st.markdown(f"""
    <div class="cert-item">
        <div class="cert-name">{cert}</div>
        <span class="cert-year">{year}</span>
        <a href="{link}" target="_blank" style="color: #00d4ff; text-decoration: none; font-weight: 600; margin-left: 15px; display: inline-block;">View Certificate →</a>
    </div>
    """, unsafe_allow_html=True)


# Contact Section
st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-heading">Get In Touch</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="contact-container">
    <div class="contact-info">
        <p style="color: #e0e0e0; font-size: 1.2rem; margin-bottom: 30px; line-height: 1.8;">
            I'm always open to discussing new opportunities, collaborations, or just having a chat about technology!
        </p>
        <div class="contact-links">
            <a style="text-decoration:none" href="mailto:shaikshariya2825@gmail.com" class="contact-link">Email</a>
            <a style="text-decoration:none" href="tel:+917660896768" class="contact-link">Phone</a>
            <a style="text-decoration:none" href="https://www.linkedin.com/in/shariya-shaik-13677a268/" target="_blank" class="contact-link">LinkedIn</a>
            <a style="text-decoration:none" href="https://github.com/ShariyaShaik" target="_blank" class="contact-link">GitHub</a>
            <a style="text-decoration:none" href="https://hackerrank.com/shaikshariya2825" target="_blank" class="contact-link">HackerRank</a>
        </div>
        <p style="color: #808080; font-size: 1.05rem; margin-top: 30px;">
            Resident in Tirupati, Andhra Pradesh, India
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)








