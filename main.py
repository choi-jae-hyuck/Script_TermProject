# -*- coding: utf-8 -*-
from tkinter import *
from http.client import HTTPSConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import re
import folium

import smtplib
from email.mime.text import MIMEText

dms='126˚59˙53.65'
dms=re.findall("\d+",dms) #숫자만 나누기


connect=None
Detail_url='http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceDetail'
List_url="http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceList"
Key='cYtnsiDywOollKA9No97lS%2B7V3H1tl2gq5F%2BJyzAxQ70dhlac0M8D84OwUrJkVVy5wC7NwpkGa05zzXUIl3BWA%3D%3D'


class TKWindow:
    def __init__(self):
        window=Tk()
        window.title("show")
        window.geometry("800x600")
        Label(window, text="시도").place(x=500,y=40)
        self.SIDOScroll=Scrollbar(window,width=20)
        self.SIDOScroll.place(x=700,y=30)
        self.SiDOList=Listbox(window,activestyle='none',width=18, height=1, borderwidth=12, relief='ridge'
                              ,yscrollcommand=self.SIDOScroll.set)
        self.SiDOList.place(x=550,y=30)
        self.InsertSIDO()

        Label(window, text="시군구").place(x=495,y=70)
        self.SIGUNScroll=Scrollbar(window,width=20)
        self.SIGUNScroll.place(x=700,y=70)
        self.SiGUNList = Listbox(window, activestyle='none', width=18, height=1, borderwidth=12, relief='ridge'
                                , yscrollcommand=self.SIGUNScroll.set)
        self.SiGUNList.place(x=550, y=70)

        self.searchButton=Button(window,text="검색",command=self.Search)
        self.searchButton.place(x=690,y=120)
        self.quickButton=Button(window,text="즐겨찾기")
        self.quickButton.place(x=620,y=120)
        Text(window,width=45,height=20).place(x=450,y=300)


        Label(window,text="관광지명").place(x=150,y=20)
        Label(window, text="설명문").place(x=155,y=60)
        Text(window,width=45,height=12).place(x=30,y=90)


        self.earth = PhotoImage(file="Image/sample.png")
        Label(window,text="Tel : 000-000-000").place(x=240,y=270)
        Label(window, image=self.earth).place(x=30, y=340)

        window.mainloop()

    def Search(self):
        sido=self.SiDOList.curselection()[0]
        sigun="a"
        self.url=userURLBuilder(List_url,ServiceKey=Key, SIDO=sido, GUNGU=str(sigun))
        print(sido)
        print(sigun)
        print(self.url)

    def InsertSIDO(self):
        self.SiDOList.insert(1, "서울특별시")
        self.SiDOList.insert(2, "부산광역시")
        self.SiDOList.insert(3, "대구광역시")
        self.SiDOList.insert(4, "인천광역시")
        self.SiDOList.insert(5, "광주광역시")
        self.SiDOList.insert(6, "대전광역시")
        self.SiDOList.insert(7, "울산광역시")
        self.SiDOList.insert(8, "제주특별자치도")
        self.SiDOList.insert(9, "경기도")
        self.SiDOList.insert(10, "강원도")
        self.SiDOList.insert(11, "충청북도")
        self.SiDOList.insert(12, "충청남도")
        self.SiDOList.insert(13, "전라북도")
        self.SiDOList.insert(14, "전라남도")
        self.SiDOList.insert(15, "경상북도")
        self.SiDOList.insert(16, "경상남도")
        self.SIDOScroll.config(command=self.SiDOList.yview)

    def ScrollMove(self):
        pass



def connectOpenAPIServer():
    global conn, server
    conn = HTTPSConnection(server)
    conn.set_debuglevel(1)

def userURLBuilder(url, **user):
    str = url + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str



TKWindow()