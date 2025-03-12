import random
import time


def spin_row():
    symbols = ["🍒","🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")


def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet *  4
        elif row[0] == "🍋":
            return bet *  5
        elif row[0] == "🔔":
            return bet *  10
        elif row[0] == "⭐":
            return bet *  20

    return 0




def main():
    balance = 100
    print("*************************")
    print("welcome to python slots")
    print("🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"current balance : ${balance}")

        bet = input("plese your bet amount : ")

        if not bet.isdigit():
            print("please enter a valid nunmber ")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient balance")
            continue

        if bet <= 0:
            print("bet must be greater than zero")
            continue

        balance -= bet

        row = spin_row()
        print("spinning......\n")
        time.sleep(1)
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"you won ${payout}")
        else:
            print("you lost this round")

        balance += payout

        play_again = input("do you want to spin again (Y/N) : ").upper()

        if play_again != "Y":
            break
    print("********************************************")
    print(f"Game over! your final balance is ${balance}")
    print("********************************************")

if __name__ == "__main__":
    main()