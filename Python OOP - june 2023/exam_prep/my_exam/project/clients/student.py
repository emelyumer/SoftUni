from project.clients.base_client import BaseClient


class Student(BaseClient):
    VALID_LOAN_TYPE = "StudentLoan"

    def __init__(self, name: str, client_id: str, income: float, interest: float = 2.0):
        super().__init__(name, client_id, income, interest)

    def increase_clients_interest(self):
        self.interest += 1.0
        return self.interest

