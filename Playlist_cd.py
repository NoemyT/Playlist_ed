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
            print("\n\033[1;33;40mEntrada inválida. Tente novamente:")
            print("\nDeseja continuar ou voltar para o menu? (c/m)")
            opc1 = input("\n\033[1;37;40mDigite sua opção: ")
            if opc1 == 'c':
                titulo = input("\nNome da música: ")
            elif opc1 == 'm':
                print("\n\033[1;33;40mVoltando para o menu...")
                return
            else:
                print("\n\033[1;31;40mOpção inválida!")    
        artista = input("\nNome do artista: ")
        while not artista.strip():
            print("\n\033[1;33;40mEntrada inválida. Tente novamente:")
            print("\nDeseja continuar ou voltar para o menu? (c/m)")
            opc2 = input("\n\033[1;37;40mDigite sua opção: ")
            if opc2 == 'c':
                artista = input("\nNome do artista: ")
            elif opc2 == 'm':
                print("\n\033[1;33;40mVoltando para o menu...")
                return
            else:
                print("\n\033[1;31;40mOpção inválida!")    
        new_node = Musica(titulo, artista)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"\n\033[1;32;40m{titulo} - {artista} adicionada a playlist!")

    def apg_mus(self):
        titulo = input("\nNome da música: ")
        while not titulo.strip():
            print("\n\033[1;33;40mEntrada vazia. Tente Novamente:")
            print("\nDeseja continuar ou voltar para o menu? (c/m)")
            opc3 = input("\n\033[1;37;40mDigite sua opção: ")
            if opc3 == 'c':
                titulo = input("\nNome da música: ")
            elif opc3 == 'm':
                print("\n\033[1;33;40mVoltando para o menu...")
                return
            else:
                print("\n\033[1;31;40mOpção inválida")    
        artista = input("\nNome do artista: ")
        while not artista.strip():
            print("\n\033[1;33;40mEntrada vazia. Tente Novamente:")
            print("\nDeseja continuar ou voltar para o menu? (c/m)")
            opc4 = input("\n\033[1;37;40mDigite sua opção: ")
            if opc4 == 'c':
                artista = input("\nNome do artista: ")
            elif opc4 == 'm':
                print("\n\033[1;33;40mVoltando para o menu...")
                return
            else:
                print("\n\033[1;31;40mOpção inválida!")    
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
                    self.tail = current_node.prev
                print(f"\n\033[1;31;40m{titulo} - {artista} deletada da playlist!")
                return
            current_node = current_node.next
        print("\n\033[1;33;40mA música não está na playlist!")

    def ver_playlist(self):
        if not self.head:
            print("\n\033[1;33;40mA playlist está vazia.")
            return
        current_node = self.head
        print("\n\033[1;34;40mMúsicas na playlist:")
        while current_node:
            print(f"\n\033[1;32;40m{current_node.titulo} - {current_node.artista}")
            current_node = current_node.next

    def shuffle(self):
        if not self.head:
            print("\n\033[1;33;40mA playlist está vazia!")
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
        print("\n\033[1;32;40mPlaylist embaralhada com sucesso!")

    def busc_mus(self):
        buscar = input("\nO que está procurando?: ")
        while not buscar.strip():
            print("\n\033[1;33;40mEntrada vazia! Tente novamente: ")
            print("\nDeseja continuar ou voltar para o menu? (c/m)")
            opc5 = input("\n\033[1;37;40mDigite sua opção: ")
            if opc5 == 'c':
                buscar = input("\n\033[1;37;40mO que está procurando?: ")
            elif opc5 == 'm':
                print("\n\033[1;33;40mVoltando para o menu...")
                return
        print("\n\033[1;34;40mMúsicas na playlist:")
        current_node = self.head
        if current_node == None: print("\n\033[1;33;40mA playlist está vazia!")
        while current_node:
            if buscar in current_node.titulo or buscar in current_node.artista:
                print(f"\n\033[1;32;40m{current_node.titulo} - {current_node.artista}")
            current_node = current_node.next    

def menu():
    print("\n\033[1;36;40m=====================================")
    print("                MENU:")
    print("\n1 - Adicionar música")
    print("2 - Deletar música")
    print("3 - Exibir playlist")
    print("4 - Embaralhar playlist")
    print("5 - Buscar na playlist")
    print("6 - Sair do menu")
    print("\n=====================================")

    while True:
        try:
            opc = int(input("\n\033[1;37;40mDigite o valor da sua opção: "))
            if opc in range(1, 7):
                return opc
            print("\n\033[1;33;40mOpção inválida. Tente novamente.")
        except ValueError:
            print("\n\033[1;33;40mEntrada inválida. Tente novamente.")

if __name__ == "__main__":
    playlist = Playlist()

while True:
    opc = menu()
    if opc == 1:
        playlist.adc_mus()
    elif opc == 2:
        playlist.apg_mus()
    elif opc == 3:
        playlist.ver_playlist()
    elif opc == 4:
        playlist.shuffle()
    elif opc == 5:
        playlist.busc_mus()            
    elif opc == 6:
        print("\n\033[1;34;40mAté a próxima!")
        print("\033[1;37;40m")
        break      