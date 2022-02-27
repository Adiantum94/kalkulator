import logging
logging.basicConfig(level=logging.DEBUG)

operation_text = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
ingredient1_text = input("Podaj składnik 1. ")
ingredient2_text = input("Podaj składnik 2. ")
result = 0

if operation_text == '1':
    result = float(ingredient1_text) + float(ingredient2_text)
    logging.info(f"Dodaję {ingredient1_text} i {ingredient2_text}")
    
elif operation_text == '2':
    result = float(ingredient1_text) - float(ingredient2_text)
    logging.info(f"Odejmuję {ingredient2_text} od {ingredient1_text}")

elif operation_text == '3':
    result = float(ingredient1_text) * float(ingredient2_text)
    logging.info(f"Mnożę {ingredient1_text} i {ingredient2_text}")

elif operation_text == '4':
    result = float(ingredient1_text) / float(ingredient2_text)
    logging.info(f"Dzielę {ingredient1_text} przez {ingredient2_text}")

else:
    print("Nie ma takiego działania!")
    exit(1)

print(f"Twój wynik to {result}")