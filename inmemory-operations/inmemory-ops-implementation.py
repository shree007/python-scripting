class inMemory:
    def __init__(self):
        self.store = {}

    def add(self, key, value):
        self.store[key]=value
        return f"key '{key}' has been added"


if __name__ =='__main__':
    db = inMemory()
    print(db.add("hello",9))