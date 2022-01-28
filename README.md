# Hilo-Specification
First team activity (team 7) 

Names: Charlie Mitts, James Chan, Spencer Kingsbury, Samuel Casellas

Date: Jan 27th, 2022

# Code Planning

There are two classes for this program:

1. Director
2. Dealer

The following responsibilities, behaviors, and statuses are as follows:

- Director:
1. Responsibilities - Run the game by verifying the conditions of the game are always true before each turn. Keeps track of the players cards and score. Asks the user two questions: if they want another turn and what their guess is for the card (whether higher or lower).

2. Behaviors:
    a. Initiate the game (main): start_game()
    b. Display the card: print_initials()
    c. Ask the player for higher or lower: guess_card()
    d. Add or subtract points: score_updates()
    e. Display the next card: display_new_card() 
    f. Display and test user's score: do_outputs()
    g. Ask the player to play again: done()

3. Status:
    a. Dealer - self.dealer (class)
    a. Player's guess - self.guess (str)
    b. Current card - self.current_card (int)
    c. Next card - self.next_card (int)
    d. Playing? - self.is_playing (bool)
    e. Player's points - dealer.score (int)

- Dealer:
1. Responsibilities - Deals a card to represent a number between 1 and 13.

2. Behavior's:
    a. Retrieve the new card - return_new_card()

3. Status:
    a. Lower range for pulling cards - self.lower_range (int)
    b. Upper range for pulling cards - self.upper_range (int)