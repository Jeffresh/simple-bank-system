import sqlite3


class Database:

    def create_card_table(self):
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS card(id INT PRIMARY KEY , 
        number VARCHAR(16) NOT NULL UNIQUE, pin VARCHAR(4) NOT NULL , balance INT DEFAULT  0)''')
        self.conn.commit()

    def add_card(self, card_number, card_pin):
        cur = self.conn.cursor()
        cur.execute(f'''INSERT INTO card(number, pin) VALUES({card_number}, {card_pin})''')
        self.conn.commit()

    def __init__(self):
        self.conn = sqlite3.connect('database/card.s3db')
        self.create_card_table()
