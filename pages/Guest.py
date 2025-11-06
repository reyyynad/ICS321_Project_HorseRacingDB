import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(
    page_title="Guest Panel - Horse Racing DB",
    page_icon="🐎",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="renadroot1010",
            database="racing"
        )
        return conn
    except mysql.connector.Error as err:
        st.error(f"Database connection error: {err}")
        return None

def execute_query(query):
    """Execute a query and return results as DataFrame"""
    conn = get_db_connection()
    if conn is None:
        return None
    
    try:
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        st.error(f"⚠️ Error executing query: {e}")
        return None
    finally:
        conn.close()

#CSS Styling 
st.markdown("""
<style>
    .stApp { background: #FFFFFF; }
    h1, h2, h3, h4, h5, h6, p, label { color: #3E2723 !important; }

    /* Input boxes styled like cards */
    .stTextInput > div > div > input,
    .stDateInput > div > div > input,
    .stSelectbox > div > div > select {
        background: #FFFFFF !important;
        border: 2px solid #D7CCC8 !important;
        border-radius: 12px !important;
        padding: 10px 14px !important;
        color: #3E2723 !important;
        font-size: 16px !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05) !important;
        transition: all 0.3s ease-in-out;
    }
    .stTextInput > div > div > input:focus,
    .stDateInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #8D6E63 !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.12) !important;
    }

    /* Buttons styled like cards */
    .stButton>button {
        background: linear-gradient(145deg, #EFEBE9, #D7CCC8) !important;
        color: #3E2723 !important;
        font-weight: bold !important;
        border: 2px solid #D7CCC8 !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-size: 16px !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    }
    .stButton>button:hover {
        background: linear-gradient(145deg, #D7CCC8, #BCAAA4) !important;
        border-color: #8D6E63 !important;
        transform: translateY(-3px);
        box-shadow: 0 6px 14px rgba(0,0,0,0.12) !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(90deg, #8D6E63, #5D4037);
        color: white;
        border-radius: 12px;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# 🐎 Guest Dashboard Header
st.markdown("<h1>👤 Guest Dashboard</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='font-size:18px;'>Welcome Guest! Explore the horse racing data below. "
    "Use the sections to view horse details, trainers, race statistics, and track information.</p>",
    unsafe_allow_html=True
)


# 1- 🐴 Browse Horses
with st.expander("🐴 Browse Horses"):
    owner_lname = st.text_input("Enter Owner's Last Name")
    if st.button("Show Horses"):
        if owner_lname:
            query1 = f"""
                SELECT 
                    h.horseName AS Horse, 
                    h.age AS Age, 
                    GROUP_CONCAT(CONCAT(t.fname, ' ', t.lname) SEPARATOR ', ') AS `Trainer(s)`
                FROM Horse h
                JOIN Owns o ON h.horseId = o.horseId
                JOIN Owner ow ON o.ownerId = ow.ownerId
                JOIN Trainer t ON h.stableId = t.stableId
                WHERE ow.lname = '{owner_lname}'
                GROUP BY h.horseId, h.horseName, h.age;
                """
            df = execute_query(query1)
            
            if df is not None:
                if df.empty:
                    st.warning(f"No horses found for owner '{owner_lname}'.")
                else:
                    st.write(f"🐴 Horses and Trainers for Owner: {owner_lname}")
                    st.dataframe(df)
        else:
            st.warning("Please enter an owner's last name.")

# 2. 🏆 View Winning Trainers
with st.expander("🏆 View Trainers of Winning Horses"):
    if st.button("Show Trainers of Winning Horses"):
        query2 = """
        SELECT 
            CONCAT(t.fname, ' ', t.lname) AS Trainer,
            h.horseName AS WinnerHorse,
            r.raceName AS RaceName
        FROM Trainer t
        JOIN Horse h ON h.stableId = t.stableId
        JOIN RaceResults rr ON rr.horseId = h.horseId
        JOIN Race r ON r.raceId = rr.raceId
        WHERE rr.results = 'first';
        """
        df = execute_query(query2)
        
        if df is not None:
            if df.empty:
                st.warning("No winning trainers found yet.")
            else:
                st.dataframe(df)

# 3. 💰 Prize Money Statistics
with st.expander("💰 Prize Money Statistics"):
    if st.button("Show Prize Statistics"):
        query3 = """
        SELECT 
            CONCAT(t.fname, ' ', t.lname) AS Trainer,
            SUM(rr.prize) AS TotalWinnings
        FROM Trainer t
        JOIN Horse h ON h.stableId = t.stableId
        JOIN RaceResults rr ON rr.horseId = h.horseId
        GROUP BY t.trainerId, t.fname, t.lname
        ORDER BY TotalWinnings DESC;
        """
        df = execute_query(query3)
        
        if df is not None:
            if df.empty:
                st.warning("No prize money records found.")
            else:
                st.dataframe(df)

# 4. 🏟 Race Track Information
with st.expander("🏟 Race Track Information"):
    if st.button("🏇 View Tracks, Races, and Horse Participation"):
        query4 = """
        SELECT 
            t.trackName AS TrackName,
            COUNT(DISTINCT r.raceId) AS RaceCount,
            COUNT(DISTINCT rr.horseId) AS TotalHorses
        FROM Track t
        JOIN Race r ON r.trackName = t.trackName
        JOIN RaceResults rr ON rr.raceId = r.raceId
        GROUP BY t.trackName
        ORDER BY RaceCount DESC;
        """
        df = execute_query(query4)
        
        if df is not None:
            if df.empty:
                st.warning("No race data available for tracks.")
            else:
                st.dataframe(df)


# FOOTER
st.markdown("""
<div class="footer">
    <h3>Horse Racing Guest Portal</h3>
    <p>Explore with insight and curiosity 🐎</p>
</div>
""", unsafe_allow_html=True)