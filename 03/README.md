# Ćwiczenie 3 — Wejście/wyjście, pliki tekstowe, `math`, `random`, `time`

## Cel ćwiczeń

Celem ćwiczeń jest tworzenie programów, które pobierają dane od użytkownika, odczytują pliki tekstowe, wykonują obliczenia i zapisują wyniki. Poznasz również moduły standardowe przydatne do obliczeń matematycznych, symulacji losowych i pomiaru czasu.

W zadaniach połączysz nowy materiał z elementami poprzednich ćwiczeń: instrukcjami warunkowymi, pętlami, funkcjami, napisami, listami i słownikami.

## Zakres materiału

- pobieranie danych przez `input()` i konwersja typów;
- wyświetlanie i formatowanie wyników przez `print()` oraz f-stringi;
- otwieranie i zamykanie plików tekstowych: `open()` oraz `with`;
- odczyt, zapis i dopisywanie danych: tryby `r`, `w`, `a`;
- przetwarzanie pliku wiersz po wierszu;
- metody tekstowe `strip()`, `split()`, `join()` i `startswith()`;
- numerowanie wierszy przez `enumerate()`;
- korzystanie z modułów `math`, `random` i `time`;
- podział programu na pobieranie danych, obliczenia i zapis raportu.

**Wymagania wstępne:** materiał ćwiczeń 1 i 2, w szczególności `if`, `for`, `while`, `break`, `continue`, `def`, `return`, operacje na napisach oraz podstawowe typy kolekcji.

---

## 1. Wejście i wyjście programu

### 1.1. Pobieranie danych przez `input()`

Funkcja `input()` wyświetla komunikat, czeka na wpisanie danych i zatwierdzenie klawiszem Enter. Jej wynikiem jest zawsze napis, również wtedy, gdy użytkownik wpisze liczbę.

```python
imie = input("Podaj imię: ")
print("Witaj,", imie)

liczba = input("Podaj liczbę: ")
print(type(liczba))  # <class 'str'>
```

Aby wykonywać obliczenia, trzeba przekonwertować napis na odpowiedni typ:

```python
liczba_probek = int(input("Podaj liczbę próbek: "))
temperatura = float(input("Podaj temperaturę: "))

print(liczba_probek * 2)
print(temperatura + 273.15)
```

### 1.2. Formatowanie wyników — f-stringi

F-string zaczyna się od litery `f`. W nawiasach klamrowych można umieścić zmienną lub wyrażenie:

```python
nazwa = "próbki A"
wynik = 12.345678

print(f"Wynik dla {nazwa}: {wynik}")
print(f"Wynik dla {nazwa}: {wynik:.2f}")
```

Zapis `:.2f` oznacza wyświetlenie liczby z dwoma miejscami po przecinku:

```text
Wynik dla próbki A: 12.35
```

Formatowanie nie zmienia wartości przechowywanej w zmiennej. Do dalszych obliczeń używaj pełnej wartości, a zaokrąglaj dopiero wynik prezentowany użytkownikowi.

Można również uzupełniać liczby zerami:

```python
godziny = 1
minuty = 4
sekundy = 9

print(f"{godziny:02d}:{minuty:02d}:{sekundy:02d}")  # 01:04:09
```

`02d` oznacza liczbę całkowitą o szerokości co najmniej dwóch znaków, uzupełnioną zerami z lewej strony.

### 1.3. Parametry `sep` i `end` funkcji `print()`

```python
print("A", "T", "G", "C", sep=";")  # A;T;G;C

print("Przetwarzanie", end="... ")
print("gotowe")  # Przetwarzanie... gotowe
```

- `sep` określa separator pomiędzy argumentami;
- `end` określa tekst dopisywany na końcu; domyślnie jest to znak nowego wiersza `\n`.

---

## 2. Pliki tekstowe

### 2.1. `open()`, `with` i tryby otwarcia

```python
with open("notatka.txt", "w", encoding="utf-8") as plik:
    plik.write("Pierwszy pomiar wykonano rano.\n")
```

