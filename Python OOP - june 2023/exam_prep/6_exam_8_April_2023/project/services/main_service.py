from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str, capacity: int = 30):
        super().__init__(name, capacity)

    def details(self):
        result = f"{self.name} Main Service:\n"
        if not self.robots:
            result += "Robots: none"
            return result

        result += f"Robots: {' '.join([robot.name for robot in self.robots])}\n"
        return result
