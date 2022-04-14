class noeud:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __getitem__(self, key):
        noeud = self.get(key)
        if node:
            return noeud

    def get(self, data):
        if data < self.data:
            return self.left.get(data) if self.left else None
        elif data > self.data:
            return self.right.get(data) if self.right else None
        return self

    def insert(self, data):