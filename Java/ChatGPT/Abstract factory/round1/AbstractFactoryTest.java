import org.junit.Test;
import static org.junit.Assert.*;

public class AbstractFactoryTest {

    @Test
    public void testWinFactory() {
        GUIFactory factory = new WinFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();

        assertTrue(button instanceof WinButton);
        assertTrue(checkbox instanceof WinCheckbox);
    }

    @Test
    public void testMacFactory() {
        GUIFactory factory = new MacFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();

        assertTrue(button instanceof MacButton);
        assertTrue(checkbox instanceof MacCheckbox);
    }

    @Test
    public void testApplicationWithWinFactory() {
        GUIFactory factory = new WinFactory();
        Application app = new Application(factory);

        assertTrue(app != null);
    }

    @Test
    public void testApplicationWithMacFactory() {
        GUIFactory factory = new MacFactory();
        Application app = new Application(factory);

        assertTrue(app != null);
    }
}
