from abc import ABC, abstractmethod

# Abstract Product A
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

# Concrete Product A1
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian Chair"

# Concrete Product A2
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern Chair"

# Abstract Product B
class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

# Concrete Product B1
class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian Sofa"

# Concrete Product B2
class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a Modern Sofa"

# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

# Concrete Factory 1
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

# Concrete Factory 2
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

# Client code
def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(chair.sit_on())
    print(sofa.lie_on())

# Client can now create families of products
if __name__ == "__main__":
    # Using Victorian Furniture
    victorian_factory = VictorianFurnitureFactory()
    client_code(victorian_factory)

    print("\n")

    # Using Modern Furniture
    modern_factory = ModernFurnitureFactory()
    client_code(modern_factory)
