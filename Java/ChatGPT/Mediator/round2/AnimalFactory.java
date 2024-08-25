public class AnimalFactory implements AbstractFactory<Animal> {
    @Override
    public Animal create(String type) {
        if ("Dog".equalsIgnoreCase(type)) {
            return new Dog();
        } else if ("Cat".equalsIgnoreCase(type)) {
            return new Cat();
        }
        return null;
    }
}
