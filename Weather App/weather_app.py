import pyowm
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from api_key import key


class weather():
    def __init__(self):
        owm = pyowm.OWM(key)
        self.mgr = owm.weather_manager()
        self.getweather = self.mgr

        self.window = tk.Tk()
        self.window.geometry('800x500')
        self.window.title('Weather App')

        icon = PhotoImage(file = 'Media/download (1).png')
        self.window.iconphoto(False,icon)

        C = Canvas(self.window, bg="blue", height=500, width=800)
        filename = PhotoImage(file = "bg.png")
        background_label = Label(self.window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()

        b = Button(self.window,command = self.start,bg = '#9933FF',width = 12,fg = 'white',text = 'Weather').place(x = 350,y = 400)
        
        
        self.window.mainloop()
    def start(self):
        self.window.destroy()

        self.window = tk.Tk()
        self.window.geometry('800x500')
        self.window.title('Weather App')

        icon = PhotoImage(file = 'Media/download (1).png')
        self.window.iconphoto(False,icon)

        C = Canvas(self.window, bg="blue", height=500, width=800)
        filename = PhotoImage(file = "Media/bgo.png")
        background_label = Label(self.window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()

        self.e1 = StringVar()

        l = Label(self.window,text = 'Enter City',fg = 'white',bg = '#C0C0C0').place(x = 380,y = 240)
        e1 = Entry(self.window,textvariable = self.e1).place(x = 350,y = 270)
        B1 = Button(self.window,bg = '#C0C0C0',command = self.check,fg = 'white',text = 'Go!').place(x = 395,y = 305)


        self.window.mainloop()
    

    def check(self):

        if self.e1.get()=='':
            messagebox.showwarning('Warning!','City name cannot be blank!')
        
        else:
            self.city = self.e1.get()
            f = self.e1.get()
            self.data = self.check_weather(f,'celsius')

            if self.data==False:
                messagebox.showerror('Error!','Error finding the city in the database')
            else:
                self.window.destroy()
                self.weather_show()
    
    def weather_show(self):
        self.window = tk.Tk()
        self.window.geometry('800x500')
        self.window.title('Weather App')

        icon = PhotoImage(file = 'Media/download (1).png')
        self.window.iconphoto(False,icon)

        C = Canvas(self.window, bg="blue", height=500, width=800)
        filename = PhotoImage(file = "bg.png")
        background_label = Label(self.window, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()

        Label(self.window,text = self.city,font =  ('Times',20),fg='Black',bg = '#E5CCFF',width = 15,height = 3).place(x = 20,y = 50)

        stat = Label(self.window,text = 'Status           ',fg = 'white',bg = '#CC99FF').place(x = 20,y = 240)
        Label(self.window,text = self.data[0],fg='Black',bg = '#E5CCFF').place(x = 120,y = 240)
        destat = Label(self.window,text = 'Detailed Status',fg = 'white',bg = '#CC99FF').place(x = 20,y = 270)
        Label(self.window,text = self.data[1],fg='black',bg = '#E5CCFF').place(x = 120,y = 270)

        Label(self.window,text = 'Temperature',fg = 'white',bg = '#CC99FF').place(x = 20,y = 300)
        Label(self.window,text = str(self.data[2]['temp'])+' C',fg='black',bg = '#E5CCFF').place(x = 120,y = 300)

        
        Label(self.window,text = 'High',fg = 'white',bg = '#CC99FF').place(x = 20,y = 330)
        Label(self.window,text = str(self.data[2]['temp_max'])+' C',fg='black',bg = '#E5CCFF').place(x = 120,y = 330)

        
        Label(self.window,text = 'Low',fg = 'white',bg = '#CC99FF').place(x = 20,y = 360)
        Label(self.window,text = str(self.data[2]['temp_min'])+' C',fg='black',bg = '#E5CCFF').place(x = 120,y = 360)

        
        Label(self.window,text = 'Feels Like',fg = 'white',bg = '#CC99FF').place(x = 20,y = 390)
        Label(self.window,text = str(self.data[2]['feels_like'])+' C',fg='black',bg = '#E5CCFF').place(x = 120,y = 390)

        self.window.mainloop()




    def check_weather(self,city,measure):
        try:
            obs = self.getweather.weather_at_place(city)
            obs = obs.weather
            status = obs.status
            detailed_status = obs.detailed_status
            temperature = obs.temperature('celsius')
            
            return [status,detailed_status,temperature]
        except:
            return False












o = weather()