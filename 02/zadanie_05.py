# Zadanie 5 — Prosty analizator sekwencji DNA
#
# Napisz program analizujący skład nukleotydowy sekwencji DNA.
# Poprawna sekwencja jest niepusta i zawiera tylko A, T, G, C
# (dopuszczalne są również małe litery).
#
# 1. Zdefiniuj funkcję poprawna_sekwencja(dna) zwracającą True/False.
# 2. Jeśli sekwencja jest niepoprawna, wypisz komunikat i zakończ analizę.
# 3. Zdefiniuj funkcję licz_nukleotyd(dna, nukleotyd), która za pomocą
#    pętli zlicza wystąpienia wskazanego nukleotydu.
# 4. Wypisz długość sekwencji i liczby wystąpień A, T, G, C.
# 5. Zdefiniuj funkcję gc_percent(dna), zwracającą procent G i C.
# 6. Wyświetl klasyfikację: poniżej 40% — "niskie GC";
#    od 40% do 60% włącznie — "średnie GC"; powyżej 60% — "wysokie GC".
#
# Przykład: ATGCGC -> długość 6, GC około 66.67%.
# Zliczaj za pomocą pętli, bez metody count().

# Rozwiązanie:

