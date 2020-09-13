import random as rd
from database.database import BankDatabaseApi


class BankSystem:
    CARDS = ['Visa', 'American Express', 'Mastercard']
    MAIN_OPTIONS = [0, 1, 2]
    USER_OPTIONS = [0, 1, 2, 3, 4, 5]

    def __init__(self):
        self.db = BankDatabaseApi()

    def check_credit_card(self, card_number):
        credit_card = self.db.get_card(card_number)
        return True if credit_card else False

    def check_pin(self, card_number, pin):
        credit_card = self.db.get_card_pin(card_number, pin)
        return True if credit_card else False

    def add_user(self, card_number, pin):
        if card_number and pin:
            self.db.add_card(card_number, pin)

    @staticmethod
    def luhn_algorithm(number_list):
        odds_index_by2 = [number_list[i] * 2 if (i + 1) % 2 == 1 else number_list[i] for i in range(len(number_list))]
        subtract_9 = [number - 9 if number > 9 else number for number in odds_index_by2]
        sum_numbers = sum(subtract_9)
        return sum_numbers

    @staticmethod
    def create_card_number():
        inn = '400000'
        account_number = str(rd.randint(0, 999999999))
        card_number = inn + '0' * (9 - len(account_number)) + account_number
        digits_sum = BankSystem.luhn_algorithm(list(map(int, card_number)))
        for i in range(10):
            if (digits_sum + i) % 10 == 0:
                return card_number + str(i)

    @staticmethod
    def create_pin():
        pin_number = str(rd.randint(0, 9999))
        return '0' * (4 - len(pin_number)) + pin_number

    def add_income(self, card_number):
        pass

    @staticmethod
    def user_menu():
        return int(input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n'))

    def create_account(self):
        print('Your card has been created')
        card_number = BankSystem.create_card_number()
        print('Your card number:\n{}'.format(card_number))
        pin_number = BankSystem.create_pin()
        print('Your card PIN:\n{}'.format(pin_number))
        self.add_user(card_number, pin_number)

    def login(self):
        card_number = input("Enter your card number:\n")
        pin = input("Enter your PIN:\n")
        if self.check_credit_card(card_number) and self.check_pin(card_number, pin):
            print("You have successfully logged in!")
            return card_number
        else:
            print("Wrong card number or PIN!")

        return None

    def get_balance(self, card_number):
        return self.db.get_balance(card_number)

    @staticmethod
    def log_out():
        print("You have successfully logged out!")

    @staticmethod
    def main_menu():
        return int(input('1. Create an account\n2. Log into account\n0. Exit\n'))

    @staticmethod
    def exit():
        print("Bye!")

    def start(self):
        option = BankSystem.main_menu()
        user_option = None
        while option != 0 and option in BankSystem.MAIN_OPTIONS:
            if option in BankSystem.MAIN_OPTIONS:
                if option == 1:
                    self.create_account()
                if option == 2:
                    logged = self.login()
                    while logged and user_option != 0:
                        user_option = self.user_menu()
                        if user_option == 1:
                            balance = self.get_balance(logged)
                            print("Balance: {}".format(balance))
                        if user_option == 2:
                            self.log_out()

            option = BankSystem.main_menu() if user_option != 0 else 0
        exit()

        if option not in BankSystem.MAIN_OPTIONS:
            raise ValueError("Invalid option '{}' ".format(option))


if __name__ == '__main__':
    my_bank = BankSystem()
    my_bank.start()
