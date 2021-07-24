import unittest
from unittest.mock import patch, call
import secretary

OWNERS_SET = {"Аристарх Павлов", "Геннадий Покемонов", "Василий Гупкин", ""}


def count_doc_at_shelfs(doc_number):
    count = 0
    for item in secretary.directories:
        if doc_number in secretary.directories[item]:
            count += secretary.directories[item].count(doc_number)
    return count


class TestSecretary(unittest.TestCase):
    def setUp(self):
        secretary.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "id", "number": "123", "name": ""}
        ]
        secretary.directories = {
            '1': ['2207 876234', '11-2', '028765'],
            '2': ['10006'],
            '3': []
        }
        print('setUp')

    def tearDown(self):
        secretary.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        secretary.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }
        print('tearDown')

    def test_check_document_existance_10006(self):
        print('test_check_document_existance_10006')
        self.assertTrue(secretary.check_document_existance('10006'))

    def test_check_document_existance_10000(self):
        print('test_check_document_existance_10000')
        self.assertFalse(secretary.check_document_existance('10000'))

    @patch('builtins.input', lambda *args: '10006')
    def test_get_doc_owner_name_10006(self):
        print('test_get_doc_owner_name_10006')
        self.assertEqual(secretary.get_doc_owner_name(), "Аристарх Павлов")

    @patch('builtins.input', lambda *args: '10000')
    def test_get_doc_owner_name_10000(self):
        print('test_get_doc_owner_name_10000')
        self.assertNotIn(secretary.get_doc_owner_name(), OWNERS_SET)

    def test_get_all_doc_owners_names(self):
        print('test_get_all_doc_owners_names')
        self.assertSetEqual(secretary.get_all_doc_owners_names(), OWNERS_SET)

    def test_remove_doc_from_shelf_single(self):
        print('test_remove_doc_from_shelf_single')
        doc_number = '10006'
        secretary.remove_doc_from_shelf(doc_number)
        self.assertFalse(count_doc_at_shelfs(doc_number) > 0)

    def test_remove_doc_from_shelf_multiple(self):
        print('test_remove_doc_from_shelf_multiple')
        doc_number = '10006'
        secretary.append_doc_to_shelf(doc_number, '5')
        secretary.remove_doc_from_shelf(doc_number)
        self.assertFalse(count_doc_at_shelfs(doc_number) > 0)
    # если существует возможность нахождения одного документа в нескольких папках,
    # то удалится первая найденная запись, а вторая останется

    @patch('builtins.input', lambda *args: '5')
    def test_add_new_shelf_5(self):
        print('test_add_new_shelf_5')
        new_shelf = '5' not in secretary.directories.keys()
        shelf_num, shelf_created = secretary.add_new_shelf()
        self.assertTrue(shelf_num in secretary.directories.keys())
        if new_shelf:
            self.assertTrue(shelf_created)
        else:
            self.assertFalse(shelf_created)

    def test_add_new_shelf_2(self):
        print('test_add_new_shelf_2')
        shelf_num = '2'
        new_shelf = shelf_num not in secretary.directories.keys()
        shelf_num, shelf_created = secretary.add_new_shelf(shelf_number=shelf_num)
        self.assertTrue(shelf_num in secretary.directories.keys())
        if new_shelf:
            self.assertTrue(shelf_created)
        else:
            self.assertFalse(shelf_created)

    @patch('builtins.input', lambda *args: '10006')
    def test_delete_doc_10006(self):
        print('test_delete_doc_10006')
        doc_number, deleted = secretary.delete_doc()
        self.assertTrue((doc_number == '10006')
                        and deleted
                        and not secretary.check_document_existance('10006')
                        and count_doc_at_shelfs(doc_number) == 0)

    @patch('builtins.input', lambda *args: '10000')
    def test_delete_doc_10000(self):
        print('test_delete_doc_10000')
        doc_number, deleted = secretary.delete_doc()
        self.assertTrue((doc_number == '10000')
                        and not deleted
                        and not secretary.check_document_existance('10006')
                        and count_doc_at_shelfs(doc_number) == 0)
    # если пользователь попытается удалить несуществующий документ, функция возвращает
    # не кортеж doc_number, deleted_state, а None, что вызовет ошибку, или потребует проверки if not None
    # правильнее было бы возвращать кортеж doc_number, False

    @patch('builtins.input', lambda *args: '10000')
    def test_get_doc_shelf_10000(self):
        print('test_get_doc_shelf_10000')
        self.assertEqual(secretary.get_doc_shelf(), None)

    @patch('builtins.input', lambda *args: '10006')
    def test_get_doc_shelf_10006(self):
        print('test_get_doc_shelf_10006')
        self.assertEqual(secretary.get_doc_shelf(), '2')

    @patch('builtins.input', lambda *args: '028765')
    def test_get_doc_shelf_028765(self):
        print('test_get_doc_shelf_028765')
        self.assertEqual(secretary.get_doc_shelf(), '1')
    # документ не существует, хотя есть отметка о размещении его в директории,
    # при этом нужно определить, как должен вести себя данный метод:
    # в идеале - исправлять это, т.е. удалять эту отметку, либо выводить сообщение об обнаруженном несоответствии
    # либо если работать "в лоб", что наверное неправильно, то все-таки выводить номер полки

    @patch('builtins.input', side_effect=['10006', '10006'])
    def test_get_doc_shelf_10006_multiple(self, param):
        print('test_get_doc_shelf_10006_multiple')
        secretary.append_doc_to_shelf('10006', '1')
        print(secretary.directories)
        self.assertEqual(secretary.get_doc_shelf(), {'1', '2'})
    # если документ может находиться сразу в нескольких директориях,
    # а в текущей реализации append_doc_to_shelf позволяет это,
    # то метод get_doc_shelf должен возвращать все директории
    # в виде списка или множества, а не только первую найденную

    @patch('builtins.input', side_effect=['11-2', '11-2', '11-2'])
    def test_append_doc_to_shelf_11_2__5(self, param):
        print('test_append_doc_to_shelf_11_2__5')
        doc_number = '11-2'
        shelf_number = '5'
        secretary.append_doc_to_shelf(doc_number, shelf_number)
        self.assertEqual(secretary.get_doc_shelf(), '1')
        self.assertEqual(secretary.get_doc_shelf(), '5')
        self.assertTrue(doc_number in secretary.directories[shelf_number])
        self.assertEqual(count_doc_at_shelfs(doc_number), 1)
    # несоответствие происходит при добавлении документа в директорию, если он уже находился в какой-то директории
    # наверное, предполагается что документ не может находиться сразу в нескольких директориях
    # данный метод используется в программе только внутри других методов, что исключает эту ошибку при выполнении кода
    # (там выполняются проверки), но при расширении функционала программы эта ошибка может помешать корректной работе

    @patch('builtins.input', side_effect=['11-2', '11-2', '11-2'])
    def test_append_doc_to_shelf_11_2__1(self, param):
        print('test_append_doc_to_shelf_11_2__1')
        doc_number = '11-2'
        shelf_number = '1'
        secretary.append_doc_to_shelf(doc_number, shelf_number)
        self.assertEqual(secretary.get_doc_shelf(), '1')
        self.assertTrue(doc_number in secretary.directories[shelf_number])
        self.assertEqual(count_doc_at_shelfs(doc_number), 1)
    # предыдущий кейс относится также и если пользователь добавляет документ в директорию,
    # в которой он и так находится, запись о нахождении документа в директории продублируется

    @patch('builtins.input', side_effect=['10006', '10006', '1', '10006'])
    def test_move_doc_to_shelf_10006(self, param):
        print('test_move_doc_to_shelf_10006')
        self.assertEqual(secretary.get_doc_shelf(), '2')
        secretary.move_doc_to_shelf()
        self.assertEqual(secretary.get_doc_shelf(), '1')
        self.assertTrue(count_doc_at_shelfs('10006') > 0)

    @patch('builtins.input', side_effect=['10000', '10000', '3', '10000'])
    def test_move_doc_to_shelf_10000(self, param):
        print('test_move_doc_to_shelf_10006')
        self.assertEqual(secretary.get_doc_shelf(), None)
        secretary.move_doc_to_shelf()
        self.assertEqual(secretary.get_doc_shelf(), None)
        self.assertTrue(count_doc_at_shelfs('10000') == 0)
    # несуществующий документ перемещается в директорию

    @patch('builtins.print')
    def test_show_document_info_10006(self, mocked_print):
        secretary.show_document_info({"type": "insurance", "number": "10006", "name": "Аристарх Павлов"})
        assert mocked_print.mock_calls == [call('insurance "10006" "Аристарх Павлов"')]

    @patch('builtins.input', side_effect=['10000', 'id', 'New Name', '5', '10000'])
    def test_add_new_doc_10000_1(self, param):
        shelfNumber = secretary.add_new_doc()
        self.assertEqual(shelfNumber, '5')
        self.assertEqual(secretary.get_doc_shelf(), '5')
        self.assertTrue(secretary.check_document_existance('10000'))
    # нет возможности создать документ, не помещая его в определенную директорию
