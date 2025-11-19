from datetime import datetime

def account_date(data_str: str) -> str:
    try:
        data_obj = datetime.strptime(data_str, '%Y-%m-%d')
        return data_obj.strftime('%d %m %Y')
    except ValueError:
        raise ValueError(f'Incorrect date format: {data_str}. Waiting for the format "YYYY-MM-DD"')

print(account_date('2024-1-1'))
