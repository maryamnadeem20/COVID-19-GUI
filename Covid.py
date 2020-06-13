from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.scrolledtext import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import random
import requests
from threading import *
from time import *
import pyttsx3
width=650
height=630

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

root=Tk()
root.title("Digital Hospital")
volume=PhotoImage(file="volume.png")

class layout:
	def __init__(self,master):
		self.canvas=Canvas(master, width=width, height=height)
		self.canvas.pack(fill=X)
		self.bgImage=PhotoImage(file="doctor.png")
		self.imgLabel=Label(self.canvas, image=self.bgImage)
		self.imgLabel.pack(fill=X)
		self.welcome=Label(self.imgLabel, text="WELCOME TO DIGITAL HEALTH  CENTER", bg="#86C9DA", fg="red", font="Helvetica 20 bold")
		self.welcome.place(relwidth=1, relheight=0.1)
		self.welcomeEnd=Label(self.imgLabel, text="HERE YOU CAN KEEP TRACK ON EVERYTHING RELATED TO\nCOVID-19", bg="#EBEDEF", fg="red", font="Helvetica 14")
		self.welcomeEnd.place(relwidth=1, relheight=0.1, rely=0.9)
		self.newsroom=Button(self.imgLabel, text="NEWSROOM", bg="#197D97", fg="white", font="Helvetica 15 bold", command=self.news)
		self.newsroom.place(height=45, width=190, rely=0.6, relx=0.05)
		self.cases=Button(self.imgLabel, text="STATISTICS", bg="#197D97", fg="white", font="Helvetica 15 bold", command=self.cases)
		self.cases.place(height=45, width=190, rely=0.6, relx=0.35)
		self.precautions=Button(self.imgLabel, text="PRECAUTIONS", bg="#197D97", fg="white", font="Helvetica 15 bold", command=self.precautions)
		self.precautions.place(height=45, width=190, rely=0.6, relx=0.65)
		self.consult=Button(self.imgLabel, text="CONSULT DR. FLOYD", bg="#197D97", fg="white", font="Helvetica 13 bold", command=self.consult)
		self.consult.place(height=45, width=190, rely=0.75, relx=0.15)
		self.exit=Button(self.imgLabel, text="EXIT", bg="#197D97", fg="white", font="Helvetica 15 bold", command=master.quit)
		self.exit.place(height=45, width=190, rely=0.75, relx=0.55)
	
	def news(self):
		self.newsWindow=Toplevel()
		self.newsWindow.resizable(width=False, height=False)
		self.newsWindow.title("Top Coronavirus News")
		self.canvasN=Canvas(self.newsWindow, width=width, height=height, bg="#D1F2EB")
		self.canvasN.pack(fill=X)
		self.labelN=Label(self.canvasN,text="NEWSROOM", bg="#138D75", fg="white", font="Helvetica 20 bold")
		self.labelN.place(relwidth=1)
		self.coronaNews()
		
	def cases(self):
		self.statistics=Toplevel()
		self.statistics.title("Coronavirus Statistics")
		self.statistics.resizable(width=False, height=False)
		self.canvasS=Canvas(self.statistics, width=width, height=height, bg="#D98880")
		self.canvasS.pack(fill=BOTH)
		self.labelS=Label(self.canvasS,text="STATISTICS", bg="#922B21", fg="white", font="Helvetica 20 bold")
		self.labelS.place(relwidth=1)
		self.worlLabel=Label(self.canvasS, text="GLOBAL STATISTICS", font="Helvetica 18 bold", bg="#D98880")
		self.worlLabel.place(relwidth=1, rely=0.1)
		self.world=Label(self.canvasS, bg="#D98880", font="Helvetica 15")
		self.world['text']=self.worldStats()
		self.world.place(relwidth=1, rely=0.15)
		self.entryLabel=Label(self.canvasS)
		self.entryS=Entry(self.canvasS, font=('Roman', 20) )
		self.entryS.place(relx=0.18, rely=0.35, height=40)
		self.buttonS=Button(self.canvasS, text="Get Stats", bg="#F2D7D5", font=("Helvetica 14"), command=lambda: self.countryStats(self.entryS.get()))
		self.buttonS.place(relx=0.6, rely=0.35, width=140, height=40)
		self.showStats=Label(self.canvasS, width=22, height=10, bg="#F2D7D5", fg="#641E16", font="Constantia 20", borderwidth=5, relief="raised", anchor=NW, padx=20, pady=10)
		self.showStats.place(rely=0.45, relx=0.2)

	def precautions(self):
		self.precautions=Toplevel()
		self.precautions.title("PRECAUTIONS")
		self.precautions.resizable(width=False, height=False)
		self.canvasP=Canvas(self.precautions, width=width, height=height, bg="#BDC3C7")
		self.canvasP.pack(fill=BOTH)
		self.labelP=Label(self.canvasP,text="PRECAUTIONS TO AVOID THE SPREAD OF COVID-19", bg="#212F3D", fg="white", font="Helvetica 15 bold")
		self.labelP.place(relwidth=1)
		sourceP=requests.get("https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public").text
		soupP=BeautifulSoup(sourceP, 'lxml')
		contentPrecaution=soupP.find_all('div', class_="content-block")[13]
		contentStart=contentPrecaution.p.text
		contentPoints=contentPrecaution.find_all('li')
		self.textPrec=Text(self.canvasP, width=55, height=100, bg="#85929E", fg="#273746", font="Times 15 bold", bd=0, wrap=WORD, padx=8, pady=10)
		self.textPrec.insert(INSERT, "\n"+contentStart+"\n\n\n")
		scrollbarP = Scrollbar(self.canvasP)
		scrollbarP.place(relheight=1, relx=0.974)
		buttonvol=Button(self.canvasP, bg="#EAECEE", command=lambda : speak(contentPoints))
		buttonvol.place(rely=0.93, relx=0.93)
		buttonvol.config(image=volume)
		for li in contentPoints:
			text=li.text
			self.textPrec.insert(INSERT, "◙  "+text+"\n\n\n")
			scrollbarP.config(command = self.textPrec.yview)
		self.textPrec.place(rely=0.09, relx=0.06, relheight=1)
		self.textPrec.config(state="disabled", cursor="arrow")
	
	def consult(self):
		self.login=Toplevel()
		self.login.title("Login")
		self.login.resizable(width=False, height=False)
		self.login.configure(width=400, height=300)
		self.pls=Label(self.login, text="Please login to continue", justify=CENTER, font="Helvetica 14 bold")
		self.pls.place(relheight=0.15,relx=0.2, rely=0.07)
		self.labelName=Label(self.login, text="Name: ", font="Helvetica 12")
		self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)
		self.entryName=Entry(self.login, font="Helvetica 14")
		self.entryName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
		self.entryName.focus()
		self.labelAge=Label(self.login, text="Age: ", font="Helvetica 12")
		self.labelAge.place(relheight=0.2, relx=0.1, rely=0.35)
		self.entryAge=Entry(self.login, font="Helvetica 14")
		self.entryAge.bind("<Return>", lambda a:self.goAhead(self.entryName.get(), self.entryAge.get()))
		self.entryName.focus()
		self.entryAge.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.35)
		self.go=Button(self.login, text="CONTINUE", font="Helvetica 14 bold", command=lambda: self.goAhead(self.entryName.get(), self.entryAge.get()))
		self.go.place(relx=0.4, rely=0.55)
	def goAhead(self, name, age):
		if age.isdecimal()==False:
			messagebox.showerror("Error", "Enter valid age")
		else:
			self.cons=Consult(name, age)
			self.login.destroy()

	def coronaNews(self):
		self.newsText=Text(self.canvasN, width=60, bg="#A2D9CE", fg="#0E6655", font="Helvetica 12 bold", bd=0, wrap=WORD, padx=10, pady=10)
		sourceNews=requests.get("https://www.who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/news").text
		soupNews=BeautifulSoup(sourceNews, 'lxml')
		newsTitles=soupNews.find_all('div', class_="list-view--item")
		string=["~" for i in range(45)]
		for newsTitle in newsTitles:
			try:
				self.newsHeadline=newsTitle.a.p.text
				self.newsText.insert(INSERT, "◙  "+self.newsHeadline+"\n")
				subtitle=newsTitle.find('p', class_='sub-title').text
				self.newsText.insert(INSERT, "- "+subtitle+"\n")
				scrollbar = Scrollbar(self.canvasN)
				scrollbar.place(relheight=1, relx=0.974)
				scrollbar.config(command = self.newsText.yview)
				
			except:
				self.newsText.insert(INSERT, "")
			self.newsText.insert(INSERT, string[:])
			self.newsText.insert(INSERT, "\n\n")
			self.newsText.place(rely=0.08, relheight=1, relx=0.06)
		self.newsText.config(state="disabled")

	def worldStats(self):
		url = "https://coronavirus-map.p.rapidapi.com/v1/summary/latest"
		header = {
		    'x-rapidapi-host': "coronavirus-map.p.rapidapi.com",
		    'x-rapidapi-key': "dfed7953b1msh420570961dac2d1p10c82bjsn8d6593e183be"
		    }
		response = requests.request("GET", url, headers=header)
		response=response.json()
		TotalConfirmed=response["data"]["summary"]["total_cases"]
		TotalDeaths=response["data"]["summary"]["deaths"]
		TotalRecovered=response["data"]["summary"]["recovered"]
		Totalactivecases=response["data"]["summary"]["active_cases"]
		Totalcritical=response["data"]["summary"]["critical"]
		return "Total Cases: {}\nTotal Deaths: {}\nTotal Recovered: {}\nActive Cases: {}\nCritical Cases: {}".format(TotalConfirmed, TotalDeaths, TotalRecovered, Totalactivecases, Totalcritical)
	def countryStats(self, country):
		url = "https://coronavirus-map.p.rapidapi.com/v1/summary/region"
		querystring = {"region":country}
		headers = {
		    'x-rapidapi-host': "coronavirus-map.p.rapidapi.com",
		    'x-rapidapi-key': "dfed7953b1msh420570961dac2d1p10c82bjsn8d6593e183be"
		    }
		self.response = requests.request("GET", url, headers=headers, params=querystring)
		self.response=self.response.json()
		try:
			totCases=self.response["data"]["summary"]["total_cases"]
			deaths=self.response["data"]["summary"]["deaths"]
			activecases=self.response["data"]["summary"]["active_cases"]
			recovered=self.response["data"]["summary"]["recovered"]
			critical=self.response["data"]["summary"]["critical"]
			res= "Total Cases: {}\nTotal Deaths: {}\nTotal Recovered: {}\nActive Cases: {}\nCritical Cases: {}".format(totCases, deaths, recovered, activecases, critical)
		except:
			res="Couldn't fetch, sorry! :(\nPlease check country name!"
		self.showStats['text']=res
		buttonvol=Button(self.showStats, text="speak", command=lambda: speak(res), bg="#CD5C5C")
		buttonvol.place(rely=0.8, relx=0.5)
		buttonvol.config(image=volume)


