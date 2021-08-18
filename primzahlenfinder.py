#! usr/bin/python
i = 2
n = 0
try:
    n = int(input('Zu prüfende Zahl: '))
except ValueError:
    print('Nur Zahlen sind möglich!')
except NameError:
    print('Nur Zahlen sind erlaubt!')

def istPrim(n):
    if n < 2:
        return False, print('Kann keine Primzahl sein!')
    for i in range(2, n):
        if n % i == 0:
            return False, print(False)
        return True, print(True)


istPrim(n)