from abc import ABC, abstractmethod

# Abstract Product A
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Abstract Product B
class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Concrete Product A1
class LightButton(Button):
    def render(self) -> str:
        return "Rendering a light button"

# Concrete Product A2
class DarkButton(Button):
    def render(self) -> str:
        return "Rendering a dark button"

# Concrete Product B1
class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering a light checkbox"

# Concrete Product B2
class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering a dark checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory 1
class LightThemeFactory(GUIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()

# Concrete Factory 2
class DarkThemeFactory(GUIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()

# Client code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())
