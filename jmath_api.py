import uvicorn
from fastapi import FastAPI
from typing import Dict, Any
from oauth2client.service_account import ServiceAccountCredentials
import gspread as gd
import pandas as pd
from data.config import KEY,JMATH_GOOGLE_SHEET,BOT_TOKEN,MONTHS
import requests
import datetime
import calendar
import numpy as np
from df2gspread import df2gspread
from threading import Thread

app = FastAPI()

def get_google_sheet_datas():
    SCOPE = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(KEY, SCOPE)
    gc = gd.authorize(credentials)
    url = f"https://docs.google.com/spreadsheets/d/{JMATH_GOOGLE_SHEET}/export?format=csv"
    df = pd.read_csv(url)
    df = df[df["Актив"] == "1.0"]
    return df

def give_current_month_dataframe():
    SCOPE = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(KEY, SCOPE)
    gc = gd.authorize(credentials)
    month = MONTHS[str(datetime.datetime.now().month)]
    url = f"https://docs.google.com/spreadsheets/d/{month}/export?format=csv"
    df = pd.read_csv(url)
    year = datetime.datetime.now().year
    month_calendar = calendar.monthcalendar(year, datetime.datetime.now().month)
    if len(df.columns) < 30:
        if 31 in month_calendar[-1]:
            for i in range(1,32):
                df[str(i)] = " "
        else:
            for i in range(1,31):
                df[str(i)] = " "
    return df


def notify_people(id,message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={id}&text={message}"
    requests.get(url)


def make_holiday_all(date):
    date_object = datetime.datetime.strptime(date, '%Y-%m-%d')
    day = str(date_object.day)
    df = give_current_month_dataframe()
    students = df["Ф.И.О."].to_list()
    for student in students:
        df[day] = np.where(df["Ф.И.О."] == student, "holiday", df[day])
    SCOPE = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(KEY, SCOPE)
    month = MONTHS[str(datetime.datetime.now().month)]
    df2gspread.upload(df, month, credentials=credentials,start_cell="A1",row_names=False)


def make_holiday(students,date):
    date_object = datetime.datetime.strptime(date, '%Y-%m-%d')
    day = str(date_object.day)
    df = give_current_month_dataframe()
    students = df["Ф.И.О."].to_list()
    for student in students:
        df[day] = np.where(df["Ф.И.О."] == student, "holiday", df[day])
    SCOPE = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(KEY, SCOPE)
    month = MONTHS[str(datetime.datetime.now().month)]
    df2gspread.upload(df, month, credentials=credentials,start_cell="A1",row_names=False)


@app.post('/jmath/api/send_message_selected_parents')
def send_students_messages(data: Dict[Any, Any]):
    if "date" in data.keys():
        make_holiday(data["students"][0]["students"], data["date"])
    df = get_google_sheet_datas()
    if len(data["text"]) == 0:
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
    else:
        students = data["students"][0]["students"]
        for student in students:
            id = df[df["Ф.И.О."] == student]["family_id"].iloc[-1]
            try:
                notify_people(int(id), data["text"])
            except:
                continue
    return 200


@app.post('/jmath/api/notify_all_parents_holiday')
def send_students_messages(data: Dict[Any, Any]):
    if "date" in data.keys():
        make_holiday_all(data["date"])
    df = get_google_sheet_datas()
    parents = df["family_id"].to_list()
    for parent in parents:
        try:
            notify_people(int(parent), data["text"])
        except:
            continue
    return 200


@app.post('/jmath/api/send_message_selected_students')
def send_students_messages(data: Dict[Any, Any]):
    df = get_google_sheet_datas()
    if len(data["text"]) == 0:
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
            id = df[df["Ф.И.О."] == student]["student_id"].iloc[-1]
            try:
                notify_people(int(id), data["text"])
            except:
                continue
    return 200


@app.post('/jmath/api/send_message_all')
def make_attendance(data: Dict[Any, Any]):
    df = get_google_sheet_datas()
    students = df["student_id"].to_list()
    parents = df["family_id"].to_list()
    for student in students:
        try:
            notify_people(int(student), data["student"])
        except:
            continue
    for parent in parents:
        try:
            notify_people(int(parent), data["parent"])
        except:
            continue
    return 200

def attend_students(students,df_main):
    df = give_current_month_dataframe()
    for student in students:
        id = df_main[df_main["Ф.И.О."] == student]["family_id"].iloc[-1]
        if students[student]["attendance"] == "true":
            date = str(datetime.datetime.now().day)
            df[date] = np.where(df["Ф.И.О."] == student, "here", df[date])
            notify_people(id, "Ваш ребенок прибыл на занятие")
        else:
            date = str(datetime.datetime.now().day)
            df[date] = np.where(df["Ф.И.О."] == student, "absent", df[date])
            notify_people(id, "Ваш ребенок не прибыл на занятие")
    SCOPE = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(KEY, SCOPE)
    month = MONTHS[str(datetime.datetime.now().month)]
    df = df.fillna(" ")
    df2gspread.upload(df, month, credentials=credentials,start_cell="A1",row_names=False)


@app.post('/jmath/api/make_attendance')
def make_attendance(data: Dict[Any, Any]):
    students = data["students"][0]["students"]
    df = get_google_sheet_datas()
    Thread(target=attend_students, args=(students,df,)).start()
    for student in students:
        print(student)
        print(df[df["Ф.И.О."] == student])
        id = df[df["Ф.И.О."] == student]["family_id"].iloc[-1]
        try:
            notify_people(int(id), students[student]["text"])
        except:
            continue
    return 200

@app.post('/jmath/api/set_times/')
def get_time(data: Dict[Any, Any]):
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

@app.post('/jmath/api/give_students/')
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


uvicorn.run(app, host="0.0.0.0", port=1007)