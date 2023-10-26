data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def extract_duration_parts(duration_str):
    parts = duration_str.split()
    weeks = parts[0]
    days = parts[2]
    hours = parts[4]
    minutes = parts[6]
    
    return [weeks, days, hours, minutes]

for item in data:
    duration_parts = extract_duration_parts(item)
    print(duration_parts)