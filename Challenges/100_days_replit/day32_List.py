import random

hello = ["Halo", "Hello", "Hola"]


def acak(number):
    angka = random.randint(0, number)
    return angka


print(hello[acak(2)])
