class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            f_worker = [w for w in self.workers if w.name == worker_name][0]
            #wrong code
            # f_worker = next(filter(lambda w: w.name == worker_name, self.workers))[0]
        except IndexError:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(f_worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        needed_sal_money = sum([w.salary for w in self.workers])

        if self.__budget < needed_sal_money:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_sal_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        all_money_animal_care = sum([a.money_for_care for a in self.animals])

        if self.__budget < all_money_animal_care:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= all_money_animal_care
        return  f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result = f"You have {len(self.animals)} animals\n"

        result += f"----- {len(lions)} Lions:\n"
        result += '\n'.join([f'{l}' for l in lions])

        result += f"\n----- {len(tigers)} Tigers:\n"
        result += '\n'.join([f'{t}' for t in tigers])

        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join([f'{c}' for c in cheetahs])

        return result

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers"

        result += f"\n----- {len(keepers)} Keepers:\n"
        result += '\n'.join([f'{k}' for k in keepers])

        result += f"\n----- {len(caretakers)} Caretakers:\n"
        result += '\n'.join([f'{c}' for c in caretakers])

        result += f"\n----- {len(keepers)} Vets:\n"
        result += '\n'.join([f'{v}' for v in vets])

        return result







