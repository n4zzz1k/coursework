import pytest
from main import format_operation_date, mask_card_number, mask_account_number

# Тестирование функции format_operation_date
def test_format_operation_date():
    assert format_operation_date('2019-12-08T22:46:21.935582') == '08.12.2019'
    assert format_operation_date('2022-05-15T14:30:45.123456') == '15.05.2022'

# Тестирование функции mask_card_number
def test_mask_card_number():
    assert mask_card_number('1234567890123456') == '1234 **** **** 3456'
    assert mask_card_number('9876543210987654') == '9876 **** **** 7654'

# Тестирование функции mask_account_number
def test_mask_account_number():
    assert mask_account_number('1234567890') == '**7890'
    assert mask_account_number('9876543210') == '**3210'

# Запуск всех тестов
if __name__ == '__main__':
    pytest.main()
