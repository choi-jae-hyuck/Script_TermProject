# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import font
import http.client
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

import re
import folium

import smtplib
from email.mime.text import MIMEText
from xml.etree import ElementTree

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
        Label(window, text="시도").place(x=500,y=45)
        TempFont = font.Font(window, size=20, weight='bold', family='Consolas')
        self.SIDOScroll=Scrollbar(window,width=20)
        self.SIDOScroll.place(x=722,y=30)
        self.SIDOLList=Listbox(window,font=TempFont,activestyle='none',width=10, height=1, borderwidth=10, relief='ridge',
                              yscrollcommand=self.SIDOScroll.set)
        self.InsertSIDO()
        self.SIDOLList.place(x=550,y=30)


        Label(window, text="시군구").place(x=495,y=110)
        #self.SIGUNScroll=Scrollbar(window,width=20)
        #self.SIGUNScroll.place(x=700,y=80)
        self.SIGUNList = Entry(window, width=25, borderwidth=3)
        self.SIGUNList.place(x=550, y=110)

        self.searchButton=Button(window,text="검색",command=self.Search)
        self.searchButton.place(x=690,y=140)
        self.quickButton=Button(window,text="즐겨찾기")
        self.quickButton.place(x=620,y=140)
        self.TEXTLIST = Listbox(window,width=45,height=20)
        self.TEXTLIST.place(x=450,y=200)
        self.TEXTLIST.bind('<<ListboxSelect>>', self.SelectBuild)

        TempFont = font.Font(window, size=20, weight='bold', family='Consolas')
        self.NAME=Label(window,text="관광지명",width=20,font=TempFont)
        self.NAME.place(x=30,y=20)
        self.TAG=Label(window, text="분류",width=100)
        self.TAG.place(x=-175,y=70)
        self.EXPLAIN=Text(window,width=45,height=14)
        self.EXPLAIN.place(x=30,y=100)





        self.Phone=Label(window,text="Tel : 000-000-000",width=20,font=TempFont)
        self.Phone.place(x=30,y=300)
        self.earth = PhotoImage(file="./Image/sample.png")
        #Label(window, image=self.earth).place(x=30, y=340)
        self.EARTH = Button(window, overrelief="solid", width=310,height=230,image=self.earth)
        self.EARTH.place(x=30, y=340)
        window.mainloop()

    def Search(self):
        sido_s=self.SIDOScroll.get()[1]
        if sido_s == 0.0625:
            self.Sido="서울특별시"
        elif sido_s == 0.125:
            self.Sido ="부산광역시"
        elif sido_s == 0.1875:
            self.Sido ="대구광역시"
        elif sido_s == 0.25:
            self.Sido ="인천광역시"
        elif sido_s == 0.3125:
            self.Sido ="광주광역시"
        elif sido_s == 0.375:
            self.Sido ="대전광역시"
        elif sido_s == 0.4375:
            self.Sido ="울산광역시"
        elif sido_s == 0.5:
            self.Sido ="제주특별자치도"
        elif sido_s == 0.5625:
            self.Sido ="경기도"
        elif sido_s == 0.625:
            self.Sido ="강원도"
        elif sido_s == 0.6875:
            self.Sido ="충청북도"
        elif sido_s == 0.75:
            self.Sido ="충청남도"
        elif sido_s == 0.8125:
            self.Sido ="전라북도"
        elif sido_s == 0.875:
            self.Sido ="전라남도"
        elif sido_s == 0.9375:
            self.Sido ="경상북도"
        elif sido_s == 1.0:
            self.Sido ="경상남도"
        self.Sigun=self.SIGUNList.get()

        self.url=userURLBuilder(List_url,ServiceKey=Key, SIDO=self.Sido, GUNGU=self.Sigun)
        print(self.url)
        self.SearchList()

    def InsertSIDO(self):
        self.SIDOLList.insert(1, "서울특별시")
        self.SIDOLList.insert(2, "부산광역시")
        self.SIDOLList.insert(3, "대구광역시")
        self.SIDOLList.insert(4, "인천광역시")
        self.SIDOLList.insert(5, "광주광역시")
        self.SIDOLList.insert(6, "대전광역시")
        self.SIDOLList.insert(7, "울산광역시")
        self.SIDOLList.insert(8, "제주특별자치도")
        self.SIDOLList.insert(9, "경기도")
        self.SIDOLList.insert(10, "강원도")
        self.SIDOLList.insert(11, "충청북도")
        self.SIDOLList.insert(12, "충청남도")
        self.SIDOLList.insert(13, "전라북도")
        self.SIDOLList.insert(14, "전라남도")
        self.SIDOLList.insert(15, "경상북도")
        self.SIDOLList.insert(16, "경상남도")
        self.SIDOScroll.config(command=self.SIDOLList.yview)

    def SearchList(self):
        self.DATALIST = []
        if self.TEXTLIST.size()>0:
            self.TEXTLIST.delete(0,END)
            self.TEXTLIST.update()

        req=requests.get(self.url)
        tree=ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")

        for item in itemElements:
            self.DATA = {}
            tag = item.find("ASctnNm")
            name = item.find("BResNm")
            self.DATA['tag']=tag.text
            self.DATA['name']=name.text
            self.DATALIST.append(self.DATA)

        for i in range(len(self.DATALIST)):
            str_name="["+ str(i+1) + "] 시설명 : " + self.DATALIST[i]['name']
            self.TEXTLIST.insert(i, str_name)

    def SelectBuild(self,evt):
        i=self.TEXTLIST.curselection()[0]
        NM=self.DATALIST[i]['name']
        self.url_d = userURLBuilder(Detail_url, ServiceKey=Key, SIDO=self.Sido, GUNGU=self.Sigun, RES_NM=NM)
        self.GoogleImageSearch(NM)

        req = requests.get(self.url_d)
        tree = ElementTree.fromstring(req.text)
        itemElements = tree.getiterator("item")
        self.DATALIST_d=[]
        for item in itemElements:
            self.DATA_d = {}
            explain=item.find("FSimpleDesc")
            phone=item.find("KPhone")
            if explain is None:
                self.DATA_d['explain'] = "설명없음"
            else:
                self.DATA_d['explain'] = explain.text
            self.DATA_d['phone'] = phone.text
            self.DATALIST_d.append(self.DATA_d)
        #print(self.DATALIST_d)
        self.NAME.configure(text=self.DATALIST[i]['name'])
        self.TAG.configure(text=self.DATALIST[i]['tag'])
        self.EXPLAIN.delete(1.0, END)
        self.EXPLAIN.update()
        self.EXPLAIN.insert(1.0,self.DATALIST_d[0]['explain'])
        self.Phone.configure(text=self.DATALIST_d[0]['phone'])

    def GoogleImageSearch(self,NM):
        from io import StringIO
        from lxml.html import parse
        import urllib.request
        from PIL import Image,ImageTk
        keyword = NM  # 키워드
        url='https://www.google.co.kr/search?q='+keyword+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1842&bih=990'
        text = requests.get(url).text
        text_source = StringIO(text)
        parsed = parse(text_source)

        doc = parsed.getroot()
        imgs = doc.findall('.//img')
        img = imgs[4].get('src')
        urllib.request.urlretrieve(img, "./Image/Build.png")

        im=Image.open("./Image/Build.png")
        im2=im.resize((300,230))
        im2.save("./Image/Build.png")

        self.earth2 = ImageTk.PhotoImage(Image.open("./Image/Build.png"))  # 안됨
        self.EARTH.config(image=self.earth2)

        self.GoogleMap(NM)

    def GoogleMap(self,NM):
        import requests
        from bs4 import BeautifulSoup
        import folium
        address=NM
        url="https://maps.googleapis.com/maps/api/geocode/xml?address="+address +"&key=AIzaSyBqGlKXTonSH1Sjd_eztuZpF2791ShpU5E"
        resq=requests.get(url)
        html=BeautifulSoup(resq.text,"lxml")
        lat=html.select("location>lat")
        lng=html.select("location>lng")
        w=lat[0].get_text()
        h=lng[0].get_text()
        map=folium.Map(location=[w,h],zoom_start=15)
        folium.Marker(location=[w,h],popup=address).add_to(map)
        map.save("./Image/Map.html")





def userURLBuilder(url, **user):
    str = url + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


TKWindow()