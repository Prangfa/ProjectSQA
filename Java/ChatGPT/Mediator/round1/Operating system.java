// WindowsButton class implementing Button interface
public class WindowsButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering a button in a Windows style.");
    }
}

// MacOSButton class implementing Button interface
public class MacOSButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering a button in a MacOS style.");
    }
}

// WindowsCheckbox class implementing Checkbox interface
public class WindowsCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("Rendering a checkbox in a Windows style.");
    }
}

// MacOSCheckbox class implementing Checkbox interface
public class MacOSCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("Rendering a checkbox in a MacOS style.");
    }
}
