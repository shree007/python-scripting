class inMemory:
    def __init__(self):
        self.store = {}

    def add(self, key, value):
        self.store[key]=value
        print(f"key '{key}' has been added")
        print("In memory after addition",self.store)
    
    def get(self, key):
        if key in self.store:
            return self.store[key]
        print(f"key '{key}' is not found")
        print("In memory after fetch",self.store)
    
    def delete(self,key):
        if key in self.store:
            del self.store[key]
            print(f"key '{key}' has been deleted")
        print(f"key '{key}' has not found ")
        print("In memory after delete",self.store)

def perform_db_ops(db_operation,key,value):
     db = inMemory()
     match db_operation:
        case "add":
            db.add(key,value)
        case "get":
            db.get(key)
        case "delete":
            deb.delete(key)
        case _:
            print(f"Invalid '{db_operation}' in memory operations")


if __name__ =='__main__':
    try:
        key = input("Enter key").strip()
        value = input("Enter value").strip()
        db_operation = input("Enter db operation you want to perform").strip()
        perform_db_ops(db_operation,key,value)
    except Exception as e:
        print("Invalid operations", e)
