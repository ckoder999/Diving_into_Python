import random

#number = 43
number = random.randint(0, 101)
while True:
   answer = input("Введите число ")

   if not answer or answer == "exit":
        break

   if not answer.isdigit():
       print("Введите норм. число")
       continue

   user_answer = int(answer)

   if user_answer < number:
       print("Число меньше")
       continue
   elif user_answer > number:
       print("Число больше")
       continue
   else:
       print("Вы угадали!")
       break