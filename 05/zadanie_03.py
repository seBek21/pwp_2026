# Zadanie 3 — Kalendarz wydarzeń
#
# Napisz funkcję przyjmującą listę par (nazwa, data). Każda data jest
# napisem w formacie RRRR-MM-DD GG:MM.
#
# 1. Zamień napisy na obiekty datetime i posortuj wydarzenia rosnąco
#    według daty i godziny.
# 2. Dla każdego wydarzenia podaj nazwę, sformatowaną datę z godziną
#    oraz liczbę dni kalendarzowych do terminu.
# 3. Zaprezentuj działanie funkcji na liście zawierającej co najmniej
#    dwa wydarzenia w kolejności innej niż chronologiczna. Dla
#    minionych terminów możesz dodać komunikat „wydarzenie minęło”.
#
# Przykładowe dane wejściowe:
#
#     wydarzenia = [
#         ("Spotkanie", "2027-01-12 19:00"),
#         ("Seminarium", "2027-01-09 10:30"),
#     ]
#
# Przy dacie odniesienia 07.01.2027 przykładowy wynik wygląda tak:
#
#     Seminarium — 09.01.2027 10:30 (za 2 dni)
#     Spotkanie — 12.01.2027 19:00 (za 5 dni)

# Rozwiązanie:
