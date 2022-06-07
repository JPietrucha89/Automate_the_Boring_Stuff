
import string


def PESEL_validation(pesel):
    pesel = str(pesel)
    # lenght and type validation
    if len(pesel) == 11:
        for char in pesel:
            if char.isnumeric() == False:
                print('Nieprawidłowy PESEL')
                return False
    else:
        print('Nieprawidłowy PESEL')
        return False
# gender validation
    # tu w sumie nie potrzeba zadnej walidacji, ale moznaby wyciagnac zmienna gender bo moze sie do czegos przydac
# day validation
    if int(pesel[4:6]) > 31:
        print('Nieprawidłowy PESEL')
        return False
# month validation
    if int(pesel[2:4]) > 32:
        print('Nieprawidłowy PESEL')
        return False
# year validation
    # tutaj tez bez zadnej walidacji, ale moznaby wyciagnac zmienna date_of_birth bo moze sie do czegos przydac
# last digit validation
    multipliers_list = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum = 0
    for i in range(0, len(pesel)-1):
        sum += multipliers_list[i] * int(pesel[i])
    last_digit = 10 - (sum % 10)
    if last_digit != int(pesel[-1]):
        print('Nieprawidłowy PESEL')
        return False
    print('Prawidłowy PESEL')
    return True


# main
PESEL_validation(12345678901)
print()
PESEL_validation(89113006798)
print()
hopefully_proper_pesel = input('Podaj swój PESEL:')
PESEL_validation(hopefully_proper_pesel)
print()
PESEL_validation('89113006798')
print()
PESEL_validation('a2345678901')
