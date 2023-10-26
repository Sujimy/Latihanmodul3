data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi untuk menghitung data float
def calculate_float_duration(duration_str):
    total_minutes = parse_duration(duration_str)
    hours_decimal = total_minutes / 60
    return round(hours_decimal, 1)

# Fungsi untuk menghitung data int
def calculate_int_duration(duration_str):
    total_minutes = parse_duration(duration_str)
    ratusan = total_minutes // 100
    sisa = total_minutes % 100
    puluhan = sisa // 10
    satuan = sisa % 10
    return {'ratusan': int(ratusan), 'puluhan': int(puluhan), 'satuan': int(satuan)}

# Fungsi untuk menghitung data string
def extract_strings(data_list):
    return [word for word in data_list.split()]

# Fungsi untuk mengurai durasi
def parse_duration(duration_str):  
    total_minutes = (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes
    return total_minutes

# Menerapkan fungsi-fungsi di atas pada data
float_data = [calculate_float_duration(d) for d in data]
int_data = [calculate_int_duration(d) for d in data]
string_data = extract_strings("Hello Python World AI")

# Mencetak hasil
print("Data float:", float_data)
print("Data Int:")
for item in int_data:
    print(item)
print("Data String:", string_data)
