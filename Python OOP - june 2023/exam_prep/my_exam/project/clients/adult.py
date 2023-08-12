from project.clients.base_client import BaseClient


class Adult (BaseClient):
    VALID_LOAN_TYPE = "MortgageLoan"

    def __init__(self, name: str, client_id: str, income: float, interest: float = 4.0):
        super().__init__(name, client_id, income, interest)

    def increase_clients_interest(self):
        self.interest += 2.0
        return self.interest
