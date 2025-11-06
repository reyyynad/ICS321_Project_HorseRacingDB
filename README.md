🐎 Horse Racing Database System

ICS321 – Database Systems Project #1
Due Date: October 18, 2025
Course: ICS321, King Fahd University of Petroleum and Minerals (KFUPM)

📘 Project Overview

This project implements a Horse Racing Database System using MySQL and a Python interface (Streamlit).
It allows two types of users — Admin and Guest — to manage and explore data about horse racing, trainers, owners, and race results.

The system is based on a relational schema with tables for stables, horses, owners, trainers, races, and tracks.
It demonstrates database design, SQL programming, procedural SQL (stored procedures, triggers), and a connected front-end interface.

🧩 Features
👨‍💼 Admin Functions

➕ Add a new race with results

❌ Delete an owner and all related information (via stored procedure)

🏇 Move a horse from one stable to another

✅ Approve a new trainer to join a stable

👤 Guest Functions

🔍 View horses by owner’s last name (with trainer details)

🏆 Browse trainers who have trained winning horses

💰 View each trainer’s total prize winnings, sorted by total amount

🗺️ List all race tracks, race counts, and total horse participants per track

🧠 Database Schema

Main Tables:

Stable(stableId, stableName, location, colors)

Horse(horseId, horseName, age, gender, registration, stableId)

Owner(ownerId, lname, fname)

Owns(ownerId, horseId)

Trainer(trainerId, lname, fname, stableId)

Race(raceId, raceName, trackName, raceDate, raceTime)

RaceResults(raceId, horseId, results, prize)

Track(trackName, location, length)

Constraints & Rules:

Each horse belongs to one stable.

Horses and owners have many-to-many relationships via Owns.

Trainers belong to one stable.

Races happen on tracks and can include multiple horses.

⚙️ Implementation Details
🧱 Backend

Database: MySQL

Procedural SQL:

Stored Procedure to delete an owner and related info

Trigger to copy horse info to old_info table on deletion

💻 Frontend

Language: Python

Libraries:

streamlit (UI)

mysql-connector-python (DB connection)

pandas (data handling)

🧰 How to Run

Import racing_schema.sql into MySQL

Run the app:

streamlit run app/main.py


Choose Admin or Guest mode to interact with the database

📸 Sample Screens
Admin Panel	Guest Panel

	
🏫 Credits

Course: ICS321 – Database Systems

Instructor: [Your Instructor’s Name]

Student: [Your Name]

Semester: Fall 2025

📜 License

This project is developed for academic purposes and may not be used commercially without permission.