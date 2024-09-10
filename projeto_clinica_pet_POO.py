import os
import sys
from arquivos import gravacao_leitura # Importa o arquivo gravacao_leitura.py que está na pasta arquivos


# Adiciona o diretório dos arquivos do projeto ao sys.path
diretorio_base = os.path.dirname(os.path.abspath(__file__)) # Converte diretório em caminho absoluto
print(f"Diretório dos arquivos: {diretorio_base}")
sys.path.append(diretorio_base) # Add diretório base ao sys (sys.path é lista dos módulos a serem importados)

# Verificação se importação foi bem sucedida
try:
    from arquivos import gravacao_leitura
    print("Importação bem-sucedida!")
except ImportError as e:
    print(f"Erro de importação: {e}")

gravacao_leitura.inicializar_arquivos() # Cria arquivos txt se não existirem

# Classe para registro dos pets
class DataPet:
    def __init__(self, responsavel='', nome='', especie='', raca='', sexo='') -> None:
        self._responsavel = responsavel
        self._nome = nome
        self._especie = especie
        self._raca = raca
        self._sexo = sexo
        
    def __str__(self):
        return (f"Responsável: {self._responsavel},\n Nome: {self._nome},\n Espécie: {self._especie},\n Raça: {self._raca},\n Sexo: {self._sexo}")

    @property
    def responsavel(self):
        return self._responsavel
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def especie(self):
        return self._especie
    
    @property
    def raca(self):
        return self._raca
    
    @property
    def sexo(self):
        return self._sexo


    @responsavel.setter
    def responsavel(self, valor):
        self._responsavel = valor
        
    @nome.setter
    def nome(self, valor):
        self._nome = valor
        
    @especie.setter
    def especie(self, valor):
        self._especie = valor
        
    @raca.setter
    def raca(self, valor):
        self._raca = valor
    
    # Setar valor como macho ou fêmea a partir daqui    
    @sexo.setter
    def sexo(self, valor):
        if valor.upper() == 'M':
            self._sexo = 'macho'
        elif valor.upper() == 'F':
            self._sexo = 'fêmea'
        else:
            raise ValueError("Sexo inválido. Use 'M' para macho ou 'F' para fêmea.")


# Classe para registro de triagem / avaliação dos pets
class TriagemPet(DataPet):
    def __init__(self, responsavel, nome, especie, raca, sexo, sintomas, diagnostico, exames, medicacao, hora) -> None:
        super().__init__(responsavel, nome, especie, raca, sexo)
        self._responsavel = responsavel
        self._nome = nome
        self._especie = especie
        self._raca = raca
        self._sexo = sexo
        self._sintomas = sintomas
        self._diagnostico = diagnostico
        self._exames = exames
        self._medicacao = medicacao
        self._hora = hora
    
    def __str__(self):
        return (f"Responsável: {self._responsavel},\n Nome: {self._nome},\n Espécie: {self._especie},\n Raça: {self._raca},\n Sexo: {self._sexo},\n Sintomas: {self._sintomas},\n Diagnóstico: {self._diagnostico},\n Exames: {self._exames},\n Medicação: {self._medicacao},\n Hora: {self._hora}")
    
    @property
    def sintomas(self):
        return self._sintomas
    
    @property
    def diagnostico(self):
        return self._diagnostico
    
    @property
    def exames(self):
        return self._exames
    
    @property
    def medicacao(self):
        return self._medicacao
    
    @property
    def hora(self):
        return self._hora

    @sintomas.setter
    def sintomas(self, valor):
        self._sintomas = valor
        
    @diagnostico.setter
    def diagnostico(self, valor):
        self._diagnostico = valor
        
    @exames.setter
    def exames(self, valor):
        self._exames = valor
        
    @medicacao.setter
    def medicacao(self, valor):
        self._medicacao = valor
        
    @hora.setter
    def hora(self, valor):
        self._hora = valor


