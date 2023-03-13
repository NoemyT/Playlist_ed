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

    def apg_mus(self):
        titulo = input("\nNome da música: ")
        artista = input("Nome do artista: ")
        current_node = self.head
        while current_node:
            if current_node.titulo == titulo and current_node.artista == artista:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.next
                print(f"\n{titulo} - {artista} deletada da playlist!")
                return
            current_node = current_node.next
        print("\nA música não está na playlist!")
                                        