- `open()` otwiera plik;
- nazwa wskazuje plik, z którym pracujemy;
- tryb określa rodzaj operacji;
- `encoding="utf-8"` ustala kodowanie tekstu, w tym polskich znaków;
- `with` zapewnia zamknięcie pliku po opuszczeniu bloku.

| Tryb | Zastosowanie | Działanie |
|---|---|---|
| `r` | odczyt | odczytuje zawartość istniejącego pliku |
| `w` | zapis | tworzy plik lub zastępuje jego dotychczasową zawartość |
| `a` | dopisywanie | zapisuje na końcu pliku; jeżeli pliku nie ma, tworzy go |

**Uwaga:** otwarcie pliku w trybie `w` usuwa jego wcześniejszą zawartość już podczas otwierania. Do raportu tworzonego od początku użyj `w`; do dziennika gromadzącego kolejne wpisy — `a`.

### 2.2. Gdzie Python szuka pliku?

Ścieżka względna odnosi się do **bieżącego katalogu roboczego**, z którego uruchomiono program. Nie musi to być katalog, w którym zapisano skrypt.

```python
with open("dane/pomiary.txt", "r", encoding="utf-8") as plik:
    print(plik.read())
```

Ten przykład zakłada uruchomienie programu z katalogu zawierającego podkatalog `dane`. Nazwa i rozszerzenie w ścieżce powinny odpowiadać nazwie pliku.

### 2.3. Trzy sposoby odczytu

**Cały plik jako jeden napis — `read()`:**

```python
with open("notatka.txt", "r", encoding="utf-8") as plik:
    zawartosc = plik.read()

print(zawartosc)
```

**Wszystkie wiersze jako lista napisów — `readlines()`:**

```python
with open("notatka.txt", "r", encoding="utf-8") as plik:
    wiersze = plik.readlines()

print(wiersze)
```

**Przetwarzanie wiersz po wierszu — pętla:**

```python
with open("notatka.txt", "r", encoding="utf-8") as plik:
    for wiersz in plik:
        print(wiersz.strip())
```

Przejście po pliku pętlą pozwala przetwarzać kolejne wiersze bez wcześniejszego wczytywania całej zawartości do listy.

### 2.4. Czyszczenie, dzielenie i łączenie tekstu

```python
wiersz = "  probka_01;12.5;37.0\n"

wiersz = wiersz.strip()
pola = wiersz.split(";")

print(pola)  # ['probka_01', '12.5', '37.0']
print(float(pola[1]))  # 12.5
```

- `strip()` usuwa białe znaki z obu końców napisu;
- `split(";")` dzieli napis w miejscach wystąpienia średnika;
- `split()` bez argumentu dzieli według białych znaków;
- `join()` łączy napisy wybranym separatorem.

```python
fragmenty = ["ATG", "CCA", "TAA"]

print("".join(fragmenty))   # ATGCCATAA
print("-".join(fragmenty))  # ATG-CCA-TAA
```

Pusty napis `""` jako separator pozwala połączyć fragmenty bez dodatkowych znaków.

### 2.5. Puste wiersze, komentarze i numery wierszy

```python
with open("dane/pomiary.txt", "r", encoding="utf-8") as plik:
    for numer, wiersz in enumerate(plik, start=1):
        tekst = wiersz.strip()

        if tekst == "" or tekst.startswith("#"):
            continue

        print(f"Wiersz {numer}: {tekst}")
```

`enumerate(plik, start=1)` dostarcza jednocześnie numer i treść wiersza. `startswith("#")` sprawdza, czy napis zaczyna się od `#`. Numerowanie obejmuje również wiersze pominięte przez `continue`, dzięki czemu zgadza się z numerami w edytorze.

### 2.6. Zapis i dopisywanie

```python
with open("wynik.txt", "w", encoding="utf-8") as plik:
    plik.write("Analiza zakończona.\n")
    plik.write("Liczba próbek: 4\n")

with open("wynik.txt", "a", encoding="utf-8") as plik:
    plik.write("Wyniki sprawdzono ponownie.\n")
```

`write()` zapisuje napis i nie dodaje automatycznie końca wiersza. Liczby trzeba zamienić na tekst, np. za pomocą f-stringa.

W tabelach tekstowych można rozdzielać kolumny tabulatorami `\t`:

