# Ćwiczenie 2 — Instrukcje warunkowe, pętle, definiowanie funkcji

## Cel ćwiczeń

Celem ćwiczeń jest poznanie mechanizmów sterowania przebiegiem programu oraz samodzielnego definiowania funkcji. Po zakończeniu zajęć student powinien potrafić budować programy, które podejmują decyzje, powtarzają operacje i dzielą rozwiązanie na mniejsze, wielokrotnie wykorzystywane fragmenty.

## Zakres materiału

- instrukcje warunkowe `if`, `elif`, `else` i ich zagnieżdżanie;
- operatory porównania oraz operatory logiczne w warunkach;
- pętle `for` i `while`;
- funkcja `range()`;
- instrukcje `break` i `continue`;
- zagnieżdżanie pętli;
- definiowanie funkcji przez `def`;
- parametry, argumenty i wartości domyślne;
- zwracanie wyników przez `return`;
- zakres zmiennych: lokalne i globalne;
- łączenie instrukcji warunkowych, pętli i funkcji.

**Wymagania wstępne:** zmienne, podstawowe typy danych, konwersja typów, operatory arytmetyczne, porównania i logiczne, `print()` oraz `input()` (ćwiczenia 01).

---

> **Jak korzystać z instrukcji:** uruchamiaj przykłady samodzielnie, zmieniaj wartości zmiennych i obserwuj wyniki. Przykłady nie są rozwiązaniami zadań.

---

## 1. Instrukcje warunkowe

Instrukcje warunkowe pozwalają wykonać różne działania w zależności od tego, czy dany warunek ma wartość `True`, czy `False`.

### 1.1. `if`, `elif`, `else`

- `if` sprawdza pierwszy warunek.
- `elif` sprawdza kolejny warunek, jeżeli wcześniejsze nie zostały spełnione.
- `else` określa działanie, gdy żaden wcześniejszy warunek nie został spełniony.

Warunki są sprawdzane kolejno; w jednym łańcuchu `if`–`elif`–`else` wykonywana jest co najwyżej jedna gałąź. Pamiętaj o dwukropku po nagłówku instrukcji i konsekwentnych wcięciach.

**Przykład — ocena wyniku:**

```python
punkty = 72

if punkty >= 90:
    print("Bardzo dobry wynik")
elif punkty >= 50:
    print("Wynik zaliczający")
else:
    print("Wynik niezaliczający")
```

Dla `punkty = 72` program wypisze `Wynik zaliczający`. Zwróć uwagę na kolejność sprawdzania warunków.

### 1.2. Warunki złożone

Do łączenia warunków służą `and`, `or` oraz `not`. Przy konstruowaniu warunków warto uwzględnić przypadki graniczne: równość, zero, wartości ujemne oraz sytuacje, w których żaden z warunków nie zachodzi.

**Przykład — kilka kryteriów jednocześnie:**

```python
wiek = 20
ma_legitymacje = True

if wiek < 26 and ma_legitymacje:
    print("Przysługuje zniżka")

if wiek < 18 or wiek >= 65:
    print("Należy sprawdzić dodatkowe uprawnienia")

if not ma_legitymacje:
    print("Brak legitymacji")
```

`and` wymaga spełnienia obu warunków, `or` co najmniej jednego, a `not` odwraca wartość logiczną.

### 1.3. Zagnieżdżanie warunków

Instrukcję warunkową można umieścić wewnątrz innej. Stosuj takie rozwiązanie, gdy drugi test ma sens dopiero po spełnieniu pierwszego.

**Do sprawdzenia:** czym różnią się dwa niezależne bloki `if` od jednego łańcucha `if`–`elif`–`else`?

**Przykład — weryfikacja liczby:**

```python
liczba = 12

if liczba > 0:
    if liczba % 2 == 0:
        print("Dodatnia i parzysta")
    else:
        print("Dodatnia i nieparzysta")
else:
    print("Niedodatnia")
```

Warunek wewnętrzny jest sprawdzany wyłącznie wtedy, gdy `liczba > 0`.

---

## 2. Pętle

Pętle pozwalają wielokrotnie wykonać fragment programu bez ręcznego powielania instrukcji.

### 2.1. Pętla `while`

Pętla `while` działa tak długo, jak długo jej warunek pozostaje prawdziwy. Należy zadbać o to, aby warunek mógł w pewnym momencie przestać być spełniony — w przeciwnym razie program może utknąć w pętli nieskończonej.

**Do sprawdzenia:** co się stanie, gdy warunek `while` jest fałszywy już przy pierwszym sprawdzeniu?

**Przykład — odliczanie:**

