import random

MAX_LINES = 3
MAX_BET = 500
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 4,
    "B": 4,
    "C": 4,
    "D": 4
}

symbol_value = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1
}

def check_winnings(columns, lines, bet, values):
    """ See if user won"""
    winnings = 0
    winning_lines = []
    
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            #index value add 1
            
    return winnings, winning_lines
            

def get_slot_machine_spin(rows, cols, symbols):
    """ Generate slot machine values """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # Key and Value
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
            #mutation vs rebinding
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    """ Transpose results """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()
        # add line after reach row

def deposit():
    """ Takes user desposit """
    while True:
        # While valid amount
        amount = input("Enter Deposit amount $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a valid amount")
        else:
            print("Please enter a number")
            
    return amount

def get_number_of_lines():
    """ Takes user betting lines """
    while True:
        # While valid amount
        lines = input("How many lines do you wish to bet on (1-" + str(MAX_LINES) + ") ? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of betting lines")
        else:
            print("Please enter a number")
            
    return lines

def get_bet():
    """ Takes user bet """
    while True:
        # While valid amount
        amount = input("Enter your bet for each line $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number")
            
    return amount

def game(balance):
    """Play the game"""
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(f"Insufficient funds to bet that amount, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on:", *winning_lines)
    
    return winnings - total_bet
    
def main():
    """ Rerun deposit function to play again """
    balance = deposit()
    while True:
        print(f"Current Balance is: ${balance}")
        answer = input("Press enter to play (q to stop)")
        if answer == "q":
            break
        else:
            balance += game(balance)
    print(f"You finished with ${balance}")
main()