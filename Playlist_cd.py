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