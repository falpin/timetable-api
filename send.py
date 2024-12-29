import requests
URL = "https://127.0.0.1:5000"
response = requests.post(f"{URL}/get_data", json="{'teacher':'Колязова А. В.'}")
if response.status_code == 200:
    print("Данные успешно отправлены!")