```python
with open("tabela.tsv", "w", encoding="utf-8") as plik:
    plik.write("probka\twynik\n")
    plik.write(f"A\t{12.3456:.3f}\n")
```

Rozszerzenie `.tsv` oznacza tutaj zwykły plik tekstowy z kolumnami rozdzielonymi tabulatorami. Nie wymaga użycia dodatkowego modułu.

---

## 3. Moduły standardowe i `math`

### 3.1. Importowanie modułu

Moduł udostępnia powiązane funkcje i stałe. Moduły `math`, `random` i `time` należą do biblioteki standardowej Pythona.

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Możliwe są też inne formy importu:

```python
import math as mt
from math import sqrt

print(mt.sqrt(25))
print(sqrt(25))
```

W zadaniach zalecany jest zapis `import math` i wywołania w rodzaju `math.sqrt()`, aby było widać, z jakiego modułu pochodzi funkcja.

### 3.2. Przydatne funkcje i stałe

| Zapis | Znaczenie | Przykład |
|---|---|---|
| `math.sqrt(x)` | pierwiastek kwadratowy | `math.sqrt(9)` → `3.0` |
| `math.sin(x)`, `math.cos(x)` | funkcje trygonometryczne; argument w radianach | `math.sin(math.pi / 2)` → około `1.0` |
| `math.radians(x)` | przeliczenie stopni na radiany | `math.radians(180)` → około `3.14159` |
| `math.exp(x)` | wartość `e**x` | `math.exp(0)` → `1.0` |
| `math.log(x)` | logarytm naturalny | `math.log(math.e)` → około `1.0` |
| `math.factorial(n)` | silnia nieujemnej liczby całkowitej | `math.factorial(5)` → `120` |
| `math.floor(x)` | zaokrąglenie w dół | `math.floor(2.8)` → `2` |
| `math.ceil(x)` | zaokrąglenie w górę | `math.ceil(2.1)` → `3` |
| `math.isclose(a, b)` | przybliżona równość liczb | `math.isclose(0.1 + 0.2, 0.3)` → `True` |
| `math.pi`, `math.e` | stałe matematyczne | odpowiednio około `3.14159` i `2.71828` |

Trzeba uwzględniać dziedzinę: `math.sqrt(x)` wymaga `x >= 0`, a `math.log(x)` — `x > 0`. Funkcja `abs(x)` zwraca wartość bezwzględną i jest dostępna bez importu.

---

## 4. Liczby pseudolosowe — `random`

### 4.1. Podstawowe funkcje

```python
import random

print(random.random())        # 0.0 <= wynik < 1.0
print(random.randint(1, 6))   # liczba całkowita od 1 do 6 włącznie
print(random.uniform(-2, 2))  # liczba zmiennoprzecinkowa między -2 a 2
print(random.choice(["A", "T", "G", "C"]))
```

**Uwaga:** `randint(a, b)` uwzględnia obie granice. Różni się tym od `range(a, b)`, które nie uwzględnia `b`. W `uniform(a, b)` końcowa granica `b` może pojawić się wskutek zaokrągleń zmiennoprzecinkowych.

### 4.2. Losowanie ze zwracaniem i bez zwracania

```python
elementy = ["A", "B", "C", "D"]

print(random.choices(elementy, k=6))  # elementy mogą się powtarzać
print(random.sample(elementy, k=3))   # różne pozycje z listy
```

`sample()` nie wybiera tej samej pozycji dwukrotnie. Jeżeli lista zawiera powtarzające się wartości, powtórzenia wartości nadal są możliwe. Dla podanej listy z czterema elementami `k` w `sample()` nie może przekroczyć `4`.

### 4.3. Ziarno generatora — `seed()`

```python
random.seed(42)
pierwszy = random.random()

random.seed(42)
drugi = random.random()

print(pierwszy == drugi)  # True
```

To samo ziarno i ta sama kolejność wywołań umożliwiają odtworzenie wyników losowania w tym samym środowisku. Przydaje się to podczas sprawdzania symulacji.

Ustawiaj ziarno raz przed serią obliczeń. Ustawianie tego samego ziarna wewnątrz każdej iteracji restartuje generator i może powodować ciągłe otrzymywanie tych samych wyników.

