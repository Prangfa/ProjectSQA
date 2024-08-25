import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class AbstractFactoryTest {

    @Test
    public void testAnimalFactory() {
        AbstractFactory<Animal> animalFactory = (AbstractFactory<Animal>) FactoryProvider.getFactory("Animal");
        
        assertNotNull(animalFactory);

        Animal dog = animalFactory.create("Dog");
        assertEquals("Dog", dog.getType());
        assertEquals("Bark", dog.makeSound());

        Animal cat = animalFactory.create("Cat");
        assertEquals("Cat", cat.getType());
        assertEquals("Meow", cat.makeSound());
    }

    @Test
    public void testColorFactory() {
        AbstractFactory<Color> colorFactory = (AbstractFactory<Color>) FactoryProvider.getFactory("Color");

        assertNotNull(colorFactory);

        Color white = colorFactory.create("White");
        assertEquals("White", white.getColor());

        Color black = colorFactory.create("Black");
        assertEquals("Black", black.getColor());
    }
}
