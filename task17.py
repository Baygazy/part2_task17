privet = input("Write, 'Hello': ")

if privet.lower() == "hello":
    vibor = int(input(
                '\n\tВыберите по номеру:'
                '\n\t1: google_kazakstan'
                '\n\t2: google_paris'
                '\n\t3: google_uar'
                '\n\t4: google_kyrgystan'
                '\n\t5: google_san_francisco'
                '\n\t6: google_germany'
                '\n\t7: google_moscow'
                '\n\t8: google_sweden'
                '\n\t'
                      ))
    laf =       {
                1: 'google_kazakstan.txt',
                2: 'google_paris.txt',
                3: 'google_uar.txt',
                4: 'google_kyrgystan.txt',
                5: 'google_san_francisco.txt',
                6: 'google_germany.txt',
                7: 'google_moscow.txt',
                8: 'google_sweden.txt'
                }
    with open(laf[vibor], "a") as filename:
        filename.write(input("Введите вашу жалобу сюда: ")+"\n")
    print(("Ваша жалоба принята."))
else:
    print("no correct.")
