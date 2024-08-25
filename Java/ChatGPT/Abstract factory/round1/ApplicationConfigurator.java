public class ApplicationConfigurator {
    public static void main(String[] args) {
        Application app;
        GUIFactory factory;

        String osName = System.getProperty("os.name").toLowerCase();
        if (osName.contains("win")) {
            factory = new WinFactory();
        } else {
            factory = new MacFactory();
        }

        app = new Application(factory);
        app.paint();
    }
}