---

## 5. Czas i pomiar wydajności — `time`

### 5.1. Bieżący czas i data

```python
import time

print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
```

`time.time()` zwraca czas w sekundach od początku epoki uniksowej. `time.strftime()` pozwala otrzymać czytelny zapis lokalnej daty i godziny. W podanym formacie `%m` oznacza miesiąc, a `%M` — minuty.

### 5.2. Wstrzymanie programu — `sleep()`

```python
print("Początek")
time.sleep(0.5)
print("Koniec")
```

`sleep()` przyjmuje liczbę sekund, również ułamkową. Rzeczywista przerwa może być dłuższa ze względu na działanie systemu operacyjnego.

### 5.3. Czas wykonania — `perf_counter()`

```python
start = time.perf_counter()

suma = 0
for liczba in range(100_000):
    suma += liczba ** 2

czas = time.perf_counter() - start
print(f"Czas obliczeń: {czas:.6f} s")
```

Do pomiaru czasu trwania używaj różnicy dwóch odczytów `perf_counter()`. Pojedynczy odczyt nie oznacza daty ani godziny. W krótkich pomiarach nie umieszczaj `input()`, zapisu pliku lub dużej liczby `print()`, jeśli interesuje Cię czas samych obliczeń.

### 5.4. Pomiar czasu a odliczanie sekund

Pętla wykonująca dziesięć razy `sleep(1)` trwa nieco dłużej niż dziesięć sekund, ponieważ wykonuje także inne instrukcje. W minutniku można wyznaczyć moment końcowy przez `perf_counter()` i za każdym razem obliczać pozostały czas od nowa. Do wyświetlania pełnych sekund przyda się `math.ceil()`.

---

## 6. Dodatkowe przykłady — łączenie poznanych konstrukcji

### 6.1. Słownik zliczeń i zapis tabeli

```python
slowa = ["kot", "pies", "kot", "ptak"]
zliczenia = {}

for slowo in slowa:
    if slowo not in zliczenia:
        zliczenia[slowo] = 0
    zliczenia[slowo] += 1

with open("slowa.tsv", "w", encoding="utf-8") as plik:
    plik.write("slowo\tliczba\n")
    for slowo, liczba in zliczenia.items():
        plik.write(f"{slowo}\t{liczba}\n")
```

Metoda `items()` umożliwia przechodzenie jednocześnie po kluczach i wartościach słownika. To rozwinięcie operacji na słownikach poznanych w ćwiczeniu 1.

### 6.2. Podział programu na funkcje

```python
def przelicz_na_kelwiny(temperatury):
    wyniki = []
    for temperatura in temperatury:
        wyniki.append(temperatura + 273.15)
    return wyniki


def zapisz_temperatury(nazwa_pliku, temperatury):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        for temperatura in temperatury:
            plik.write(f"{temperatura:.2f}\n")


dane = [0, 20, 37]
wyniki = przelicz_na_kelwiny(dane)
zapisz_temperatury("temperatury_kelwiny.txt", wyniki)
```

Pierwsza funkcja wykonuje obliczenia i zwraca dane. Druga zapisuje gotowy wynik. Dzięki temu sposób wyświetlania lub zapisu można zmienić bez przerabiania samych obliczeń.

### 6.3. Przeliczanie sekund na godziny, minuty i sekundy

```python
czas = 3672

godziny = czas // 3600
minuty = (czas % 3600) // 60
sekundy = czas % 60

print(f"{godziny:02d}:{minuty:02d}:{sekundy:02d}")  # 01:01:12
```

W tym przykładzie wracają operatory `//` i `%` z pierwszego ćwiczenia.

---

## 7. Zadania do wykonania

### Zadanie 1 — Raport z pomiarów laboratoryjnych

Napisz program analizujący plik tekstowy zawierający po jednym pomiarze w wierszu. W pliku mogą występować także puste wiersze i komentarze zaczynające się od `#`. Załóż, że plik zawiera co najmniej jeden pomiar, a każdy wiersz z pomiarem zawiera jedną skończoną liczbę.

**Wymagania:**

