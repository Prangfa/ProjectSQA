// Main.java
public class Main {
    public static void main(String[] args) {
        GUIFactory factory;
        String osName = System.getProperty("os.name").toLowerCase();
        
        if (osName.contains("win")) {
            factory = new WindowsFactory();
        } else {
            factory = new MacOSFactory();
        }

        Application app = new Application(factory);
        app.paint();
    }
}
