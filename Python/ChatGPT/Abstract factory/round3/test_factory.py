import pytest
from factory import *

def test_light_theme_factory():
    factory = LightThemeFactory()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    
    assert isinstance(button, LightButton)
    assert button.render() == "Rendering a light button"
    
    assert isinstance(checkbox, LightCheckbox)
    assert checkbox.render() == "Rendering a light checkbox"

def test_dark_theme_factory():
    factory = DarkThemeFactory()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    
    assert isinstance(button, DarkButton)
    assert button.render() == "Rendering a dark button"
    
    assert isinstance(checkbox, DarkCheckbox)
    assert checkbox.render() == "Rendering a dark checkbox"
