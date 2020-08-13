class BankSystem:
    CARDS = ['Visa', 'American Express', 'Mastercard']
    OPTIONS = [0, 1, 2]

    def check_credit_card(self, card_number):
        pass

    @staticmethod
    def main_menu():
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

    def start(self):
        option = BankSystem.main_menu()
        while option != 0 and option in BankSystem.OPTIONS:
            option = BankSystem.main_menu()


if __name__ == '__main__':
    my_bank = BankSystem()
