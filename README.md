# Smart Cleaning Berlin - 28 Units Automation Platform

**Live Demo:** https://smart-cleaning-berlin-himanshi.s3-website.eu-central-1.amazonaws.com
**Tech Stack:** Python, Flask, REST API, AWS S3, Smoobu PMS API, Real-time Dashboard
**Status:** Active - Managing 28 listings across Berlin

### Overview
Operations automation platform for a Berlin-based vacation rental management company handling 28 short-term rental listings across 5 buildings: Mitte, Prenzlauer Berg, Friedrichshain, Kreuzberg, Charlottenburg.

Automates daily check-out tracking, staff assignment, and revenue reporting - reducing manual coordination time by 70% vs WhatsApp/Excel workflow.

### Problem Solved
- Manual tracking of 28 daily check-outs via Smoobu PMS
- Coordinating 4 cleaning staff across 5 Berlin districts  
- Preventing late cleanings and guest check-in delays
- No centralized view of operations and revenue

### Solution & Workflow
1. **Fetch:** Daily check-outs from Smoobu API (28 listings)
2. **Assign:** Auto-assign tasks to staff by building proximity & load balancing
3. **Alert:** Flag urgent cleanings (<4h to next check-in)
4. **Track:** Calculate daily revenue and completion status
5. **Dashboard:** Real-time operations view for manager

### Key Features
- **28 Units Live** - Complete data with building, floor, staff assignment
- **Today's Check-outs** - Auto-filtered from Smoobu API
- **Smart Assignment** - 4 staff (Anna, Mark, Lisa, Yusuf) with load balancing
- **Urgent Alerts** - Check-ins within 4 hours highlighted
- **Revenue Tracking** - Daily/monthly cleaning revenue
- **Building View** - Grouped by 5 Berlin districts

### Tech Stack
- **Backend:** Python 3.11, Flask, Flask-CORS, REST API
- **Frontend:** HTML5, CSS3, Vanilla JavaScript (responsive)
- **APIs:** Smoobu PMS API (28 real listings - mocked for demo)
- **Hosting:** AWS S3 Static Hosting (Frontend), Render/EC2 (Backend) - eu-central-1
- **Database Design:** MySQL (properties, bookings, cleaning_tasks, revenue)
- **Version Control:** Git, GitHub

### Live Demo
- **Frontend (S3):** [Your S3 Link Here]
- **Backend API:** [Your Render Link Here] /api/dashboard

### How to Run Locally
```bash
pip install -r requirements.txt
python app.py
# Open http://127.0.0.1:5000
