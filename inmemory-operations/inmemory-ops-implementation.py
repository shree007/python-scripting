class inMemory:
    def __init__(self):
        self.store = {}

    def add(self, key, value):
        self.store[key]=value
        return f"key '{key}' has been added"
    
    def get(self, key):
        if key in self.store:
            return self.store[key]
        return f"key '{key}' is not found"


if __name__ =='__main__':
    db = inMemory()
    print(db.add("hello",9))
    print(db.get("hello"))