# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
class Money:
    def __init__(self, pounds: int, pence: int):
        if not isinstance(pounds, int):
            raise TypeError("Pounds must be an integer")

        if not isinstance(pence, int):
            raise TypeError("Pence must be an integer")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        total_pounds = self.pounds + other.pounds
        total_pence = self.pence + other.pence

        if total_pence >= 100:
            total_pounds += total_pence // 100
            total_pence = total_pence % 100

        return Money(total_pounds, total_pence)
