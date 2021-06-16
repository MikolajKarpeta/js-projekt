from decimal import *
from datetime import *
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import time
import datetime



class BadNominalException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Money():
    """Klasa sprawdzajaca monety oraz banknoty"""
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
    """Główna klasa do obsługi logiki"""
    def __init__(self):
        self._moneycount = dict.fromkeys(list(map(Decimal, ['0.01', '0.02', '0.05', \
                                                            '0.1', '0.2', '0.5', '1', '2', '5'])), 0)
        self._moneysum = 0
        self._data_rozpoczecia = datetime.datetime.now()
        self._czy_zmiana_czas = 0

    def nowa_data(self, date: datetime.datetime):
        """Funkcja ustawia date rozpoczecia biletu na tą podana przez urzytkownika"""
        self._data_rozpoczecia = date
    def czy_zmienic_czas(self):
        """Funkcja informuje ze urzytkownik nacisnął przycisk do zmiany czasu"""
        self._czy_zmiana_czas = self._czy_zmiana_czas + 1
    def add(self, coin):
        """Funkcja dodate monety do skarbonki"""

        if not isinstance(coin, Money):
            print("zly nominal")
            return
        #ustawienie limitu ilosc monet
        #oraz sprawdzanie czy nie został on przepełniony
        if coin.get_val() not in (10, 20, 50):
            if self._moneycount[coin.get_val()] == 200:
                print("Magazyn monet tego nominalu jest pelny")
                return
            else:
                self._moneycount[coin.get_val()] += 1
        self._moneysum += coin.get_val()
        print("Dodano", coin.get_val(), "kredytu")

    def get_bal(self):
        """Funkcja zwraca sume wrzuconych monet"""
        return self._moneysum

    def bilet_dlugosc(self):
        """Funkcja liczy długosc biletu od czasu rozpoczęcia z sumy wrzuconych monet. Zwraca czas w sekundach"""
        # ilosc_minut = 0
        a = ParkingMeter.get_bal(self)
        #jeśli suma wrzuconych monet jest mniejsza bądz równa 2
        #program liczy dlugosc biletu z tego wzoru
        if a <= 2.0:
            self._ilosc_sekund = a / 2 * 60 * 60
            return int(self._ilosc_sekund)
        # jeśli suma wrzuconych monet jest mniejsza bądz równa  6
        # program liczy dlugosc biletu z tego wzoru
        elif a <= 6.0:
            a = a - 2
            self._ilosc_sekund = (60 + (a / 4 * 60)) * 60
            return int(self._ilosc_sekund)
        # jeśli suma wrzuconych monet jest wieksza niz 6
        # program liczy dlugosc biletu z tego wzoru
        else:
            a = a - 6
            self._ilosc_sekund = (120 + (a / 5 * 60)) * 60
            return int(self._ilosc_sekund)

    def dzien_tyg(self):
        """Funkcja sprawdza jakim dniem tygodnia jest podany dzień. Zwraca liczbę od 0 do 6 które odpowiadają poszczególnym dnią tygodnia"""
        today = date.today()
        self._dzien = today.weekday()
        return self._dzien

    def ile_do_20(self, data: datetime.datetime):
        """Funkcja liczy ile sekund zostało do 20"""
        dwudziesta = data.replace(hour=20, minute=0, second=0, microsecond=0)
        return (dwudziesta - data).total_seconds()




    def bilet_do_kiedy(self):
        """Funkcja liczy do kiedy ważny jest bilet. Zwraca datę zakończenia biletu"""
        # Pobieranie ile sekund zostało opłaconych
        zaplacone_sekundy = ParkingMeter.bilet_dlugosc(self)

        # Ustawienie daty rozpoczęcia biletu na datę aktualna
        do_kiedy = datetime.datetime.now()

        #Zamiana daty rozpoczęcia na tą podaną przez urzytkoniwka jeśli nacisnął on przycisk do zmiany daty
        if self._czy_zmiana_czas > 0:
            do_kiedy = self._data_rozpoczecia
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
            sekundy_do_20 = ParkingMeter.ile_do_20(self, do_kiedy)

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
        """Sprawdza czy podana rejestracja jest poprawna. Jeśli tak zwraca podany numer, jeśli nie zwraca pustego stringa"""
        if (len(plate) > 8 or len(plate) < 4) or not all(c.isdigit() or c.isupper() for c in plate):

            return ""
        return plate
