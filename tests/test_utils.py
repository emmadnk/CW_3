from src.utils import get_executed_operations


def test_get_executed_operations():
    """
    Тестисрование функции,
    :return:
    """
    operations =[
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        },
        {},
        {
            "state": "aaaaaaa",
        },
    ]

    expected_operations = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        },
    ]

    assert get_executed_operations(operations) == expected_operations



