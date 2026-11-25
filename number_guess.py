import random 
secret = random.randint(1,100)
while True:
    choice = input("What's your level 'Easy' or 'Hard'.\n").lower()
    if choice == 'easy': 
        attempt = 10 
        break
    elif choice == 'hard':
        attempt = 5
        break
    else: print("Please follow instructions") 
    

eligible = True
while True:
    guess = int(input("Make a guess Between 1-100\n"))
    if guess == secret:
        print("Yeah That is correct You Win!!!")
        break
    if guess > secret:
        attempt -= 1
        print("Yeah You Manage To Close But Still Your NO. Is TOO BIG!!")
        print(f"Attempt Left {attempt}")
    elif guess < secret:
        attempt -= 1
        print("Yeah You Manage To Close But Still Your NO. Is TOO SMALL!!")
        print(f"Attempt Left {attempt}")
    if attempt == 0:
        print(f"You fail to guess correct answer But here is The Secret No. {secret}")
        eligible = False
        break