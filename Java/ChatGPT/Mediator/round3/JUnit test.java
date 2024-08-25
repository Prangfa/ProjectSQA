// ApplicationTest.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class ApplicationTest {

    @Test
    public void testWindowsFactory() {
        GUIFactory factory = new WindowsFactory();
        Application app = new Application(factory);
        
        // Testing WindowsButton and WindowsCheckbox
        assertTrue(factory.createButton() instanceof WindowsButton);
        assertTrue(factory.createCheckbox() instanceof WindowsCheckbox);
    }

    @Test
    public void testMacOSFactory() {
        GUIFactory factory = new MacOSFactory();
        Application app = new Application(factory);
        
        // Testing MacOSButton and MacOSCheckbox
        assertTrue(factory.createButton() instanceof MacOSButton);
        assertTrue(factory.createCheckbox() instanceof MacOSCheckbox);
    }
}
