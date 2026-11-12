# Zadanie 2 — Analiza plików FASTA
#
# Napisz skrypt, który za pomocą input() prosi użytkownika o ścieżkę
# do katalogu z plikami .fasta.
#
# 1. Odczytaj każdy plik .fasta z podanego katalogu. Przyjmij, że
#    poprawny plik zawiera jeden niepusty rekord z sekwencją DNA
#    złożoną z liter A, T, C, G. Uwzględnij również małe litery.
# 2. Oblicz długość sekwencji i liczbę wystąpień każdego z czterech
#    nukleotydów.
# 3. W katalogu wyniki/ zapisz osobny raport dla każdej sekwencji.
#    Jako nazwy pliku użyj identyfikatora (pierwszego słowa po >)
#    i rozszerzenia .txt. Przyjmij, że identyfikatory są unikalne
#    i nadają się na nazwy plików.
# 4. Obsłuż FileNotFoundError, gdy katalog wejściowy nie istnieje.
#    Dla niepoprawnego rekordu zgłoś ValueError, wypisz nazwę pliku
#    i przejdź do następnego.
#
# Do prób możesz użyć katalogu sekwencje/ z materiałów kursu lub
# zapisać poniższy rekord jako plik proba_01.fasta:
#
#     >proba_01
#     ACGT
#     AAGC
#
# Przykładowy raport wyniki/proba_01.txt:
#
#     Długość: 8
#     A: 3
#     T: 1
#     C: 2
#     G: 2

# Rozwiązanie:
