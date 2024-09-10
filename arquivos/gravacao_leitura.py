from datetime import datetime
import os


# Se os arquivos txt não existirem na pasta arquivos cria os arquivos txt
def inicializar_arquivos(nome_pasta='arquivos'):
    pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), '') # Encontra o caminho da pasta arquivos
    arquivos = ['cadastro.txt', 'triagem.txt', 'arquivo.txt']
    # Itera os arquivos na pasta
    for arquivo in arquivos:
        # Caminho completo de cada arquivo txt dentro da pasta
        caminho_arquivo = os.path.join(pasta, arquivo)
        # Verifica se o arquivo txt existe, se não, cria um arquivo vazio
        if not os.path.exists(caminho_arquivo):
            try:
                with open(caminho_arquivo, 'w') as f:
                    pass  # Cria o arquivo vazio
                print(f"Arquivo criado: {caminho_arquivo}")
            except PermissionError as e: # Caso dê erro
                print(f"Erro ao criar o arquivo {caminho_arquivo}: {e}") # Retorna o erro

       
# Diretório principal
diretorio_base = os.path.dirname(os.path.abspath(__file__))
# Caminho para a pasta 'arquivos'
pasta = os.path.join(diretorio_base, '')
# Caminho para os arquivos .txt dentro da pasta 'arquivos'
caminho_cadastro = os.path.join(pasta, 'cadastro.txt')
caminho_triagem = os.path.join(pasta, 'triagem.txt')
caminho_arquivo = os.path.join(pasta, 'arquivo.txt')


# Registra a data e hora atuais do pc em execussão no formato dd/mm/yyyy - hh:mm.
def registrar_data_hora():
    agora = datetime.now() # Pega hora atual
    data_hora_formatada = agora.strftime('%d/%m/%Y - %H:%M') # Formata hora
    return data_hora_formatada

        
# Verifica se já existe cadastro para o mesmo responsavel e mesmo animal, é chamada dentro das funções de buscar cadastro e cadastrar         
def validar_cadastro(responsavel, nome):
    with open(caminho_cadastro, "r") as arquivo:
        for linha in arquivo: # Itera no arquivo txt
            partes = linha.strip().split(',')
            if len(partes) == 5:  # Verifica se a linha tem 5 partes
                responsavel1, nome1, especie, raca, sexo = partes # Define os indices da linha
                if responsavel.strip().title() == responsavel1.strip().title() and nome.strip().title() == nome1.strip().title():
                    return True  # Se responsável e nome da linha forem os mesmos passados pelo usuário, retorna True
    return False


