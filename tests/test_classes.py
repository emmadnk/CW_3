from src.classes import Operation


def test_operation_instance():
    """
    Тестирование функций классаб которая выводит операции со статусом 'EXECUTED'
    """
    op = Operation(
        date="2019-08-26T10:50:58.294041",
        state="EXECUTED",
        currency_name="руб.",
        pk=441945886,
        amount="31957.58",
        description="Перевод организации",
        from_="Maestro 1596837868705199",
        to="Счет 64686473678894779589"

    )

    assert op.covert_payment_data("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert op.from_ == "Maestro 1596 83** **** 5199"
    assert op.to == "Счет **9589"
    assert op.covert_payment_date() =="26.08.2019"
    assert str(op) == (
            "26.08.2019 Перевод организации\n"
            "Maestro 1596 83** **** 5199 -> Счет **9589\n"
            "31957.58 руб.\n"
        )