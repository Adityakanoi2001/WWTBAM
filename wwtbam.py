from time import sleep
from random import randint

status = "on"
money = 0
help_score = 2
jokers = ["A) The 50/50", "B) The Audience", "C) The Telephone"]

def ask_question(question, answers, correct, amount, audience, phone):
  print(question)
  for answer in answers:
    print(answer)
    sleep(1)
  user_answer = input("What is your answer ?(A-D or J for lifeline) ")
  if user_answer.upper() == "J":
    use_joker(correct, amount, audience, phone)
  elif user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)   
  else:
    global help_score
    if help_score > 0:
      help()
      for answer in answers:
        print(answer)
        sleep(1)
      user_answer2 = input("What is your answer ?(A-D or J for lifeline) ")
      if user_answer2.upper() == "J":
        use_joker(correct, amount, audience, phone)
      elif user_answer2.upper() == correct:
        print(" ")
        correct_answer(amount)
        sleep(2)
      else:
        print(" ")
        game_over()
    else:
      print(" ")
      game_over()

def correct_answer(amount):
  sleep(1)
  print("That is...")
  sleep(1)
  print("CORRECT!!")
  print(" ")  
  global money
  money = amount
  print(" ")
  sleep(1)
  print(f"Very well done {name}, you just won",chr(8377),f"{money}!")
  print(" ")

def use_joker(correct, amount, audience, phone):
  print(" ")  
  global jokers
  if len(jokers) == 0:
    print("Sorry, you have no lifeline left!")
    user_answer = input("What is your answer? ")
    if user_answer.upper() == correct:
      print(" ")
      correct_answer(amount)
    else:
      print(" ")
      game_over()    
  else:    
    print("You have the following lifelines:")
    for joker in jokers:
      print(f"{joker}")
    joker_selection = input("Which lifeline would you like to use?")
    if joker_selection.upper() == "A":
      jokers.remove("A) The 50/50")
      jokerA(correct, amount)
    elif joker_selection.upper() == "B":
      jokers.remove("B) The Audience")
      jokerB(correct, amount, audience)
    elif joker_selection.upper() == "C":
      jokers.remove("C) The Telephone")
      jokerC(correct,amount,phone)

