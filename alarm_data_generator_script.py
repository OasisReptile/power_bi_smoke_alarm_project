import csv, random
from datetime import datetime, timedelta

n = 100
out_file = "fact_inspections.csv"

lat_range = (54.60820475426634, 54.337998652049926)
lon_range = (-1.063721069466439, -1.8168882192424871)

employee_id = [1001, 1002, 1003, 1004, 1005, 1006, 1007]

start_date = "2026-01-01"
end_date   = "2026-12-31"

def random_employee_id():
    return random.choice(employee_id)

def random_smoke_alarm():
    present = random.choices(["Yes", "No", "Not Visited"], weights=[0.7, 0.1, 0.2])[0]
    if present == "Not Visited":
        return ("Not Visited", "N/A")
    elif present == "No":
        return ("No", "N/A")
    else:
        working = random.choices(["Yes", "No"], weights=[0.85, 0.15])[0]
        return ("Yes", working)

def random_date_between(start_date_str, end_date_str):
    fmt = "%Y-%m-%d"
    start = datetime.strptime(start_date_str, fmt).date()
    end = datetime.strptime(end_date_str, fmt).date()
    delta_days = (end - start).days
    random_days = random.randint(0, delta_days)
    return (start + timedelta(days=random_days)).isoformat()

with open(out_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["latitude", "longitude", "property_id", "assigned_to_id",
                     "smoke_alarm_present", "smoke_alarm_working", "inspection_date"])
    for i in range(n):
        lat = random.uniform(*lat_range)
        lon = random.uniform(*lon_range)
        property_id = 2001 + i
        assigned_to = random_employee_id()
        present, status = random_smoke_alarm()
        inspection_date = random_date_between(start_date, end_date)
        writer.writerow([lat, lon, property_id, assigned_to, present, status, inspection_date])
