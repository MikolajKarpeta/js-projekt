from decimal import *
from datetime import *
from tkinter import *
from tkinter import messagebox
from tkcalendar import *

import Parkometr
from Parkometr import *
import time
import datetime

class BadInputException(Exception):
    pass
class interface():

    def __init__(self):
        self._moneycount = dict.fromkeys(list(map(Decimal, ['0.01', '0.02', '0.05', \
                                                            '0.1', '0.2', '0.5', '1', '2', '5'])), 0)
        self._moneysum = 0
        self._data_rozpoczecia = datetime.datetime.now()
        self._czy_zmiana_czas = 1

    #funckje odpowiedzianle za wrzucanie monet
    #wywołują one funkcje add taką ilosc razy jaka była podana na spinboxie
    def przycisk0_01zl(self, ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(0.01))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk0_02zl(self):
        for x in range(int(self._ilosc_monet_spinbox.get())):
            Parkometr.ParkingMeter.add(self, Money(0.02))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk0_05zl(self, ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(0.05))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk0_1zl(self,ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(0.1))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk0_2zl(self,ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(0.2))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk0_5zl(self,ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(0.5))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk1zl(self,ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(1))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk2zl(self,ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(2))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk5zl(self,ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(5))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk10zl(self, ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(10))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk20zl(self,ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(20))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    def przycisk50zl(self,ilosc_monet):
        for x in range(int(ilosc_monet)):
            Parkometr.ParkingMeter.add(self, Money(50))
        print(str(Parkometr.ParkingMeter.bilet_do_kiedy(self)) + "\n")

    #funckja odpowiedzialna za zmiane godziny na tą podata przez urzytkownika
    def zmiana_czasu(self, data_nowa):
        """czytanie aktualnej daty oraz zmiana jej na format "strptime"
        #oraz późniejsze porównanie tej daty z tą podaną przez urzytkownika
        #po to by nie mógł kupić on biletu zaczynającego się w przeszłości"""
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

        data_od_urzytkownika = datetime.datetime.strptime(data_nowa, '%Y/%m/%d|%H:%M')
        #funkcja po której wykonaniu czas od którego liczona jest długoscc biletu
        #zmieniona jest na tą podaną przez urzytkownika
        Parkometr.ParkingMeter.czy_zmienic_czas(self)

        #sprawdzanie czy urzytkownik nie chciał podać daty która już minęła
        #jesli tak wyskakuję okno z błedem
        if data_od_urzytkownika < data:
            print("\nPodana data nie może byc przeszłą")
        #jeśli nie data zostaje zmieniona
        else:
            Parkometr.ParkingMeter.nowa_data(self, data_od_urzytkownika)
            print("\n"+ str(data_od_urzytkownika))


    #funkcja odpowiedzialna za wypisanie biletu
    def wypisanie_biletu(self, tablica):

        #pierszy warunek sprawdza czy do bankomatu zostały wprowadzone jakieś monety jeśli nie
        #na ekranie pojawia się okno z błędem
        if Parkometr.ParkingMeter.get_bal(self) <= 0:
            raise BadInputException

        #drugi warunek sprawdza czy podana tablica rejestracyjna jesy poprawna
        #jesli nie na ekranie pojawi się okno z błędem
        elif Parkometr.ParkingMeter.check_plate(self, tablica) == "":
            raise BadInputException

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
                "Numer rejestracyjny:    " + Parkometr.ParkingMeter.check_plate(self, tablica) + "\nGodzina rozpoczęcia:  " + str(
                    poczatek) + "\nGodzina wyjazdu:        " + str(wyjazd))
            messagebox.showinfo(title="BILET", message=bilet)
