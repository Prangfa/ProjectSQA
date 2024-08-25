import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class FurnitureShopTest {

    @Test
    public void testVictorianFurniture() {
        FurnitureFactory factory = new VictorianFurnitureFactory();
        FurnitureShop shop = new FurnitureShop(factory);
        shop.furnish();
        // Assert if no exception is thrown, code is executed
        assertDoesNotThrow(() -> shop.furnish());
    }

    @Test
    public void testModernFurniture() {
        FurnitureFactory factory = new ModernFurnitureFactory();
        FurnitureShop shop = new FurnitureShop(factory);
        shop.furnish();
        // Assert if no exception is thrown, code is executed
        assertDoesNotThrow(() -> shop.furnish());
    }

    @Test
    public void testFurnitureCreation() {
        FurnitureFactory victorianFactory = new VictorianFurnitureFactory();
        FurnitureFactory modernFactory = new ModernFurnitureFactory();

        Chair victorianChair = victorianFactory.createChair();
        Sofa victorianSofa = victorianFactory.createSofa();
        Chair modernChair = modernFactory.createChair();
        Sofa modernSofa = modernFactory.createSofa();

        assertTrue(victorianChair instanceof VictorianChair);
        assertTrue(victorianSofa instanceof VictorianSofa);
        assertTrue(modernChair instanceof ModernChair);
        assertTrue(modernSofa instanceof ModernSofa);
    }
}
