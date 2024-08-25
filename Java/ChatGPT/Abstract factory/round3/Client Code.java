public class FurnitureShop {
    private Chair chair;
    private Sofa sofa;

    public FurnitureShop(FurnitureFactory factory) {
        chair = factory.createChair();
        sofa = factory.createSofa();
    }

    public void furnish() {
        chair.sitOn();
        sofa.lieOn();
    }
}
