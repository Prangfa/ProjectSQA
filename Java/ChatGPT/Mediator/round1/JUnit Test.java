import org.junit.Test;
import static org.junit.Assert.*;

public class AbstractFactoryTest {

    @Test
    public void testWindowsFactory() {
        GUIFactory factory = new WindowsFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();

        assertTrue(button instanceof WindowsButton);
        assertTrue(checkbox instanceof WindowsCheckbox);
    }

    @Test
    public void testMacOSFactory() {
        GUIFactory factory = new MacOSFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();

        assertTrue(button instanceof MacOSButton);
        assertTrue(checkbox instanceof MacOSCheckbox);
    }
}
