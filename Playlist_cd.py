import random

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
        while not titulo.strip():
            print("\nEntrada inválida. Tente novamente:")
            print("\nDeseja continuar ou voltar para o menu? (c/m)")
            opc1 = input("\nDigite sua opção: ")
            if opc1 == 'c':
                titulo = input("\nNome da música: ")
            elif opc1 == 'm':
                print("\nVoltando para o menu...")
                return
            else:
                print("\nOpção inválida!")    
        artista = input("\nNome do artista: ")
        while not artista.strip():
            print("\nEntrada inválida. Tente novamente:")
            print("\nDeseja continuar ou voltar para o menu? (c/m)")
            opc2 = input("\nDigite sua opção: ")
            if opc2 == 'c':
                artista = input("\nNome do artista: ")
            elif opc2 == 'm':
                print("\nVoltando para o menu...")
                return
            else:
                print("\nOpção inválida!")    
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
        while not titulo.strip():
            print("\nEntrada vazia. Tente Novamente:")
            print("\nDeseja continuar ou voltar para o menu? (c/m)")
            opc3 = input("\nDigite sua opção: ")
            if opc3 == 'c':
                titulo = input("\nNome da música: ")
            elif opc3 == 'm':
                print("\nVoltando para o menu...")
                return
            else:
                print("\nOpção inválida")    
        artista = input("\nNome do artista: ")
        while not artista.strip():
            print("\nEntrada vazia. Tente Novamente:")
            print("\nDeseja continuar ou voltar para o menu? (c/m)")
            opc4 = input("\nDigite sua opção: ")
            if opc4 == 'c':
                artista = input("\nNome do artista: ")
            elif opc4 == 'm':
                print("\nVoltando para o menu...")
                return
            else:
                print("\nOpção inválida!")    
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

    def shuffle(self):
        if not self.head:
            print("\nA playlist está vazia!")
            return
        musicas = []
        current_node = self.head
        while current_node:
            musicas.append(current_node)
            current_node = current_node.next
        random.shuffle(musicas)
        self.head = musicas[0]
        self.head.prev = None
        self.tail = musicas[-1]
        self.tail.next = None
        for i in range(len(musicas)-1):
            musicas[i].next = musicas[i+1]
            musicas[i+1].prev = musicas[i]
        print("\nPlaylist embaralhada com sucesso!")                    

playlist = Playlist()

while True:
    print("\n=====================================")
    print("                MENU:")
    print("\n1 - Adicionar música")
    print("2 - Deletar música")
    print("3 - Exibir playlist")
    print("4 - Embaralhar playlist")
    print("5 - Sair do menu")
    print("\n=====================================")
    opc = int(input("\nDigite o valor da sua opção: "))
    if opc == 1:
        playlist.adc_mus()
    elif opc == 2:
        playlist.apg_mus()
    elif opc == 3:
        playlist.ver_playlist()
    elif opc == 4:
        playlist.shuffle()        
    elif opc == 5:
        print("\nAté a próxima!")
        break
    else:
        print("\nOpção Inválida! Tente Novamente.")    