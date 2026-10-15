# Smart Cleaning Berlin - 28 Units Automation Platform
Python | Flask | Smoobu API | AWS S3 + EC2 | SQL

Managing automation for 28 short-term rental apartments across 7 buildings in Berlin (Brandenburgische Str 16, Kurfürstendamm 103, Kudamm Collection, Schildhornstr 88, Babelsberger, Seesener).

## Features
- Multi-calendar dashboard syncing Airbnb + Booking.com via Smoobu Channel Manager
- Today's check-outs / check-ins auto-detection
- Auto-assign cleaning staff
- Revenue tracking, occupancy tracking
- 28 properties database

## Tech Stack
- Backend: Python, Flask, REST API, Flask-Cors
- Frontend: HTML5, CSS3, JavaScript
- API: Smoobu API integration (prototype on mock data - staff account limitation)
- Deployment: Frontend on AWS S3 Static Hosting, Backend on EC2 / Render
- Database Design: MySQL (properties, bookings, cleaning_tasks, revenue)

## Live Demo
- Frontend: [YOUR S3 LINK]
- Backend API: [YOUR RENDER LINK]

## How to Run
pip install -r requirements.txt
python app.py
-> http://127.0.0.1:5000

## For Blue Card / Ausländerbehörde
This project proves IT Management role in cleaning company - automation of 28 listings via API integration, not manual cleaning.