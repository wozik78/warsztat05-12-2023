# stworzenie raportu przetworzenie danych dane generowane generatorem
# wykorzystać dokorator do pomiaru czasu operacji
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"czas wykonania funkcji {func.__name__}: {execution_time} sekundy")
        return result

    return wrapper


@measure_time
def generuj_wartosci(dane):
    for i in range(x):
        yield i


def przetworz_dane(dane):
    return [element for element in dane if element % 2 == 0]


def generuj_raport(dane):
    for element in generator_danych(dane):
        print(f"raport dla systemu:{element}")


dane = range(100_000)
pr_dane = przetworz_dane(dane)
generuj_raport(pr_dane)
