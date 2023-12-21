import tkinter as tk
import pandas as pd
from time import gmtime, strftime

window = tk.Tk()
window.title('Advertising time recommendation')
window.geometry("500x300")

gender_options = ["Male", "Female"]
leisure_options = ["TV/Youtube","Surf web", "Eating", "Relaxing"]
province_options = [
    'Ha Noi', 'Lao Cai', 'Son La', 'Yen Bai', 'Hoa Binh', 'Thai Nguyen', 'Lang Son', 'Quang Ninh',
    'Bac Giang', 'Phu Tho', 'Hai Phong', 'Hung Yen', 'Ha Nam', 'Nam Dinh', 'Thanh Hoa', 'Nghe An',
    'Ha Tinh', 'Quang Binh', 'Hue', 'Da Nang', 'Binh Dinh', 'Khanh Hoa', 'Gia Lai', 'Dak Lak',
    'Lam Dong', 'Binh Phuoc', 'Tay Ninh', 'Binh Duong', 'Dong Nai', 'Vung Tau', 'HCM', 'Long An',
    'Tien Giang', 'Dong Thap', 'An Giang', 'Kien Giang', 'Can Tho', 'Hau Giang', 'Bac Lieu'
]

# Biến để lưu giá trị được chọn
selected_gender = tk.StringVar(window)
selected_gender.set(gender_options[1])  # Giá trị mặc định
selected_leisure = tk.StringVar(window)
selected_leisure.set(leisure_options[0])

# Thêm nhãn cho các trường nhập liệu
label_gender = tk.Label(window, text="Gender:", bg="white", fg="black")
label_area = tk.Label(window, text="Province:", bg="white", fg="black")
label_age = tk.Label(window, text="Age:", bg="white", fg="black")
label_field = tk.Label(window, text="Activity", bg="white", fg="black")
label_time = tk.Label(window, text="Time suitable for run Ads:", bg="white", fg="black")

# Thêm các trường nhập liệu
entry_gender = tk.OptionMenu(window, selected_gender, *gender_options)
entry_area = tk.Entry(window, width=10, bg="white", fg="black")
entry_age = tk.Entry(window, width=10, bg="white", fg="black")
entry_field = tk.OptionMenu(window, selected_leisure, *leisure_options)
entry_gender.config(width=10)
entry_field.config(width=10)


def get_gender_id_category(gender):
    if gender == "Male":
        return 1
    elif gender == "Female":
        return 2
def get_area_id(area):
    if area == 'Ha Noi':
        return 1
    elif area == 'Lao Cai':
        return 10
    elif area == 'Son La':
        return 14
    elif area == 'Yen Bai':
        return 15
    elif area == 'Hoa Binh':
        return 17
    elif area == 'Thai Nguyen':
        return 19
    elif area == 'Lang Son':
        return 20
    elif area == 'Quang Ninh':
        return 22
    elif area == 'Bac Giang':
        return 24
    elif area == 'Phu Tho':
        return 25
    elif area == 'Hai Phong':
        return 31
    elif area == 'Hung Yen':
        return 33
    elif area == 'Ha Nam':
        return 35
    elif area == 'Nam Dinh':
        return 36
    elif area == 'Thanh Hoa':
        return 38
    elif area == 'Nghe An':
        return 40
    elif area == 'Ha Tinh':
        return 42
    elif area == 'Quang Binh':
        return 44
    elif area == 'Hue':
        return 46
    elif area == 'Da Nang':
        return 48
    elif area == 'Binh Dinh':
        return 52
    elif area == 'Khanh Hoa':
        return 56
    elif area == 'Gia Lai':
        return 64
    elif area == 'Dak Lak':
        return 66
    elif area == 'Lam Dong':
        return 68
    elif area == 'Binh Phuoc':
        return 70
    elif area == 'Tay Ninh':
        return 72
    elif area == 'Binh Duong':
        return 74
    elif area == 'Dong Nai':
        return 75
    elif area == 'Vung Tau':
        return 77
    elif area == 'HCM':
        return 79
    elif area == 'Long An':
        return 80
    elif area == 'Tien Giang':
        return 82
    elif area == 'Dong Thap':
        return 87
    elif area == 'An Giang':
        return 89
    elif area == 'Kien Giang':
        return 91
    elif area == 'Can Tho':
        return 92
    elif area == 'Hau Giang':
        return 93
    elif area == 'Bac Lieu':
        return 95
def get_activity_id(activity):
    if activity == "Entertainment":
        return [1201, 1202, 1203, 1299]
    elif activity == "TV/Youtube":
        return 1402
    elif activity == "Surf web":
        return 1404
    elif activity == "Eating":
        return 1502
    elif activity == "Relaxing":
        return 1506
    else:
        return None
