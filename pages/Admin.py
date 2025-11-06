import streamlit as st
import mysql.connector

# Page Config
st.set_page_config(
    page_title="Admin Panel - Horse Racing DB",
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Styling
st.markdown("""
<style>
    .stApp { background: #FFFFFF; }

    h1, h2, h3, h4, h5, h6, p, label {
        color: #3E2723 !important;
    }

    .stTextInput > div > div > input,
    .stDateInput > div > div > input,
    .stTimeInput > div > div > input {
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
    .stTimeInput > div > div > input:focus {
        border-color: #8D6E63 !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.12) !important;
    }

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


# HEADER
st.markdown("<h1>🔑 Admin Dashboard</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='font-size:18px;'>Welcome Admin! Manage races, owners, horses, and trainers here. "
    "All changes update the <b>Horse Racing Database</b> in real-time.</p>",
    unsafe_allow_html=True
)

# Helper function for DB connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="renadroot1010",
        database="racing"
    )


# 1️⃣ ADD NEW RACE
with st.expander("➕ Add New Race"):
    race_id = st.text_input("Race ID")
    race_name = st.text_input("Race Name")
    track_name = st.text_input("Track Name")
    race_date = st.date_input("Race Date")
    race_time = st.time_input("Race Time")

    if st.button("Add Race"):
        if not (race_id and race_name and track_name): # check if user entered all the required info
            st.warning("⚠️ Please fill in all fields before adding a race.")
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO Race VALUES (%s, %s, %s, %s, %s)", # The SQL query ro add a new race inro the Race table
                    (race_id, race_name, track_name, race_date, race_time)
                )
                conn.commit()
                st.success(f"✅ Race '{race_name}' added successfully!") # success
            except mysql.connector.Error as e:
                st.error(f"❌ Database Error: {e}")
            finally:
                cursor.close()
                conn.close()

# 2️⃣ DELETE OWNER
with st.expander("🗑 Delete Owner"):
    owner_id = st.text_input("Enter Owner ID to delete")
    confirm = st.checkbox("I confirm I want to delete this owner and related records")

    if st.button("Delete Owner"):
        if not owner_id: # check if user entered an owner ID or not
            st.warning("⚠️ Please enter an Owner ID.")
        elif not confirm: # check if user confirmed or not
            st.warning("⚠️ Please confirm before deleting.") 
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.callproc("delete_owner", [owner_id]) # calling the stored procedure
                conn.commit()
                st.success(f"✅ Owner {owner_id} deleted successfully!") # success
            except mysql.connector.Error as e:
                st.error(f"❌ Error: {e}")
            finally:
                cursor.close()
                conn.close()

# 3️⃣ MOVE HORSE
with st.expander("🏇 Move Horse to Another Stable"):
    horse_id = st.text_input("Horse ID")
    new_stable = st.text_input("New Stable ID")

    if st.button("Move Horse"):
        if not (horse_id and new_stable): # check if user entered something or not
            st.warning("⚠️ Please enter both Horse ID and Stable ID.")
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                # to verify horse exists
                cursor.execute("SELECT COUNT(*) FROM Horse WHERE horseId=%s", (horse_id,)) # The SQL Query to selecrs the required horse
                if cursor.fetchone()[0] == 0:
                    st.error("❌ Horse ID not found.") #Handeling the case if horse ID does not exist
                else:
                    cursor.execute("SELECT COUNT(*) FROM Stable WHERE stableId=%s", (new_stable,))
                    if cursor.fetchone()[0] == 0:
                        st.error("❌ Stable ID not found.") #Handeling the case if stable ID does not exist
                    else:
                        cursor.execute("UPDATE Horse SET stableId=%s WHERE horseId=%s", # SQL Query to set the new stable for the horse
                                       (new_stable, horse_id))
                        conn.commit()
                        st.success(f"✅ Horse {horse_id} moved to Stable {new_stable}!") # success 

            except mysql.connector.Error as e:
                st.error(f"❌ Database Error: {e}")
            finally:
                cursor.close()
                conn.close()


# 4️⃣ APPROVE TRAINER
with st.expander("✅ Approve New Trainer"):
    trainer_id = st.text_input("Trainer ID") # Prompting all required info for the trainer table ( i.e. all column names )
    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    stable_id = st.text_input("Stable ID")

    if st.button("Approve Trainer"):
        if not (trainer_id and fname and lname and stable_id): # Handleing the case if the user did not provide any info 
            st.warning("⚠️ Please fill in all fields before approval.")
        else:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO Trainer VALUES (%s,%s,%s,%s)", # If the row entred by the user already exists SQL will automatically drop this new row since its a duplicate
                    (trainer_id, fname, lname, stable_id)
                )
                conn.commit()
                st.success(f"✅ Trainer {fname} {lname} approved for Stable {stable_id}!") # success
            except mysql.connector.Error as e:
                st.error(f"❌ Error: {e}")
            finally:
                cursor.close()
                conn.close()

# Footer
st.markdown("""
<div class="footer">
    <h3>Horse Racing Admin Panel</h3>
    <p>Manage with confidence 🏆</p>
</div>
""", unsafe_allow_html=True)
