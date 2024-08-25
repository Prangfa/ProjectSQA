// MacButton.java
public class MacButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering a button in Mac style.");
    }
}

// WindowsButton.java
public class WindowsButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering a button in Windows style.");
    }
}

// MacCheckbox.java
public class MacCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("Rendering a checkbox in Mac style.");
    }
}

// WindowsCheckbox.java
public class WindowsCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("Rendering a checkbox in Windows style.");
    }
}
