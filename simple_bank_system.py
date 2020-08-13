class BankSystem:
    CARDS = ['Visa', 'American Express', 'Mastercard']
    OPTIONS = [0, 1, 2]

    def __init__(self):
        users = {}

    @staticmethod
    def check_credit_card(card_number):
        pass

    @staticmethod
    def user_menu():
        pass

    @staticmethod
    def create_account():
        pass

    @staticmethod
    def login():
        pass

    @staticmethod
    def get_balance():
        pass

    @staticmethod
    def log_out():
        pass

    @staticmethod
    def main_menu():
        return int(input('1. Create an account\n2. Log into account\n0. Exit\n'))

    def start(self):
        option = BankSystem.main_menu()
        while option != 0 and option in BankSystem.OPTIONS:
            option = BankSystem.main_menu()
            if option in BankSystem.OPTIONS:
                if option == 1:
                    BankSystem.create_account()
                if option == 2:
                    BankSystem.login()

        if option not in BankSystem.OPTIONS:
            raise ValueError("Invalid option '{}' ".format(option))


if __name__ == '__main__':
    my_bank = BankSystem()
    my_bank.start()
