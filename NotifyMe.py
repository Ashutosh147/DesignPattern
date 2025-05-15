"""
🧩 Problem Statement
When a product is out of stock on Amazon, users can click a "Notify Me" button to get notified once the product is back in stock.

Design a system where:

Users can subscribe to a product.

When the product is restocked, all subscribed users are notified.

Use the Observer Design Pattern to implement the solution.

🧠 Design Pattern: Observer
Subject (Product): Keeps track of observers and notifies them of state changes (stock availability).

Observer (User): Wants to be notified when the subject changes.

🏗️ Classes Overview
Class	Role
User	Observer who wants to be notified
Product	Subject being observed

✅ 1. Clarify the Requirements
Start by asking questions to remove ambiguity:

"Before jumping in, let me confirm the requirements."

Users can subscribe to get notified when a product is out of stock.

Once the product is back in stock, notify all subscribed users.

Notifications are one-way (no need for real-time chat).

Should users be notified only once or every time the product is restocked?

Do we need to persist subscriptions (e.g., DB), or is in-memory okay for now?

Interviewer might say:

“In-memory is fine for now.”

“Only notify once per restock.”

✅ 2. High-Level Design / Core Components
Explain the key objects you’ll need:

a. Product (Subject):
Holds state (e.g., in stock / out of stock).

Has a list of subscribed users.

Notifies them when the state changes to in-stock.

b. User (Observer):
Can subscribe to products.

Gets notified when the product is restocked.

c. Relationship:
"This is a classic case of the Observer Design Pattern."

Subject → Notifies observers when a state change occurs.

Observers → React when notified (e.g., show message, send email).

✅ 3. Why Observer Pattern?
"Observer pattern is ideal here because:"

We want to decouple the Product from the notification logic.

New users can subscribe/unsubscribe without changing the Product code.

It allows for scalability (adding other observers like Email/SMS later).

✅ 4. Low-Level Design (LLD)
“Let me describe the classes I’d use.”

🧱 Observer (Interface)
Method: update(product_name)

👤 User implements Observer
Properties: name

Method: update prints or sends a notification.

📦 Subject (Interface)
Methods: register_observer, remove_observer, notify_observers

📦 Product implements Subject
Properties: name, in_stock, observers[]

Methods:

register_observer(user)

remove_observer(user)

set_stock_status(in_stock: bool)

notify_observers()

✅ 5. Sample Workflow
Explain this flow clearly:

Product is out of stock.

Users subscribe to it.

Product is updated as in-stock.

All observers (users) are notified via update() method.

"""




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
