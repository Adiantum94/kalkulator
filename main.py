import logging
logging.basicConfig(level=logging.DEBUG)

operation_text = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
ingredient1_text = ''
while ingredient1_text is not float:
  try:
    ingredient1_text = float(input("Podaj składnik 1. "))
    break
  except ValueError:
    print('Podana wartość nie jest liczbą')

ingredient2_text = ''
while ingredient2_text is not float:
  try:
    ingredient2_text = float(input("Podaj składnik 2. "))
    break
  except ValueError:
    print('Podana wartość nie jest liczbą')

logging.debug("The program was called with this parameters %s, %s, %s" % (operation_text, ingredient1_text, ingredient2_text))
logging.debug("First parameter is %s" % operation_text)

if operation_text == '1':
  result = ingredient1_text + ingredient2_text
  logging.info(f"Dodaję {ingredient1_text} i {ingredient2_text}")
  print(f"Twój wynik to {result}")

elif operation_text == '2':
  result = ingredient1_text - ingredient2_text
  logging.info(f"Odejmuję {ingredient2_text} od {ingredient1_text}")
  print(f"Twój wynik to {result}")
   
elif operation_text == '3':
  result = ingredient1_text * ingredient2_text
  logging.info(f"Mnożę {ingredient1_text} i {ingredient2_text}")
  print(f"Twój wynik to {result}")

elif operation_text == '4':
  result = ingredient1_text / ingredient2_text
  logging.info(f"Dzielę {ingredient1_text} przez {ingredient2_text}")
  print(f"Twój wynik to {result}")

else:
  print("Nie ma takiego działania!")
  exit(1)


    