data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def parse_duration(duration_str):
    weeks, days, hours, minutes = 0, 0, 0, 0
    
    parts = duration_str.split()
    for i in range(0, len(parts), 2):
        value = int(parts[i])
        unit = parts[i + 1]
        if unit == "minggu":
            weeks = value
        elif unit == "hari":
            days = value
        elif unit == "jam":
            hours = value
        elif unit == "menit":
            minutes = value
    
    total_minutes = (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes
    return total_minutes

OutputData = list(map(parse_duration, data))
print(OutputData)
