import random as rd


class BankSystem:
    CARDS = ['Visa', 'American Express', 'Mastercard']
    MAIN_OPTIONS = [0, 1, 2]
    USER_OPTIONS = [0, 1, 2]

    def __init__(self):
        self.users = {}

    def check_credit_card(self, card_number):
        return card_number in self.users

    def check_pin(self, card_number, pin):
        return self.users[card_number] == pin

    def add_user(self, card_number, pin):
        self.users.update({card_number: pin})

    @staticmethod
    def create_card_number():
        inn = '400000'
        account_number = str(rd.randint(0, 9999999999))
        card_number = inn + '0' * (10 - len(account_number)) + account_number
        return card_number

    @staticmethod
    def create_pin():
        pin_number = str(rd.randint(0, 9999))
        return '0' * (4 - len(pin_number)) + pin_number

    @staticmethod
    def user_menu():
        return int(input('1. Balance\n2. Log out\n0. Exit\n'))

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
            return True
        else:
            print("Wrong card number or PIN!")

        return False

    @staticmethod
    def get_balance():
        print("Balance 0")

    @staticmethod
    def log_out():
        print("You have successfully logged out!")

    @staticmethod
    def main_menu():
        return int(input('1. Create an account\n2. Log into account\n0. Exit\n'))

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
                            self.get_balance()
                        if user_option == 2:
                            self.log_out()

            option = BankSystem.main_menu() if user_option != 0 else 0
        print("Bye!")

        if option not in BankSystem.MAIN_OPTIONS:
            raise ValueError("Invalid option '{}' ".format(option))


if __name__ == '__main__':
    my_bank = BankSystem()
    my_bank.start()