def jokerA(correct, amount):
  answers = ["A", "B", "C", "D"]
  joker_answer = [correct]  
  answers.remove(correct)
  number = randint(0, 2)
  joker_answer.append(answers[number])
  joker_answer.sort()
  print(".")
  print("..")
  print("...")  
  print(f"The remaining answers are {joker_answer[0]} and {joker_answer[1]}")
  user_answer = input("What is your answer? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
  else:
    print(" ")
    game_over()

def jokerB(correct, amount, audience):
  print(".")
  print("..")
  print("...")
  print(f"The audience vote is: {audience}")
  sleep(3)
  user_answer = input("What is your answer? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
    sleep(2)
  else:
    print(" ")
    game_over()

def jokerC(correct, amount, phone):
  print(".")
  print("..")
  print("...")
  print(f"Here is what your Telephone Friend said:")
  print(phone)
  user_answer = input("What is your answer? ")
  if user_answer.upper() == correct:
    print(" ")
    correct_answer(amount)
  else:
    print(" ")
    game_over()

def help():
  global help_score
  help_score -= 1
  print(" ")
  print("...are you SURE that is correct?")
  print("again the possibilities are:")
def game_over():
  global status
  status = "off"
  print("That is...")
  print("wrong!")
  print(" ")
  print(f"sorry {name}, you lost!")
  print(" ")
  print(" ")
  print("GAME OVER!")

question1 = "FIRST QUESTION for 50",chr(8377),"Who is known as \"Father of Nation\" in India ?"
answers1 = ["A)Netaji Subash Chandra Bose", "B)Pandit Jawaharlal Nehru", "C)Sarder Vallabbhai Patel", "D)Mahatama Gandhi"]
correct1 = "D"
amount1 = 50
audience1 = ["A: 0%", "B: 2%", "C: 0%", "D: 98%"]
phone1 = "Ya its pretty simple I am sure the answer is D - Gandhi!!"

question2 = "THE 100",chr(8377),"Which district Jog Falls is located?"
answers2 = ["A) Kannur", "B) Shivmoga", "C) Mysore", "D) Shimla"]
correct2 = "B"
amount2 = 100
audience2 = ["A: 2%", "B: 95%", "C: 2%", "D: 1%"]
phone2 = "Im sure the answer is B,yes its in shivmoga,karnataka !"

question3 = "NOW THE 200",chr(8377),"QUESTION: In India,GST stands for ...?"
answers3 = ["A) Goods and Service Transaction ", "B) Goods and Service Total ", "C) Goods and Service Tax", "D) Goverment and Service Tax"]
correct3 = "C"
amount3 = 200
audience3 = ["A: 15%", "B: 10%", "C: 75%", "D: 0%"]
phone3 = "Oh, umm, isn't it C? I think it is C. Yes,Goods and Service Tax probably!"

question4 = "OUR 300",chr(8377),"QUESTION:In 2008, Rajasthan Royals became the first winner of which annual sporting event?"
answers4 = ["A) PSL", "B) BPL", "C) IPL", "D) BBL"]
correct4 = "C"
amount4 = 300
audience4 = ["A: 28%", "B: 3%", "C: 68%", "D: 1%"]
phone4 = "Well... IPL mostly thats where Rajastahn Royal play, so C right?"

question5 = "THE 500",chr(8377),"QUESTION: Which river flows through the capital of India?"
answers5 = ["A) Ganga", "B) Kaveri", "C) Tapi", "D) Yamuna"]
correct5 = "D"
amount5 = 500
audience5 = ["A: 21%", "B: 12%", "C: 19%", "D: 48%"]
phone5 = "Oh, a play on words... is it A or D? I think D."

question6 = "1,000",chr(8377)," QUESTION: The purity of which of these is normally measured in carats or karats?"
answers6 = ["A) Gold", "B) Aluminium", "C) Silver", "D) Platinum"]
correct6 = "A"
amount6 = 1000
audience6 = ["A: 58%", "B: 4%", "C: 21%", "D: 17%"]
phone6 = "I know that karats are used...I don't know what they are though... go with A!"

question7 = "OUR 2,000",chr(8377)," QUESTION: Which of these is a character from ‘The Thousand and One Nights’?"
answers7 = ["A) Tintin", "B) Baba Yaga", "C) Othello", "D) Alladin"]
correct7 = "D"
amount7 = 2000
audience7 = ["A: 4%", "B: 3%", "C: 11%", "D: 82%"]
phone7 = "It is his most famous Stories! The answer is D!"

question8 = "NEXT, THE 4,000",chr(8377)," QUESTION: In which country would you expect to be greeted with the word 'bonjour'?"
answers8 = ["A) France", "B) Italy", "C) Spain", "D) Wales"]
correct8 = "A"
amount8 = 4000
audience8 = ["A: 72%", "B: 12%", "C: 14%", "D: 2%"]
phone8 = "Isn't that french? So A should be the answer, right?"

question9 = "OUR 8,000",chr(8377)," QUESTION: Without whose consent can a bill passed by Parliament not be law in India?"
answers9 = ["A) Preident", "B) Vice-President", "C) Prime Minister", "D) Governor"]
correct9 = "A"
amount9 = 8000
audience9 = ["A: 48%", "B: 38%", "C: 14%", "D: 0%"]
phone9 = "It is either A or B, I am not sure though..."

question10 = "NOW FOR 16,000",chr(8377),"QUESTION: What are Jaguar, Mirage and MiG names of?"
answers10 = ["A)Nucler Missiles ", "B)Rocket Launchers ", "C)Fighter Jets ", "D)Bulletproof Cars "]
correct10 = "C"
amount10 = 16000
audience10 = ["A: 15%", "B: 8%", "C: 77%", "D: 0%"]
phone10 = "umm...its somthing with Air Force,I think: try C!"

question11 = "32,000",chr(8377)," FOR THIS ONE: When was ‘Jana Gana Mana’ officially adopted as our National Anthem?"
answers11 = ["A) 1947 ", "B) 1975 ", "C) 1950 ", "D) 1949"]
correct11 = "C"
amount11 = 32000
audience11 = ["A: 17%", "B: 42%", "C: 39%", "D: 2%"]
phone11 = "Ohh... I don't know if it is D or C. Definately not B."

question12 = "THE 64,000",chr(8377)," QUESTION: Which capital city do Heathrow and Gatwick airports serve?"
answers12 = ["A) Tokyo", "B) Rio de Janero", "C) London", "D) Washington D.C"]
correct12 = "C"
amount12 = 64000
audience12 = ["A: 19%", "B: 26%", "C: 28%", "D: 27%"]
phone12 = "I am terribly sorry but I have no idea."

question13 = "125,000",chr(8377)," QUESTION: According to WHO, which of these diseases has been completely eradicated?"
answers13 = ["A) Small Pox", "B) Chicken Pox", "C) Influenza", "D) Tuberculosis"]
correct13 = "A"
amount13 = 125000
audience13 = ["A: 38%", "B: 16%", "C: 21%", "D: 15%"]
phone13 = "I have no idea but B,C,D are very common so it might be A ... Small pox probably"

question14 = "OUR 500,000",chr(8377)," QUESTION:Which Indian ruler sent a Buddhist missionary to Ceylon in 251 BC?"
answers14 = ["A) Chanadragupt Maurya", "B) Chatrapati Shivaji Maharaj", "C) Vikramaditya", "D) Ashok - The great"]
correct14 = "D"
amount14 = 500000
audience14 = ["A: 9%", "B: 31%", "C: 11%", "D: 49%"]
phone14 = "I thinks its C or D but not sure i am not good in history much."

question15 = "AND NOW: THE FINAL 1,000,000",chr(8377)," QUESTION!!!!! Which district of Assam became part of Pakistan after the 1947 plebiscite?"
answers15 = ["A) Tinsukia", "B) Sylhet", "C) Lohit", "D) Dibhang"]
correct15 = "B"
amount15 = 1000000
audience15 = ["A: 32%", "B: 29%", "C: 28%", "D: 11%"]
phone15 = "I have absolutely no clue! But wait,i think it might be B, can it? How many people live on the earth?!"
print(" ")
print("Ladies and Gentlemen!")
print("Welcome to a new round of")
print(" ")
sleep(0.5)
print("WHO")
print("WANTS")
print("TO")
print("BE")
print("A")
print("MILLIONAIRE?!")
print(" ")
sleep(1.3)

print("OUR FIRST CANDIDATE TONIGHT IS ....")
print(" ")
name = input("What is your name? - Enter your name :")
print(" ")
sleep(1.0)
print(f"Everyone, a BIG ROUND OF APPLAUSE FOR OUR CANDIDATE {name.upper()}!")
print(" ")

print("ok, let's get started. First a reminder, you have 3 Lifelines:")
sleep(2)
for joker in jokers:
  print(f"{joker}-Lifeline")
  sleep(1.5)
print("You can only use ONE lifeline for each question.")
sleep(2.5)
print(" ")
print(" ")
print("OK, let's go!")
print(" ")
print(" ")
sleep(1.5)

ask_question(question1, answers1, correct1, amount1, audience1, phone1)

if status == "on":
  ask_question(question2, answers2, correct2, amount2, audience2, phone2)

if status == "on":
  ask_question(question3, answers3, correct3, amount3, audience3, phone3)

if status == "on":
  ask_question(question4, answers4, correct4, amount4, audience4, phone4)

if status == "on":
  ask_question(question5, answers5, correct5, amount5, audience5, phone5)

if status == "on":
  ask_question(question6, answers6, correct6, amount6, audience6, phone6)

if status == "on":
  ask_question(question7, answers7, correct7, amount7, audience7, phone7)

if status == "on":
  ask_question(question8, answers8, correct8, amount8, audience8, phone8)

if status == "on":
  ask_question(question9, answers9, correct9, amount9, audience9, phone9)

if status == "on":
  ask_question(question10, answers10, correct10, amount10, audience10, phone10)

if status == "on":
  ask_question(question11, answers11, correct11, amount11, audience11, phone11)

if status == "on":
  ask_question(question12, answers12, correct12, amount12, audience12, phone12)

if status == "on":
  ask_question(question13, answers13, correct13, amount13, audience13, phone13)

if status == "on":
  ask_question(question14, answers14, correct14, amount14, audience14, phone14)

if status == "on":
  ask_question(question15, answers15, correct15, amount15, audience15, phone15)

if status == "on":
  print("CONGRATULAAAAAAAAAAAAATIONS!!!!!!")
  sleep(2)
  print(" ")
  print("YOU ARE THE WINNER OF ")
  sleep(2)
  print("ONE")
  sleep(1)
  print("MILLION!!")
  sleep(1)
  print("DOLLARS!!!!!!!!!!!!!!!!")
  print(" ")
  print(" ")
  sleep(2)
  print("OUR LATEST MEMBER IN THE ALL TIME HALL OF FAME...")
  print(" ")
  sleep(3)
  print("IS...")
  print(" ")
  sleep(1.5)
  print("THE UNFORGETABLE NEW MILLIONAIRE: ")
  print(" ")
  sleep(3)
  print(f"{name.upper()}!!!")
  sleep(1.5)
  print(f"*incredibly loud applause and cheering*")
  sleep(1.5)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print(f"   {name.upper()}!!!")
  sleep(1)
  print("   ...")
  sleep(3)
  print(" ")
  print(" ")
  print(" ")
  print("THE END")





