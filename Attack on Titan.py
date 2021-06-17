
import random

#BlackJack Game

suits=("Hearts","Diamond","Spades","Clubs")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

# Card Class

class Card():
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
        self.value=values[ranks]

    def __str__(self):
        return f"{self.suits} of {self.ranks}"

# Deck Class

class Deck():
    def __init__(self):

        self.all_cards=[]

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def pick_one(self):
        return self.all_cards.pop()


#Player Class

class Player():
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def add_card(self,new_card):
        self.all_cards.append(new_card)

    def remove_card(self):
        return self.all_cards.pop()






# LOGIC OF GAME

Player_user=Player("Ivar")
Player_comp=Player("Ragnar")

def game(balance_of_player,balance_of_computer):

    # BALANCE
    """
    try:
        print(f"Balance of Player {balance_of_player}")
        print(f"Balance of Computer {balance_of_computer}")
    except:
        balance_of_player = 100
        balance_of_computer = 200
    """


    bet=20
    game_on=True
    target=0

    Deck_of_Cards=Deck()
    Deck_of_Cards.shuffle()

    i=0
    while i<2:

        Player_comp.add_card(Deck_of_Cards.pick_one())
        Player_user.add_card(Deck_of_Cards.pick_one())
        i=i+1

    print("Player Cards")
    print(Player_user.all_cards[0])
    print(Player_user.all_cards[1])

    print("\nComputer Cards")
    print(Player_comp.all_cards[0])
    print("\n")

    print(f"The user points are {Player_user.all_cards[0].value + Player_user.all_cards[1].value}")
    print(f"The computer points are {Player_comp.all_cards[0].value}")

    condition_one=True
    condition_two=True
    while condition_one:

        amount_of_bet=int(input("Please place ur bet:"))

        if balance_of_player > amount_of_bet :
            condition_two=False

        if condition_two==True:
            print("Your balance is insufficient as per your bet \nPlease re-enter your bet")
        else:
            balance_of_player = balance_of_player - amount_of_bet
            balance_of_computer = balance_of_computer - amount_of_bet
            bet=amount_of_bet
            condition_one=False

        print(f"Your Current Balance is {balance_of_player}\n")

    condition_to_pick=True




    while condition_to_pick:

        sum_of_points = 0
        response = input(" Do You want to pick one more card from the deck\n Then print Yes\n Otherwise No\n")
        print("\n")

        for item in Player_user.all_cards:
            sum_of_points = sum_of_points + item.value

        if response.lower()=="yes":
            Player_user.add_card(Deck_of_Cards.pick_one())
            print("User gets an:")
            print(Player_user.all_cards[-1])

            sum_of_points = sum_of_points + Player_user.all_cards[-1].value

            if Player_user.all_cards[-1].value == 11:
                print("you want to take value of ACE as 1 or 11")
                value=int(input())
                sum_of_points = sum_of_points - 11 + value
            print(f"Player points are {sum_of_points}")

            if sum_of_points > 21 :
                print("\nUser has been lost")
                game_on=False
                break
            elif sum_of_points == 21 :
                print("\nYou have now won blackjack \n Because you have exact 21 points....\nNow you get 150 percent bet return from computer")
                balance_of_player = balance_of_player + (5/2)*(bet)
                balance_of_computer = balance_of_computer - (-1/2)*(bet)
                game_on=False
                break
            else:
                print("\nYour points are still less than 21")
                target=sum_of_points
        else:
            break

    if game_on==False:
        pass
    else:
        print("Computer hidden card is...")
        print(Player_comp.all_cards[-1].value)
        print("\nNow the computer turn is to play\n")
        condition_to_pick_by_computer= True

        sum_of_points_of_comp = 0
        for item in Player_comp.all_cards:
            sum_of_points_of_comp = sum_of_points_of_comp + item.value

        while condition_to_pick_by_computer:

            print("computer pick a card from the deck\n")
            Player_comp.add_card(Deck_of_Cards.pick_one())
            print("computer gets ....\n")
            print(Player_comp.all_cards[-1])

            sum_of_points_of_comp = sum_of_points_of_comp + Player_comp.all_cards[-1].value

            if sum_of_points_of_comp > 21:
                print(" Computer has lost")
                balance_of_computer = balance_of_computer + (2*bet)
                break
            elif sum_of_points_of_comp == 21:
                print("Computer has blackjack the game")
                balance_of_computer = balance_of_computer + (2 * bet)
                break
            elif sum_of_points_of_comp > target:
                print("User has won the game")
                balance_of_player = balance_of_player + (2*bet)
                break
            else:
                print("Computer pick one more card ,to make it close to win")
                continue

    print(f"Balance of User {balance_of_player}")
    print(f"Balance of Computer {balance_of_computer}")

balance_of_player=100
balance_of_computer=200
x=True

while x:
    response=input("Do you want 2 play the game .....\nIf want to continue Type Yes \n Otherwise no\n")
    if response.lower()=="yes":
        game(balance_of_player,balance_of_computer)
    else:
        x=False





