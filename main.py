# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import webbrowser
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
        self.window=Tk()
        self.window.title("show")
        self.window.geometry("700x600")
        Label(self.window, text="시도").place(x=440,y=45)
        TempFont = font.Font(self.window, size=20, weight='bold', family='Consolas')
        self.Sido = "서울특별시"
        self.SIDOScroll=Scrollbar(self.window,width=20)
        self.SIDOScroll.place(x=650,y=30)
        self.SIDOLList=Listbox(self.window,font=TempFont,activestyle='none',width=10, height=1, borderwidth=10, relief='ridge',
                              yscrollcommand=self.SIDOScroll.set)
        self.InsertSIDO()
        self.SIDOLList.place(x=480,y=30)


        Label(self.window, text="시군구").place(x=430,y=110)
        #self.SIGUNScroll=Scrollbar(self.window,width=20)
        #self.SIGUNScroll.place(x=700,y=80)
        self.SIGUNList = Entry(self.window, width=25, borderwidth=3)
        self.SIGUNList.place(x=480, y=110)

        self.searchButton=Button(self.window,text="검색",command=self.Search)
        self.searchButton.place(x=635,y=140)
        self.graphImage = ImageTk.PhotoImage(Image.open("./Image/graph.png"))
        self.graphButton=Button(self.window,text="지역별 리스트",command=self.newWindow,image=self.graphImage)
        self.graphButton.place(x=570,y=140)

        self.MailAddress=Entry(self.window,width=25, borderwidth=3)
        self.MailAddress.place(x=385, y=550)
        self.MailImage=ImageTk.PhotoImage(Image.open("./Image/mail.png"))
        self.MailButton = Button(self.window, image=self.MailImage, command=self.SendMail)
        self.MailButton.place(x=585, y=545)
        self.TEXTLIST = Listbox(self.window,width=40,height=20)
        self.TEXTLIST.place(x=380,y=200)
        self.TEXTLIST.bind('<<ListboxSelect>>', self.SelectBuild)

        TempFont = font.Font(self.window, size=20, weight='bold', family='Consolas')
        self.NAME=Label(self.window,text="관광지명",width=20,font=TempFont)
        self.NAME.place(x=30,y=20)
        self.TAG=Label(self.window, text="분류",width=80)
        self.TAG.place(x=-95,y=70)
        self.EXPLAIN=Text(self.window,width=45,height=14)
        self.EXPLAIN.place(x=30,y=100)

        self.Phone=Label(self.window,text="Tel : 000-000-000",width=20,font=TempFont)
        self.Phone.place(x=30,y=300)
        self.earth = PhotoImage(file="./Image/sample.png")
        #Label(self.window, image=self.earth).place(x=30, y=340)
        self.EARTH = Button(self.window, overrelief="solid", width=310,height=230,image=self.earth,command=self.OpenMap)
        self.EARTH.place(x=30, y=340)
        self.window.mainloop()

    def ScrollSido(self):
        sido_s = self.SIDOScroll.get()[1]
        if sido_s == 0.0625:
            self.Sido = "서울특별시"
        elif sido_s == 0.125:
            self.Sido = "부산광역시"
        elif sido_s == 0.1875:
            self.Sido = "대구광역시"
        elif sido_s == 0.25:
            self.Sido = "인천광역시"
        elif sido_s == 0.3125:
            self.Sido = "광주광역시"
        elif sido_s == 0.375:
            self.Sido = "대전광역시"
        elif sido_s == 0.4375:
            self.Sido = "울산광역시"
        elif sido_s == 0.5:
            self.Sido = "제주특별자치도"
        elif sido_s == 0.5625:
            self.Sido = "경기도"
        elif sido_s == 0.625:
            self.Sido = "강원도"
        elif sido_s == 0.6875:
            self.Sido = "충청북도"
        elif sido_s == 0.75:
            self.Sido = "충청남도"
        elif sido_s == 0.8125:
            self.Sido = "전라북도"
        elif sido_s == 0.875:
            self.Sido = "전라남도"
        elif sido_s == 0.9375:
            self.Sido = "경상북도"
        elif sido_s == 1.0:
            self.Sido = "경상남도"

    def Search(self):
        self.ScrollSido()
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
        self.NM=self.DATALIST[i]['name']
        self.url_d = userURLBuilder(Detail_url, ServiceKey=Key, SIDO=self.Sido, GUNGU=self.Sigun, RES_NM=self.NM)
        self.GoogleImageSearch(self.NM)

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

        self.earth2 = ImageTk.PhotoImage(Image.open("./Image/Build.png"))
        self.EARTH.config(image=self.earth2)

        self.GoogleMap(self.NM)

    def GoogleMap(self,NM):
        import requests
        from bs4 import BeautifulSoup
        import folium
        address=self.NM
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

    def SendMail(self):
        import mimetypes
        import smtplib
        import spam
        from email.mime.base import MIMEBase
        from email.mime.image import MIMEImage
        from email.mime.text import MIMEText

        # global value
        host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = ".\Image\Map.html"
        htmlFileName2 = ".\Image\Build.png"

        senderAddr = spam.ID()  # 보내는 사람 email 주소.
        recipientAddr = self.MailAddress.get()  # 받는 사람 email 주소.

        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = "Script Tour Mail "
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        # MIME 문서를 생성합니다.
        text = MIMEText("스크립트 관광지 사진 \n"
                        +"관광지 :"+self.NM+"\n"
                        +"설명 :"+self.DATALIST_d[0]['explain']+"\n"
                        +"전화번호 :"+self.DATALIST_d[0]['phone']+"\n")
        htmlFD = open(htmlFileName, 'rb')
        htmlFD2 = open(htmlFileName2, 'rb')
        HtmlPart = MIMEBase(htmlFD.read(), 'html', _charset='UTF-8')
        HtmlPart2 = MIMEImage(htmlFD2.read(), 'png', _charset='UTF-8')
        htmlFD.close()
        htmlFD2.close()

        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(text)
        msg.attach(HtmlPart)
        msg.attach(HtmlPart2)

        # 메일을 발송한다.
        s = smtplib.SMTP(host, port)
        # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(spam.ID(), spam.password())
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

    def newWindow(self):
        self.ScrollSido()
        List={}
        if self.Sido=="서울특별시":
            List = {"강남구":10,"강동구":4,"강북구":2,"강서구":9,"관악구":0,"광진구":4,"구로구":0,"금천구":3,
                    "노원구":2,"도봉구":1,"동대문구":5,"동작구":0,"마포구":6,"서대문구":3,"서초구":9,"성동구":2,
                    "성북구":2,"송파구":8,"양천구":0,"영등포구":6,"용산구":7,"은평구":2,"종로구":10,"중구":10,
                    "중랑구":1,}
        elif self.Sido=="부산광역시":
            List={"강서구":1,"금정구":0,"남구":2,"동구":7,"동래구":5,"부산진구":2,"북구":4,"사상구":2,"사하구":3,
                  "서구":3,"수영구":6,"연제구":2,"영도구":2,"중구":9,"해운대구":3,"기장군":3}
        elif self.Sido == "대구광역시":
            List={"남구":5,"달서구":7,"동구":10,"북구":2,"서구":1,"수성구":9,"중구":10,"달성군":9}
        elif self.Sido == "인천광역시":
            List={"계양구":4,"남동구":4,"동구":3,"미추홀구":2,"부평구":6,"서구":5,"연수구":6,"중구":10,
            "강화군":10,"옹진군":8}
        elif self.Sido == "광주광역시":
            List={"광산구":3,"남구":9,"동구":10,"북구":10,"서구":6}
        elif self.Sido == "대전광역시":
            List = {"대덕구": 1, "동구": 4, "서구": 4, "유성구": 10, "중구": 3}
        elif self.Sido == "울산광역시":
            List = {"남구":6,"동구":7,"북구":2,"중구":6,"울주군":10}
        elif self.Sido == "제주특별자치도":
            List={"제주시":10,"서귀포시":10}
        elif self.Sido =="경기도":
            List={"고양시":10,"과천시":6,"광명시":8,"광주시":6,"구리시":2,"군포시":0,"김포시":10,"남양주시":10,
                  "동두천시":6,"부천시":10,"성남시":8,"수원시":10,"시흥시":10,"안산시":10,"안성시":10,"안양시":8,
                  "양주시":8,"여주시":10,"오산시":2,"용인시":10,"의왕시":0,"의정부시":5,"이천시":6,"파주시":10,
                  "평택시":0,"포천시":10,"하남시":1,"화성시":5,"가평군":10,"양평군":10,"연천군":10}
        elif self.Sido == "강원도":
            List={"강릉시":10,"동해시":9,"삼척시":7,"속초시":10,"원주시":10,"춘천시":10,"태백시":10,"고성군":9,
                  "양구군":10,"양양군":10,"영월군":10,"인제군":10,"정선군":10,"철원군":10,"평창군":10,"홍천군":5,
            "화천군":0,"횡성군":8}
        elif self.Sido == "충청북도":
            List={"제천시":10,"청주시":10,"충주시":10,"괴산군":10,"단양군":10,"보은군":10,"영동군":10,
            "옥천군":4,"음성군":4,"증평군":5,"진천군":10}
        elif self.Sido == "충청남도":
            List={"계룡시":1,"공주시":10,"논산시":6,"당진시":6,"보령시":9,"서산시":5,"아산시":10,"천안시":10,
            "금산군":7,"부여군":10,"서천군":8,"예산군":10,"청양군":10,"태안군":10,"홍성군":10}
        elif self.Sido == "전라북도":
            List={"전주시":10,"군산시":10,"김제시":4,"남원시":10,"익산시":8,"정읍시":10,"고창군":10,"무주군":10,
            "부안군":10,"순창군":10,"완주군":10,"임실군":10,"장수군":10,"진안군":7}
        elif self.Sido == "전라남도":
            List={"광양시":10,"나주시":10,"목포시":10,"순천시":10,"여수시":10,"강진군":10,"고흥군":10,"곡성군":10,
            "구례군":10,"담양군":8,"무안군":10,"보성군":10,"신안군":10,"영광군":10,"영암군":8,"완도군":8,
            "장성군":7,"장흥군":8,"진도군":10,"해남군":10,"함평군":5,"화순군":10}
        elif self.Sido == "경상북도":
            List={"경산시":9,"경주시":10,"구미시":10,"김천시":10,"문경시":10,"상주시":9,"안동시":10,"영주시":10,
            "영천시":10,"포항시":10,"고령군":10,"군위군":6,"봉화군":5,"성주군":10,"예천군":4,"영덕군":10,"영양군":7,
            "울릉군":7,"울진군":10,"의성군":7,"청도군":10,"청송군":10,"칠곡군":6}
        elif self.Sido == "경상남도":
            List={"거제시":10,"김해시":10,"밀양시":10,"사천시":9,"양산시":10,"진주시":5,"창원시":0,"통영시":10,
            "거창군":10,"고성군":4,"남해군":6,"산청군":7,"의령군":1,"창녕군":9,"하동군":10,"함안군":2,"함양군":3,
                  "합천군":6}
        self.graphwindow = Toplevel(self.window)
        self.canvas = Canvas(self.graphwindow, bg="white", width=400, height=200)
        self.canvas.config(scrollregion=(0, 0, 150, len(List)*40))
        sbar = Scrollbar(self.graphwindow)
        sbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack()
        position=0
        for i in List.keys():
            self.canvas.create_text(20 , 20 + position * 40, text=i, tags="bar")
            self.canvas.create_rectangle(60,15 + position * 40 ,60+(List[i]/10)*200,30 + position * 40, tags="bar")
            self.canvas.create_text(70+(List[i]/10)*200, 22 + position * 40, text=List[i], tags="bar")
            position+=1


    def OpenMap(self):
        import webbrowser
        url = '.\Image\Map.html'
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        print(url)
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)


def userURLBuilder(url, **user):
    str = url + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


TKWindow()