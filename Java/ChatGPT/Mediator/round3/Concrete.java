// WindowsButton.java
public class WindowsButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering a button in Windows style.");
    }
}

// MacOSButton.java
public class MacOSButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering a button in MacOS style.");
    }
}

// WindowsCheckbox.java
public class WindowsCheckbox implements Checkbox {
    @Override
    public void check() {
        System.out.println("Checking a checkbox in Windows style.");
    }
}

// MacOSCheckbox.java
public class MacOSCheckbox implements Checkbox {
    @Override
    public void check() {
        System.out.println("Checking a checkbox in MacOS style.");
    }
