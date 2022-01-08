import sqlite3

db = sqlite3.connect('../luysbd.db')
cursor = db.cursor()

cursor.execute(
'''
SELECT (SELECT name FROM items WHERE items.id = item_id) as 'product',
(SELECT name FROM users WHERE users.id = (SELECT customer_id FROM orders WHERE orders.customer_id = order_id)) as 'name',
(SELECT surname FROM users WHERE users.id = (SELECT customer_id FROM orders WHERE orders.customer_id = order_id)) as 'status',
 price_per_item as 'price',
 count as 'count'
 FROM order_list WHERE order_list.order_id = 2;
'''
)
print(cursor.fetchall())
db.close()