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


class TKWindow:
    def __init__(self):
        window=Tk()
        window.title("show")
        window.geometry("800x600")
        Label(window, text="시도").place(x=500,y=40)
        self.sido=Entry(window,text='',justify=RIGHT,width=25)
        self.sido.place(x=550,y=40)

        Label(window, text="시군구").place(x=495,y=70)
        self.sigun=Entry(window,text='',justify=RIGHT,width=25)
        self.sigun.place(x=550,y=70)

        self.searchButton=Button(window,text="검색")
        self.searchButton.place(x=690,y=100)
        self.quickButton=Button(window,text="즐겨찾기")
        self.quickButton.place(x=620,y=100)
        Text(window,width=45,height=20).place(x=450,y=300)


        Label(window,text="관광지명").place(x=150,y=20)
        Label(window, text="설명문").place(x=155,y=60)
        Text(window,width=45,height=12).place(x=30,y=90)


        self.earth = PhotoImage(file="Image/sample.png")
        Label(window,text="Tel : 000-000-000").place(x=240,y=270)
        Label(window, image=self.earth).place(x=30, y=340)

        window.mainloop()



TKWindow()