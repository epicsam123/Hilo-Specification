
def Input(input_message, expected_variable_type="any", options_available=None, Lower_Range=None, Upper_Range=None, case_sensitive=False):
    """
    Function purpose: A custom-made input function that avoids exceptions.

    Parameters:
    input_message - the message for the computer to print asking for the variable.
    expected_variable_type - str: looks for either a "string", "integer", or "any".
    options_available - tuple (,): look and see if the variable equals any of the expected options
    case_sensitive - Bool (default is False)
    """
    import re
    def Check_data_type():
        while True:
            users_variable = input(input_message)
            if expected_variable_type == "any":
                return users_variable
            elif expected_variable_type == "string":
                try:
                    users_variable = int(users_variable)
                    pass
                except ValueError:
                    return users_variable
            elif expected_variable_type == "integer":
                try:
                    users_variable = int(users_variable)
                    return users_variable
                except ValueError:
                    pass
            else:
                print("\nUser error: Incorrect argument\n")
                break
            print(f"\nWrong data type. Expected a(n) {expected_variable_type}.\n")
            
    def Check_options(users_variable):
        case_sensitive_statement = ""
        String = False
        try:
            test_for_string = users_variable + 34
        except TypeError:
            String = True
        if options_available != None: # looking for specific answer
            for option in options_available:
                if case_sensitive == False and String == True:
                    if option.lower() == users_variable.lower():
                        return users_variable
                else:
                    if users_variable == option:
                        return users_variable
            options_available_print = str(options_available)
            options_available_print = re.sub('[()\']', '', options_available_print) #Gets rid of ()'
            if String == True and case_sensitive == True:
                case_sensitive_statement = " (case sensitive)"
            print(f"\nExpected a specific answer{case_sensitive_statement}. Please choose from among the following list: {options_available_print}\n")
            return None # specific answer not found
        elif Upper_Range != None or Lower_Range != None:
            if Upper_Range == None:
                if users_variable >= Lower_Range:
                    return users_variable
                else:
                    print(f"\nNumber not in range. Please enter a number at or above {Lower_Range}.\n")

            elif Lower_Range == None:
                if users_variable <= Upper_Range:
                    return users_variable
                else:
                    print(f"\nNumber not in range. Please enter a number at or below {Upper_Range}.\n")
            else: #two ranges
                if Lower_Range <= users_variable <= Upper_Range:
                    return users_variable
                else:
                    print(f"\nNumber not in range. Please enter a number between {Lower_Range} and {Upper_Range}.\n")
        else:
            return users_variable # not looking for specific answer

            
    variable_to_output = None

    while variable_to_output == None:
        variable_to_output = Check_options(Check_data_type())
    
    return variable_to_output

import random

class Dealer:
    def __init__(self, lower_range, upper_range):
        self.lower_range = lower_range
        self.upper_range = upper_range

    def return_new_card(self):
        return random.randint(self.lower_range, self.upper_range)

class Director:
    def __init__(self, score, dealer): # A director knows a dealer
        self.dealer = dealer
        self.guess = ''
        self.current_card = 0
        self.next_card = self.dealer.return_new_card()
        self.is_playing = True
        self.score = score
        
    def start_game(self):
        print(f"Welcome to hilo! Your starting score is {self.score}")
        while self.is_playing:
            self.print_initials()
            self.guess_card()
            self.display_new_card()
            self.score_updates()
            self.do_outputs()
            self.done()
    
            
    def print_initials(self):
        card1 = self.next_card
        self.current_card = card1
        print(f"Your card is {card1}")
    
    def guess_card(self):
        user_guess = Input("Higher or lower? [h/l] ", "string", options_available=('h','l'))
        self.guess= user_guess

    def score_updates(self):
        if not self.is_playing:
            return 
        if (int(self.current_card)>int(self.next_card) and self.guess.lower() == "h") or\
            (int(self.current_card)<int(self.next_card) and self.guess.lower() == "l"):
            self.score -= 75
        elif (int(self.current_card)==int(self.next_card)):
            self.score -= 75
        else:
            self.score += 100
            
    def display_new_card(self):
        card2 = self.dealer.return_new_card()
        self.next_card = card2
        print(f"The card is {card2}")
        
    def do_outputs(self):
        print(f"Your score is: {self.score}")
        self.is_playing = (self.score > 0) # Involuntary game over
        
    def done(self):
        if not self.is_playing:
            return
        deal_card = Input("Deal card? [y/n] ", "string", options_available=('y','n'))
        self.is_playing = (deal_card == "y") # Voluntary game over

