import random

MAX_LINE=3
MAX_VALUE=100
MIN_VALUE=1
ROWS=3
COLS=3
symbol_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8
}
symbol_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_line.append(line+1)
    return winnings, winning_line


def generate_symbols(rows,cols,symbol):
    all_symbols = []
    for symbol,symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):                                    #generate symbols for each column
        column=[]
        current_symbol=all_symbols[:]                        #here current_symbol is the copy of the all_symbols
        for _ in range(rows):                                #generate symbols for each row
            value=random.choice(current_symbol)
            current_symbol.remove(value)                     #removing the value to avoid repeations
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=' | ')
            else:
                print(column[row],end='')
        print()
def deposit():
    while True:
        amount=input("How much would you like to deposit?$")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Invalid deposit amount. Please enter a positive number.")
        else:
            print("Invalid deposit amount. Please enter a number.")
    return amount

def get_the_number_lines():
    while True:
        line=input("Enter the number of lines to Bet (1-" + str(MAX_LINE) + "): ")
        if line.isdigit():
            line=int(line)
            if 1<=line<=MAX_LINE:
                break
            else:
                print("please enter a valid line number")
        else:
            print("Invalid line number. Please enter a number.")
    return line

def get_bet():
    while True:
        amount=input("How much would you like to Bet on each line?$")
        if amount.isdigit():
            amount=int(amount)
            if MIN_VALUE<=amount<=MAX_VALUE:
                break
            else:
                print(f"Enter a valid amount between ${MIN_VALUE}-${MAX_VALUE}")
        else:
            print("Invalid bet amount. Please enter a number.")
    return amount
def spin(balance):
    line=get_the_number_lines()
    while True:
        bet=get_bet()
        total_bet=bet*line
        if total_bet>balance:
            print(f"insufficient balance.your current balance ${balance}")
        else:
            break

    print(f"You're betting ${bet} on {line} lines.Total bet is ${total_bet}")
    slots=generate_symbols(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_line=check_winnings(slots,line,bet,symbol_value)
    print(f"Congratulations! You won ${winnings}")
    print("You Won on",*winning_line)
    return winnings-total_bet

def main():
    balance=deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press enter to Play... or press "'q'" to Quit : ")
        if answer.lower()=='q':
            break
        balance+=spin(balance)
    print(f"You left with balance{balance}")
main()
