// Concrete Product A1
public class WinButton implements Button {
    @Override
    public void paint() {
        System.out.println("You have created a Windows Button.");
    }
}

// Concrete Product A2
public class MacButton implements Button {
    @Override
    public void paint() {
        System.out.println("You have created a Mac Button.");
    }
}

// Concrete Product B1
public class WinCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("You have created a Windows Checkbox.");
    }
}

// Concrete Product B2
public class MacCheckbox implements Checkbox {
    @Override
    public void paint() {
        System.out.println("You have created a Mac Checkbox.");
    }
}

// Concrete Factory 1
public class WinFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new WinButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WinCheckbox();
    }
}

// Concrete Factory 2
public class MacFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new MacButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new MacCheckbox();
    }
}
