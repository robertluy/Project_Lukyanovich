import sqlite3


class DB:
    def __init__(self, path: str):
        self.connection = sqlite3.connect(path)
        self.new_cursor()

    def new_cursor(self):
        self.cursor = self.connection.cursor()

    def order_list(self, par):
        self.cursor.execute(
            '''
            SELECT "id" as 'order ID',
            (SELECT name FROM users WHERE users.id = customer_id) as 'name',
            (SELECT surname FROM users WHERE users.id = customer_id) as 'status',
             date,
             total,
             state,
             (SELECT country FROM adr WHERE adr.id = address_id) as 'country',
             (SELECT city FROM adr WHERE adr.id = address_id) as 'city',
             (SELECT street FROM adr WHERE adr.id = address_id) as 'street',
             (SELECT house FROM adr WHERE adr.id = address_id) as 'house',
             (SELECT floor FROM adr WHERE adr.id = address_id) as 'floor',
             (SELECT flat FROM adr WHERE adr.id = address_id) as 'flat',
             (SELECT postcode FROM adr WHERE adr.id = address_id) as 'postcode'
             FROM orders WHERE orders.customer_id = :par;
            ''', {'par': par}
        )
        return self.cursor.fetchall()

    def order_info(self, par):
        self.cursor.execute(
            '''
            SELECT (SELECT name FROM items WHERE items.id = item_id) as 'product',
            (SELECT name FROM users WHERE users.id = (SELECT customer_id FROM orders WHERE orders.customer_id = order_id)) as 'name',
            (SELECT surname FROM users WHERE users.id = (SELECT customer_id FROM orders WHERE orders.customer_id = order_id)) as 'status',
             price_per_item as 'price',
             count as 'count'
             FROM order_list WHERE order_list.order_id = :par;
            ''', {'par': par}
        )
        return self.cursor.fetchall()

    def address_list(self, par):
        self.cursor.execute(
            '''
            SELECT "address_id" as 'address id',
            (SELECT name FROM users WHERE users.id = customer_id) as 'name',
            (SELECT surname FROM users WHERE users.id = customer_id) as 'status',
             (SELECT country FROM adr WHERE adr.id = address_id) as 'country',
             (SELECT city FROM adr WHERE adr.id = address_id) as 'city',
             (SELECT street FROM adr WHERE adr.id = address_id) as 'street',
             (SELECT house FROM adr WHERE adr.id = address_id) as 'house',
             (SELECT floor FROM adr WHERE adr.id = address_id) as 'floor',
             (SELECT flat FROM adr WHERE adr.id = address_id) as 'flat',
             (SELECT postcode FROM adr WHERE adr.id = address_id) as 'postcode'
             FROM user_adr WHERE user_adr.customer_id = :par;
            ''', {'par': par}
        )
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close()