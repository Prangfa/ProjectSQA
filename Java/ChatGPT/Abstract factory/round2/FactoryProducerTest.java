// FactoryProducerTest.java
import org.junit.Test;
import static org.junit.Assert.*;

public class FactoryProducerTest {

    @Test
    public void testMacFactory() {
        GUIFactory factory = FactoryProducer.getFactory("MAC");
        assertNotNull("Factory should not be null for MAC", factory);
        assertTrue("Factory should be instance of MacFactory", factory instanceof MacFactory);
        
        Button button = factory.createButton();
        assertNotNull("Button should not be null", button);
        assertTrue("Button should be instance of MacButton", button instanceof MacButton);
        button.paint(); // Optional: Observe the output
        
        Checkbox checkbox = factory.createCheckbox();
        assertNotNull("Checkbox should not be null", checkbox);
        assertTrue("Checkbox should be instance of MacCheckbox", checkbox instanceof MacCheckbox);
        checkbox.paint(); // Optional: Observe the output
    }

    @Test
    public void testWindowsFactory() {
        GUIFactory factory = FactoryProducer.getFactory("WINDOWS");
        assertNotNull("Factory should not be null for WINDOWS", factory);
        assertTrue("Factory should be instance of WindowsFactory", factory instanceof WindowsFactory);
        
        Button button = factory.createButton();
        assertNotNull("Button should not be null", button);
        assertTrue("Button should be instance of WindowsButton", button instanceof WindowsButton);
        button.paint(); // Optional: Observe the output
        
        Checkbox checkbox = factory.createCheckbox();
        assertNotNull("Checkbox should not be null", checkbox);
        assertTrue("Checkbox should be instance of WindowsCheckbox", checkbox instanceof WindowsCheckbox);
        checkbox.paint(); // Optional: Observe the output
    }

    @Test
    public void testUnknownFactory() {
        GUIFactory factory = FactoryProducer.getFactory("LINUX");
        assertNull("Factory should be null for unknown OS type", factory);
    }
    
    @Test
    public void testNullFactory() {
        GUIFactory factory = FactoryProducer.getFactory(null);
        assertNull("Factory should be null when OS type is null", factory);
    }
}
