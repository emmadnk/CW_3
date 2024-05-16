import json
from pathlib import Path
from src.classes import Operation


def load_json(path: Path):
    """
    Функция, которая открывает файл с операциями клиента
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_executed_operations(operations):
    """
    Функция, которая выводит операции со статусом 'EXECUTED"
    """
    return [
        operation
        for operation in operations
        if operation.get("state") == "EXECUTED"
           ]


def get_instances(operations):
    """
    Функция, которая возвращает список экземпляров класса
    """
    instances = []
    for operation in operations:
        operation_amount = operation["operationAmount"]
        op = Operation(
            date=operation["date"],
            pk=operation["id"],
            state=operation["state"],
            to=operation["to"],
            from_=operation.get("from"),
            description=operation["description"],
            amount=operation_amount["amount"],
            currency_name=operation_amount["currency"]["name"],
        )
        instances.append(op)
    return instances


def sort_operations_by_date(operations: list[Operation]):
    """
    Функция, которая сортирует операции по дате
    """
    return sorted(operations, reverse=True)