def convert_time(minute):
    return strftime("%H:%M", gmtime(int(minute) * 60))
def get_time(gender, area, age, field):
    # Tải dữ liệu time-use survey vietnamese và gán vào 3 biến để có thể phân tích từng khung thời gian
    df_morning = pd.read_csv("thatsgood.csv", encoding='latin-1')
    df_afternoon = pd.read_csv("thatsgood.csv", encoding='latin-1')
    df_evening = pd.read_csv("thatsgood.csv", encoding='latin-1')

    # Chuyển dữ liệu từ string sang mã
    gender = get_gender_id_category(gender)
    area = get_area_id(area)
    field = get_activity_id(field)

    # Lọc dữ liệu theo giới tính, khu vực và độ tuổi
    df_morning = df_morning[df_morning["gender"] == gender]
    df_afternoon = df_afternoon[df_afternoon["gender"] == gender]
    df_evening = df_evening[df_evening["gender"] == gender]

    df_morning = df_morning[df_morning["MATINH"] == area]
    df_afternoon = df_afternoon[df_afternoon["MATINH"] == area]
    df_evening = df_evening[df_evening["MATINH"] == area]

    # df_morning = df_morning[df_morning["age"] == age]
    # df_afternoon = df_afternoon[df_afternoon["age"] == age]
    # df_evening = df_evening[df_evening["age"] == age]

    df_morning = df_morning[df_morning["Q401"] == field]
    df_afternoon = df_afternoon[df_afternoon["Q401"] == field]
    df_evening = df_evening[df_evening["Q401"] == field]

    # Thêm các trường BEGIN, END và Duration
    df_morning = df_morning[(0 <= df_morning["BEGIN"] / 60 - 4) & (df_morning["BEGIN"] / 60 - 4 < 12)]
    df_afternoon = df_afternoon[(12 <= df_afternoon["BEGIN"] / 60 - 4) & (df_afternoon["BEGIN"] / 60 - 4 < 18)]
    df_evening = df_evening[(18 <= df_evening["BEGIN"] / 60 - 4) & (df_evening["BEGIN"] / 60 - 4 <= 24)]

    # Tìm khoảng thời gian trung bình hoạt động nhiều nhất
    sum_morning_duration = df_morning["Duration"].sum()
    sum_afternoon_duration = df_afternoon["Duration"].sum()
    sum_evening_duration = df_evening["Duration"].sum()

    # Gán biến thời gian bắt đầu
    begin_morning = df_morning["BEGIN"].min()
    begin_afternoon = df_afternoon["BEGIN"].min()
    begin_evening = df_evening["BEGIN"].min()

    #Gán biến thời gian trung bình hoạt động
    average_morning = df_morning["Duration"].mean()
    average_afternoon = df_afternoon["Duration"].mean()
    average_evening = df_evening["Duration"].mean()

    variables = {'morning': sum_morning_duration, 'afternoon': sum_afternoon_duration, 'evening': sum_evening_duration}
    max_variables = max(variables, key=variables.get)

    if max_variables == "morning":
        return "Vào buổi sáng bắt đầu lúc {} AM, Khoảng thời gian ước tính: {} phút".format(convert_time(begin_morning), int(average_morning))
    elif max_variables == "afternoon":
        return "Vào buổi chiều bắt đầu lúc {} PM, Khoảng thời gian ước tính {} phút".format(convert_time(begin_afternoon), int(average_afternoon))
    else:
        return "Vào buổi tối bắt đầu lúc {} PM, Khoảng thời gian ước tính {} phút".format(convert_time(begin_evening), int(average_evening))
def submit_info():
    # Lấy thông tin từ các trường nhập liệu
    gender = selected_gender.get()
    area = entry_area.get()
    age = int(entry_age.get())
    field = selected_leisure.get()

    # Xử lý thông tin và đưa ra thời gian quảng cáo
    time = get_time(gender, area, age, field)

    # Hiển thị thời gian quảng cáo
    label_time.config(text=time)


# Thêm nút để gửi thông tin
button_submit = tk.Button(window, text="Submit", command=submit_info)

# Sắp xếp các widget
label_gender.grid(row=0, column=0, padx=10, pady=10)
entry_gender.grid(row=0, column=1, padx=10, pady=10)
label_area.grid(row=1, column=0, padx=10, pady=10)
entry_area.grid(row=1, column=1, padx=10, pady=10)
label_age.grid(row=2, column=0, padx=10, pady=10)
entry_age.grid(row=2, column=1, padx=10, pady=10)
label_field.grid(row=3, column=0, padx=10, pady=10)
entry_field.grid(row=3, column=1, padx=10, pady=10)
button_submit.grid(row=4, column=1, padx=10, pady=10)
label_time.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