```python
licznik = 3

while licznik > 0:
    print(licznik)
    licznik -= 1

print("Start!")
```

Program wypisze `3`, `2`, `1`, a następnie `Start!`. Instrukcja `licznik -= 1` zapobiega nieskończonemu wykonywaniu pętli.

### 2.2. Pętla `for` i `range()`

Pętla `for` wykonuje instrukcje dla kolejnych wartości z iterowanego obiektu. Funkcja `range()` pozwala wyznaczyć sekwencję liczb całkowitych na podstawie wartości początkowej, końcowej i kroku.

Pamiętaj, że **wartość końcowa `range()` nie jest uwzględniana**. Krok może być dodatni lub ujemny, ale nie może wynosić zero.

**Przykład — trzy warianty `range()`:**

```python
for i in range(4):
    print(i)  # 0, 1, 2, 3

for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

for i in range(10, 0, -2):
    print(i)  # 10, 8, 6, 4, 2
```

`range(stop)` zaczyna od zera; `range(start, stop, step)` pozwala wskazać początek i krok. `stop` jest wyłączony.

### 2.3. `break` i `continue`

- `break` natychmiast kończy działanie najbliższej otaczającej pętli.
- `continue` pomija pozostałą część bieżącej iteracji i przechodzi do następnej.

W pętli `while` trzeba uważać, aby `continue` nie pomijało aktualizacji zmiennej sterującej.

**Przykład — pomijanie i przerwanie:**

```python
for liczba in range(1, 11):
    if liczba % 2 == 0:
        continue  # pomiń liczby parzyste

    if liczba > 7:
        break  # zakończ pętlę

    print(liczba)
```

Wynik: `1`, `3`, `5`, `7`. `continue` nie kończy całej pętli, w przeciwieństwie do `break`.

### 2.4. Zagnieżdżone pętle

Pętlę można umieścić wewnątrz innej pętli. Każdy przebieg pętli zewnętrznej uruchamia pętlę wewnętrzną. Taka konstrukcja przydaje się m.in. do sprawdzania wszystkich par wartości lub tworzenia tabel.

**Do sprawdzenia:** czym różni się liczba iteracji dwóch pętli następujących po sobie od dwóch pętli zagnieżdżonych?

**Przykład — tabliczka mnożenia 3 × 3:**

```python
for wiersz in range(1, 4):
    for kolumna in range(1, 4):
        print(wiersz * kolumna, end=" ")
    print()  # nowy wiersz
```

Pętla zewnętrzna wykona się trzy razy, a wewnętrzna trzy razy dla każdego jej przebiegu — łącznie dziewięć mnożeń.

---

## 3. Definiowanie funkcji

Funkcje umożliwiają wydzielenie fragmentu programu odpowiedzialnego za konkretne zadanie. Dzięki temu można wywołać tę samą operację wielokrotnie, bez kopiowania jej implementacji.

### 3.1. `def`, parametry i argumenty

Funkcję definiuje się słowem kluczowym `def`. **Parametry** są nazwami podanymi w definicji funkcji, a **argumenty** to wartości przekazywane podczas wywołania.

Parametrom można przypisać wartości domyślne, dzięki czemu odpowiednie argumenty mogą zostać pominięte podczas wywołania.

**Przykład — funkcja z parametrem domyślnym:**

```python
def powitaj(imie, powitanie="Cześć"):
    print(powitanie, imie)

powitaj("Anna")
powitaj("Jan", "Dzień dobry")
```

`imie` i `powitanie` są parametrami funkcji. Napisy `"Anna"` i `"Jan"` są argumentami przekazywanymi podczas wywołania.

### 3.2. `return` a `print()`

- `return` zwraca wynik do miejsca wywołania funkcji i kończy jej wykonywanie.
- `print()` wyświetla informację na ekranie, ale sam w sobie nie zwraca wyniku obliczeń funkcji.

Funkcja bez jawnego `return` zwraca `None`.

**Przykład — wynik obliczeń a jego wyświetlenie:**

```python
def pole_prostokata(a, b):
    return a * b

pole = pole_prostokata(3, 5)
print("Pole:", pole)
```

Funkcja zwraca liczbę `15`, którą można zapisać w zmiennej i wykorzystać w kolejnych obliczeniach. Samo `print()` jedynie ją wyświetla.

### 3.3. Zmienne lokalne i globalne

Zmienne utworzone wewnątrz funkcji są co do zasady lokalne: istnieją w zakresie jej wykonania. Zmienne zdefiniowane poza funkcjami należą do zakresu globalnego. W zadaniach zaleca się przekazywanie danych przez argumenty i zwracanie wyników zamiast modyfikowania zmiennych globalnych.

