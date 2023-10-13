import uvicorn
from fastapi import FastAPI
from typing import Dict, Any
from oauth2client.service_account import ServiceAccountCredentials
import gspread as gd
import pandas as pd
from data.config import KEY,JMATH_GOOGLE_SHEET,BOT_TOKEN
import requests

app = FastAPI()

def get_google_sheet_datas():
    SCOPE = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(KEY, SCOPE)
    gc = gd.authorize(credentials)
    url = f"https://docs.google.com/spreadsheets/d/{JMATH_GOOGLE_SHEET}/export?format=csv"
    df = pd.read_csv(url)
    df = df[df["Актив"] == "1.0"]
    return df


def notify_people(id,message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={id}&text={message}"
    requests.get(url)


@app.post('/api/send_message_selected_students')
def send_students_messages(data: Dict[Any, Any]):
    df = get_google_sheet_datas()
    print(data["field"])
    if data["field"] == 'Уведомления отдельно':
        students = data["students"][0]["students"]
        for student in students:
            if len(students[student]["text"]) != 0:
                id = df[df["Ф.И.О."] == student]["student_id"].iloc[-1]
                try:
                    notify_people(int(id), students[student]["text"])
                except:
                    continue
            else:
                continue
    else:
        students = data["students"][0]["students"]
        for student in students:
            if len(students[student]["text"]) != 0:
                id = df[df["Ф.И.О."] == student]["family_id"].iloc[-1]
                try:
                    notify_people(int(id), students[student]["text"])
                except:
                    continue
            else:
                continue
    return 200


@app.post('/api/send_message_all')
def make_attendance(data: Dict[Any, Any]):
    df = get_google_sheet_datas()
    students = df["student_id"].to_list()
    parents = df["family_id"].to_list()
    for student in students:
        try:
            continue
            # notify_people(int(student), data["student"])
        except:
            continue
    for parent in parents:
        try:
            continue
            # notify_people(int(parent), data["parent"])
        except:
            continue
    return 200


@app.post('/api/make_attendance')
def make_attendance(data: Dict[Any, Any]):
    students = data["students"][0]["students"]
    df = get_google_sheet_datas()
    # Thread(target=attend_students, args=(students,)).start()
    for student in students:
        id = df[df["Ф.И.О."] == student]["family_id"].iloc[-1]
        try:
            notify_people(int(id), students[student]["text"])
        except:
            continue
    return 200

@app.post('/api/set_times/')
def get_time(data: Dict[Any, Any]):
    print(data)
    if data["subject"] == "Математика":
        data = get_google_sheet_datas()
        returning_data = data[data["Предмет"] == "Математика"]
    elif data["subject"] == "Немецкий":
        data = get_google_sheet_datas()
        returning_data = data[data["Предмет"] == "Немецкий"]
    elif data["subject"] == "Японский":
        data = get_google_sheet_datas()
        returning_data = data[data["Предмет"] == "Японский"]
    return {'status':list(returning_data["Время"].unique())}, 200

@app.post('/api/give_students/')
def get_time(data: Dict[Any, Any]):
    if data["subject"] == "Математика":
        dataframe = get_google_sheet_datas()
        returning_data = dataframe[dataframe["Предмет"] == "Математика"]
        students = returning_data[returning_data["Время"] == data["time"]]
        students = students["Ф.И.О."].to_list()
    elif data["subject"] == "Немецкий":
        dataframe = get_google_sheet_datas()
        returning_data = dataframe[dataframe["Предмет"] == "Немецкий"]
        students = returning_data[returning_data["Время"] == data["time"]]
        students = students["Ф.И.О."].to_list()
    elif data["subject"] == "Японский":
        dataframe = get_google_sheet_datas()
        returning_data = dataframe[dataframe["Предмет"] == "Японский"]
        students = returning_data[returning_data["Время"] == data["time"]]
        students = students["Ф.И.О."].to_list()
    return {'status':students}, 200

@app.post('/api/registration')
def registration(data: Dict[Any, Any]):
    return 200

uvicorn.run(app, host="0.0.0.0", port=1010)