1. Pobierz od użytkownika ścieżkę do pliku. Do pierwszej próby użyj `dane/pomiary.txt`.
2. Zdefiniuj funkcję `wczytaj_pomiary(nazwa_pliku)`, która zwraca listę pomiarów.
3. Po usunięciu skrajnych białych znaków pomijaj puste wiersze i komentarze. Pozostałe wiersze przekonwertuj na liczby przez `float()`. Wartości ujemne są dozwolone.
4. Zdefiniuj funkcję `statystyki(pomiary)`, która zwraca słownik z liczbą pomiarów, minimum, maksimum, średnią arytmetyczną i odchyleniem standardowym populacji.
5. Odchylenie policz według wzoru poniżej, używając pętli i `math.sqrt()`.
6. Wyświetl podsumowanie i zapisz je do `raport_pomiary.txt` w trybie `w`. Raport ma zawierać także datę analizy. Średnią i odchylenie zapisz z sześcioma miejscami po przecinku.

**Wzory:** dla `n` pomiarów `x_1, ..., x_n`:

```text
srednia = (x_1 + ... + x_n) / n
odchylenie = sqrt(((x_1 - srednia)**2 + ... + (x_n - srednia)**2) / n)
```

Używamy mianownika `n`. Dla pojedynczego pomiaru odchylenie wynosi `0`.

**Sprawdź:** w dołączonym pliku wartości to `10`, `12`, `14`, `16`. Średnia wynosi `13`, a odchylenie około `2.236068`. Sprawdź też plik z jednym pomiarem oraz plik z kilkoma takimi samymi pomiarami.

### Zadanie 2 — Analiza białka z pliku FASTA

Rozbuduj analizę sekwencji z poprzednich ćwiczeń: tym razem dane mają pochodzić z pliku FASTA, a wynik ma zostać zapisany w tabeli. Wykorzystaj plik `dane/1E7A.fasta`.

Pierwszy niepusty wiersz pliku FASTA jest nagłówkiem zaczynającym się od `>`. Kolejne wiersze zawierają fragmenty tej samej sekwencji:

```text
>bialko_kontrolne
AKAK
GWY
```

Sekwencja z tego przykładu to `AKAKGWY`. Nagłówek nie jest jej częścią. Załóż, że plik zawiera dokładnie jeden rekord z niepustą sekwencją białkową. W sekwencji występują wyłącznie jednoliterowe oznaczenia 20 standardowych aminokwasów; dopuszczalne są wielkie i małe litery:

```python
aminokwasy = "ACDEFGHIKLMNPQRSTVWY"
```

**Wymagania:**

1. Pobierz od użytkownika ścieżkę do pliku FASTA.
2. Zdefiniuj funkcję `wczytaj_fasta(nazwa_pliku)`, która zwraca nagłówek bez znaku `>` oraz połączoną sekwencję zapisaną wielkimi literami. Pomijaj puste wiersze i usuwaj skrajne białe znaki z każdego wiersza.
3. Zdefiniuj funkcję `sklad_aminokwasowy(sekwencja)`, która zwraca słownik z liczbą wystąpień każdego z 20 aminokwasów, również tych nieobecnych w sekwencji. Zliczanie wykonaj za pomocą pętli.
4. Wyświetl nagłówek, długość sekwencji oraz najczęściej występujący aminokwas i liczbę jego wystąpień. Przy remisie pokaż wszystkie takie aminokwasy w kolejności alfabetycznej.
5. Zapisz plik `sklad_bialka.tsv` w trybie `w`, z nagłówkiem `aminokwas`, `liczba`, `procent` i 20 wierszami danych w kolejności alfabetycznej. Kolumny rozdziel tabulatorami; udziały procentowe podaj z dwoma miejscami po przecinku.

**Sprawdź:** plik `dane/kontrola.fasta` zawiera sekwencję z przykładu. Jej długość to `7`, a najczęstsze aminokwasy to `A` i `K` — po `2` wystąpienia, czyli po około `28.57%`. Suma zliczeń musi być równa długości sekwencji. Zaokrąglone procenty nie muszą sumować się dokładnie do `100.00`.

### Zadanie 3 — Wyznaczanie liczby π metodą Monte Carlo

