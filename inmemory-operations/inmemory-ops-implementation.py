class InMemory:
    def __init__(self):
        self.store = {}

    def add(self, key, value):
        self.store[key] = value
        print(f"Key '{key}' has been added.")
        print("In-memory after addition:", self.store)

    def get(self, key):
        if key in self.store:
            print(f"Value for key '{key}': {self.store[key]}")
        else:
            print(f"Key '{key}' is not found.")
        print("In-memory after fetch:", self.store)

    def delete(self, key):
        if key in self.store:
            del self.store[key]
            print(f"Key '{key}' has been deleted.")
        else:
            print(f"Key '{key}' is not found.")
        print("In-memory after delete:", self.store)


def perform_db_ops(db, db_operation, key, value=None):
    match db_operation:
        case "add":
            db.add(key, value)
        case "get":
            db.get(key)
        case "delete":
            db.delete(key)
        case _:
            print(f"Invalid operation '{db_operation}'")


if __name__ == '__main__':
    db = InMemory()
    print("In-memory database is running. Type 'cancel' to exit.")

    while True:
        try:
            db_operation = input("\nEnter operation (add/get/delete) or type 'cancel' to exit: ").strip().lower()
            if db_operation == "cancel":
                print("Exiting the in-memory database.")
                break
            key = input("Enter key: ").strip()
            value = None
            if db_operation == "add":
                value = input("Enter value: ").strip()
            perform_db_ops(db, db_operation, key, value)
        except Exception as e:
            print("Error:", e)