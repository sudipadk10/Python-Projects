#Rock Paper Scissers 

import random
item = ['Rock','Paper','Scissers']

def main():
    Bot = random.choice(item)
    print("\n Rock Paper Scissers ")
    player = input("Enter your choice : ")
    print("Bot :"+Bot)
    if player == Bot:
        print("It's a tie!")
    else:
        if player == 'Rock':
            if Bot == 'Paper':
                print("Bot Won")

            else :
                print("You Won !!!")
            
        elif player == 'Paper':
            if Bot == 'Rock':
                print("You won !!!")
            else :
                print("Bot Won")
        elif player == 'Scissorrs':
            if Bot == 'Paper':
                print("You won !!!")
            else :
                print("Bot Won")
        else:
            print("Wrong input.")

        
if __name__ == '__main__':
  while(True):
    main()
    input()
    print("1.Play Again 2.Quit")
    choice=int(input("Enter 1 or 2 :"))
    if choice == 1:
        continue
    else:
        break   