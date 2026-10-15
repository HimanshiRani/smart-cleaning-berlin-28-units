from flask import Flask, jsonify, render_template
from flask_cors import CORS
from data import PROPERTIES, BOOKINGS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/stats")
def stats():
    total_properties = len(PROPERTIES)
    buildings = len(set(p["building"] for p in PROPERTIES))
    checkout_today = [b for b in BOOKINGS if b["status"] == "Checkout Today"]
    checkin_today = [b for b in BOOKINGS if b["status"] == "Checkin Today"]
    pending_cleaning = [b for b in BOOKINGS if b["cleaner"] in ["Pending", "To Assign", "Pending"]]
    monthly_revenue = sum(b["revenue"] for b in BOOKINGS)
    
    return jsonify({
        "total_properties": total_properties,
        "total_buildings": buildings,
        "checkout_today": checkout_today,
        "checkin_today": checkin_today,
        "pending_cleaning": len(pending_cleaning),
        "monthly_revenue": monthly_revenue,
        "all_bookings": BOOKINGS,
        "all_properties": PROPERTIES
    })

@app.route("/api/cleaning")
def cleaning():
    tasks = []
    for b in BOOKINGS:
        if b["status"] == "Checkout Today":
            tasks.append({
                "apartment": b["apartment"],
                "building": b["building"],
                "task": "Full Cleaning + Linen Change",
                "priority": "Urgent - Guest checkout 11:00",
                "cleaner": b["cleaner"],
                "platform": b["platform"]
            })
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)