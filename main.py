from decimal import *
from datetime import *
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import time
import datetime

weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


class BadNominalException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Money():

    def __init__(self, val):
        val = Decimal(float(val)).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        allowed = list(map(Decimal, ['0.01', '0.02', '0.05', \
                                     '0.1', '0.2', '0.5', '1', '2', '5', '10', '20', '50']))
        if val in allowed:
            self._val = val
        else:
            raise BadNominalException(val)

    def get_val(self):
        return self._val


class ParkingMeter():

    def __init__(self):
        self._moneycount = dict.fromkeys(list(map(Decimal, ['0.01', '0.02', '0.05', \
                                                            '0.1', '0.2', '0.5', '1', '2', '5'])), 0)
        self._moneysum = 0
        self._nowa_data = datetime.datetime.now
        self._czy_zmiana_czas = 1

    def add(self, coin):
        if not isinstance(coin, Money):
            print("zly nominal")
            return
        if coin.get_val() not in (10, 20, 50):
            if self._moneycount[coin.get_val()] == 4:
                print("Magazyn monet tego nominalu jest pelny")
                return
            else:
                self._moneycount[coin.get_val()] += 1
        self._moneysum += coin.get_val()
        print("Dodano", coin.get_val(), "kredytu")

    def get_bal(self):
        return self._moneysum

    def bilet_dlugosc(self):
        # ilosc_minut = 0
        a = self.get_bal()
        if a <= 2.0:
            self._ilosc_sekund = a / 2 * 60 * 60
            return int(self._ilosc_sekund)
        elif a <= 6.0:
            a = a - 2
            self._ilosc_sekund = (60 + (a / 4 * 60)) * 60
            return int(self._ilosc_sekund)

        else:
            a = a - 6
            self._ilosc_sekund = (120 + (a / 5 * 60)) * 60
            return int(self._ilosc_sekund)

    def dzien_tyg(self):
        today = date.today()
        self._dzien = today.weekday()
        return self._dzien

    def ile_do_20(self, data: datetime.datetime):
        dwudziesta = data.replace(hour=20, minute=0, second=0, microsecond=0)
        return (dwudziesta - data).total_seconds()



    def bilet_do_kiedy(self):
        # pobierz ile sekund wart jest bilet
        zaplacone_sekundy = self.bilet_dlugosc()

        # pobierz obecną date
        # do_kiedy = obecna_data
        do_kiedy = datetime.datetime.now()

        if self._czy_zmiana_czas > 1:
            do_kiedy = self._nowa_data


        # w petli aktualizuj do_kiedy
        while zaplacone_sekundy != 0:


            ## jeśli do_kiedy jest poza okresem płatnego parkowania, przesuń na początek najbliższego okresu płatnego parkowania
            if do_kiedy.weekday() == 6:
                do_kiedy += datetime.timedelta(1)
                do_kiedy = do_kiedy.replace(hour=8, minute=0, second=0, microsecond=0)
            if do_kiedy.weekday() == 5:
                do_kiedy += datetime.timedelta(2)
                do_kiedy = do_kiedy.replace(hour=8, minute=0, second=0, microsecond=0)

            ## godzina okresu płatnego
            if do_kiedy.hour >= 20:
                do_kiedy += datetime.timedelta(1)
                do_kiedy = do_kiedy.replace(hour=8, minute=0, second=0, microsecond=0)
                continue
            elif do_kiedy.hour < 8:
                do_kiedy = do_kiedy.replace(hour=8, minute=0, second=0, microsecond=0)

            ## pobierz ilość sekund -> ile_do_20(do_kiedy)  -> sekundy_do_20 = ile_do_20(do_kiedy)
            sekundy_do_20 = self.ile_do_20(do_kiedy)

            ## jeśli zaplacone_sekundy >= sekundy_do_20, do_kiedy += sekundy_do_20, sekundy_do_wykorzystania -= sekundy_do_20
            if zaplacone_sekundy >= sekundy_do_20:
                do_kiedy += datetime.timedelta(seconds=sekundy_do_20)
                zaplacone_sekundy -= sekundy_do_20
            else:
                do_kiedy += datetime.timedelta(seconds=zaplacone_sekundy)
                zaplacone_sekundy = 0
                # koniec petli

        return do_kiedy

    def check_plate(self, plate):
        if (len(plate) > 8 or len(plate) < 4) or not all(c.isdigit() or c.isupper() for c in plate):
            messagebox.showerror("Niepoprawny nr rejestracyjny", "chujowe blachy")
            return ""


        return plate


    def main(self):
        def przycisk0_01zl():
            for x in range(ile_monet()):
                self.add(Money(0.01))
            print(self.bilet_do_kiedy())

        def przycisk0_02zl():
            for x in range(ile_monet()):
                self.add(Money(0.02))
            print(self.bilet_do_kiedy())

        def przycisk0_05zl():
            for x in range(ile_monet()):
                self.add(Money(0.05))
            print(self.bilet_do_kiedy())

        def przycisk0_1zl():
            for x in range(ile_monet()):
                self.add(Money(0.1))
            print(self.bilet_do_kiedy())

        def przycisk0_2zl():
            for x in range(ile_monet()):
                self.add(Money(0.2))
            print(self.bilet_do_kiedy())

        def przycisk0_5zl():
            for x in range(ile_monet()):
                self.add(Money(0.5))
            print(self.bilet_do_kiedy())

        def przycisk1zl():
            for x in range(ile_monet()):
                self.add(Money(1))
            print(self.bilet_do_kiedy())

        def przycisk2zl():
            for x in range(ile_monet()):
                self.add(Money(2))
            print(self.bilet_do_kiedy())

        def przycisk5zl():
            for x in range(ile_monet()):
                self.add(Money(5))
            print(self.bilet_do_kiedy())

        def przycisk10zl():
            for x in range(ile_monet()):
                self.add(Money(10))
            print(self.bilet_do_kiedy())

        def przycisk20zl():
            for x in range(ile_monet()):
                self.add(Money(20))
            print(self.bilet_do_kiedy())

        def przycisk50zl():
            for x in range(ile_monet()):
                self.add(Money(50))

            print(self.bilet_do_kiedy())

        okno = Tk()
        okno.geometry('1000x500')

        przycisk1 = Button(okno, text="Wrzuć \n 0.01zł", height=5, width=12, command=przycisk0_01zl,
                           activebackground='green')
        przycisk1.place(x=0, y=100)

        przycisk2 = Button(okno, text="Wrzuć \n 0.02zł", height=5, width=12, command=przycisk0_02zl,
                           activebackground='green')
        przycisk2.place(x=100, y=100)

        przycisk3 = Button(okno, text="Wrzuć \n 0.05zł", height=5, width=12, command=przycisk0_05zl,
                           activebackground='green')
        przycisk3.place(x=200, y=100)

        przycisk4 = Button(okno, text="Wrzuć \n 0.1zł", height=5, width=12, command=przycisk0_1zl,
                           activebackground='green')
        przycisk4.place(x=0, y=190)

        przycisk5 = Button(okno, text="Wrzuć \n 0.2zł", height=5, width=12, command=przycisk0_2zl,
                           activebackground='green')
        przycisk5.place(x=100, y=190)

        przycisk6 = Button(okno, text="Wrzuć \n 0.5zł", height=5, width=12, command=przycisk0_5zl,
                           activebackground='green')
        przycisk6.place(x=200, y=190)

        przycisk7 = Button(okno, text="Wrzuć \n 1zł", height=5, width=12, command=przycisk1zl, activebackground='green')
        przycisk7.place(x=0, y=280)

        przycisk8 = Button(okno, text="Wrzuć \n 2zł", height=5, width=12, command=przycisk2zl, activebackground='green')
        przycisk8.place(x=100, y=280)

        przycisk9 = Button(okno, text="Wrzuć \n 5zł", height=5, width=12, command=przycisk5zl, activebackground='green')
        przycisk9.place(x=200, y=280)

        przycisk10 = Button(okno, text="Wrzuć \n 10zł", height=5, width=12, command=przycisk10zl,
                            activebackground='green')
        przycisk10.place(x=0, y=370)

        przycisk11 = Button(okno, text="Wrzuć \n 20zł", height=5, width=12, command=przycisk20zl,
                            activebackground='green')
        przycisk11.place(x=100, y=370)

        przycisk12 = Button(okno, text="Wrzuć \n 50zł", height=5, width=12, command=przycisk50zl,
                            activebackground='green')
        przycisk12.place(x=200, y=370)

        napis_tablica = Label(okno, text='Podaj Nr tablicy \nrejestracyjnej pojazdu', font='ariel 10', width=18,
                              height=3)
        napis_tablica.place(x=20, y=-5)

        napis_ile_monet = Label(okno, text='Podaj ilość \n monet', font='ariel 10', width=20, height=3)
        napis_ile_monet.place(x=160, y=-5)
        tablica = Entry(okno, width=21, font='ariel 12')
        tablica.place(x=2, y=44)

        def czytnie_tablicy():
            print(tablica.get())
            self.check_plate(tablica.get())

        przycisk13 = Button(okno, text="Zatwierdź Nr Tablicy", width=26, command=czytnie_tablicy,
                            activebackground='green')
        przycisk13.place(x=2, y=70)

        def czas_okno():
            aktualny_czas = time.strftime('%I:%M:%S:%p')
            zegar['text'] = aktualny_czas
            zegar.after(1000, czas_okno)

        zegar = Label(okno, font='ariel 18', width=12, height=2, bg='black', fg='red')
        zegar.place(x=1000, y=20)

        def ile_monet():
            return int(ilosc_monet.get())

        ilosc_monet = Spinbox(from_=0, to=200, wrap=True, width=10)
        ilosc_monet.place(x=199, y=44)
        def zmiana_czasu():
            YEAR = datetime.date.today().year
            MONTH = datetime.date.today().month
            DATE = datetime.date.today().day
            HOUR = datetime.datetime.now().hour
            MINUTE = datetime.datetime.now().minute
            SECONDS = datetime.datetime.now().second

            data = datetime.datetime.now
            data = datetime.datetime.strptime(str(YEAR) + " " + str(MONTH) + " " + str(DATE) + " " + str(HOUR) + " " + str(MINUTE) + " " + str(SECONDS),'%Y %m %d %H %M %S')
            self._czy_zmiana_czas = self._czy_zmiana_czas + 1
            self._data_od_urzytkownika = datetime.datetime.strptime(cal.get_date(), '%m/%d/%y')
            self._data_od_urzytkownika = self._data_od_urzytkownika.replace(hour=int(hour.get()), minute=int(min.get()))
            if self._data_od_urzytkownika < data:
                messagebox.showerror("Niepoprawna data", "Została podana \n Zla data")
            else:
                self._nowa_data = self._data_od_urzytkownika

        def wypisanie_biletu():            YEAR = datetime.date.today().year
            YEAR = self._nowa_data.datetime.year
            MONTH = self._nowa_data.datetime.month
            DATE = self._nowa_data.datetime.day
            HOUR = self._nowa_data.datetime.hour
            MINUTE = self._nowa_data.datetime.minute
            SECONDS = self._nowa_data.datetime.second
            self._nowa_data = datetime.datetime.strptime
            bilet = str("Numer rejestracyjny - " + self.check_plate(tablica.get())+"\n Godzina rozpoczęcia"+ str(YEAR) + " " + str(MONTH) + " " + str(DATE) + " " + str(HOUR) + " " + str(MINUTE) + " " + str(SECONDS))
            messagebox.showinfo(title="BILET", message = bilet)

        przycisk_zmiana_czasu = Button(okno,text = 'Zatwierdź \n Zmiane czasu', width = 17,height = 2, command =zmiana_czasu)
        przycisk_zmiana_czasu.place(x=420, y=232)
        hour = Spinbox(from_=8, to=20, wrap=True, width=2, state="readonly")
        hour.place(x=300, y=232)
        godziny = Label(okno, text='Godziny', font='ariel 10', width=5, height=1)
        godziny.place(x = 340, y= 232)
        min = Spinbox(from_=0, to=59, wrap=True, width=2, state="readonly")
        min.place(x=300, y=254)
        minuty = Label(okno, text='Minuty', font='ariel 10', width=5, height=1)
        minuty.place(x=340, y=254)
        suma_wrzuconych_monet = Label(okno, text=self.get_bal(), font='ariel 10', width=5, height=1)
        suma_wrzuconych_monet.place(x=400,y=400)


        zatwierdz_bilet = Button(okno,  text='Zatwierdz Bilet',command = wypisanie_biletu, font='ariel 20', width=15, height=1)
        zatwierdz_bilet.place(x=300,y=280)
        cal = Calendar(okno)
        cal.place(x= 300, y=44)

        czas_okno()
        okno.mainloop()


bankomat = ParkingMeter()
bankomat.main()