# Classe para interface, número inputado retornará self com função correspondente        
class Menu():
    def __init__(self) -> None:
        self._opcao = {
            '1': self.cadastrar_animal,
            '2': self.buscar_cadastro,
            '3': self.triagem,
            '4': self.buscar_triagem,
            '5': self.avaliacao,
            '6': self.buscar_triagem,
            '7': self.arquivar,
            '8': self.buscar_arquivo,
            '9': self.deletar_arquivo,
            '0': self.sair}
        self.title = """\n\n*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*\n*===*===*===*===*===*===*===*===*===*===*===*Clínica Pet Saúde*===*===*===*===*===*===*===*===*===*===*===*\n*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*\n\n"""
    
    
    def exibir_menu(self):
        print(self.title)
        print(("""Escolha uma opção:                                                         :--:        ---:                     
                                                                          =+++++:    :+++++=                
                                                                         =+++++++   :+++++++-                     
                [1] Cadastrar novo animal                                ++++++++   :+++++++=             
                [2] Buscar registro do animal                    -=+=-    =+++++:    -+++++=    -=+=-     
                [3] Triagem do animal                           -++++++-    :::        :::    -++++++:  
                [4] Buscar triagem do animal                    :+++++++                      :+++++++: 
                [5] Avaliação médica                             -+++++=     :-==++++==-:     =++++=:    
                [6] Buscar avaliação médica                         ::    :=++++++++++++++=:    ::  
                [7] Arquivar atendimento                                -++++++= =++= =+++++=:  
                [8] Buscar atendimento arquivado                      :+++++++:        :++++++=:        
                [9] Deletar atendimento arquivado                    =++++++++-        -++++++++-  
                [0] Sair                                            -++++++++++=:    -=++++++++++- 
                                                                    =+++++++++++++==+++++++++++++= 
                                                                    -++++++++++++++++++++++++++++:      
                                                                     :-=++=-:            :-=++=- 
                """))                                            
    
    
    # Função para executar a função correspondente ao nº do input
    def executar_opcao(self, opcao):
        funcao = self._opcao.get(opcao) # Pega a função correspondente a opção
        if funcao:
            funcao() # retorna a função
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    
    
    # Função para cadastrar animal        
    def cadastrar_animal(self):
        print(self.title)
        responsavel = input("Digite o nome do responsável pelo animal: ").title()
        nome = input("Digite o nome do animal: ").title()
        especie = input("Digite a espécie do animal: ").title()
        raca = input("Digite a raça do animal: ").title()
        # Atribui a classe DataPet para um "objeto"
        cadastro_pet = DataPet(responsavel, nome, especie, raca, sexo="") # Sexo do animal será setado abaixo
        while True: # testa de acordo com o setter
            try:
                sexo = input("Digite o sexo do animal (M/F): ")
                cadastro_pet.sexo = sexo 
                break
            except ValueError as e:
                print(e) # Retorna qual o erro          
        print(cadastro_pet) # Chama str da classe
        # Chama função do arquivo gravacao_leitura.py
        gravacao_leitura.registrar_cadastro(cadastro_pet.responsavel, cadastro_pet.nome, cadastro_pet.especie, cadastro_pet.raca, cadastro_pet.sexo)
  
    
    # Função para buscar cadastro do animal
    def buscar_cadastro(self):
        print(self.title)
        responsavel = input("Digite o nome do responsável pelo animal: ").title()
        nome = input("Digite o nome do animal: ").title()
        # Chama função do arquivo gravacao_leitura.py
        gravacao_leitura.buscar_cadastro(responsavel, nome)
 
    
    # Função para registrar triagem do animal
    def triagem(self):
        print(self.title)
        responsavel = input("Digite o nome do responsável pelo animal: ").title()
        nome = input("Digite o nome do animal: ").title()
        # Verifica se o cadastro existe com esses dados
        cadastro = gravacao_leitura.buscar_cadastro(responsavel, nome)
        # Se cadastro não existir
        if cadastro is None:
            print("Cadastro não encontrado.")
            return      
        # Se cadastro existir prossegue daqui e pega os índices do cadastro e pede sintomas
        especie = cadastro[2]
        raca = cadastro[3]
        sexo = cadastro[4]
        sintomas = input("Quais os sintomas do animal? ")
        diagnostico = "None"
        exames = "None"
        medicacao = "None"
        # Chama função do arquivo gravacao_leitura.py
        hora = gravacao_leitura.registrar_data_hora()
        # Atribui a classe TriagemPet para um "objeto"
        triagem_pet = TriagemPet(responsavel, nome, especie, raca, sexo, sintomas, diagnostico, exames, medicacao, hora)
        print(triagem_pet) # Chama str 
        # Chama função do arquivo gravacao_leitura.py
        gravacao_leitura.registrar_triagem(triagem_pet.responsavel, triagem_pet.nome, triagem_pet.especie, triagem_pet.raca, triagem_pet.sexo, triagem_pet.sintomas, triagem_pet.hora)   

    
    # Função para buscar triagem 
    def buscar_triagem(self):
        print(self.title)
        responsavel = input("Digite o nome do responsável pelo animal: ").title()
        nome = input("Digite o nome do animal: ").title()
        # Chama função do arquivo gravacao_leitura.py
        gravacao_leitura.buscar_triagem(responsavel, nome)


    # Função para fazer avaliação do animal após triagem
    def avaliacao(self):
        print(self.title)
        responsavel = input("Digite o nome do responsável pelo animal: ").title()
        nome = input("Digite o nome do animal: ").title()
        # Chama função do arquivo gravacao_leitura.py
        # Se não encontrar cadastro
        if not gravacao_leitura.validar_cadastro(responsavel, nome):
            print("Cadastro não encontrado.")
            return
        # Se encontrar cadastro
        # Chama função do arquivo gravacao_leitura.py e atribui variável
        triagem = gravacao_leitura.buscar_triagem(responsavel, nome)
        # Utiliza os índices do resultado da busca
        especie = triagem[1]
        raca = triagem[2]
        sexo = triagem[3]
        sintomas = triagem[4]
        diagnostico = input("Qual o diagnóstico para o animal? ")
        exames = input("O animal necessita de exames? Quais? ")
        medicacao = input("O animal necessita de medicações? Quais? ")
        # Chama função do arquivo gravacao_leitura.py
        hora = gravacao_leitura.registrar_data_hora()
        # Atribui a classe TriagemPet para um "objeto"
        avaliacao_pet = TriagemPet(responsavel, nome, especie, raca, sexo, sintomas, diagnostico, exames, medicacao, hora)
        print(avaliacao_pet) # Chama str da classe
        # Chama função do arquivo gravacao_leitura.py
        gravacao_leitura.atualizar_dados(avaliacao_pet.responsavel, avaliacao_pet.nome, avaliacao_pet.especie, avaliacao_pet.raca, avaliacao_pet.sexo, avaliacao_pet.sintomas, avaliacao_pet.diagnostico, avaliacao_pet.exames, avaliacao_pet.medicacao, avaliacao_pet.hora)
    
    
    # Função para arquivar registro da triagem / avaliação    
    def arquivar(self):
        print(self.title)
        responsavel = input("Digite o nome do responsável pelo animal: ").title()
        nome = input("Digite o nome do animal: ").title()
        # Chama função do arquivo gravacao_leitura.py
        gravacao_leitura.arquivar(responsavel, nome)


    # Função para buscar arquivo
    def buscar_arquivo(self):
        print(self.title)
        responsavel = input("Digite o nome do responsável pelo animal: ").title()
        nome = input("Digite o nome do animal: ").title()
        # Chama função do arquivo gravacao_leitura.py
        gravacao_leitura.buscar_arquivo(responsavel, nome)


    # Função para deletar registro do arquivo
    def deletar_arquivo(self):
        print(self.title)
        responsavel = input("Digite o nome do responsável pelo animal: ").title()
        nome = input("Digite o nome do animal: ").title()
        # Chama função do arquivo gravacao_leitura.py
        gravacao_leitura.deletar_arquivo(responsavel, nome)


    
    def sair(self):
        print("Saindo...")
        exit()    
     
              
def main():
    # Atribui a classe Menu para um "objeto"
    menu = Menu()
    while True:
        # Chama função para exibir menu da classe Menu
        menu.exibir_menu()
        opcao = input("Escolha uma opção: ")
        # Chama função da classe Menu que chama a função correspondente ao nº inputado
        menu.executar_opcao(opcao)


# Se o arquivo for o principal, se for rodado diretamente, chama função main para iniciar o loop
if __name__ == "__main__":
    main()