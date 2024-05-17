import random
choice = ['Stone', 'Paper', 'Scissor']
c=1
score = 0
while c==1 :
    computer_choice = random.choice(choice)
    b=computer_choice.lower()
    print('''Choice one option : 
1. Stone
2. Paper 
3. Scissor''')
    your_choice = input("Enter your Choice : ")
    a = your_choice.lower()

    if a == b :
        print("Tie !!!")
    
    if a == 'stone' and b == 'paper' :
        print("Computer win !!!")
    
    if a == 'stone' and b == 'scissor' :
        print("You win !!!")
        score= score+1
    
    if a == 'paper' and b == 'scissor' :
        print("Computer win !!!")
    
    if a == 'paper' and b == 'stone' :
        print("You win !!!")
        score= score+1
    
    if a == 'scissor' and b == 'stone' :
        print("Computer win !!!")
    
    if a == 'scissor' and b == 'paper' :
        print("You win !!!")
        score= score+1
    
    print("Computer choice : " + computer_choice)
    print("Your score : ")
    print(score)
    c = int(input("You want to continue(0/1) : "))
