public class Cat implements Animal {
    @Override
    public String getType() {
        return "Cat";
    }

    @Override
    public String makeSound() {
        return "Meow";
    }
}
