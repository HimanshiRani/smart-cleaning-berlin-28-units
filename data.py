# Smart Cleaning - 28 Properties - Berlin
# Based on real Smoobu Multi-Calendar structure

PROPERTIES = [
    # Brandenburgische 16 - 4 units
    {"id": 1, "building": "Brandenburgische Str 16", "name": "Brandenburger Tor", "type": "1BR", "floor": "2.OG"},
    {"id": 2, "building": "Brandenburgische Str 16", "name": "Fernsehturm", "type": "Studio", "floor": "3.OG"},
    {"id": 3, "building": "Brandenburgische Str 16", "name": "Funkturm", "type": "Studio", "floor": "3.OG"},
    {"id": 4, "building": "Brandenburgische Str 16", "name": "Siegessäule", "type": "2BR", "floor": "4.OG"},
    
    # Kurfürstendamm 103 - 12 units (401-412)
    {"id": 5, "building": "Kurfürstendamm 103", "name": "401", "type": "Studio", "floor": "4.OG"},
    {"id": 6, "building": "Kurfürstendamm 103", "name": "402", "type": "1BR", "floor": "4.OG"},
    {"id": 7, "building": "Kurfürstendamm 103", "name": "403", "type": "1BR", "floor": "4.OG"},
    {"id": 8, "building": "Kurfürstendamm 103", "name": "404", "type": "Studio", "floor": "4.OG"},
    {"id": 9, "building": "Kurfürstendamm 103", "name": "405", "type": "2BR", "floor": "4.OG"},
    {"id": 10, "building": "Kurfürstendamm 103", "name": "406", "type": "1BR", "floor": "4.OG"},
    {"id": 11, "building": "Kurfürstendamm 103", "name": "407", "type": "2BR", "floor": "4.OG"},
    {"id": 12, "building": "Kurfürstendamm 103", "name": "408", "type": "Studio", "floor": "4.OG"},
    {"id": 13, "building": "Kurfürstendamm 103", "name": "409", "type": "1BR", "floor": "4.OG"},
    {"id": 14, "building": "Kurfürstendamm 103", "name": "410", "type": "1BR", "floor": "4.OG"},
    {"id": 15, "building": "Kurfürstendamm 103", "name": "411", "type": "2BR", "floor": "4.OG"},
    {"id": 16, "building": "Kurfürstendamm 103", "name": "412", "type": "Studio", "floor": "4.OG"},
    
    # Kudamm Collection - 7 units
    {"id": 17, "building": "Kudamm Collection", "name": "Kudamm Grand Giga", "type": "2BR", "floor": "1.OG"},
    {"id": 18, "building": "Kudamm Collection", "name": "Kudamm 1.Amsterdam", "type": "1BR", "floor": "2.OG"},
    {"id": 19, "building": "Kudamm Collection", "name": "Kudamm 2.Madrid", "type": "1BR", "floor": "2.OG"},
    {"id": 20, "building": "Kudamm Collection", "name": "Kudamm 3.London", "type": "Studio", "floor": "3.OG"},
    {"id": 21, "building": "Kudamm Collection", "name": "Kudamm 4.Paris", "type": "1BR", "floor": "3.OG"},
    {"id": 22, "building": "Kudamm Collection", "name": "Kudamm 5.Rom", "type": "2BR", "floor": "4.OG"},
    {"id": 23, "building": "Kudamm Collection", "name": "Kudamm 6.Berlin", "type": "Penthouse", "floor": "5.OG"},
    
    # Other Buildings - 5 units
    {"id": 24, "building": "Schildhornstr 88", "name": "Schildhorn Alpha", "type": "2BR", "floor": "1.OG"},
    {"id": 25, "building": "Schildhornstr 88", "name": "Schildhorn Beta", "type": "2BR", "floor": "2.OG"},
    {"id": 26, "building": "Babelsberger Str", "name": "Babelsberger Loft", "type": "1BR", "floor": "3.OG"},
    {"id": 27, "building": "Seesener Str 41A", "name": "5.OG Stylish City Apt", "type": "2BR", "floor": "5.OG"},
    {"id": 28, "building": "Seesener Str 46", "name": "5OG Central Berlin Apt", "type": "1BR", "floor": "5.OG"},
]

BOOKINGS = [
    {"id": 101, "apartment": "401", "building": "Kurfürstendamm 103", "platform": "Booking.com", "guest": "Guest A", "checkin": "2026-10-13", "checkout": "2026-10-15", "cleaner": "Anna", "status": "Checkout Today", "revenue": 89},
    {"id": 102, "apartment": "Brandenburger Tor", "building": "Brandenburgische Str 16", "platform": "Airbnb", "guest": "Guest B", "checkin": "2026-10-12", "checkout": "2026-10-15", "cleaner": "Pending", "status": "Checkout Today", "revenue": 120},
    {"id": 103, "apartment": "402", "building": "Kurfürstendamm 103", "platform": "Booking.com", "guest": "Guest C", "checkin": "2026-10-14", "checkout": "2026-10-15", "cleaner": "Maria", "status": "Checkout Today", "revenue": 95},
    {"id": 104, "apartment": "Kudamm 1.Amsterdam", "building": "Kudamm Collection", "platform": "Booking.com", "guest": "Guest D", "checkin": "2026-10-10", "checkout": "2026-10-16", "cleaner": "Anna", "status": "Checkout Tomorrow", "revenue": 110},
    {"id": 105, "apartment": "403", "building": "Kurfürstendamm 103", "platform": "Airbnb", "guest": "Guest E", "checkin": "2026-10-15", "checkout": "2026-10-18", "cleaner": "To Assign", "status": "Checkin Today", "revenue": 135},
    {"id": 106, "apartment": "Siegessäule", "building": "Brandenburgische Str 16", "platform": "Booking.com", "guest": "Guest F", "checkin": "2026-10-15", "checkout": "2026-10-20", "cleaner": "John", "status": "Checkin Today", "revenue": 210},
    {"id": 107, "apartment": "404", "building": "Kurfürstendamm 103", "platform": "Booking.com", "guest": "Guest G", "checkin": "2026-10-11", "checkout": "2026-10-17", "cleaner": "Maria", "status": "Occupied", "revenue": 180},
    {"id": 108, "apartment": "Kudamm 6.Berlin", "building": "Kudamm Collection", "platform": "Booking.com", "guest": "Guest H", "checkin": "2026-10-16", "checkout": "2026-10-19", "cleaner": "Pending", "status": "Checkin Tomorrow", "revenue": 250},
    {"id": 109, "apartment": "Schildhorn Alpha", "building": "Schildhornstr 88", "platform": "Airbnb", "guest": "Guest I", "checkin": "2026-10-01", "checkout": "2026-10-30", "cleaner": "Weekly", "status": "Long Stay", "revenue": 1800},
    {"id": 110, "apartment": "5.OG Stylish City Apt", "building": "Seesener Str 41A", "platform": "Booking.com", "guest": "Maintenance", "checkin": "2026-10-15", "checkout": "2026-10-16", "cleaner": "Blocked", "status": "Blocked", "revenue": 0},
]