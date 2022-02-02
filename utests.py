import unittest
from func import DB


class test_db(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.database = DB("luysbd.db")

    def test_list_of_orders_customer_2(self):
        res = self.database.order_list(2)
        self.assertEqual(res,
                         [(3, 'Александр', 'Админ', '12.12.2020', 20, 'Russia', 'Россия', 'Москва', 'Зеленая', '1', '2', '22', '1111')])

    def test_list_of_items_order_id_1(self):
        res = self.database.order_info(1)
        self.assertEqual(res, [('Акула', 'Роберт', 'Админ', 20, 40)])

    def test_address_list_id_1(self):
        res = self.database.address_list(1)
        self.assertEqual(res, [(2, 'Роберт', 'Админ', 'Россия', 'Москва', 'Лебезятная', '2', '3', '33', '2222')])


if __name__ == '__main__':
    unittest.main()