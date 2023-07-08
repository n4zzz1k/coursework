import json

def mask_card_number(card_number):
    if card_number is None:
        return ''
    masked = ' '.join([card_number[:4], '****', '****', card_number[-4:]])
    return masked

def mask_account_number(account_number):
    if account_number is None:
        return ''
    masked = '**' + account_number[-4:]
    return masked

def format_operation_date(date):
    parts = date.split('T')
    date_parts = parts[0].split('-')
    formatted_date = '.'.join(date_parts[::-1])
    return formatted_date

def print_recent_operations(operations, num_operations=5):
    for op in operations[:num_operations]:
        date = format_operation_date(op['date'])
        description = op['description']
        from_account = op.get('from')
        to_account = op.get('to')
        amount_currency = op.get('operationAmount')
        if isinstance(amount_currency, dict):
            amount = amount_currency.get('amount', '')
            currency_info = amount_currency.get('currency', {})
            currency = currency_info.get('name', '')
        else:
            amount, currency = '', ''

        masked_from = mask_account_number(from_account) if from_account else ''
        masked_to = mask_account_number(to_account) if to_account else ''

        print(f"{date} {description}")
        if masked_from:
            print(f"Счет {masked_from} -> Счет {masked_to}")
        else:
            print(f" -> Счет {masked_to}")
        print(f"{amount} {currency}")
        print()

# Открываем файл с операциями
with open('operations.json', 'r') as file:
    operations = json.load(file)

# Отсортируем операции по дате в порядке убывания
executed_operations = sorted([op for op in operations if op.get('state') == 'EXECUTED'], key=lambda op: op['date'], reverse=True)

# Выводим список последних операций
print_recent_operations(executed_operations, num_operations=5)
