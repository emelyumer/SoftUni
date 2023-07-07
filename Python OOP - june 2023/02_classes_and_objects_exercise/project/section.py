from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        for tsk in self.tasks:
            if tsk == task_name:
                tsk.completed = True
                return f"Completed task {task_name}"

    def clean_section(self):
        initial_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {initial_len - len(self.tasks)} tasks."

    def view_section(self):
        tasks = '\n'.join([t.details() for t in self.tasks])

        return f"Section {self.name}:\n" + \
            f"{tasks}"


