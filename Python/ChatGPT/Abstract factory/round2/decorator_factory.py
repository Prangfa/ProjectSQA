from abc import ABC, abstractmethod

# Abstract Product
class Widget(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Concrete Product A
class Button(Widget):
    def render(self) -> str:
        return "Rendering a Button"

# Concrete Product B
class Checkbox(Widget):
    def render(self) -> str:
        return "Rendering a Checkbox"

# Abstract Factory
class WidgetFactory(ABC):
    @abstractmethod
    def create_widget(self) -> Widget:
        pass

# Concrete Factory A
class ButtonFactory(WidgetFactory):
    def create_widget(self) -> Widget:
        return Button()

# Concrete Factory B
class CheckboxFactory(WidgetFactory):
    def create_widget(self) -> Widget:
        return Checkbox()

# Abstract Decorator
class WidgetDecorator(Widget):
    def __init__(self, widget: Widget):
        self._widget = widget

    @abstractmethod
    def render(self) -> str:
        pass

# Concrete Decorator A
class BorderDecorator(WidgetDecorator):
    def render(self) -> str:
        return f"{self._widget.render()} with a border"

# Concrete Decorator B
class ScrollDecorator(WidgetDecorator):
    def render(self) -> str:
        return f"{self._widget.render()} with scroll functionality"

def main():
    # Create a button using the factory
    button_factory = ButtonFactory()
    button = button_factory.create_widget()
    
    # Decorate the button
    bordered_button = BorderDecorator(button)
    scrolled_bordered_button = ScrollDecorator(bordered_button)
    
    print(scrolled_bordered_button.render())
    
    # Create a checkbox using the factory
    checkbox_factory = CheckboxFactory()
    checkbox = checkbox_factory.create_widget()
    
    # Decorate the checkbox
    bordered_checkbox = BorderDecorator(checkbox)
    
    print(bordered_checkbox.render())

if __name__ == "__main__":
    main()
