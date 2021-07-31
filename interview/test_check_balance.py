import pytest
import check_balance

class TestCheckBalance:
    def setup_class(self):
        pass

    def setup(self):
        pass

    @pytest.mark.parametrize('input_string, result',
                             [('(((([{}]))))', True),
                              ('[([])((([[[]]])))]{()}', True),
                              ('{{[()]}}', True),
                              ('}{}', False),
                              ('{{[(])]}}', False),
                              ('[[{())}]', False)])
    def test_check_balance(self, input_string, result):
        assert result == check_balance.check_balance(input_string)

