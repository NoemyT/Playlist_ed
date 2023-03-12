class Musica:
    def __init__(self, titulo, artista, prev=None, next=None):
        self.titulo = titulo
        self.artista = artista
        self.prev = prev
        self.next = next

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def adc_mus(self):
        titulo = input("\nNome da música: ")
        artista = input("Nome do artista: ")
        new_node = Musica(titulo, artista)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"\n{titulo} - {artista} adicionada a playlist!")        