// FactoryProducer.java
public class FactoryProducer {
    public static GUIFactory getFactory(String osType) {
        if (osType == null) {
            return null;
        }
        if (osType.equalsIgnoreCase("MAC")) {
            return new MacFactory();
        } else if (osType.equalsIgnoreCase("WINDOWS")) {
            return new WindowsFactory();
        }
        return null;
    }
}