Napisz program szacujący wartość liczby π przez losowanie punktów. Następnie porównaj dokładność i czas obliczeń dla różnych liczb punktów.

Losujemy punkty `(x, y)` równomiernie w kwadracie `[-1, 1] × [-1, 1]`. Punkt leży wewnątrz koła jednostkowego lub na jego brzegu, jeżeli:

```text
x**2 + y**2 <= 1
```

Pole kwadratu wynosi `4`, a pole koła jednostkowego wynosi π. Stąd przybliżenie:

```text
pi_przyblizone = 4 * liczba_punktow_w_kole / liczba_wszystkich_punktow
```

**Wymagania:**

1. Pobierz od użytkownika całkowite ziarno generatora oraz dodatnią liczbę całkowitą powtórzeń `r`. Na początek przyjmij ziarno `42` i `r = 3`.
2. Zdefiniuj funkcję `oszacuj_pi(n)`, która losuje `n` punktów za pomocą `random.uniform(-1, 1)` i zwraca przybliżenie π oraz liczbę punktów w kole. Nie przechowuj wszystkich współrzędnych — wystarczy licznik trafień.
3. Wykonaj po `r` osobnych symulacji dla każdej wartości `n`: `1000`, `10_000`, `100_000`. Użyj zagnieżdżonych pętli. Ziarno ustaw raz, przed całą serią.
4. Dla każdej symulacji oblicz błąd bezwzględny `abs(pi_przyblizone - math.pi)` oraz zmierz czas wykonania samej funkcji `oszacuj_pi()` przez `time.perf_counter()`.
5. Zapisz każdą próbę w pliku `wyniki_pi.tsv`, w kolumnach: `ziarno`, `n`, `powtorzenie`, `w_kole`, `pi`, `blad`, `czas_s`. Numeruj powtórzenia od `1`. Przybliżenie i błąd zapisuj z sześcioma miejscami po przecinku, czas z dziewięcioma.
6. Wyświetl i zapisz w `podsumowanie_pi.txt` średnie przybliżenie π, średni błąd bezwzględny i średni czas dla każdej wartości `n`. Średni błąd to średnia błędów poszczególnych prób, a nie błąd średniego przybliżenia.
7. Po wykonaniu programu dopisz do `podsumowanie_pi.txt` 2–3 zdania własnego komentarza: jak zwiększenie liczby punktów wpłynęło na dokładność i czas w Twoich wynikach?

**Sprawdź:** dla `r = 3` tabela powinna zawierać `9` wierszy danych. Wynik każdej próby musi należeć do przedziału `[0, 4]`. Powtórne uruchomienie z tym samym ziarnem i parametrami w tym samym środowisku powinno odtworzyć wyniki liczbowe; czasy mogą się różnić.

**Uwaga:** większa liczba punktów nie gwarantuje mniejszego błędu w każdej pojedynczej próbie. To metoda losowa. Podczas pomiaru nie wypisuj każdego punktu ani nie stosuj `sleep()`.

### Zadanie 4 — Minutnik interwałowy z dziennikiem

Napisz program, który przeprowadza serię odcinków pracy i przerw, odlicza pozostały czas i zapisuje przebieg sesji do pliku.

**Wymagania:**