**Przykład — dwa zakresy zmiennych:**

```python
stawka = 10  # zmienna globalna

def oblicz_koszt(liczba_godzin):
    koszt = liczba_godzin * stawka  # koszt jest lokalny
    return koszt

print(oblicz_koszt(4))  # 40
# print(koszt)  # NameError: zmienna lokalna nie jest dostępna tutaj
```

Funkcja może odczytać zmienną globalną, ale w praktyce lepiej przekazywać potrzebne wartości jako argumenty. Słowo kluczowe `global` umożliwia modyfikację zmiennej globalnej wewnątrz funkcji, lecz w tych ćwiczeniach nie jest potrzebne.

### 3.4. Łączenie funkcji z pętlami i warunkami

Funkcja może zawierać instrukcje warunkowe oraz pętle. Może też wywoływać inne funkcje. W bardziej złożonych zadaniach warto rozdzielić pobieranie danych, obliczenia i prezentację wyników.

**Do sprawdzenia:** dlaczego funkcja, która zwraca wynik, jest łatwiejsza do ponownego wykorzystania niż funkcja, która wyłącznie go wyświetla?

**Przykład — sumowanie dodatnich wartości:**

```python
def suma_dodatnich(liczby):
    wynik = 0
    for liczba in liczby:
        if liczba > 0:
            wynik += liczba
    return wynik

print(suma_dodatnich([3, -2, 5, 0]))  # 8
```

Funkcja łączy pętlę, instrukcję warunkową i `return`. Lista jest tu jedynie przykładowym zbiorem danych — jej szczegółowe operacje nie są wymagane w zadaniach.

---


## 4. Dodatkowe przykłady — od prostych konstrukcji do całych programów

Poniższe przykłady służą do samodzielnego uruchamiania i modyfikowania. Nie są zadaniami do oddania. Warto zmieniać dane wejściowe i przewidywać wyniki przed wykonaniem kodu.

### 4.1. Warunki — granice przedziałów

```python
punkty = 72
if punkty < 0 or punkty > 100:
    print("Niepoprawna liczba punktów")
elif punkty >= 90:
    print("Bardzo dobry")
elif punkty >= 60:
    print("Zaliczone")
else:
    print("Nie zaliczono")
```

Kolejność gałęzi `elif` ma znaczenie. Po spełnieniu pierwszego warunku Python pomija pozostałe.

### 4.2. Warunki — liczba parzysta i dodatnia

```python
n = 18
if n > 0 and n % 2 == 0:
    print("Liczba dodatnia i parzysta")
else:
    print("Nie spełnia obu warunków")
```

### 4.3. Warunki — sprawdzanie nukleotydu

```python
nukleotyd = "G"
if nukleotyd == "A" or nukleotyd == "G":
    print("Puryna")
elif nukleotyd == "C" or nukleotyd == "T":
    print("Pirymidyna")
else:
    print("Nieznany nukleotyd")
```

### 4.4. Warunki zagnieżdżone — ocena danych

```python
wiek = 20
zgoda = True
if wiek >= 18:
    if zgoda:
        print("Można kontynuować")
    else:
        print("Brak zgody")
else:
    print("Wymagana pełnoletność")
```

### 4.5. `for` — różne warianty `range()`

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

for i in range(10, 0, -2):
    print(i)  # 10, 8, 6, 4, 2
```

Górna granica `range()` nie jest uwzględniana.

### 4.6. `for` — sumowanie bez gotowej funkcji

```python
suma = 0
for liczba in range(1, 6):
    suma += liczba
print(suma)  # 15
```

### 4.7. `for` — przechodzenie po sekwencji DNA

```python
dna = "ATGCCA"
for nukleotyd in dna:
    print(nukleotyd)
```

Napisy są iterowalne: pętla odwiedza kolejno każdy znak.

### 4.8. `for` — liczenie wybranego znaku

```python
tekst = "BANAN"
licznik = 0
for znak in tekst:
    if znak == "A":
        licznik += 1
print(licznik)  # 2
```

### 4.9. `while` — licznik i warunek zakończenia

```python
licznik = 1
while licznik <= 5:
    print(licznik)
    licznik += 1
```

W pętli `while` trzeba zadbać o zmianę wartości wpływającej na warunek, aby uniknąć pętli nieskończonej.

### 4.10. `while` — ponawianie pytania

```python
odpowiedz = ""
while odpowiedz != "tak":
    odpowiedz = input("Wpisz 'tak', aby zakończyć: ").lower()
