# 🐎 Horse Racing Database System – ICS321 Project 1

**Course:** ICS321 – Database Systems  
**University:** King Fahd University of Petroleum and Minerals (KFUPM)  
**Group Members:** Renad Elsafi & Joud Aljabri  
**Semester:** Fall 2025 (251)

---

## 📘 Project Overview

This project implements a **Horse Racing Database System** using **MySQL** as the backend and a **Python (Streamlit)** interface as the frontend.  
It supports two user roles — **Admin** and **Guest** — to manage and explore data about **horses, stables, owners, trainers, and races**.

The system demonstrates:
- Database design and normalization  
- SQL programming (DDL and DML)  
- Procedural SQL concepts (Stored Procedures and Triggers)  
- Integration between Python and MySQL through Streamlit  

---

## 🧩 Features

### 👨‍💼 Admin Functions
- ➕ **Add a new race** with results  
- ❌ **Delete an owner** and all related information *(via stored procedure)*  
- 🏇 **Move a horse** from one stable to another  
- ✅ **Approve a new trainer** to join a stable  

### 👤 Guest Functions
- 🔍 **Browse horses** by owner’s last name *(with trainer details)*  
- 🏆 **View trainers** who have trained winning horses *(1st place)*  
- 💰 **View total prize winnings** per trainer, sorted by total amount  
- 🗺️ **List race tracks**, race counts, and total horse participants per track  

---

## 🧠 Database Schema

### **Main Tables**
- **Stable**(stableId, stableName, location, colors)  
- **Horse**(horseId, horseName, age, gender, registration, stableId)  
- **Owner**(ownerId, lname, fname)  
- **Owns**(ownerId, horseId)  
- **Trainer**(trainerId, lname, fname, stableId)  
- **Race**(raceId, raceName, trackName, raceDate, raceTime)  
- **RaceResults**(raceId, horseId, results, prize)  
- **Track**(trackName, location, length)  

### **Constraints & Relationships**
- Each **horse** belongs to one **stable**.  
- A **horse** can have multiple **owners** (many-to-many via `Owns`).  
- Each **trainer** belongs to one **stable**.  
- A **race** takes place on a **track** and can include multiple horses.  
- **Owners** may own multiple horses across multiple stables.  

---

## ⚙️ Implementation Details

### 🧱 Backend
- **Database:** MySQL  
- **Procedural SQL:**
  - Stored Procedure → Deletes an owner and all related information.  
  - Trigger → Copies deleted horse info into an `old_info` table.  

### 💻 Frontend
- **Language:** Python  
- **Framework:** Streamlit  
- **Libraries Used:**
  - `streamlit` → User interface  
  - `mysql-connector-python` → Database connection  
  - `pandas` → Data handling and display  

---

## 🧰 How to Run

1. **Set up the Database**
   - Open MySQL Workbench or MySQL CLI.  
   - Import the schema file:
     ```bash
     source ./racing_schema.sql
     ```
   - Verify that the database name in your Python connection matches the created schema.

2. **Run the Application**
   ```bash
   streamlit run app/main.py
````

3. **Login Options**

   * Choose **Admin** or **Guest** mode from the Streamlit sidebar.
   * Interact with the database based on your selected role.


---

## 📜 License

This project was developed **for academic purposes only** as part of the ICS321 course and may not be used commercially without permission.

