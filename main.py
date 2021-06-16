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
    """Klasa projektu odpowiadająca za interface"""

    def __init__(self):
        self._moneycount = dict.fromkeys(list(map(Decimal, ['0.01', '0.02', '0.05', \
                                                            '0.1', '0.2', '0.5', '1', '2', '5'])), 0)
        self._moneysum = 0
        self._data_rozpoczecia = datetime.datetime.now()
        self._czy_zmiana_czas = 1

    #funckje odpowiedzianle za wrzucanie monet
    #wywołują one funkcje add taką ilosc razy jaka była podana na spinboxie
    def przycisk0_01zl(self):
        """Dodaje monety o nominale 1gr do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.01))

    def przycisk0_02zl(self):
        """Dodaje monety o nominale 2gr do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.02))

    def przycisk0_05zl(self):
        """Dodaje monety o nominale 5gr do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.05))

    def przycisk0_1zl(self):
        """Dodaje monety o nominale 10gr do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.1))

    def przycisk0_2zl(self):
        """Dodaje monety o nominale 20gr do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.2))

    def przycisk0_5zl(self):
        """Dodaje monety o nominale 50gr do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.5))

    def przycisk1zl(self):
        """Dodaje monety o nominale 1zł do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(1))

    def przycisk2zl(self):
        """Dodaje monety o nominale 2zł do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(2))

    def przycisk5zl(self):
        """Dodaje monety o nominale 5zł do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(5))

    def przycisk10zl(self):
        """Dodaje monety o nominale 10zł do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(10))

    def przycisk20zl(self):
        """Dodaje monety o nominale 20zł do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(20))

    def przycisk50zl(self):
        """Dodaje monety o nominale 50zł do sumy, przyjmuje ilosc monet"""
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(50))

    #funckja odpowiedzialna za zmiane godziny na tą podata przez urzytkownika
    def zmiana_czasu(self):
        """Funkcja zmienia czas od którego zaczynać się będzie bilet, na ten podany przez urzytkownika w oknie aplikacji"""

        #czytanie aktualnej daty oraz zmiana jej na format "strptime"
        #oraz późniejsze porównanie tej daty z tą podaną przez urzytkownika
        #po to by nie mógł kupić on biletu zaczynającego się w przeszłości
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

        #funkcja po której wykonaniu czas od którego liczona jest długoscc biletu
        #zmieniona jest na tą podaną przez urzytkownika
        Parkometr.ParkingMeter.czy_zmienic_czas(self)

        #sczytanie miesięcy/dni/lat z kalendarza oraz zastąpienie nimi aktualnej daty
        data_od_urzytkownika = datetime.datetime.strptime(self.cal.get_date(), '%m/%d/%y')

        #sczytanie ze spinboxów godzin oraz sekund oraz zatąpienie nimi aktualnej godziny
        data_od_urzytkownika = data_od_urzytkownika.replace(hour=int(self._hour.get()), minute=int(self._min.get()))


        #sprawdzanie czy urzytkownik nie chciał podać daty która już minęła
        #jesli tak wyskakuję okno z błedem
        if data_od_urzytkownika < data:
            messagebox.showerror("Niepoprawna data", "Została podana \n Zla data")
        #jeśli nie data zostaje zmieniona
        else:
            Parkometr.ParkingMeter.nowa_data(self, data_od_urzytkownika)

    #funkcja odpowiedzialna za wypisanie biletu
    def wypisanie_biletu(self):
        """Funkcja wypisuje bilet w formacie
            Numer tablicy-
            Data rozpoczęcia-
            Data końca biletu -
            Jest też odpowiedzialna za sprawdzenie czy urzytkownik wrzucił monety
            oraz czy rejestracja jest poprawna."""
        #pierszy warunek sprawdza czy do bankomatu zostały wprowadzone jakieś monety jeśli nie
        #na ekranie pojawia się okno z błędem
        if Parkometr.ParkingMeter.get_bal(self) <= 0:
            messagebox.showerror(title="Błąd", message="Prosze wrzucić monety")

        #drugi warunek sprawdza czy podana tablica rejestracyjna jesy poprawna
        #jesli nie na ekranie pojawi się okno z błędem
        elif Parkometr.ParkingMeter.check_plate(self, self._tablica.get()) == "":
            messagebox.showerror("Niepoprawny nr rejestracyjny", "Prosze wpisać prawidlowy numer rejestracyjny")

        #Gdy rejestracja jest poprawna oraz zosyały wrzucone monety program drukuje bilet
        else:

            #pobieranie daty waznosci biletu
            wyjazd = Parkometr.ParkingMeter.bilet_do_kiedy(self)
            wyjazd = wyjazd.replace(microsecond=0)

            #data rozpoczęcia biletu jest data podana od urzytkownika
            #bądz moment wydrukowania biletu jesli urzytkownik nie zatwierdził zmiany daty
            poczatek = self._data_rozpoczecia
            poczatek = poczatek.replace(microsecond=0)

            #okno z biletem w formacie
            #Numer tablicy-
            #Data rozpoczęcia-
            #Data końca biletu -
            bilet = str(
                "Numer rejestracyjny:    " + Parkometr.ParkingMeter.check_plate(self, self._tablica.get()) + "\nGodzina rozpoczęcia:  " + str(
                    poczatek) + "\nGodzina wyjazdu:        " + str(wyjazd))
            messagebox.showinfo(title="BILET", message=bilet)

    def main(self):
        """Funkcja zawierająca okno aplikacji oraz wszystkie zawarte w nim funkcjonalnosci"""

        #tworze okno o tytule parkomat oraz o podanych wymiarach
        okno = Tk()
        okno.title("Parkomat")
        okno.geometry('560x460')

        #przyciski odpowiedzialne za wrzucanie monet w formacie
        # (w jakim oknie się znajdują, tekst na nich wyświetlony, wysokosc, szerokosc, funckja wywolana po ich nacisniecu)
        przycisk_0_01zl = Button(okno, text="Wrzuć \n 0.01zł", height=5, width=12, command=self.przycisk0_01zl,
                           activebackground='green')
        przycisk_0_01zl.place(x=0, y=100)

        przycisk_0_02zl = Button(okno, text="Wrzuć \n 0.02zł", height=5, width=12, command=self.przycisk0_02zl,
                           activebackground='green')
        przycisk_0_02zl.place(x=100, y=100)

        przycisk_0_05zl = Button(okno, text="Wrzuć \n 0.05zł", height=5, width=12, command=self.przycisk0_05zl,
                           activebackground='green')
        przycisk_0_05zl.place(x=200, y=100)

        przycisk_0_1zl = Button(okno, text="Wrzuć \n 0.1zł", height=5, width=12, command=self.przycisk0_1zl,
                           activebackground='green')
        przycisk_0_1zl.place(x=0, y=190)

        przycisk_0_2zl = Button(okno, text="Wrzuć \n 0.2zł", height=5, width=12, command=self.przycisk0_2zl,
                           activebackground='green')
        przycisk_0_2zl.place(x=100, y=190)

        przycisk_0_5zl = Button(okno, text="Wrzuć \n 0.5zł", height=5, width=12, command=self.przycisk0_5zl,
                           activebackground='green')
        przycisk_0_5zl.place(x=200, y=190)

        przycisk_1zl = Button(okno, text="Wrzuć \n 1zł", height=5, width=12, command=self.przycisk1zl, activebackground='green')
        przycisk_1zl.place(x=0, y=280)

        przycisk_2zl = Button(okno, text="Wrzuć \n 2zł", height=5, width=12, command=self.przycisk2zl, activebackground='green')
        przycisk_2zl.place(x=100, y=280)

        przycisk_5zl = Button(okno, text="Wrzuć \n 5zł", height=5, width=12, command=self.przycisk5zl, activebackground='green')
        przycisk_5zl.place(x=200, y=280)

        przycisk_0_10zl = Button(okno, text="Wrzuć \n 10zł", height=5, width=12, command=self.przycisk10zl,
                            activebackground='green')
        przycisk_0_10zl.place(x=0, y=370)

        przycisk_0_20zl = Button(okno, text="Wrzuć \n 20zł", height=5, width=12, command=self.przycisk20zl,
                            activebackground='green')
        przycisk_0_20zl.place(x=100, y=370)

        przycisk_0_50zl = Button(okno, text="Wrzuć \n 50zł", height=5, width=12, command=self.przycisk50zl,
                            activebackground='green')
        przycisk_0_50zl.place(x=200, y=370)

        #wyswietlenie informacji gdzie nalezy wybrac ilosc wrzucanych monet
        napis_ile_monet = Label(okno, text='Podaj ilość \n monet', font='ariel 10', width=20, height=3)
        napis_ile_monet.place(x=160, y=-5)

        #spinbox z mający zakres od 0 do 200 w którym mozna wybrac ile monet danego nominalu chcemy wrzucic
        self._ilosc_monet_spinbox = Spinbox(from_=0, to=200, wrap=True, width=10)
        self._ilosc_monet_spinbox.place(x=199, y=44)


        #infomacja tekstowa gdzie nalezy wpisać numer tablicy rejestracyjnej
        napis_tablica = Label(okno, text='Podaj Nr tablicy \nrejestracyjnej pojazdu', font='ariel 10', width=18,
                              height=3)
        napis_tablica.place(x=20, y=-5)

        #pole które pobiera informacje od urzytkownika w formie wpisanego stringu
        self._tablica = Entry(okno, width=21, font='ariel 12')
        self._tablica.place(x=2, y=44)

        # przycisk odpowiedzialny za zmiane daty na ta podana przez urzytkownika
        przycisk_zmiana_czasu = Button(okno, text='Zatwierdź \n Zmiane czasu', width=17, height=2,
                                       command=self.zmiana_czasu)
        przycisk_zmiana_czasu.place(x=420, y=232)


        #poszczególne częsci interfejsu odpowiedzianke za sczytanie daty
        #spinbox który pozwala na podanie urzytkownikowi godziny
        self._hour = Spinbox(from_=8, to=20, wrap=True, width=2, state="readonly")
        self._hour.place(x=300, y=232)

        #informacja gdzie nalezy podac godzine
        self._godziny = Label(okno, text='Godziny', font='ariel 10', width=5, height=1)
        self._godziny.place(x = 340, y= 232)

        #spinbox który pozwala na podanie urzytkownikowi minuty
        self._min = Spinbox(from_=0, to=59, wrap=True, width=2, state="readonly")
        self._min.place(x=300, y=254)
        #informacja gdzie nalezy podac minuty
        self.minuty = Label(okno, text='Minuty', font='ariel 10', width=5, height=1)
        self.minuty.place(x=340, y=254)

        #Calendar zawarte w Tkinter pozwala wybrac date na interaktywnym kalendarzu
        #oraz zwraca ją w formacie (miesiace/dni/lata)
        self.cal = Calendar(okno)
        self.cal.place(x= 300, y=44)

        #przycisk kończący tranzakcje zatwierdza wszystkie informacje podane przez urzytkownika oraz drukuje bilet
        zatwierdz_bilet = Button(okno,  text='Zatwierdz Bilet',command = self.wypisanie_biletu, font='ariel 20', width=15, height=1)
        zatwierdz_bilet.place(x=300,y=280)
        okno.mainloop()

bankomat = interface()
bankomat.main()