# Busca o cadastro do animal no txt, se exisir retorna seus dados
def buscar_cadastro(responsavel, nome):
    # Se validar cadastro retornar False
    if not validar_cadastro(responsavel, nome):
        print("Cadastro não encontrado.")
        return
    # Se validar cadastro retornar True
    with open(caminho_cadastro, "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(',') # Define vírgula como separador das partes da linha
            if len(partes) == 5:
                responsavel1, nome1, especie, raca, sexo = partes # Define os indices da linha
                # Se responsavel, nome passados forem iguais aos da linha retorna o registro
                if responsavel.strip().title() == responsavel1.strip().title() and nome.strip().title() == nome1.strip().title():
                    print(f"Registro do animal:\n"
                      
                      f"Responsável: {responsavel1}\n"
                      f"Nome: {nome1}\n"
                      f"Espécie: {especie}\n"
                      f"Raça: {raca}\n"
                      f"Sexo: {sexo}")
                    return partes
    return None   


# Grava o cadastro do animal no txt
def registrar_cadastro(responsavel, nome, especie, raca, sexo):
    # Se já existir
    if validar_cadastro(responsavel, nome):
        print("Animal já cadastrado.")
        return
    # Se não existir
    with open(caminho_cadastro, "a") as arquivo:
        if os.path.getsize(caminho_cadastro) > 0: # Se arquivo não estiver vazio
            arquivo.write('\n')  # Adiciona nova linha apenas se o arquivo não estiver vazio
        arquivo.write(f"{responsavel},{nome},{especie},{raca},{sexo}")
    print(f"Cadastro realizado com sucesso.")
    return
    

# Verifica se já existe triagem para o mesmo responsavel e mesmo animal, é chamada dentro das funções de buscar triagem e fazer triagem         
def validar_triagem(responsavel, nome):
    with open(caminho_triagem, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            # Se linha começar e terminar com []
            if linha.startswith('[') and linha.endswith(']'):
                linha = linha[1:-1]  # Remove colchetes externos
                # Define ],[ como separador das partes para pegar partes internas das listas
                partes = linha.split('],[')         
                # Remover colchetes extras e torna partes uma lista de strings, onde cada string contém uma lista da linha
                partes = [p.strip('[]') for p in partes]
                # Divide a primeira parte por vírgulas para obter o responsável e nome
                responsavel_nome = partes[0].split(',')
                if len(responsavel_nome) >= 2:
                    responsavel1 = responsavel_nome[0].strip().strip("'").strip()
                    nome1 = responsavel_nome[1].strip().strip("'").strip()
                    # Normalizar e comparar
                    responsavel1 = responsavel1.title()
                    nome1 = nome1.title()
                    responsavel = responsavel.strip().title()
                    nome = nome.strip().title()
                    # Se responsável, nome passados forem iguais da primeira lista da linha retorna True                  
                    if responsavel == responsavel1 and nome == nome1:
                        return True
    return False


# Busca a triagem do animal, se exisir retorna seus dados
def buscar_triagem(responsavel, nome):
    # Se triagem não existir
    if not validar_triagem(responsavel, nome):
        print("Triagem não encontrada.")
        return
    # Se existir
    with open(caminho_triagem, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            # Se linha iniciar e terminar com []
            if linha.startswith('[') and linha.endswith(']'):
                linha = linha[1:-1]  # Remove colchetes externos
                # Define ],[ como separador das partes para pegar partes internas das listas
                partes = linha.split('],[')         
                # Remover colchetes extras e torna partes uma lista de strings, onde cada string contém uma lista da linha
                partes = [p.strip('[]').strip() for p in partes]
                # Divida a primeira parte por vírgulas para obter o responsável e nome
                responsavel_nome = partes[0].split(',')
                if len(responsavel_nome) >= 2:
                    responsavel1 = responsavel_nome[0].strip().strip("'").strip()
                    nome1 = responsavel_nome[1].strip().strip("'").strip()
                    # Normalizar e comparar
                    responsavel1 = responsavel1.title()
                    nome1 = nome1.title()
                    responsavel = responsavel.strip().title()
                    nome = nome.strip().title()
                    # Se responsável, nome passados forem iguais da primeira lista da linha retorna os dados
                    if responsavel == responsavel1 and nome == nome1:
                        # Seleciona os dados pelo índice
                        especie = partes[1]
                        raca = partes[2]
                        sexo = partes[3]
                        sintomas = partes[4]
                        diagnostico = partes[5]
                        exames = partes[6]
                        medicacao = partes[7]
                        hora = partes[8]

                        print(f"Triagem do animal:\n"
                              f"Responsável: {responsavel1}\n"
                              f"Nome: {nome1}\n"
                              f"Espécie: {especie}\n"
                              f"Raça: {raca}\n"
                              f"Sexo: {sexo}\n"
                              f"Sintomas: {sintomas}\n"
                              f"Diagnóstico: {diagnostico}\n"
                              f"Exames: {exames}\n"
                              f"Medicação: {medicacao}\n"
                              f"Hora: {hora}")
                        return partes
    return None


# Grava a triagem do animal no txt
def registrar_triagem(responsavel, nome, especie, raca, sexo, sintomas, hora, diagnostico="None", exames="None", medicacao="None"):
    # Se animal passou pela triagem pergunta se quer refazer
    if validar_triagem(responsavel, nome):
        print("Animal já passou pela triagem.")
        escolha = input("Deseja refazer triagem? (s/n): ").strip().lower()
        if escolha == 's':
            # Reescreve os dados
            atualizar_dados(responsavel, nome, especie, raca, sexo, sintomas, diagnostico, exames, medicacao, hora)
            print("Dados atualizados")
        else:
            print("Os dados existentes foram mantidos.")
        return
    # Formata os dados como listas
    dados_formatados = (
        f"[{responsavel}, {nome}],"
        f"[{especie}],"
        f"[{raca}],"
        f"[{sexo}],"
        f"[{sintomas}],"
        f"[{diagnostico}],"
        f"[{exames}],"
        f"[{medicacao}],"
        f"[{hora}]")
    with open(caminho_triagem, "a") as arquivo:
        if os.path.getsize(caminho_triagem) > 0: # Se o arquivo não estiver vazio
            arquivo.write('\n')  # Adiciona nova linha apenas se o arquivo não estiver vazio
        arquivo.write(dados_formatados)
    print(f"Triagem realizada com sucesso.")
    return


# Atualiza os dados da triagem / avaliação
def atualizar_dados(responsavel, nome, especie, raca, sexo, sintomas, diagnostico, exames, medicacao, hora):
    with open(caminho_triagem, "r") as arquivo:
        linhas = arquivo.readlines() # Lê e define as linhas 
    with open(caminho_triagem, "w") as arquivo:
        for linha in linhas:
            linha = linha.strip()
            # Se linha iniciar e terminar com []
            if linha.startswith('[') and linha.endswith(']'):
                # Remove os colchetes das extremidades e separa as partes
                linha = linha[1:-1]
                # Define ],[ como separador das partes para pegar partes internas das listas
                partes = linha.split('],[')
                # Remover colchetes extras e torna partes uma lista de strings, onde cada string contém uma lista da linha
                partes = [p.strip('[]').strip() for p in partes]
                # Extrai o responsável e o nome da primeira parte
                responsavel_nome = partes[0].split(', ')
                responsavel1 = responsavel_nome[0].strip().strip("'")
                nome1 = responsavel_nome[1].strip().strip("'")
                # Se responsável, nome passados forem iguais da primeira lista da linha atualiza os dados
                if responsavel1 == responsavel and nome1 == nome:
                    # Atualiza a linha existente com os novos dados
                    dados_formatados = (
                        f"[{responsavel}, {nome}],"
                        f"[{especie}],"
                        f"[{raca}],"
                        f"[{sexo}],"
                        f"[{sintomas}],"
                        f"[{diagnostico}],"
                        f"[{exames}],"
                        f"[{medicacao}],"
                        f"[{hora}]"
                    )
                    print("Atualizando dados...")
                    print(f"Responsável: {responsavel}")
                    print(f"Nome: {nome}")
                    print(f"Espécie: {especie}")
                    print(f"Raça: {raca}")
                    print(f"Sexo: {sexo}")
                    print(f"Sintomas: {sintomas}")
                    print(f"Diagnóstico: {diagnostico}")
                    print(f"Exames: {exames}")
                    print(f"Medicação: {medicacao}")
                    print(f"Hora: {hora}")
                    arquivo.write(dados_formatados + '\n')
                else:
                    # Mantém as linhas existentes
                    nova_linha = (
                        f"[{partes[0]}],"
                        f"[{partes[1]}],"
                        f"[{partes[2]}],"
                        f"[{partes[3]}],"
                        f"[{partes[4]}],"
                        f"[{partes[5]}],"
                        f"[{partes[6]}],"
                        f"[{partes[7]}],"
                        f"[{partes[8]}]"
                    )
                    arquivo.write(nova_linha + '\n')
            else:
                # Reescreve todas as linhas como eram
                arquivo.write(linha + '\n')


# Move triagem / avaliação para arquivamento
def arquivar(responsavel, nome):
    # Verifica se existe o registro em triagem
    if not validar_triagem(responsavel, nome):
        print("Triagem / avaliação não encontrada.")
        return
    # Se existir
    with open(caminho_triagem, "r") as arquivo:
        linhas = arquivo.readlines()
    registro_arquivar = None # Registro para ser arquivado inicia em None
    outros_registros = [] # Todos os outros registros para voltarem para triagem
    for linha in linhas:
        linha = linha.strip()  
        # Se linha iniciar e terminar com []
        if linha.startswith('[') and linha.endswith(']'):
            # Remove os colchetes das extremidades e separa as partes
            linha = linha[1:-1]
            # Define ],[ como separador das partes para pegar partes internas das listas
            partes = linha.split('],[')
            # Remover colchetes extras e torna partes uma lista de strings, onde cada string contém uma lista da linha
            partes = [p.strip('[]').strip() for p in partes]
            # Extrai o responsável e o nome da primeira parte
            responsavel_nome = partes[0].split(', ')
            responsavel1 = responsavel_nome[0].strip().strip("'").strip()
            nome1 = responsavel_nome[1].strip().strip("'").strip()      
            # Se responsável, nome passados forem iguais da primeira lista da linha grava linha em arquivos e apaga de triagem
            if responsavel1 == responsavel and nome1 == nome:
                registro_arquivar = linha # Pega toda a linha do registro
                
            else:
                outros_registros.append(f"[{'],['.join(partes)}]\n") # Reescreve os arquivos restantes de volta em triagem de volta em suas listas
        else:
            outros_registros.append(linha + '\n') 
    if registro_arquivar: # Se encontrar o registro retorna o registro e confirma arquivamento
        especie = partes[1]
        raca = partes[2]
        sexo = partes[3]
        sintomas = partes[4]
        diagnostico = partes[5]
        exames = partes[6]
        medicacao = partes[7]
        hora = partes[8]
        print(f"Triagem / avaliação encontrada:\nResponsável: {responsavel}\nNome: {nome}\nEspécie: {especie}\nRaça: {raca}\nSexo: {sexo}\nSintomas: {sintomas}\nDiagnóstico: {diagnostico}\nExames: {exames}\nMedicação: {medicacao}\nHora: {hora}")
        opcao = input("Deseja arquivar triagem / avaliação? (s/n): ").strip().lower()
        if opcao == "s":
            # Reescreve o restante do arquivo de triagem sem o registro arquivado
            with open(caminho_triagem, "w") as arquivo:
                arquivo.writelines(outros_registros)   
            # Adiciona o registro ao arquivo de arquivamento
            with open(caminho_arquivo, "a") as arquivo:
                if os.path.getsize(caminho_arquivo) > 0: # Se arquivo não for vazio adiciona linha em branco
                    arquivo.write('\n')
                arquivo.write(f"[{registro_arquivar}]\n")
            
            print("Triagem / avaliação arquivada com sucesso.")
        else:
            print("Triagem / avaliação não transferida.")
    else:
        print("Triagem / avaliação não encontrada.")
    return False


# Valida arquivo para usar em buscar arquivo
def validar_arquivo(responsavel, nome):
    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            # Se linha iniciar e terminar com []
            if linha.startswith('[') and linha.endswith(']'):
                # Remove os colchetes das extremidades e separa as partes
                linha = linha[1:-1]
                # Define ],[ como separador das partes para pegar partes internas das listas
                partes = linha.split('],[')
                # Remover colchetes extras e torna partes uma lista de strings, onde cada string contém uma lista da linha
                partes = [p.strip('[]').strip() for p in partes]
                # Divida a primeira parte por vírgulas para obter o responsável e nome
                responsavel_nome = partes[0].split(',')
                if len(responsavel_nome) >= 2:
                    responsavel1 = responsavel_nome[0].strip().strip("'").strip()
                    nome1 = responsavel_nome[1].strip().strip("'").strip()
                    # Normalizar e comparar
                    responsavel1 = responsavel1.title()
                    nome1 = nome1.title()
                    responsavel = responsavel.strip().title()
                    nome = nome.strip().title()
                    # Se responsável, nome passados forem iguais da primeira lista da linha retorna True
                    if responsavel == responsavel1 and nome == nome1:
                        return True
    return False
  

# Buscar registro arquivado 
def buscar_arquivo(responsavel, nome):
    # Verifica se registro existe
    if not validar_arquivo(responsavel, nome):
        print("Arquivo não encontrado.")
        return
    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            # Se linha iniciar e terminar com []
            if linha.startswith('[') and linha.endswith(']'):
                # Remove os colchetes das extremidades e separa as partes
                linha = linha[1:-1]
                # Define ],[ como separador das partes para pegar partes internas das listas
                partes = linha.split('],[')
                # Remover colchetes extras e torna partes uma lista de strings, onde cada string contém uma lista da linha
                partes = [p.strip('[]').strip() for p in partes]
                # Divida a primeira parte por vírgulas para obter o responsável e nome
                responsavel_nome = partes[0].split(',')
                if len(responsavel_nome) >= 2:
                    responsavel1 = responsavel_nome[0].strip().strip("'").strip()
                    nome1 = responsavel_nome[1].strip().strip("'").strip()
                    # Normalizar e comparar
                    responsavel1 = responsavel1.title()
                    nome1 = nome1.title()
                    responsavel = responsavel.strip().title()
                    nome = nome.strip().title()
                    # Se responsável, nome passados forem iguais da primeira lista da linha retorna o registro arquivado
                    if responsavel == responsavel1 and nome == nome1:
                        # Formata dados pelo índice
                        especie = partes[1]
                        raca = partes[2]
                        sexo = partes[3]
                        sintomas = partes[4]
                        diagnostico = partes[5]
                        exames = partes[6]
                        medicacao = partes[7]
                        hora = partes[8]

                        print(f"Arquivo do animal:\n"
                              f"Responsável: {responsavel1}\n"
                              f"Nome: {nome1}\n"
                              f"Espécie: {especie}\n"
                              f"Raça: {raca}\n"
                              f"Sexo: {sexo}\n"
                              f"Sintomas: {sintomas}\n"
                              f"Diagnóstico: {diagnostico}\n"
                              f"Exames: {exames}\n"
                              f"Medicação: {medicacao}\n"
                              f"Hora: {hora}")
                        return partes
    return None


# Deleta arquivo em arquivamento
def deletar_arquivo(responsavel, nome):
    # Verifica se o registro existe
    if not validar_arquivo(responsavel, nome):
        print("Arquivo não encontrado.")
        return
    opcao = input(f"Deseja deletar arquivo do responsável: {responsavel}, animal: {nome}? (s/n): ").strip().lower()
    if opcao == "s":
        with open(caminho_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        outros_registros = [] # Todos os outros registros para voltarem para arquivo
        for linha in linhas:
            linha = linha.strip()  
            # Se linha iniciar e terminar com []
            if linha.startswith('[') and linha.endswith(']'):
                # Remove os colchetes das extremidades e separa as partes
                linha = linha[1:-1]
                # Define ],[ como separador das partes para pegar partes internas das listas
                partes = linha.split('],[')
                # Remover colchetes extras e torna partes uma lista de strings, onde cada string contém uma lista da linha
                partes = [p.strip('[]').strip() for p in partes]
                # Extrai o responsável e o nome da primeira parte
                responsavel_nome = partes[0].split(', ')
                responsavel1 = responsavel_nome[0].strip().strip("'").strip()
                nome1 = responsavel_nome[1].strip().strip("'").strip()               
                # Se responsável, nome passados forem diferentes do encontrado grava de volta no arquivo
                if responsavel1 != responsavel or nome1 != nome:
                    outros_registros.append(f"[{'],['.join(partes)}]\n") # append do restante do arquivo na lista sem o selecionado
            else:
                outros_registros.append(linha + '\n')
        # E era aqui que deveria estar o with open, antes estava dentro do loop do for, por isso o erro
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.writelines(outros_registros)       
        print("Arquivo deletado com sucesso.")
    else:
        print("Arquivo não deletado.")
