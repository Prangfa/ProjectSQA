import unittest

# Assuming the original code is in a module named `decorator_factory`
# If it's in the same file, you can directly use the classes without importing.
from decorator_factory import *

class TestWidgetFactoryAndDecorator(unittest.TestCase):

    def test_button_render(self):
        button_factory = ButtonFactory()
        button = button_factory.create_widget()
        self.assertEqual(button.render(), "Rendering a Button")

    def test_checkbox_render(self):
        checkbox_factory = CheckboxFactory()
        checkbox = checkbox_factory.create_widget()
        self.assertEqual(checkbox.render(), "Rendering a Checkbox")

    def test_border_decorator_on_button(self):
        button_factory = ButtonFactory()
        button = button_factory.create_widget()
        bordered_button = BorderDecorator(button)
        self.assertEqual(bordered_button.render(), "Rendering a Button with a border")

    def test_scroll_decorator_on_button(self):
        button_factory = ButtonFactory()
        button = button_factory.create_widget()
        scrolled_button = ScrollDecorator(button)
        self.assertEqual(scrolled_button.render(), "Rendering a Button with scroll functionality")

    def test_border_and_scroll_decorator_on_button(self):
        button_factory = ButtonFactory()
        button = button_factory.create_widget()
        bordered_button = BorderDecorator(button)
        scrolled_bordered_button = ScrollDecorator(bordered_button)
        self.assertEqual(scrolled_bordered_button.render(), "Rendering a Button with a border with scroll functionality")

    def test_border_decorator_on_checkbox(self):
        checkbox_factory = CheckboxFactory()
        checkbox = checkbox_factory.create_widget()
        bordered_checkbox = BorderDecorator(checkbox)
        self.assertEqual(bordered_checkbox.render(), "Rendering a Checkbox with a border")

    def test_scroll_decorator_on_checkbox(self):
        checkbox_factory = CheckboxFactory()
        checkbox = checkbox_factory.create_widget()
        scrolled_checkbox = ScrollDecorator(checkbox)
        self.assertEqual(scrolled_checkbox.render(), "Rendering a Checkbox with scroll functionality")

    def test_border_and_scroll_decorator_on_checkbox(self):
        checkbox_factory = CheckboxFactory()
        checkbox = checkbox_factory.create_widget()
        bordered_checkbox = BorderDecorator(checkbox)
        scrolled_bordered_checkbox = ScrollDecorator(bordered_checkbox)
        self.assertEqual(scrolled_bordered_checkbox.render(), "Rendering a Checkbox with a border with scroll functionality")

if __name__ == "__main__":
    unittest.main()
