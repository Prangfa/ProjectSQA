// Product A interface
public interface Button {
    void paint();
}

// Product B interface
public interface Checkbox {
    void paint();
}

// Abstract Factory
public interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}