1. Pobierz dodatnią liczbę odcinków pracy, czas jednego odcinka oraz czas przerwy. Oba czasy użytkownik podaje w formacie `HH:MM:SS`.
2. Zdefiniuj funkcję `czas_na_sekundy(tekst)`, która zwraca łączną liczbę sekund. Załóż, że zapis zawiera dokładnie trzy liczby całkowite: nieujemne godziny oraz minuty i sekundy z przedziału `0–59`. Dopuszczalne są np. `00:01:05` i `0:1:5`.
3. Przyjmij, że czas pracy jest większy od zera, a czas przerwy jest nieujemny.
4. Zdefiniuj funkcję `formatuj_czas(sekundy)`, która zwraca napis z godzinami, minutami i sekundami, np. `65` → `00:01:05`.
5. Zdefiniuj funkcję `odliczaj(sekundy, opis)`, która wyświetla opis etapu oraz pozostały czas, aktualizuje go mniej więcej co sekundę i kończy komunikatem `Czas minął!`. Zastosuj `while` oraz `time.sleep()`.
6. Wyznacz moment końca etapu przez `time.perf_counter()` i obliczaj pozostały czas na podstawie aktualnego odczytu. Do prezentacji zaokrąglaj dodatnią liczbę sekund w górę przez `math.ceil()`. Zakończenie odliczania ma zależeć od zegara, a nie wyłącznie od liczby wykonanych wywołań `sleep(1)`.
7. Pomiędzy kolejnymi odcinkami pracy uruchamiaj przerwę. Po ostatnim odcinku nie dodawaj przerwy; przerwę o długości zero pomijaj.
8. Do pliku `dziennik_minutnika.txt` dopisuj w trybie `a`: początek sesji z datą, parametry, początek i koniec każdego wykonanego etapu oraz planowany i rzeczywisty czas całej sesji. Rzeczywisty czas mierz od początku pierwszego odliczania do końca ostatniego, z pominięciem wcześniejszego wprowadzania danych.

**Sprawdź:** dla `2` odcinków pracy po `00:00:03` i przerwy `00:00:02` kolejność to:

```text
Praca 1 → 3 sekundy
Przerwa 1 → 2 sekundy
Praca 2 → 3 sekundy
```

Planowany czas wynosi `8` sekund; rzeczywisty może być nieco dłuższy. Sprawdź także sesję z jednym odcinkiem pracy oraz sesję z zerowym czasem przerwy.

**Wskazówka:** obliczenia czasu wykonuj w sekundach. Na format `HH:MM:SS` przeliczaj wynik dopiero podczas wyświetlania.

### Zadanie 5 — Własna ruletka z saldem i historią gry

Zbuduj konsolową ruletkę europejską z polami od `0` do `36`. Gracz zaczyna z saldem `1000` wirtualnych żetonów i może rozegrać wiele rund.

**Kolory pól:**

- `0` — zielony;
- czerwone pola:

  ```python
  czerwone = {
      1, 3, 5, 7, 9, 12, 14, 16, 18,
      19, 21, 23, 25, 27, 30, 32, 34, 36
  }
  ```

- pozostałe liczby z zakresu `1–36` — czarne.

Kolorów nie wyznaczaj na podstawie parzystości — np. `12` jest czerwone, a `11` czarne.

**Dostępne zakłady:**

| Typ zakładu | Dozwolone typowanie | Warunek wygranej | Wypłata po wygranej |
|---|---|---|---:|
| `liczba` | liczba całkowita `0–36` | dokładne trafienie liczby | `36 * stawka` |
| `kolor` | `czerwony` lub `czarny` | trafienie koloru | `2 * stawka` |
| `parzystosc` | `parzyste` lub `nieparzyste` | trafienie parzystości liczby z zakresu `1–36` | `2 * stawka` |

W jednej rundzie gracz wybiera **jeden** typ zakładu i jedno typowanie. Dla wyniku `0` wszystkie zakłady na kolor i parzystość przegrywają. Na zero można postawić przez zakład typu `liczba`.

**Rozliczanie salda:** najpierw odejmij stawkę, a po losowaniu dodaj wypłatę. Przy przegranej wypłata wynosi `0`. Wypłata obejmuje zwrot postawionej stawki.

```text
saldo_po = saldo_przed - stawka + wyplata
```

Przykład dla salda `1000` i stawki `10`:

- trafienie liczby: `1000 - 10 + 360 = 1350`;
- trafienie koloru: `1000 - 10 + 20 = 1010`;
- przegrana: `1000 - 10 + 0 = 990`.

**Wymagania:**