class Consult:
	def __init__(self, name, age):
		self.name=name
		self.age=int(age)
		self.consultWindow=Toplevel()
		self.consultWindow.title("Your Digital Helper")
		self.consultWindow.resizable(width=False, height=False)
		self.consultWindow.configure(width=470, height=550, bg="#17202A")
		self.labelHead=Label(self.consultWindow, bg="#17202A", fg="#EAECEE", text="DR FLOYD", font="Helvetica 13 bold", pady=5)
		self.labelHead.place(relwidth=1)
		self.line=Label(self.consultWindow,width=450, bg="#ABB2B9")
		self.line.place(relwidth=1, rely=0.07, relheight=0.012)
		self.textCons=Text(self.consultWindow, width=20, height=2,bg="#17202A", fg="#EAECEE", font="Helvetica 14", padx=5, pady=5)
		self.textCons.place(relheight=0.745, relwidth=1, rely=0.08)
		self.labelBottom=Label(self.consultWindow, bg="#ABB2B9", height=80)
		self.labelBottom.place(relwidth=1, rely=0.825)
		self.entryMsg=Entry(self.labelBottom,bg="#2C3E50", fg="#EAECEE", font="Helvetica 13")
		self.entryMsg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
		self.entryMsg.bind("<Return>", lambda a:self.send(self.entryMsg.get()))
		self.entryMsg.focus()
		self.buttonMsg=Button(self.labelBottom, text="Send", font="Helvetica 12 bold", width=20, bg="#ABB2B9", command= lambda: self.send(self.entryMsg.get()))
		self.buttonMsg.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
		self.greet=["Hi, "+self.name+" I am your digital helper, Floyd.", "Hello! I'm here to help you, "+self.name+"! I'm Floyd.", "Hey, "+self.name+"! This is Floyd, your digital helper!" ]
		self.greet2=random.choice(self.greet)
		self.textCons.insert(END, random.choice(self.greet)+"\n", 'bot')
		self.textCons.tag_configure('bot', relief='raised', wrap=WORD, lmargin1=10, rmargin=100, foreground='#C7DCF0')
		self.textCons.config(cursor="arrow")
		scrollbar = Scrollbar(self.textCons)
		scrollbar.place(relheight=1, relx=0.974)
		scrollbar.config(command = self.textCons.yview)
		speak(self.greet2)

	def send(self,message):
		self.textCons.config(state=NORMAL)
		self.textCons.tag_configure('user', relief='raised', wrap=WORD, lmargin1=70, rmargin=15, justify=RIGHT, foreground="#ECDCC7")
		message=message.lower()
		self.entryMsg.delete(0, END)
		if message=="hello" or message=="hi" or message =="hey":
			self.textCons.insert(END, message+"\n", 'user')
			self.textCons.insert(END, "How are you?\n", 'bot')
			speak("How are you?")
		elif message =="not well" or message == "ill" or message == "not fine" or message == "bad" or message == "sick" or message =="tired":
			self.textCons.insert(END, message+"\n", 'user')
			self.textCons.insert(END, "Uh oh! Let's see!\n", 'bot')
			self.textCons.insert(END, "Where would you like to begin?\n", 'bot')
			speak("Uh oh! Let's see! Where would you like to begin?")
			self.options()
		elif message =="well" or message == "fine" or message == "i'm fine" or message == "good" or message == "awesome" or message =="great":
			self.textCons.insert(END, message+"\n", 'user')
			self.textCons.insert(END, "Wonderful!\n", 'bot')
			self.textCons.insert(END, "Where would you like to begin?\n", 'bot')
			speak("Wonderful! Where would you like to begin?")
			self.options()
		else:
			self.textCons.insert(END, "\n"+message+"\n", 'user')
			sorry=["Sorry, what?", "Please try again!", "I'm sorry, I couldn't catch"]
			sorry2=random.choice(sorry)
			self.textCons.insert(END, "\n"+sorry2+"\n", 'bot')
			speak(random.choice(sorry))
		self.textCons.config(state=DISABLED)
		self.textCons.yview(END)

	def options(self):
		self.textCons.config(state=NORMAL)
		self.buttonKnow=Button(self.textCons, text="Learn about Coronavirus", font="Helvetica 8 bold", command= self.whatscorona)
		self.buttonKnow.bind("<Button-1>", lambda a: self.textCons.insert(INSERT, "\nLearn about Coronavirus\n", 'user'))
		self.buttonKnow.place(relx=0.3, rely=0.55, width=180, height=40)
		self.buttonTest=Button(self.textCons, text="Test for symptoms", font="Helvetica 8 bold", command=self.confirm)
		self.buttonTest.bind("<Button-1>", lambda a: self.textCons.insert(INSERT, "\nTest me for symptoms\n", 'user'))
		self.buttonTest.place(relx=0.3, rely=0.7, width=180, height=40)
		self.textCons.config(state=DISABLED)
		self.textCons.yview(END)
	def whatscorona(self):
		self.textCons.config(state=NORMAL)
		self.buttonTest.place_forget()
		self.buttonKnow.place_forget()
		coronaDef="\nCoronaviruses are a large family of viruses which may cause illness in animals or humans.  In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19.\n"
		self.textCons.insert(END, "\n"+coronaDef+"\n", 'bot')
		sleep(0)
		t1=Thread(target=speak, args=(coronaDef, ))
		t1.start()
		sleep(1)
		self.buttonTest2 = Button(self.textCons, text="Test for symptoms", font="Helvetica 8 bold", width=20, height=2, command=self.confirm)
		self.buttonTest2.bind("<Button-1>", lambda a: self.textCons.insert(INSERT, "\nTest me for symptoms\n", 'user'))
		self.textCons.window_create(INSERT, window=self.buttonTest2, padx=170)
		self.textCons.see(END)
		self.textCons.config(state=DISABLED)
	def confirm(self):
		self.buttonTest.place_forget()
		self.buttonKnow.place_forget()
		self.textCons.config(state=NORMAL)
		self.textCons.insert(INSERT, "\n\nI will ask you certain questions to evaluate your medical needs\n\n", 'bot')
		self.textCons.insert(INSERT, "\nShall we begin?\n\n")
		speak("I will ask you certain questions to evaluate your medical needs. Shall we begin?")
		self.buttonYes = Button(self.textCons, text="YES", font="Helvetica 8 bold", width=20, height=2, command=self.questions)
		self.buttonYes.bind("<Button-1>", lambda a: self.textCons.insert(INSERT, "\nYes\n", 'user'))
		self.textCons.window_create(INSERT, window=self.buttonYes, padx=170)
		self.buttonNo = Button(self.textCons, text="EXIT", font="Helvetica 8 bold", width=20, height=2, command=self.textCons.quit)
		self.buttonNo.bind("<Button-1>", lambda a: self.textCons.insert(INSERT, "\nNo\n", 'user'))
		self.textCons.window_create(INSERT, window=self.buttonNo, padx=170)
		self.textCons.see(END)
		try:
			self.textCons.delete(self.buttonTest2)
		except:
			pass
		self.textCons.config(state=DISABLED)
	def questions(self):
		c=0
		self.textCons.delete(self.buttonYes)
		self.textCons.delete(self.buttonNo)
		cough=messagebox.askquestion("", "Do you have cough?")
		if cough=="yes":
			c+=1
		sleep(0.7)
		cold=messagebox.askquestion("", "Do you have cold?")
		if cold=="yes":
			c+=1
		sleep(0.7)
		diarrhea=messagebox.askquestion("", "Are you having Diarrhea?")
		if diarrhea=="yes":
			c+=1
		sleep(0.7)
		sorethroat=messagebox.askquestion("", "Are you having a sore throat?")
		if sorethroat=="yes":
			c+=1
		sleep(0.7)
		myalgia=messagebox.askquestion("", "Are you experiencing MYALGIA or body ache?")
		if myalgia=="yes":
			c+=1
		sleep(0.7)
		headache=messagebox.askquestion("", "Do you have a headache?")
		if headache=="yes":
			c+=1
		sleep(0.7)
		fever=messagebox.askquestion("", "Do you have fever? (Temperature 37.8 C and above)")
		if fever=="yes":
			c+=1
		sleep(0.7)
		diffBreathe=messagebox.askquestion("", "Are you having difficulty in breathing?")
		if diffBreathe=="yes":
			c+=2
		sleep(0.7)
		fatigue=messagebox.askquestion("", "Are you experiencing fatigue?")
		if fatigue=="yes":
			c+=2
		sleep(0.7)
		travelled=messagebox.askquestion("", "Have you travelled in the last 14 days?")
		if travelled=="yes":
			c+=3
		sleep(0.7)
		infectedArea=messagebox.askquestion("", "Do you have travel history to a COVID-19 infected area?")
		if infectedArea=="yes":
			c+=3
		sleep(0.7)
		contact=messagebox.askquestion("", "Are you taking care of a COVID-19 patient or are in direct contact with them?")
		if contact=="yes":
			c+=3
		self.textCons.config(state=NORMAL)
		if 0<=c<=2:
			if 0<=self.age<=7 or self.age>41:
				evaluation11="\nWell "+self.name+", nothing too serious as of now, but considering your age group, you need to take extra care and precautions\n"
				self.textCons.insert(INSERT, evaluation11, 'bot')
				t11=Thread(target=speak, args=(evalualtion11, ))
				t11.start()
			elif 8<=self.age<=41:
				evaluation12="\n"+self.name+", nothing too serious as of now also considering the age group you fall in. However, you should still observe and take precautions\n"
				self.textCons.insert(INSERT, evaluation12, 'bot')
				t12=Thread(target=speak, args=(evalualtion12, ))
				t12.start()

		elif 3<=c<=5:
			if 0<=self.age<=7 or self.age>41:
				evalualtion21="\n"+self.name+", you need to keep yourself hydrated and maintain personal hygiene. Take extra precautions because the immune system of the age group you fall in is a bit weaker. Observe yourself and re-evaluate in 2 days.\n"
				self.textCons.insert(INSERT, evalualtion21, 'bot')
				t21=Thread(target=speak, args=(evalualtion21, ))
				t21.start()
			elif 8<=self.age<=41:
				evalualtion22="\nOkay "+self.name+", you need to keep yourself hydrated and maintain personal hygiene. Observe yourself and re-evaluate in 2 days.\n"
				self.textCons.insert(INSERT, evalualtion22, 'bot')
				t22=Thread(target=speak, args=(evalualtion22, ))
				t22.start()
		
		elif 6<=c<=12:
			if 0<=self.age<=7 or self.age>41:
				evalualtion31="\nHmm! "+self.name+", considering your age group and hence the immunity, this is not ignorable, you need to consult a doctor as soon as possible\n"
				self.textCons.insert(INSERT,evalualtion31 , 'bot')
				t31=Thread(target=speak, args=(evalualtion31, ))
				t31.start()
			elif 8<=self.age<=41:
				evalualtion32="\nHmm! "+self.name+", this is not ignorable! You should seek a consultation with a doctor.\n"
				self.textCons.insert(INSERT, evalualtion32, 'bot')
				t32=Thread(target=speak, args=(evalualtion32, ))
				t32.start()
		
		elif 12<=c<=24:
			evalualtion4="\nIt's serious. Seek medical help immediately, "+self.name+"!\n"
			self.textCons.insert(INSERT, evalualtion4 , 'bot')
			t32=Thread(target=speak, args=(evalualtion4, ))
			t32.start()
		self.textCons.see(END)
		self.textCons.config(state=DISABLED)


def speak(reply):
	engine.say(reply)
	engine.runAndWait()


# root.wm_attributes('-transparentcolor','grey')
lay=layout(root)
root.resizable(width=False, height=False)
root.mainloop()