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

    def ver_playlist(self):
        if not self.head:
            print("\nA playlist está vazia.")
            return
        current_node = self.head
        while current_node:
            print(f"\n{current_node.titulo} by {current_node.artista}")
            current_node = current_node.next    

playlist = Playlist()

while True:
    print("\n=====================================")
    print("                MENU:")
    print("\n1 - Adicionar música")
    print("2 - Deletar música")
    print("3 - Exibir playlist")
    print("4 - Sair do menu")
    print("\n=====================================")
    opc = int(input("\nDigite o valor da sua opção: "))
    if opc == 1:
        playlist.adc_mus()
    elif opc == 2:
        playlist.apg_mus()
    elif opc == 3:
        playlist.ver_playlist()    
    elif opc == 4:
        print("\nAté a próxima!")
        break
    else:
        print("\nOpção Inválida! Tente Novamente.")    