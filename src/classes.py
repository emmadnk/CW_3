import datetime


class Operation:
    def __init__(self, pk, state, date, amount, currency_name, description, from_: str | None, to):
       self.pk = pk
       self.state = state
       self.date = date
       self.amount = amount
       self.currency_name = currency_name
       self.description = description
       self.from_ = self.covert_payment_data(from_) if from_ is not None else ""
       self.to = self.covert_payment_data(to)


    def covert_payment_data(self, payment_data):
        """
        Функция, которая преобразует счет и номер карты в замаскированный вид
        """
        if payment_data.startswith('Счет'):
            first_4 = payment_data[0: 4]
            last_4 = payment_data[-4:]
            return f"{first_4} **{last_4}"
        else:
            first_str = payment_data[0: -12]
            last_4_str = payment_data[-4:]
            five_six_str = payment_data[-12: -10]
            return f"{first_str} {five_six_str}** **** {last_4_str}"


    def covert_payment_date(self):
        """
        Функция, которая преобразует дату из международного принятого формата в формат ДД.ММ.ГГГГ
        """
        iso_date = datetime.datetime.fromisoformat(self.date)
        return iso_date.strftime("%d.%m.%Y")


#методы сравнения для сортировки операций по дате
    def __lt__(self, other):
        return self.date < other.date


    def __gt__(self, other):
        return self.date > other.date


    def __str__(self):
        date = self.covert_payment_date()
        return (
            f"{date} {self.description}\n"
            f"{self.from_} -> {self.to}\n"
            f"{self.amount} {self.currency_name}\n"
        )