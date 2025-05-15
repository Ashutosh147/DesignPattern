from typing import List

# Observer Interface
class Observer:
    def update(self, product_name: str):
        raise NotImplementedError("Subclass must implement update method")

# Concrete Observer
class User(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, product_name: str):
        print(f"[Notification to {self.name}] The product '{product_name}' is now back in stock!")

# Subject Interface
class Subject:
    def register_observer(self, observer: Observer):
        raise NotImplementedError

    def remove_observer(self, observer: Observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError

# Concrete Subject
class Product(Subject):
    def __init__(self, name: str):
        self.name = name
        self.in_stock = False
        self._observers: List[Observer] = []

    def register_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"[System] {observer.name} subscribed to '{self.name}'")

    def remove_observer(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"[System] {observer.name} unsubscribed from '{self.name}'")

    def notify_observers(self):
        print(f"[System] Notifying {len(self._observers)} user(s) about '{self.name}'...")
        for observer in self._observers:
            observer.update(self.name)

    def set_stock_status(self, in_stock: bool):
        self.in_stock = in_stock
        if in_stock:
            print(f"[System] '{self.name}' is now in stock!")
            self.notify_observers()
        else:
            print(f"[System] '{self.name}' is now out of stock.")

# Test the functionality
if __name__ == "__main__":
    # Create product
    ps5 = Product("PlayStation 5")

    # Create users
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Users subscribe to the product
    ps5.register_observer(alice)
    ps5.register_observer(bob)

    # Product goes out of stock
    ps5.set_stock_status(False)

    # Charlie subscribes later
    ps5.register_observer(charlie)

    # Product comes back in stock
    ps5.set_stock_status(True)
