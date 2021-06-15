from decimal import *
from datetime import *
from tkinter import *
from tkinter import messagebox
from tkcalendar import *

import Parkometr
from Parkometr import *
import time
import datetime


class interface():

    def __init__(self):
        self._moneycount = dict.fromkeys(list(map(Decimal, ['0.01', '0.02', '0.05', \
                                                            '0.1', '0.2', '0.5', '1', '2', '5'])), 0)
        self._moneysum = 0
        self._data_rozpoczecia = datetime.datetime.now()
        self._czy_zmiana_czas = 1


    def przycisk0_01zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.01))


    def przycisk0_02zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.02))

    def przycisk0_05zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.05))

    def przycisk0_1zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.1))

    def przycisk0_2zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.2))

    def przycisk0_5zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.5))

    def przycisk1zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(1))

    def przycisk2zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(2))

    def przycisk5zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(5))

    def przycisk10zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(10))

    def przycisk20zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(20))

    def przycisk50zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(50))

    def czytnie_tablicy(self):
        print(tablica.get())
        self.check_plate(tablica.get())



    def zmiana_czasu(self):
        YEAR = datetime.date.today().year
        MONTH = datetime.date.today().month
        DATE = datetime.date.today().day
        HOUR = datetime.datetime.now().hour
        MINUTE = datetime.datetime.now().minute
        SECONDS = datetime.datetime.now().second

        data = datetime.datetime.now
        data = datetime.datetime.strptime(
            str(YEAR) + " " + str(MONTH) + " " + str(DATE) + " " + str(HOUR) + " " + str(MINUTE) + " " + str(
                SECONDS), '%Y %m %d %H %M %S')
        Parkometr.ParkingMeter.czy_zmienic_czas(self)
        data_od_urzytkownika = datetime.datetime.strptime(self.cal.get_date(), '%m/%d/%y')
        data_od_urzytkownika = data_od_urzytkownika.replace(hour=int(self._hour.get()), minute=int(self._min.get()))
        if data_od_urzytkownika < data:
            messagebox.showerror("Niepoprawna data", "Została podana \n Zla data")
        else:
            Parkometr.ParkingMeter.nowa_data(self, data_od_urzytkownika)

    def wypisanie_biletu(self):
        if Parkometr.ParkingMeter.get_bal(self) <= 0:
            messagebox.showerror(title="Błąd", message="Prosze wrzucić monety")
        elif Parkometr.ParkingMeter.check_plate(self, self._tablica.get()) == "":
            messagebox.showerror("Niepoprawny nr rejestracyjny", "Prosze wpisać prawidlowy numer rejestracyjny")
        else:
            wyjazd = Parkometr.ParkingMeter.bilet_do_kiedy(self)
            wyjazd = wyjazd.replace(microsecond=0)
            poczatek = self._data_rozpoczecia
            poczatek = poczatek.replace(microsecond=0)
            bilet = str(
                "Numer rejestracyjny:    " + Parkometr.ParkingMeter.check_plate(self, self._tablica.get()) + "\nGodzina rozpoczęcia:  " + str(
                    poczatek) + "\nGodzina wyjazdu:        " + str(wyjazd))
            messagebox.showinfo(title="BILET", message=bilet)

    def main(self):
        okno = Tk()
        okno.geometry('1000x500')

        przycisk1 = Button(okno, text="Wrzuć \n 0.01zł", height=5, width=12, command=self.przycisk0_01zl,
                           activebackground='green')
        przycisk1.place(x=0, y=100)

        przycisk2 = Button(okno, text="Wrzuć \n 0.02zł", height=5, width=12, command=self.przycisk0_02zl,
                           activebackground='green')
        przycisk2.place(x=100, y=100)

        przycisk3 = Button(okno, text="Wrzuć \n 0.05zł", height=5, width=12, command=self.przycisk0_05zl,
                           activebackground='green')
        przycisk3.place(x=200, y=100)

        przycisk4 = Button(okno, text="Wrzuć \n 0.1zł", height=5, width=12, command=self.przycisk0_1zl,
                           activebackground='green')
        przycisk4.place(x=0, y=190)

        przycisk5 = Button(okno, text="Wrzuć \n 0.2zł", height=5, width=12, command=self.przycisk0_2zl,
                           activebackground='green')
        przycisk5.place(x=100, y=190)

        przycisk6 = Button(okno, text="Wrzuć \n 0.5zł", height=5, width=12, command=self.przycisk0_5zl,
                           activebackground='green')
        przycisk6.place(x=200, y=190)

        przycisk7 = Button(okno, text="Wrzuć \n 1zł", height=5, width=12, command=self.przycisk1zl, activebackground='green')
        przycisk7.place(x=0, y=280)

        przycisk8 = Button(okno, text="Wrzuć \n 2zł", height=5, width=12, command=self.przycisk2zl, activebackground='green')
        przycisk8.place(x=100, y=280)

        przycisk9 = Button(okno, text="Wrzuć \n 5zł", height=5, width=12, command=self.przycisk5zl, activebackground='green')
        przycisk9.place(x=200, y=280)

        przycisk10 = Button(okno, text="Wrzuć \n 10zł", height=5, width=12, command=self.przycisk10zl,
                            activebackground='green')
        przycisk10.place(x=0, y=370)

        przycisk11 = Button(okno, text="Wrzuć \n 20zł", height=5, width=12, command=self.przycisk20zl,
                            activebackground='green')
        przycisk11.place(x=100, y=370)

        przycisk12 = Button(okno, text="Wrzuć \n 50zł", height=5, width=12, command=self.przycisk50zl,
                            activebackground='green')
        przycisk12.place(x=200, y=370)

        napis_tablica = Label(okno, text='Podaj Nr tablicy \nrejestracyjnej pojazdu', font='ariel 10', width=18,
                              height=3)
        napis_tablica.place(x=20, y=-5)

        napis_ile_monet = Label(okno, text='Podaj ilość \n monet', font='ariel 10', width=20, height=3)
        napis_ile_monet.place(x=160, y=-5)
        self._tablica = Entry(okno, width=21, font='ariel 12')
        self._tablica.place(x=2, y=44)



        przycisk13 = Button(okno, text="Zatwierdź Nr Tablicy", width=26, command=self.czytnie_tablicy,
                            activebackground='green')
        przycisk13.place(x=2, y=70)


        self._ilosc_monet_spinbox = Spinbox(from_=0, to=200, wrap=True, width=10)
        self._ilosc_monet_spinbox.place(x=199, y=44)

        przycisk_zmiana_czasu = Button(okno,text = 'Zatwierdź \n Zmiane czasu', width = 17,height = 2, command =self.zmiana_czasu)
        przycisk_zmiana_czasu.place(x=420, y=232)
        self._hour = Spinbox(from_=8, to=20, wrap=True, width=2, state="readonly")
        self._hour.place(x=300, y=232)
        self._godziny = Label(okno, text='Godziny', font='ariel 10', width=5, height=1)
        self._godziny.place(x = 340, y= 232)
        self._min = Spinbox(from_=0, to=59, wrap=True, width=2, state="readonly")
        self._min.place(x=300, y=254)
        minuty = Label(okno, text='Minuty', font='ariel 10', width=5, height=1)
        minuty.place(x=340, y=254)


        zatwierdz_bilet = Button(okno,  text='Zatwierdz Bilet',command = self.wypisanie_biletu, font='ariel 20', width=15, height=1)
        zatwierdz_bilet.place(x=300,y=280)
        self.cal = Calendar(okno)
        self.cal.place(x= 300, y=44)


        okno.mainloop()

bankomat = interface()
bankomat.main()
