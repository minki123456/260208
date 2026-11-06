import html

import streamlit as st

st.set_page_config(page_title="자기소개", page_icon="✳", layout="wide")

# 자기소개 내용은 아래 PROFILE의 값만 바꾸면 됩니다.
PROFILE = {
    "name": "이름",
    "tagline": "나를 한 문장으로 소개해 보세요.",
    "introduction": "관심사와 경험, 앞으로 해보고 싶은 일을 소개해 보세요.",
    "interests": ["관심 분야 1", "관심 분야 2", "관심 분야 3"],
    "project_title": "기억에 남는 경험",
    "project_description": "프로젝트의 역할과 결과, 배운 점을 적어보세요.",
    "email": "",
}

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Jua&family=Nunito:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #51495e;
        --muted: #827b91;
        --paper: #fffdfb;
        --line: #ece5ee;
        --blue: #b8d2f5;
        --pink: #f5c8d2;
        --yellow: #f7e9b5;
        --mint: #cce9d9;
        --lavender: #e2d8f1;
    }

    .stApp {
        background: var(--paper);
        color: var(--ink);
        font-family: 'Nunito', 'Jua', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent; }
    .block-container {
        max-width: 1180px;
        padding: 2rem 2.5rem 4rem;
    }
    .profile-page { color: var(--ink); }
    .mono, .eyebrow, .section-index, .masthead, .art-label, .footer-label {
        font-family: 'DM Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 0;
    }
    .masthead {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid var(--ink);
        padding: 0.6rem 0 1rem;
        font-size: 0.72rem;
    }
    .masthead nav { display: flex; gap: 1.4rem; }
    .masthead a { color: var(--ink); text-decoration: none; }
    .hero {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 3rem;
        align-items: center;
        padding: 5rem 0 4.5rem;
    }
    .eyebrow { color: #8e9fc8; font-size: 0.75rem; }
    .eyebrow::before {
        content: "";
        display: inline-block;
        width: 0.55rem;
        height: 0.55rem;
        margin-right: 0.55rem;
        background: var(--pink);
        transform: rotate(45deg);
    }
    .hero h1 {
        font-size: 4.8rem;
        line-height: 1.08;
        font-weight: 800;
        margin: 1.2rem 0;
        letter-spacing: 0;
        word-break: keep-all;
    }
    .hero h1 span { color: #8e9fc8; }
    .hero-role {
        color: var(--muted);
        font-size: 1.15rem;
        line-height: 1.7;
        max-width: 34rem;
        white-space: pre-line;
    }
    .hero-art {
        min-height: 330px;
        background-color: #e5effb;
        background-image: linear-gradient(rgba(255, 255, 255, 0.55) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.55) 1px, transparent 1px);
        background-size: 24px 24px;
        color: var(--ink);
        position: relative;
        overflow: hidden;
        padding: 1.25rem;
        border: 1px solid #d7e4f5;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .art-label { font-size: 0.7rem; }
    .art-composition { position: relative; height: 190px; }
    .art-block {
        position: absolute;
        width: 43%;
        height: 72%;
        top: 14%;
        left: 18%;
        background: var(--yellow);
        border: 2px solid rgba(255, 255, 255, 0.8);
        border-radius: 4px;
        transform: rotate(-8deg);
    }
    .art-block-alt {
        top: 5%;
        left: 43%;
        background: var(--pink);
        transform: rotate(9deg);
    }
    .art-word {
        position: absolute;
        z-index: 1;
        top: 20%;
        left: 29%;
        color: var(--ink);
        font-size: 3rem;
        line-height: 0.9;
        font-weight: 700;
        transform: rotate(-8deg);
    }
    .art-footer { display: flex; justify-content: space-between; align-items: end; }
    .art-footer strong { font-size: 1.6rem; font-weight: 500; }
    .art-footer span { font-size: 0.68rem; }
    .content-section {
        display: grid;
        grid-template-columns: 0.34fr 1fr;
        gap: 2rem;
        border-top: 1px solid var(--line);
        padding: 2rem 0 2.5rem;
    }
    .section-index {
        color: #78657d;
        background: var(--lavender);
        font-size: 0.72rem;
        padding: 0.35rem 0.55rem;
        border-radius: 4px;
        width: max-content;
        height: max-content;
    }
    .section-content h2 {
        font-size: 1.8rem;
        line-height: 1.25;
        margin: 0 0 1rem;
        font-weight: 800;
    }
    .section-content p {
        max-width: 48rem;
        font-size: 1.05rem;
        line-height: 1.9;
        color: #41454d;
        white-space: pre-line;
        margin: 0;
    }
    .tags { display: flex; flex-wrap: wrap; gap: 0.55rem; margin-top: 1.2rem; }
    .tag {
        border: 1px solid #e6dce9;
        padding: 0.45rem 0.75rem;
        font-size: 0.85rem;
        border-radius: 4px;
        background: var(--pink);
    }
    .tag:nth-child(4n + 2) { background: var(--mint); }
    .tag:nth-child(4n + 3) { background: var(--yellow); }
    .tag:nth-child(4n) { background: var(--lavender); }
    .quiet { color: var(--muted); font-size: 0.9rem; }
    .project-row {
        display: grid;
        grid-template-columns: 0.8fr 1.2fr;
        gap: 2rem;
        border-top: 1px solid var(--line);
        padding: 1.2rem 0;
    }
    .project-row:first-of-type { margin-top: 1rem; }
    .project-row h3 { margin: 0; font-size: 1.15rem; font-weight: 600; }
    .project-row p { font-size: 0.95rem; }
    .contact-section {
        margin-top: 1rem;
        background: var(--yellow);
        padding: 2rem;
        border: 1px dashed #dece8e;
        border-radius: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1.5rem;
    }
    .contact-section h2 { margin: 0.4rem 0 0; font-size: 2rem; }
    .contact-section a { color: var(--ink); font-weight: 600; }
    .footer-label { font-size: 0.7rem; }
    .footer-note { margin-top: 1.5rem; color: var(--muted); font-size: 0.75rem; }

    @media (max-width: 760px) {
        .block-container { padding: 1rem 1.1rem 2.5rem; }
        .masthead { align-items: flex-start; gap: 1rem; }
        .masthead nav { gap: 0.7rem; font-size: 0.62rem; }
        .hero { grid-template-columns: 1fr; gap: 2rem; padding: 3.5rem 0; }
        .hero h1 { font-size: 3.1rem; }
        .hero-art { min-height: 250px; }
        .art-composition { height: 130px; }
        .art-word { font-size: 2.3rem; }
        .content-section { grid-template-columns: 1fr; gap: 0.8rem; padding: 1.5rem 0 2rem; }
        .project-row { grid-template-columns: 1fr; gap: 0.5rem; }
        .contact-section { align-items: flex-start; flex-direction: column; padding: 1.5rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

safe_name = html.escape(PROFILE["name"].strip())
safe_tagline = html.escape(PROFILE["tagline"].strip())
safe_introduction = html.escape(PROFILE["introduction"].strip())
safe_project_title = html.escape(PROFILE["project_title"].strip())
safe_project_description = html.escape(PROFILE["project_description"].strip())
safe_email = html.escape(PROFILE["email"].strip(), quote=True)

name_heading = f"안녕하세요,<br><span>{safe_name}</span>입니다."
tagline_text = safe_tagline
introduction_text = safe_introduction
interest_items = [html.escape(item.strip()) for item in PROFILE["interests"] if item.strip()]
interest_markup = "".join(f'<span class="tag">{item}</span>' for item in interest_items)
if not interest_markup:
    interest_markup = '<span class="quiet">아직 등록된 관심 분야가 없습니다.</span>'

project_heading = safe_project_title
project_text = safe_project_description
contact_markup = f'<a href="mailto:{safe_email}">{safe_email}</a>' if safe_email else '<span>연락처</span>'

st.markdown(
    f"""
    <main class="profile-page">
        <header class="masthead">
            <div>ABOUT ME&nbsp; / &nbsp;PROFILE 01</div>
            <nav><a href="#about">ABOUT</a><a href="#interests">INTERESTS</a><a href="#work">WORK</a></nav>
        </header>
        <section class="hero">
            <div>
                <div class="eyebrow">A LITTLE INTRODUCTION</div>
                <h1>{name_heading}</h1>
                <p class="hero-role">{tagline_text}</p>
            </div>
            <div class="hero-art" aria-hidden="true">
                <div class="art-label">PERSONAL / 01</div>
                <div class="art-composition">
                    <div class="art-block"></div>
                    <div class="art-block art-block-alt"></div>
                    <div class="art-word">ME<br>IN<br>WORDS</div>
                </div>
                <div class="art-footer"><strong>MY POINT OF VIEW</strong><span>EST. 2026</span></div>
            </div>
        </section>
        <section class="content-section" id="about">
            <div class="section-index">01 / ABOUT</div>
            <div class="section-content">
                <h2>저는 이런 사람입니다.</h2>
                <p>{introduction_text}</p>
            </div>
        </section>
        <section class="content-section" id="interests">
            <div class="section-index">02 / INTERESTS</div>
            <div class="section-content">
                <h2>요즘 관심 있는 것</h2>
                <div class="tags">{interest_markup}</div>
            </div>
        </section>
        <section class="content-section" id="work">
            <div class="section-index">03 / EXPERIENCE</div>
            <div class="section-content">
                <h2>기억에 남는 경험</h2>
                <div class="project-row">
                    <h3>{project_heading}</h3>
                    <p>{project_text}</p>
                </div>
            </div>
        </section>
        <footer class="contact-section" id="contact">
            <div><div class="footer-label">SAY HELLO</div><h2>이야기를 나눠요.</h2></div>
            <div>{contact_markup}</div>
        </footer>
        <div class="footer-note">MADE WITH MY OWN STORY</div>
    </main>
    """,
    unsafe_allow_html=True,
)