1. Zdefiniuj funkcję `kolor_liczby(n)`, która dla numeru pola z zakresu `0–36` zwraca `zielony`, `czerwony` albo `czarny`.
2. Zdefiniuj funkcję `oblicz_wyplate(typ_zakladu, typowanie, stawka, wynik)`, która zwraca wypłatę. Dla typu `liczba` typowanie jest liczbą całkowitą; dla pozostałych typów — napisem z tabeli.
3. Zdefiniuj funkcję `ruletka()`, która prowadzi grę w pętli `while`. Przed rundą pokaż saldo i pobierz rodzaj zakładu. Wpisanie `koniec` zamiast rodzaju zakładu ma kończyć sesję.
4. Pobierz typowanie i stawkę. Załóż, że gracz wybiera zakłady i typowania z tabeli oraz podaje dodatnią całkowitą stawkę nieprzekraczającą salda. Odpowiedzi tekstowe sprowadź do małych liter i usuń skrajne spacje.
5. Odejmij stawkę i wylosuj jeden wynik przez `random.randint(0, 36)`. W każdej rozegranej rundzie wykonuj dokładnie jedno losowanie.
6. Wyświetl wylosowaną liczbę, jej kolor, wynik zakładu, wypłatę i nowe saldo. Grę zakończ po wpisaniu `koniec` albo po wyczerpaniu żetonów. Nie dodawaj uzupełniania salda.
7. Na początku sesji utwórz plik `historia_ruletki.tsv` w trybie `w` i zapisz nagłówki: `czas`, `runda`, `typ`, `typowanie`, `stawka`, `wynik`, `kolor`, `wyplata`, `saldo`. Po każdej rozegranej rundzie dopisz jeden wiersz. Numeruj rundy od `1`.
8. Na końcu wyświetl i zapisz do `podsumowanie_ruletki.txt`: liczbę rozegranych rund, liczbę wygranych i przegranych, procent wygranych, saldo końcowe, bilans względem początkowych `1000` żetonów i czas sesji. Czas mierz przez `time.perf_counter()` od pierwszego pytania o rodzaj zakładu do zakończenia gry — obejmuje również namysł gracza.
9. Uwzględnij zakończenie sesji przed pierwszym losowaniem: liczba rund i procent wygranych wynoszą wtedy `0`, a saldo pozostaje równe `1000`.

**Sprawdź funkcje niezależnie od losowań:**

```python
kolor_liczby(0)  # "zielony"
kolor_liczby(12)  # "czerwony"
kolor_liczby(11)  # "czarny"

oblicz_wyplate("liczba", 7, 10, 7)  # 360
oblicz_wyplate("liczba", 0, 10, 0)  # 360
oblicz_wyplate("kolor", "czarny", 10, 11)  # 20
oblicz_wyplate("kolor", "czerwony", 10, 11)  # 0
oblicz_wyplate("parzystosc", "parzyste", 10, 12)  # 20
oblicz_wyplate("parzystosc", "parzyste", 10, 0)  # 0
```

Sprawdź także stawkę równą całemu saldu i zakończenie gry bez rozegrania rundy. Nie zmieniaj zasad rozliczania po zobaczeniu wylosowanego wyniku.

---

## 8. Punktacja

| Zadanie | Punkty |
|---|---:|
| 1 — Raport z pomiarów | 1 |
| 2 — Analiza białka z FASTA | 1 |
| 3 — Monte Carlo i liczba π | 1 |
| 4 — Minutnik interwałowy | 1 |
| 5 — Własna ruletka | 1 |
| **Razem** | **5** |

Każde zadanie jest oceniane pod kątem poprawności obliczeń, realizacji wymagań, podziału na funkcje oraz poprawnego odczytu lub zapisu plików.

---

## 9. Podsumowanie i dokumentacja

Po wykonaniu ćwiczenia powinieneś potrafić pobierać dane użytkownika, przetwarzać pliki tekstowe, tworzyć raporty, wykonywać obliczenia z `math`, budować symulacje z `random` oraz mierzyć i kontrolować czas przez `time`. Poznane wcześniej funkcje, pętle i kolekcje pozwalają połączyć te operacje w większy program.

Dokumentacja biblioteki standardowej:

- [Funkcje wbudowane: m.in. `input()`, `print()`, `open()` i `enumerate()`](https://docs.python.org/3/library/functions.html)
- [`math` — funkcje i stałe matematyczne](https://docs.python.org/3/library/math.html)
- [`random` — generowanie liczb pseudolosowych](https://docs.python.org/3/library/random.html)
- [`time` — czas, opóźnienia i pomiary](https://docs.python.org/3/library/time.html)
