from typing import List


class EmailValidator:
    def __init__(self, min_length, mails: List, domains: List):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if len(name) < self.min_length:
            return False
        return True

    def __is_mail_valid(self, mail):
        if mail not in self.mails:
            return False
        return True

    def __is_domain_valid(self, domain):
        if domain not in self.domains:
            return False
        return True

    def validate(self, email):
        data = email.split("@")
        username = data[0]
        mail, domain = data[1].split(".")

        if self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))