from typing import List
import sys

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_TYPES_LOAN = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_TYPES_CLIENT = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list = []
        self.clients: List[BaseClient] = []

    # @staticmethod
    # def get_class(class_name: str):
    #     return getattr(sys.modules[__name__], class_name)

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.VALID_TYPES_LOAN.keys():
            raise Exception("Invalid loan type!")

        loan = BankApp.VALID_TYPES_LOAN[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in BankApp.VALID_TYPES_CLIENT:
            raise ValueError("Invalid client type!")

        if not self.capacity > len(self.clients):
            return "Not enough bank capacity."

        if client_type == "Student":
            client = Student(client_name, client_id, income)
            self.clients.append(client)
            return f"{client_type} was successfully added."

        if client_type == "Adult":
            client = Adult(client_name, client_id, income)
            self.clients.append(client)
            return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        if loan_type not in BankApp.VALID_TYPES_LOAN:
            raise Exception("Invalid loan type!")

        gr_client = [c for c in self.clients if client_id == c.client_id][0]
        gr_loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]

        if gr_client.VALID_LOAN_TYPE != loan_type:
            raise Exception("Inappropriate loan type!")

        gr_client.loans.append(gr_loan)
        self.loans.remove(gr_loan)
        return f"Successfully granted {loan_type} to {gr_client.name} with ID {gr_client.client_id}."

    def remove_client(self, client_id: str):
        try:
            rem_client = [c for c in self.clients if client_id == c.client_id][0]
        except IndexError:
            raise Exception("No such client!")

        if len(rem_client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(rem_client)
        return f"Successfully removed {rem_client.name} with ID {rem_client.client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for ll in self.loans:
            if loan_type == ll.__class__.__name__:
                ll.increase_interest_rate()
                counter += 1

        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for cc in self.clients:
            if cc.interest < min_rate:
                cc.increase_clients_interest()
                counter += 1

        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        result = f"Active Clients: {len(self.clients)}\n"

        total_income = sum([c.income for c in self.clients])
        result += f"Total Income: {total_income:.2f}\n"

        all_cl_loans = []
        for cl in self.clients:
            if len(cl.loans) > 0:
                for cll in cl.loans:
                    all_cl_loans.append(cll.amount)

        total_sum = sum(list(map(lambda x: int(x), all_cl_loans)))
        result += f"Granted Loans: {len(all_cl_loans)}, Total Sum: {total_sum:.2f}\n"

        all_bank_loans = []
        for bl in self.loans:
            all_bank_loans.append(bl.amount)

        result += f"Available Loans: {len(all_bank_loans)}, Total Sum: {sum(all_bank_loans):.2f}\n"

        all_cl_interest = [c.interest for c in self.clients]
        if not all_cl_interest:
            result += f"Average Client Interest Rate: 0.00"
        else:
            average_cl_int = sum(all_cl_interest) / len(all_cl_interest)

            result += f"Average Client Interest Rate: {average_cl_int:.2f}"

        return result
