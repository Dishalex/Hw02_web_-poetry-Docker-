from abc import ABC, abstractmethod
import rich


class UserInterface(ABC):
    @abstractmethod
    def show_contacts(self, contacts):
        pass

    @abstractmethod
    def show_notes(self, notes):
        pass

    @abstractmethod
    def show_commands(self, commands):
        pass


class ConsoleUserInterface(UserInterface):
    def show_contacts(self, contacts):
        rich.print(contacts)

    def show_notes(self, notes):
        # Логіка виведення нотаток у консоль
        pass

    def show_commands(self, commands):
        rich.print(commands)


class WebUserInterface(UserInterface):
    def show_contacts(self, contacts):
        # Логіка виведення контактів на веб-сторінці
        pass

    def show_notes(self, notes):
        # Логіка виведення нотаток на веб-сторінці
        pass

    def show_commands(self):
        # Логіка виведення доступних команд на веб-сторінці
        pass
