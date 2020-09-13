import sqlite3


class Database:

    def create_card_table(self):
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS card(id INTEGER, 
        number TEXT, pin TEXT , balance INTEGER  DEFAULT 0)''')
        self.conn.commit()

    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.create_card_table()


class BankDatabaseApi:

    def add_card(self, card_number, card_pin):
        cur = self.conn.cursor()
        cur.execute(f'''INSERT INTO card(number, pin) VALUES({card_number}, {card_pin})''')
        self.conn.commit()

    def get_card(self, card_number):
        cur = self.conn.cursor()
        cur.execute(f'''SELECT * from card where number == {card_number}''')
        row = cur.fetchone()
        return row

    def get_card_pin(self, card_number, pin_number):
        cur = self.conn.cursor()
        cur.execute(f'''SELECT * from card where number == {card_number} and pin =={pin_number} ''')
        row = cur.fetchone()
        return row

    def remove_card(self, card_number):
        cur = self.conn.cursor()
        cur.execute(f''' DELETE from card where number =={card_number}''')
        self.conn.commit()

    def mod_balance(self, card_number):
        pass

    def mod_pin(self, card_number, new_pin):
        pass

    def get_balance(self, card_number):
        cur = self.conn.cursor()
        cur.execute(f'''SELECT balance from card where number == {card_number}''')
        row = cur.fetchone()

        return row[0]

    def __init__(self):
        self.conn = sqlite3.connect('file:database/card.s3db?mode=rw', uri=True)


if __name__ == '__main__':
    Database()
