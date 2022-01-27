import random

class dealer:
    def __init__(self):
        self.value=random.randint(1,13)
        self.score = 500

class Director:
    def __init__(self):
        self.guess = ''
        self.card = 0
        self.next_card = dealer().value
        self.is_playing = True
        self.score = dealer().score
    def start_game(self):
        while self.is_playing:
            self.print_initials()
            self.guess_card()
            self.display_new_card()
            self.score_updates()
            self.do_outputs()
            self.done()
    def print_initials(self):

        card1= self.next_card
        self.card = card1
        print(f"Your card is {card1}")
    
    def guess_card(self):
        user_guess = input("Higher or lower? [h/l]")
        self.guess= user_guess

       
    def score_updates(self):
        if not self.is_playing:
            return 
        if (int(self.card)>int(self.next_card) and self.guess.lower() == "h") or (int(self.card)<int(self.next_card) and self.guess.lower() == "l"):
            self.score -=75
        elif (int(self.card)==int(self.next_card)):
            self.score -=75
        else:
            self.score+=100
    def display_new_card(self):
        card2=dealer().value
        self.next_card=card2
        print(f"The card is {card2}")
    def do_outputs(self):
        if not self.is_playing:
            return
        print(f"Your score is: {self.score}")
        self.is_playing == (self.score > 0)
    def done(self):
        deal_card = input("Deal card? [y/n]")
        self.is_playing = (deal_card == "y")

director = Director()
director.start_game()