print("Koniec")
```

### 4.11. `break` — zatrzymanie po znalezieniu wartości

```python
for liczba in range(1, 20):
    if liczba % 7 == 0:
        print("Pierwsza wielokrotność 7:", liczba)
        break
```

### 4.12. `continue` — pomijanie elementów

```python
for liczba in range(1, 11):
    if liczba % 2 == 0:
        continue
    print(liczba)  # tylko liczby nieparzyste
```

### 4.13. Zagnieżdżone pętle — pary wartości

```python
for x in range(1, 4):
    for y in range(1, 3):
        print(x, y)
```

Pętla wewnętrzna wykonuje wszystkie iteracje dla każdej iteracji pętli zewnętrznej.

### 4.14. Funkcje — argumenty pozycyjne

```python
def pole_prostokata(a, b):
    return a * b

wynik = pole_prostokata(3, 5)
print(wynik)  # 15
```

### 4.15. Funkcje — argument domyślny

```python
def powitanie(imie, jezyk="pl"):
    if jezyk == "pl":
        return "Cześć, " + imie
    return "Hello, " + imie

print(powitanie("Ala"))
print(powitanie("Ala", "en"))
```

### 4.16. `return` a `print()` — różnica praktyczna

```python
def dodaj(a, b):
    return a + b

def pokaz_sume(a, b):
    print(a + b)

x = dodaj(2, 3)
y = pokaz_sume(2, 3)
print(x)  # 5
print(y)  # None
```

`print()` wyświetla dane, a `return` przekazuje wynik wywołania funkcji do dalszych obliczeń.

### 4.17. Funkcje — wiele wywołań i ponowne wykorzystanie

```python
def celsius_na_kelviny(t):
    return t + 273.15

for temperatura in (0, 20, 37):
    print(temperatura, celsius_na_kelviny(temperatura))
```

### 4.18. Zmienne lokalne — niezależność wywołań

```python
def podwoj(liczba):
    wynik = liczba * 2
    return wynik

print(podwoj(4))
print(podwoj(7))
# print(wynik)  # błąd: zmienna lokalna nie istnieje poza funkcją
```

### 4.19. Zmienne globalne — odczyt a modyfikacja

```python
stawka = 0.23

def cena_brutto(netto):
    return netto * (1 + stawka)

print(cena_brutto(100))
```

Funkcja może odczytać zmienną globalną. Zwykle czytelniej jest jednak przekazać potrzebną wartość jako argument.

### 4.20. Łączenie konstrukcji — wyszukiwanie wartości

```python
def pierwsza_podzielna(przedzial, dzielnik):
    for liczba in range(1, przedzial + 1):
        if liczba % dzielnik == 0:
            return liczba
    return None

print(pierwsza_podzielna(10, 4))  # 4
print(pierwsza_podzielna(3, 4))   # None
```

Instrukcja `return` natychmiast kończy działanie funkcji.

### 4.21. Łączenie konstrukcji — prosty filtr sekwencji

```python
def licz_puryny(sekwencja):
    licznik = 0
    for znak in sekwencja.upper():
        if znak == "A" or znak == "G":
            licznik += 1
    return licznik

print(licz_puryny("ATGCCA"))  # 3
```

### 4.22. Łączenie konstrukcji — wielokrotne obliczenia

```python
def srednia_dodatnich(liczby):
    suma = 0
    ile = 0
    for liczba in liczby:
        if liczba <= 0:
            continue
        suma += liczba
        ile += 1
    if ile == 0:
        return None
    return suma / ile

print(srednia_dodatnich([-2, 2, 4, 6]))  # 4.0
```

### 4.23. Wcięcia i najczęstsze błędy

Wcięcia wyznaczają bloki kodu. Porównaj:

```python
for i in range(3):
    print("W pętli:", i)
print("Po pętli")
```

oraz:

```python
for i in range(3):
    print("W pętli:", i)
    print("Nadal w pętli")
