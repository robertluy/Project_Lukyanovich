import sqlite3

db = sqlite3.connect('../luysbd.db')
cursor = db.cursor()

cursor.execute(
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
 FROM orders WHERE orders.customer_id = 2;
'''
)
print(cursor.fetchall())
db.close()