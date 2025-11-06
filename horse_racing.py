import streamlit as st
import base64


st.set_page_config(
    page_title="Horse Racing DB",
    page_icon="🏇",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

horse_img = get_base64_image("images/horse.webp")

#CSS Styling ---
st.markdown("""
<style>
    .main {
        background: #FFFFFF;
        color: #3E2723;
    }

    .stApp {
        background: #FFFFFF;
    }

    /* hero sec */
    .hero-section {
        padding: 3rem 0;
        margin: 2rem 0;
    }

    .hero-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
    }

    .hero-content {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 3rem;
    }

    .hero-text {
        flex: 1;
        max-width: 600px;
    }

    .greeting {
        font-size: 1.5rem;
        color: #6D4C41;
        margin-bottom: 1rem;
        font-weight: 500;
    }

    .main-title {
        font-size: 2.5rem;
        color: #3E2723;
        margin-bottom: 1.5rem;
        line-height: 1.2;
        font-weight: 700;
    }

    .highlight {
        color: #8D6E63;
        font-weight: 700;
    }

    .description {
        font-size: 1.1rem;
        color: #5D4037;
        line-height: 1.8;
        margin-bottom: 2rem;
    }

    /* image container */
    .hero-image {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .character-img {
        width: 100%;
        height: auto;
        border-radius: 15px;
        transition: all 0.4s ease-in-out;
        transform: scale(1);
        animation: float 3s ease-in-out infinite;
    filter: drop-shadow(0 20px 40px rgba(146, 69, 17, 0.7));


    }
    @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}

    /* admin/guest cards */
    .role-card {
        background: linear-gradient(145deg, #EFEBE9, #D7CCC8);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-top: 4px solid #8D6E63;
        transition: all 0.4s ease;
    }

    .role-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.15);
        border-top: 4px solid #6D4C41;
    }

    .function-item {
        display: flex;
        align-items: start;
        margin: 0.8rem 0;
        padding: 0.8rem;
        background: rgba(255, 255, 255, 0.7);
        border-radius: 8px;
        border-left: 3px solid #A1887F;
        transition: all 0.3s ease;
    }

    .function-item:hover {
        background: rgba(255, 255, 255, 0.95);
        border-left: 3px solid #6D4C41;
        transform: translateX(8px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    /* footer */
    .footer {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(90deg, #8D6E63, #5D4037);
        color: white;
        border-radius: 15px;
        margin-top: 3rem;
    }

    .footer h3 {
        margin-bottom: 0.5rem;
    }

    .feature-badge {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 1.5rem 2rem;
        border-radius: 15px;
        min-width: 180px;
        cursor: pointer;
        transition: all 0.4s ease;
        border: 2px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    .feature-badge:hover {
        background: rgba(255, 255, 255, 0.25);
        border-color: rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        transform: translateY(-10px) scale(1.05);
    }

    @media (max-width: 768px) {
        .hero-content {
            flex-direction: column;
        }
        .main-title {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown(f"""
<section class="hero-section">
    <div class="hero-container">
        <div class="hero-content">
            <div class="hero-text">
                <h1 class="greeting">
                    Welcome to <span class="highlight">Horse Racing Database</span>
                </h1>
                <p class="description">
                    A website for managing and exploring horse racing information — designed for both <b>Admins</b> and <b>Guests</b>.
                    Track horses, manage races, monitor trainers, and analyze performance metrics — all in one powerful platform.
                    Enjoy a seamless experience built for efficiency, accuracy, and ease of use.
                </p>
            </div>
            <div class="hero-image">
                        <img
                        src="data:image/webp;base64,{horse_img}"
                        alt="Horse racing illustration"
                        class="character-img"
                    />
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ADMIN/GUEST
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="role-card">
        <h2 style="color: #5D4037; margin-bottom: 1rem;"> Admin Functions</h2>
        <div class="function-item"><div><strong>Add New Races</strong><br><small>Create races with full race details and specifications</small></div></div>
        <div class="function-item"><div><strong>Delete Owners</strong><br><small>Remove owners and related records using stored procedures</small></div></div>
        <div class="function-item"><div><strong>Move Horses</strong><br><small>Transfer horses between different stables</small></div></div>
        <div class="function-item"><div><strong>Approve Trainers</strong><br><small>Review and approve new trainers to join stables</small></div></div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="role-card">
        <h2 style="color: #5D4037; margin-bottom: 1rem;">Guest Functions</h2>
        <div class="function-item"><div><strong>Browse Horses</strong><br><small>View horse names, ages, and their trainers</small></div></div>
        <div class="function-item"><div><strong>View Winning Trainers</strong><br><small>See trainers who trained winning horses and their race details</small></div></div>
        <div class="function-item"><div><strong>Prize Money Statistics</strong><br><small>View total prize money won by trainers' horses</small></div></div>
        <div class="function-item"><div><strong>Race Track Information</strong><br><small>List race tracks with race counts and participating horses</small></div></div>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("""
<div class="footer">
    <h3>Excellence in Horse Racing Management</h3>
    <p>Your trusted partner for comprehensive racing data and insights</p>
    <div style="margin-top: 1.5rem; display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
        <div class="feature-badge">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
            <strong>Professional</strong>
            <p style="font-size: 0.85rem; opacity: 0.9;">Industry-standard solutions</p>
        </div>
        <div class="feature-badge">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
            <strong>Efficient</strong>
            <p style="font-size: 0.85rem; opacity: 0.9;">Lightning-fast performance</p>
        </div>
        <div class="feature-badge">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
            <strong>Accurate</strong>
            <p style="font-size: 0.85rem; opacity: 0.9;">Precise data management</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
