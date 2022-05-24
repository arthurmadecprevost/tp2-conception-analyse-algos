class Noeud:

    def __init__(self, data):
        self.data = data
        self.gauche = None
        self.droite = None
        self.parent = None

    def __getitem__(self, key):
        noeud = self.get(key)
        if node:
            return noeud

    def __str__(self):
        return str(self.data)

    def get(self, data):
        if data < self.data:
            return self.gauche.get(data) if self.gauche else None
        elif data > self.data:
            return self.droite.get(data) if self.droite else None
        return self

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                self.left.parent = self
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                self.right.parent = self
            else:
                self.right.insert(data)

def abr_filiforme(p, data):
    noeud =  Noeud(data[0])
    if(data[1]> noeud.data):
        noeud.droite = Noeud(data[1])
        enfant = noeud.droite
    else :
        noeud.gauche = Noeud(data[1])
        enfant = noeud.gauche
    for i in range(2, pow(2, p+1)-1):
        if(data[i]> data[i-1]):
            enfant.droite = Noeud(data[i])
            enfant = enfant.droite
        else :
            enfant.gauche = Noeud(data[i])
            enfant = enfant.gauche
        
    return noeud

r = abr_filiforme(2, [10, 20, 1, 150, 45, 69999, 54])

print(r)