import streamlit as st

# Page Config
st.set_page_config(
    page_title="MultiGPT Studio",
    page_icon="✦",
    layout="wide"
)

# ---------- THEME TOGGLE ----------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# ---------- MASTER CSS ----------
def inject_css(theme):
    if theme == "dark":
        bg_primary     = "#080A0F"
        bg_secondary   = "#0E1118"
        bg_card        = "#111520"
        bg_card_hover  = "#161C2E"
        border_color   = "#1E2740"
        accent         = "#5B8DEF"
        accent2        = "#A259FF"
        accent_glow    = "rgba(91,141,239,0.18)"
        text_primary   = "#EDF0F7"
        text_secondary = "#7A85A3"
        text_muted     = "#424D68"
        tag_bg         = "rgba(91,141,239,0.12)"
        sidebar_bg     = "#0B0D16"
        sidebar_border = "#161C2E"
        badge_bg       = "rgba(162,89,255,0.13)"
        shine          = "rgba(255,255,255,0.03)"
    else:
        bg_primary     = "#F5F6FA"
        bg_secondary   = "#ECEEF5"
        bg_card        = "#FFFFFF"
        bg_card_hover  = "#F0F2FB"
        border_color   = "#D8DCF0"
        accent         = "#3B6FD4"
        accent2        = "#7C3AED"
        accent_glow    = "rgba(59,111,212,0.13)"
        text_primary   = "#111828"
        text_secondary = "#4A5370"
        text_muted     = "#9AA3BF"
        tag_bg         = "rgba(59,111,212,0.09)"
        sidebar_bg     = "#ECEEF5"
        sidebar_border = "#D0D4E8"
        badge_bg       = "rgba(124,58,237,0.10)"
        shine          = "rgba(255,255,255,0.5)"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

    /* ── GLOBAL RESET ── */
    html, body, [class*="css"] {{
        font-family: 'DM Sans', sans-serif;
        color: {text_primary};
    }}

    /* ── APP BACKGROUND ── */
    .stApp {{
        background-color: {bg_primary};
        background-image:
            radial-gradient(ellipse 80% 50% at 20% 0%, {accent_glow}, transparent),
            radial-gradient(ellipse 60% 40% at 80% 100%, rgba(162,89,255,0.07), transparent);
    }}

    /* ── SIDEBAR ── */
    section[data-testid="stSidebar"] {{
        background: {sidebar_bg} !important;
        border-right: 1px solid {sidebar_border} !important;
        padding-top: 20px;
    }}
    section[data-testid="stSidebar"] * {{
        color: {text_primary} !important;
    }}
    section[data-testid="stSidebar"] .stSelectbox label {{
        font-family: 'Syne', sans-serif;
        font-size: 11px;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: {text_muted} !important;
        font-weight: 500;
    }}

    /* ── HIDE STREAMLIT CHROME ── */
    #MainMenu, footer, header {{ visibility: hidden; }}
    .block-container {{ padding-top: 2rem; padding-bottom: 3rem; max-width: 1100px; }}

    /* ══════════════════════════════════════
       TYPOGRAPHY COMPONENTS
    ══════════════════════════════════════ */

    .pg-eyebrow {{
        font-family: 'Syne', sans-serif;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: {accent};
        text-align: center;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }}
    .pg-eyebrow::before, .pg-eyebrow::after {{
        content: '';
        width: 28px;
        height: 1px;
        background: {accent};
        opacity: 0.5;
    }}

    .pg-hero-title {{
        font-family: 'Syne', sans-serif;
        font-size: clamp(42px, 7vw, 72px);
        font-weight: 800;
        line-height: 1.08;
        letter-spacing: -0.025em;
        text-align: center;
        color: {text_primary};
        margin: 0 0 18px 0;
    }}
    .pg-hero-title span {{
        background: linear-gradient(135deg, {accent}, {accent2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}

    .pg-subtitle {{
        font-family: 'DM Sans', sans-serif;
        font-size: 17px;
        font-weight: 300;
        color: {text_secondary};
        text-align: center;
        line-height: 1.7;
        max-width: 520px;
        margin: 0 auto 40px auto;
    }}

    /* ══════════════════════════════════════
       CARDS
    ══════════════════════════════════════ */
    .tool-card {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 28px 24px;
        margin-bottom: 16px;
        transition: all 0.25s cubic-bezier(.4,0,.2,1);
        position: relative;
        overflow: hidden;
    }}
    .tool-card::before {{
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, {shine}, transparent 60%);
        pointer-events: none;
    }}
    .tool-card:hover {{
        border-color: {accent};
        background: {bg_card_hover};
        box-shadow: 0 0 0 1px {accent}, 0 8px 32px {accent_glow};
        transform: translateY(-2px);
    }}
    .tool-card-icon {{
        font-size: 26px;
        margin-bottom: 10px;
        display: block;
    }}
    .tool-card-title {{
        font-family: 'Syne', sans-serif;
        font-size: 17px;
        font-weight: 700;
        color: {text_primary};
        margin-bottom: 7px;
        letter-spacing: -0.01em;
    }}
    .tool-card-desc {{
        font-size: 14px;
        color: {text_secondary};
        line-height: 1.6;
        font-weight: 300;
    }}
    .tool-card-tag {{
        display: inline-block;
        background: {tag_bg};
        color: {accent};
        font-family: 'Syne', sans-serif;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        padding: 3px 10px;
        border-radius: 100px;
        margin-top: 12px;
    }}

    /* ══════════════════════════════════════
       FEATURE PILLS
    ══════════════════════════════════════ */
    .feat-row {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
        margin: 32px 0;
    }}
    .feat-pill {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 100px;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: 400;
        color: {text_primary};
        display: flex;
        align-items: center;
        gap: 8px;
        letter-spacing: 0.01em;
        transition: all 0.2s;
    }}
    .feat-pill:hover {{
        border-color: {accent};
        background: {bg_card_hover};
    }}
    .feat-pill-dot {{
        width: 6px; height: 6px;
        border-radius: 50%;
        background: {accent};
        flex-shrink: 0;
    }}

    /* ══════════════════════════════════════
       DIVIDER
    ══════════════════════════════════════ */
    .styled-divider {{
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, {border_color}, transparent);
        margin: 40px 0;
    }}

    /* ══════════════════════════════════════
       SECTION HEADER
    ══════════════════════════════════════ */
    .section-header {{
        font-family: 'Syne', sans-serif;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: {text_muted};
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    .section-header::after {{
        content: '';
        flex: 1;
        height: 1px;
        background: {border_color};
    }}

    /* ══════════════════════════════════════
       STAT / BADGE STRIP
    ══════════════════════════════════════ */
    .stat-strip {{
        display: flex;
        gap: 0;
        border: 1px solid {border_color};
        border-radius: 14px;
        overflow: hidden;
        margin: 0 0 40px 0;
        background: {bg_card};
    }}
    .stat-item {{
        flex: 1;
        padding: 18px 0;
        text-align: center;
        border-right: 1px solid {border_color};
    }}
    .stat-item:last-child {{ border-right: none; }}
    .stat-num {{
        font-family: 'Syne', sans-serif;
        font-size: 22px;
        font-weight: 800;
        color: {accent};
        line-height: 1;
    }}
    .stat-label {{
        font-size: 11px;
        color: {text_muted};
        margin-top: 4px;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        font-weight: 500;
    }}

    /* ══════════════════════════════════════
       PAGE-SPECIFIC HERO (INNER PAGES)
    ══════════════════════════════════════ */
    .page-hero {{
        padding: 32px 0 24px 0;
        border-bottom: 1px solid {border_color};
        margin-bottom: 32px;
    }}
    .page-hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: {badge_bg};
        color: {accent2};
        font-family: 'Syne', sans-serif;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        padding: 5px 14px;
        border-radius: 100px;
        margin-bottom: 16px;
    }}
    .page-title {{
        font-family: 'Syne', sans-serif;
        font-size: clamp(30px, 5vw, 48px);
        font-weight: 800;
        letter-spacing: -0.02em;
        color: {text_primary};
        margin: 0 0 10px 0;
        line-height: 1.1;
    }}
    .page-subtitle {{
        font-size: 16px;
        color: {text_secondary};
        font-weight: 300;
        line-height: 1.6;
        max-width: 560px;
    }}

    /* ══════════════════════════════════════
       CHAT FEATURE CHIPS
    ══════════════════════════════════════ */
    .chip-row {{
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-bottom: 28px;
    }}
    .chip {{
        background: {tag_bg};
        border: 1px solid {border_color};
        color: {text_secondary};
        font-size: 13px;
        padding: 7px 16px;
        border-radius: 100px;
        font-weight: 400;
        display: flex; align-items: center; gap: 6px;
    }}

    /* ══════════════════════════════════════
       ANSWER / OUTPUT CARD
    ══════════════════════════════════════ */
    .output-card {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-left: 3px solid {accent};
        border-radius: 12px;
        padding: 24px;
        margin-top: 20px;
    }}
    .output-card-label {{
        font-family: 'Syne', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: {accent};
        margin-bottom: 10px;
    }}

    /* ══════════════════════════════════════
       FOOTER
    ══════════════════════════════════════ */
    .app-footer {{
        text-align: center;
        padding: 40px 0 10px;
        font-size: 13px;
        color: {text_muted};
        letter-spacing: 0.05em;
    }}
    .app-footer strong {{
        color: {text_secondary};
        font-weight: 500;
    }}

    /* ══════════════════════════════════════
       STREAMLIT WIDGET OVERRIDES
    ══════════════════════════════════════ */
    .stTextInput > div > div > input,
    .stSelectbox > div > div,
    .stFileUploader > div {{
        background: {bg_card} !important;
        border: 1px solid {border_color} !important;
        color: {text_primary} !important;
        border-radius: 10px !important;
    }}
    .stTextInput > div > div > input:focus {{
        border-color: {accent} !important;
        box-shadow: 0 0 0 3px {accent_glow} !important;
    }}
    .stButton > button {{
        background: linear-gradient(135deg, {accent}, {accent2}) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 10px !important;
        font-family: 'Syne', sans-serif !important;
        font-weight: 600 !important;
        letter-spacing: 0.05em !important;
        padding: 10px 26px !important;
        transition: opacity 0.2s !important;
    }}
    .stButton > button:hover {{
        opacity: 0.88 !important;
        box-shadow: 0 4px 20px {accent_glow} !important;
    }}
    .stSuccess {{
        background: rgba(72,187,120,0.1) !important;
        border: 1px solid rgba(72,187,120,0.3) !important;
        border-radius: 10px !important;
        color: #48BB78 !important;
    }}
    .stSpinner > div {{ border-top-color: {accent} !important; }}

    </style>
    """, unsafe_allow_html=True)

inject_css(st.session_state.theme)

# ---------- SIDEBAR ----------
with st.sidebar:
    # Theme toggle at top
    col_l, col_r = st.columns([1, 1])
    with col_l:
        if st.button("☀ Light" if st.session_state.theme == "dark" else "☀ Light", key="light_btn"):
            st.session_state.theme = "light"
            st.rerun()
    with col_r:
        if st.button("◑ Dark", key="dark_btn"):
            st.session_state.theme = "dark"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    menu = st.selectbox(
        "Navigate",
        ["Home", "Chatbot", "Image Generator", "Document QA", "Content Generator"]
    )

# ══════════════════════════════════════════════════════
#  HOME
# ══════════════════════════════════════════════════════
if menu == "Home":

    st.markdown("<div class='pg-eyebrow'>✦ AI MultiTool Studio</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='pg-hero-title'>
        Everything AI,<br><span>All Together</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div class='pg-subtitle'>One unified workspace for chatbots, image generation, document intelligence, and AI-powered content creation.</div>", unsafe_allow_html=True)

    # Stat strip
    st.markdown("""
    <div class='stat-strip'>
        <div class='stat-item'><div class='stat-num'>4</div><div class='stat-label'>AI Tools</div></div>
        <div class='stat-item'><div class='stat-num'>∞</div><div class='stat-label'>Possibilities</div></div>
        <div class='stat-item'><div class='stat-num'>1</div><div class='stat-label'>Workspace</div></div>
        <div class='stat-item'><div class='stat-num'>0</div><div class='stat-label'>Complexity</div></div>
    </div>
    """, unsafe_allow_html=True)

    # Tool cards
    st.markdown("<div class='section-header'>AI Tools</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='tool-card'>
            <span class='tool-card-icon'>💬</span>
            <div class='tool-card-title'>AI Chatbot</div>
            <div class='tool-card-desc'>Ask questions, get explanations, brainstorm ideas — all in a seamless chat interface.</div>
            <span class='tool-card-tag'>Gemini 2.0 Flash Lite</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='tool-card'>
            <span class='tool-card-icon'>📄</span>
            <div class='tool-card-title'>Document QA</div>
            <div class='tool-card-desc'>Upload any PDF and extract answers instantly with AI-powered document understanding.</div>
            <span class='tool-card-tag'>PDF · Instant</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='tool-card'>
            <span class='tool-card-icon'>🎨</span>
            <div class='tool-card-title'>Image Generator</div>
            <div class='tool-card-desc'>Turn text prompts into stunning AI-generated visuals with Pollinations AI.</div>
            <span class='tool-card-tag'>Text → Image</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='tool-card'>
            <span class='tool-card-icon'>✍️</span>
            <div class='tool-card-title'>Content Generator</div>
            <div class='tool-card-desc'>Generate blogs, captions, emails, scripts, and more at any length in seconds.</div>
            <span class='tool-card-tag'>6 Content Types</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='styled-divider'>", unsafe_allow_html=True)

    # Why section as pills
    st.markdown("<div class='section-header'>Why MultiGPT</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='feat-row'>
        <div class='feat-pill'><div class='feat-pill-dot'></div> Lightning-fast AI responses</div>
        <div class='feat-pill'><div class='feat-pill-dot'></div> Multiple tools in one place</div>
        <div class='feat-pill'><div class='feat-pill-dot'></div> Beginner-friendly interface</div>
        <div class='feat-pill'><div class='feat-pill-dot'></div> Modern smart workspace</div>
        <div class='feat-pill'><div class='feat-pill-dot'></div> No account needed</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='app-footer'>Powered by AI &nbsp;·&nbsp; Built by <strong>Azmi</strong> ❤️</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
#  CHATBOT
# ══════════════════════════════════════════════════════
elif menu == "Chatbot":

    import google.generativeai as genai

    genai.configure(api_key="AIzaSyAxuDzlJsQ9yP_A5vmE-JWnUHDbDPkAIBA")
    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    st.markdown("""
    <div class='page-hero'>
        <div class='page-hero-badge'>✦ Gemini 2.0 Flash Lite</div>
        <div class='page-title'>AI Chatbot</div>
        <div class='page-subtitle'>Ask anything — from quick facts to deep explanations, creative writing or code.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='chip-row'>
        <div class='chip'>⚡ Instant responses</div>
        <div class='chip'>🧠 Contextual memory</div>
        <div class='chip'>🚀 Smart conversations</div>
    </div>
    """, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask me anything…")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                response = model.generate_content(prompt)
                ai_reply = response.text
                st.markdown(ai_reply)
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    st.markdown("<div class='app-footer'>Powered by <strong>Gemini AI</strong> ✨</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
#  IMAGE GENERATOR
# ══════════════════════════════════════════════════════
elif menu == "Image Generator":

    from PIL import Image
    import requests
    from io import BytesIO

    st.markdown("""
    <div class='page-hero'>
        <div class='page-hero-badge'>✦ Text to Image</div>
        <div class='page-title'>Image Generator</div>
        <div class='page-subtitle'>Describe anything and watch it materialise as an AI-generated image.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='chip-row'>
        <div class='chip'>🎨 High quality output</div>
        <div class='chip'>⚡ Fast generation</div>
        <div class='chip'>💾 Downloadable</div>
    </div>
    """, unsafe_allow_html=True)

    prompt_img = st.text_input("Describe your image", placeholder="e.g. A futuristic city at dusk, cinematic lighting…")
    generate = st.button("✦ Generate Image")

    if generate and prompt_img:
        with st.spinner("Creating your image…"):
            url = f"https://image.pollinations.ai/prompt/{prompt_img}"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            st.image(img, use_container_width=True)
            st.download_button(
                "⬇ Download Image",
                data=response.content,
                file_name="generated_image.png",
                mime="image/png"
            )

    st.markdown("<div class='app-footer'>Powered by <strong>Pollinations AI</strong> 🎨</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
#  DOCUMENT QA
# ══════════════════════════════════════════════════════
elif menu == "Document QA":

    import google.generativeai as genai
    import PyPDF2

    genai.configure(api_key="AIzaSyAxuDzlJsQ9yP_A5vmE-JWnUHDbDPkAIBA")
    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    st.markdown("""
    <div class='page-hero'>
        <div class='page-hero-badge'>✦ PDF Intelligence</div>
        <div class='page-title'>Document QA</div>
        <div class='page-subtitle'>Upload a PDF and ask questions — AI reads it so you don't have to.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='chip-row'>
        <div class='chip'>📄 PDF support</div>
        <div class='chip'>🧠 AI comprehension</div>
        <div class='chip'>📚 Smart Q&A</div>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        pdf_text = "".join([page.extract_text() for page in pdf_reader.pages])
        st.success("PDF uploaded successfully ✅")

        question = st.text_input("Ask a question from the document")
        ask = st.button("✦ Ask AI")

        if ask and question:
            with st.spinner("Reading & thinking…"):
                prompt = f"Answer the question based on this document.\n\nDocument:\n{pdf_text}\n\nQuestion:\n{question}"
                response = model.generate_content(prompt)
                answer = response.text

            st.markdown(f"""
            <div class='output-card'>
                <div class='output-card-label'>AI Answer</div>
                <div>{answer}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='app-footer'>Powered by <strong>Document AI</strong> 📚</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
#  CONTENT GENERATOR
# ══════════════════════════════════════════════════════
elif menu == "Content Generator":

    import google.generativeai as genai

    genai.configure(api_key="AIzaSyAxuDzlJsQ9yP_A5vmE-JWnUHDbDPkAIBA")
    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    st.markdown("""
    <div class='page-hero'>
        <div class='page-hero-badge'>✦ AI Writing</div>
        <div class='page-title'>Content Generator</div>
        <div class='page-subtitle'>Generate polished blogs, captions, emails, scripts, and more in seconds.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='chip-row'>
        <div class='chip'>⚡ Instant content</div>
        <div class='chip'>🧠 Creative AI writing</div>
        <div class='chip'>🚀 6 content types</div>
    </div>
    """, unsafe_allow_html=True)

    content_type = st.selectbox("Content Type", ["Blog Post", "Instagram Caption", "Email", "YouTube Script", "Story", "Product Description"])
    topic = st.text_input("Topic", placeholder="e.g. Benefits of AI in Education")
    length = st.select_slider("Length", options=["Short", "Medium", "Long"])

    generate_content = st.button("✦ Generate Content")

    if generate_content and topic:
        with st.spinner("Crafting your content…"):
            prompt = f"Generate a {length} {content_type} about: {topic}\n\nMake it creative, engaging and professional."
            response = model.generate_content(prompt)
            ai_content = response.text

        st.markdown(f"""
        <div class='output-card'>
            <div class='output-card-label'>Generated {content_type}</div>
        </div>
        """, unsafe_allow_html=True)
        st.write(ai_content)

        st.download_button("⬇ Download Content", data=ai_content, file_name="generated_content.txt", mime="text/plain")
        st.success("Content generated successfully ✦")

    st.markdown("<div class='app-footer'>Powered by <strong>AI Writing</strong> ✨</div>", unsafe_allow_html=True)