```

Pamiętaj o dwukropku po `if`, `elif`, `else`, `for`, `while` i nagłówku `def`. Do porównania używa się `==`, nie `=`.

---

## 5. Zadania do wykonania

### Zadanie 1 — Klasyfikacja temperatury

Napisz program, który pobiera temperaturę w stopniach Celsjusza i klasyfikuje ją według następujących reguł:

- poniżej `0°C` — „mróz”;
- od `0°C` do poniżej `15°C` — „chłodno”;
- od `15°C` do `25°C` włącznie — „umiarkowanie”;
- powyżej `25°C` — „gorąco”.

Umieść klasyfikację w funkcji `klasyfikuj_temperature(t)`, która **zwraca** odpowiedni napis. Wyświetl wynik poza funkcją.

**Sprawdź:** `-5`, `0`, `14.9`, `15`, `25`, `25.1`.


### Zadanie 2 — Suma liczb spełniających warunek

Napisz funkcję `suma_podzielnych(n, k)`, która oblicza sumę dodatnich liczb całkowitych nie większych niż `n`, podzielnych przez `k`.

- Wykorzystaj `for` i `range()`.
- Sprawdzaj podzielność operatorem `%`.
- Dla `n < 1` lub `k = 0` zwróć `0`.
- Nie korzystaj z gotowego wzoru na sumę ciągu.

**Przykład:** dla `n = 10` i `k = 3` wynik wynosi `18` (`3 + 6 + 9`).



### Zadanie 3 — Analiza liczby pierwszej

Napisz program, który pobiera dwie dodatnie liczby całkowite `a` i `b`, a następnie znajduje wszystkie liczby pierwsze w przedziale domkniętym od `a` do `b`.

**Wymagania:**

1. Zdefiniuj funkcję `czy_pierwsza(n)` zwracającą `True` albo `False`.
2. Zdefiniuj funkcję `policz_pierwsze(a, b)`, która zwraca liczbę liczb pierwszych w zadanym przedziale.
3. W programie głównym wypisz każdą znalezioną liczbę pierwszą oraz ich łączną liczbę.
4. Dla `a > b` wyświetl komunikat o niepoprawnym przedziale.
5. Pamiętaj, że `1` nie jest liczbą pierwszą.

**Przykład:** dla przedziału `10–20` znalezione liczby to `11`, `13`, `17`, `19`, a ich liczba wynosi `4`.

### **Zadanie 4 — Symulacja wzrostu populacji bakterii**

Załóż, że populacja bakterii początkowo liczy `N0` komórek i co godzinę zwiększa się o `p` procent. Napisz program wyznaczający, po ilu **pełnych godzinach** populacja po raz pierwszy osiągnie lub przekroczy zadaną wartość `N_docelowe`.

**Wymagania:**

1. Zdefiniuj zmienne `N0`, `p` i `N_docelowe`, przypisując im odpowiednie wartości.
2. Zdefiniuj funkcję `czas_wzrostu(N0, p, N_docelowe)` zwracającą liczbę godzin.
3. Zastosuj pętlę `while` i aktualizuj liczebność populacji w każdej iteracji.
4. Po każdej godzinie wypisz numer godziny i aktualną liczebność populacji.
5. Dla `N0 >= N_docelowe` zwróć `0`, jeżeli parametry są poprawne.
6. Dla `N0 <= 0`, `p <= 0` lub `N_docelowe <= 0` wyświetl informację o niepoprawnych parametrach.

**Dane przykładowe:**

- `N0 = 100`
- `p = 100`
- `N_docelowe = 800`

**Oczekiwany wynik:**

    Godzina 1: 200 komórek
    Godzina 2: 400 komórek
    Godzina 3: 800 komórek

    Populacja osiągnęła wartość docelową po 3 godzinach.

### Zadanie 5 — Prosty analizator sekwencji DNA

Napisz program, który pobiera od użytkownika sekwencję DNA i analizuje jej skład nukleotydowy. Załóż, że poprawna sekwencja składa się wyłącznie z liter `A`, `T`, `G`, `C` (małe litery również są dopuszczalne).

**Wymagania:**

1. Zdefiniuj funkcję `poprawna_sekwencja(dna)`, która zwraca `True`, jeżeli sekwencja jest niepusta i zawiera wyłącznie dozwolone nukleotydy.
2. Jeżeli sekwencja jest niepoprawna, wypisz komunikat i zakończ analizę.
3. Zdefiniuj funkcję `licz_nukleotyd(dna, nukleotyd)`, która za pomocą pętli zlicza wystąpienia wskazanego nukleotydu.
4. Wypisz długość sekwencji i liczbę wystąpień `A`, `T`, `G` oraz `C`.
5. Zdefiniuj funkcję `gc_percent(dna)`, która zwraca procentową zawartość `G` i `C`.
6. Wyświetl klasyfikację: poniżej `40%` — „niskie GC”, od `40%` do `60%` włącznie — „średnie GC”, powyżej `60%` — „wysokie GC”.

**Przykład:** dla sekwencji `ATGCGC` długość wynosi `6`, a zawartość GC wynosi około `66.67%`.

**Ograniczenie:** zliczanie nukleotydów wykonaj samodzielnie za pomocą pętli; nie używaj metody `count()`.

---

## 6. Punktacja

| Zadanie | Punkty |
|---|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 1 |
| 5 | 1 |
| **Razem** | **5** |

---
