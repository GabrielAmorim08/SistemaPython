#########################
# nome: Gabriel Rodrigues Amorim
# curso: Análise e desenvolvimento de sistemas
#########################
import json
dict_dadosEstudantes = {}
lista_dadosEstudantes = []

dict_dadosProfessores = {}
lista_dadosProfessores = []

dict_dadosDisciplinas = {}
lista_dadosDisciplinas = []

dict_dadosTurmas = {}
lista_dadosTurmas = []

dict_dadosMatriculas = {}
lista_dadosMatriculas = []
#Declarando função do menu principal
def MenuPrincipal():
    #Menu principal
    print("\n-=-=-=-=-=-Menu principal-=-=-=-=-=-\n")
    print("1- Estudantes")
    print("2- Professores")
    print("3- Disciplinas")
    print("4- Turmas")
    print("5- Matrículas")
    print("6- Sair")
def MenuOpercoes():
    #Menu de operações 
    print("1- Incluir")
    print("2- Listar")
    print("3- Atualizar")
    print("4- Excluir")
    print("5- Voltar ao menu principal")
def IncluirCadastro():
        global opcao
        #Adiciona o nome do estudante em uma váriavel String
        if opcao == 1:
            codigo = int(input("Digite o código do usuario: "))
            dict_dadosEstudantes["codigo"] = codigo
            nome = input("Digite o nome do usuario: ")
            dict_dadosEstudantes["nome"] = nome
            cpf = input("Digite o cpf do usuario: ")
            dict_dadosEstudantes["cpf"] = cpf
            #Adiciona o nome do estudante acima na lista utilizando o append()
            lista_dadosEstudantes.append(dict_dadosEstudantes.copy())
            SalvarDados(lista_dadosEstudantes,"Estudantes")
        elif opcao == 2:
            codigo = int(input("Digite o código do usuario: "))
            dict_dadosProfessores["codigo"] = codigo
            nome = input("Digite o nome do usuario: ")
            dict_dadosProfessores["nome"] = nome
            cpf = input("Digite o cpf do usuario: ")
            dict_dadosProfessores["cpf"] = cpf
            #Adiciona o nome do estudante acima na lista utilizando o append()
            lista_dadosProfessores.append(dict_dadosProfessores.copy())
            SalvarDados(lista_dadosProfessores,"Professores")
        elif opcao == 3:
            codigo = int(input("Digite o código da disciplina: "))
            dict_dadosDisciplinas["codigo"] = codigo
            nome = input("Digite o nome da disciplina: ")
            dict_dadosDisciplinas["nome"] = nome
            #Adiciona o nome do estudante acima na lista utilizando o append()
            lista_dadosDisciplinas.append(dict_dadosDisciplinas.copy())
            SalvarDados(lista_dadosDisciplinas,"Disciplinas")
        elif opcao == 4:
            if len (lista_dadosTurmas) == 0:
                print("Lista sem cadastro\n")
                codigoT = int(input("Digite o código da turma: "))
                dict_dadosTurmas["codigoT"] = codigoT
                codigoP = int(input("Digite o codigo do professor: "))
                dict_dadosTurmas["codigoP"] = codigoP
                codigoD = int(input("Digite o codigo da disciplina: "))
                dict_dadosTurmas["codigoD"] = codigoD
                #Adiciona o nome do estudante acima na lista utilizando o append()
                lista_dadosTurmas.append(dict_dadosTurmas.copy())
                SalvarDados(lista_dadosTurmas,"Turmas")
            else:
                codigoT = int(input("Digite o código da turma: "))
                for codigo in lista_dadosTurmas:
                    if(codigo["codigoT"] == codigoT):
                        print("Codigo da turma já existe")
                        continue
                    else:
                        dict_dadosTurmas["codigoT"] = codigoT
                        codigoP = int(input("Digite o codigo do professor: "))
                        dict_dadosTurmas["codigoP"] = codigoP
                        codigoD = int(input("Digite o codigo da disciplina: "))
                        dict_dadosTurmas["codigoD"] = codigoD
                        #Adiciona o nome do estudante acima na lista utilizando o append()
                        lista_dadosTurmas.append(dict_dadosTurmas.copy())
                        SalvarDados(lista_dadosTurmas,"Turmas")
                        break
        elif opcao == 5:
            
            for codigo in lista_dadosMatriculas:
                codigoT = int(input("Digite o código da turma: "))
                if(codigo["codigoT"] == codigoT):
                    print("Codigo já existe")
                else:
                    dict_dadosMatriculas["codigo"] = codigoT
                    codigoE = input("Digite o codigo do estudante: ")
                    if(codigo["codigoE"] == codigoT):
                        print("Codigo já existe")
                    else:
                        dict_dadosMatriculas["codigo"] = codigoE
                        #Adiciona o nome do estudante acima na lista utilizando o append()
                        lista_dadosMatriculas.append(dict_dadosMatriculas.copy())
                        SalvarDados(lista_dadosMatriculas,"Matriculas")
            
def ListarCadastro():
    global opcao
    if opcao == 1:
        #verificação de quantos dados tem dentro da lista. 
        #Só vai exibir se a lista não estiver vazia!!!
        RecuperarDados(lista_dadosEstudantes)
        if len(lista_dadosEstudantes) > 0:    
            #Listagem dos nomes por um laço for percorrendo o tamanho da lista    
            for i in range (len(lista_dadosEstudantes)):
                print(lista_dadosEstudantes[i])
        #Se o if falhar, ou seja se a lista estiver vazia ele vai exibir essa mensagem ao usuario.
        else:
            print("\nNão há usuario cadastrados\n")           

    elif opcao == 2:
        #verificação de quantos dados tem dentro da lista. 
        #Só vai exibir se a lista não estiver vazia!!!
        RecuperarDados(lista_dadosProfessores)
        if len(lista_dadosProfessores) > 0:    
            #Listagem dos nomes por um laço for percorrendo o tamanho da lista    
            for i in range (len(lista_dadosProfessores)):
                print(lista_dadosProfessores[i])
        #Se o if falhar, ou seja se a lista estiver vazia ele vai exibir essa mensagem ao usuario.
        else:
            print("\nNão há usuario cadastrados\n")           
    elif opcao == 3:
        #verificação de quantos dados tem dentro da lista. 
        #Só vai exibir se a lista não estiver vazia!!!
        RecuperarDados(lista_dadosDisciplinas)
        if len(lista_dadosDisciplinas) > 0:    
            #Listagem dos nomes por um laço for percorrendo o tamanho da lista    
            for i in range (len(lista_dadosDisciplinas)):
                print(lista_dadosDisciplinas[i])
        #Se o if falhar, ou seja se a lista estiver vazia ele vai exibir essa mensagem ao usuario.
        else:
            print("\nNão há usuario cadastrados\n")          
    elif opcao == 4:
        #verificação de quantos dados tem dentro da lista. 
        #Só vai exibir se a lista não estiver vazia!!!
        RecuperarDados(lista_dadosTurmas)
        if len(lista_dadosTurmas) > 0:    
            #Listagem dos nomes por um laço for percorrendo o tamanho da lista    
            for i in range (len(lista_dadosTurmas)):
                print(lista_dadosTurmas[i])
        #Se o if falhar, ou seja se a lista estiver vazia ele vai exibir essa mensagem ao usuario.
        else:
            print("\nNão há usuario cadastrados\n")        
    elif opcao == 5:
        #verificação de quantos dados tem dentro da lista. 
        #Só vai exibir se a lista não estiver vazia!!!
        RecuperarDados(lista_dadosMatriculas)
        if len(lista_dadosMatriculas) > 0:    
            #Listagem dos nomes por um laço for percorrendo o tamanho da lista    
            for i in range (len(lista_dadosMatriculas)):
                print(lista_dadosMatriculas[i])
        #Se o if falhar, ou seja se a lista estiver vazia ele vai exibir essa mensagem ao usuario.
        else:
            print("\nNão há usuario cadastrados\n")
def AtualizarCadastro():
    global opcao
    if opcao == 1:          
        #Solicita o codigo do usuario
        resposta = int(input("Digite o código do usuario: "))
        #procura o codigo na lista
        for pessoa in lista_dadosEstudantes:
            if pessoa["codigo"] == resposta:
                #solicita novos dados para o usuario e armazena em variaveis
                atualizar_nome = input("Digite o novo nome: ")
                atualizar_codigo = int(input("Digite o novo código: "))
                atualizar_cpf = input("Digite o novo cpf: ")
                #atualiza todos os dados com os novos dados
                pessoa["codigo"] = atualizar_codigo
                pessoa["nome"] = atualizar_nome
                pessoa["cpf"] = atualizar_cpf
                print("Dados atualizados com sucesso")
                break
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Usuario não cadastrado")
                break
    elif opcao == 2:
        #Solicita o codigo do usuario
        resposta = int(input("Digite o código do usuario: "))
        #procura o codigo na lista
        for pessoa in lista_dadosProfessores:
            if pessoa["codigo"] == resposta:
                #solicita novos dados para o usuario e armazena em variaveis
                atualizar_nome = input("Digite o novo nome: ")
                atualizar_codigo = int(input("Digite o novo código: "))
                atualizar_cpf = input("Digite o novo cpf: ")
                #atualiza todos os dados com os novos dados
                pessoa["codigo"] = atualizar_codigo
                pessoa["nome"] = atualizar_nome
                pessoa["cpf"] = atualizar_cpf
                print("Dados atualizados com sucesso")
                break
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Usuario não cadastrado")
                break
         
    elif opcao == 3:
        #Solicita o codigo do usuario
        resposta = int(input("Digite o código da Disciplina: "))
        #procura o codigo na lista
        for pessoa in lista_dadosDisciplinas:
            if pessoa["codigo"] == resposta:
                #solicita novos dados para o usuario e armazena em variaveis
                atualizar_codigoD = int(input("Digite o novo código: "))
                atualizar_nome = input("Digite o novo nome: ")
                #atualiza todos os dados com os novos dados
                pessoa["codigo"] = atualizar_codigoD
                pessoa["nome"] = atualizar_nome
                print("Dados atualizados com sucesso")
                break
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Usuario não cadastrado")
                break
    elif opcao == 4:
        #Solicita o codigo do usuario
        resposta = int(input("Digite o código da Turma: "))
        #procura o codigo na lista
        for pessoa in lista_dadosTurmas:
            if pessoa["codigoT"] == resposta:
                #solicita novos dados para o usuario e armazena em variaveis
                atualizar_codigoT = int(input("Digite o novo código da turma: "))
                if atualizar_codigoT in pessoa["codigoT"]:
                    print("Codigo já existe")
                else:
                    atualizar_codigoP = int(input("Digite o novo código do professor: "))
                    atualizar_codigoD = int(input("Digite o novo código da disciplina: "))
                    #atualiza todos os dados com os novos dados
                    pessoa["codigoT"] = atualizar_codigoT
                    pessoa["codigoP"] = atualizar_codigoP
                    pessoa["codigoD"] = atualizar_codigoD
                    print("Dados atualizados com sucesso")
                    break
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Usuario não cadastrado")
                break
        
    elif opcao == 5:
        #Solicita o codigo do usuario
        resposta = int(input("Digite o código da matricula: "))
        #procura o codigo na lista
        for pessoa in lista_dadosMatriculas:
            if pessoa["codigo"] == resposta:
                #solicita novos dados para o usuario e armazena em variaveis
                atualizar_codigoT = int(input("Digite o novo código da turma: "))
                atualizar_codigoE = int(input("Digite o novo código do estudante: "))
                #atualiza todos os dados com os novos dados
                pessoa["codigoT"] = atualizar_codigoT
                pessoa["codigoP"] = atualizar_codigoE
                print("Dados atualizados com sucesso")
                break
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Usuario não cadastrado")
                break  
def ExcluirCadastro():
    global opcao
    if opcao == 1:
        #Solicita o codigo do usuario
        resposta = int(input("Digite o codigo do usuario: "))
        #procura o codigo na lista
        for codigo in lista_dadosEstudantes:
            if codigo["codigo"] == resposta:
                #Se achar ele remove e exibe uma mensagem para o usuario
                lista_dadosEstudantes.remove(codigo)
                print("Usuario removido com sucesso")
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Usuario não cadastrado")         

    elif opcao == 2:
        #Solicita o codigo do usuario
        resposta = int(input("Digite o codigo do usuario: "))
        #procura o codigo na lista
        for codigo in lista_dadosProfessores:
            if codigo["codigo"] == resposta:
                #Se achar ele remove e exibe uma mensagem para o usuario
                lista_dadosProfessores.remove(codigo)
                print("Usuario removido com sucesso")
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Usuario não cadastrado")        
    elif opcao == 3:
        #Solicita o codigo do usuario
        resposta = int(input("Digite o codigo da Disciplina: "))
        #procura o codigo na lista
        for codigo in lista_dadosDisciplinas:
            if codigo["codigo"] == resposta:
                #Se achar ele remove e exibe uma mensagem para o usuario
                lista_dadosDisciplinas.remove(codigo)
                print("Disciplina removida com sucesso")
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Disciplina não cadastrado")        
    elif opcao == 4:
        #Solicita o codigo do usuario
        resposta = int(input("Digite o codigo da Turma: "))
        #procura o codigo na lista
        for codigo in lista_dadosTurmas:
            if codigo["codigo"] == resposta:
                #Se achar ele remove e exibe uma mensagem para o usuario
                lista_dadosTurmas.remove(codigo)
                print("Turma removida com sucesso")
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Turma não cadastrado")
    elif opcao == 5:
        #Solicita o codigo do usuario
        resposta = int(input("Digite o codigo da Matricula: "))
        #procura o codigo na lista
        for codigo in lista_dadosMatriculas:
            if codigo["codigo"] == resposta:
                #Se achar ele remove e exibe uma mensagem para o usuario
                lista_dadosMatriculas.remove(codigo)
                print("Matricula removida com sucesso")
            else:
                #Se não ele retorna um usuario não cadastrado
                print("Matricula não cadastrado")   
def SalvarDados(lista_dados,dados):
    global opcao
    print("Desejar salvar os dados?")
    print("1-Sim")
    print("2-Não")
    resposta = int(input("Escolha uma das opções: "))
    if resposta == 1:    
        with open(dados, "w") as arquivo:
            json.dump(lista_dados, arquivo)
def RecuperarDados(dados):
    print("Desejar salvar os dados?")
    print("1-Sim")
    print("2-Não")
    resposta = int(input("Escolha uma das opções: "))
    if resposta == 1:    
        try:
            with open(dados, "r") as arquivo:
                lista = json.load(arquivo)
            return lista
        except:
            return []

while(True):
    #Chamando a função do menu principal
    MenuPrincipal()
    #Escolha das oções utilizando o input
    opcao = int(input("Escolha uma das opções acima: "))
    #Bloco da opção estudantes
    if(opcao == 1):
        while(True):
            print("\n-=-=-=-=-=-Estudantes-=-=-=-=-=-\n")
            #Chamando função do menu de operação
            MenuOpercoes()
            #Escolha das operações
            escolha = int(input("Escolha uma das opções acima: "))

            if(escolha == 1):
                print("-=-=-=-=-=-Incluir estudantes-=-=-=-=-=-\n")
                #Chamando a função incluir
                IncluirCadastro()

            elif(escolha == 2):
                print("-=-=-=-=-=-Lista dos estudantes-=-=-=-=-=-\n")
                #Chamando a função listar
                ListarCadastro()

            elif(escolha == 3):
                print("-=-=-=-=-=-Atualizar cadastro-=-=-=-=-=-\n")
                #Chamando a função atualizar
                AtualizarCadastro()

            elif(escolha == 4):
                print("-=-=-=-=-=-Remover cadastro-=-=-=-=-=-\n")
                #Chamando a função excluir
                ExcluirCadastro()
                
            elif(escolha == 5):
                print("\nVocê voltou ao menu principal \n")
                break

            else:
                print("\nOpção invalida\n")

    #professores
    elif(opcao == 2):
        print("EM DESENVOLVIMENTO")
        while(True):
            print("\n-=-=-=-=-=-Professores-=-=-=-=-=-\n")
            print("1- Incluir")
            print("2- Listar")
            print("3- Atualizar")
            print("4- Excluir")
            print("5- Voltar ao menu principal")
            escolha = int(input("Escolha uma das opções acima: "))
            if(escolha == 1):
                print("-=-=-=-=-=-Incluir Professor-=-=-=-=-=-\n")
                #Chamando a função incluir
                IncluirCadastro()

            elif(escolha == 2):
                print("-=-=-=-=-=-Lista dos Professores-=-=-=-=-=-\n")
                #Chamando a função listar
                ListarCadastro()

            elif(escolha == 3):
                print("-=-=-=-=-=-Atualizar cadastro-=-=-=-=-=-\n")
                #Chamando a função atualizar
                AtualizarCadastro()

            elif(escolha == 4):
                print("-=-=-=-=-=-Remover cadastro-=-=-=-=-=-\n")
                #Chamando a função excluir
                ExcluirCadastro()
                
            elif(escolha == 5):
                print("\nVocê voltou ao menu principal \n")
                break
            else:
                print("\nOpção invalida\n")
    #disciplinas
    elif(opcao == 3):
        while(True):
            print("\n-=-=-=-=-=-Disciplinas-=-=-=-=-=-\n")
            print("1- Incluir")
            print("2- Listar")
            print("3- Atualizar")
            print("4- Excluir")
            print("5- Voltar ao menu principal")
            escolha = int(input("Escolha uma das opções acima: "))
            if(escolha == 1):
                print("-=-=-=-=-=-Incluir Disciplina-=-=-=-=-=-\n")
                #Chamando a função incluir
                IncluirCadastro()

            elif(escolha == 2):
                print("-=-=-=-=-=-Lista das Disciplinas-=-=-=-=-=-\n")
                #Chamando a função listar
                ListarCadastro()

            elif(escolha == 3):
                print("-=-=-=-=-=-Atualizar Disciplina-=-=-=-=-=-\n")
                #Chamando a função atualizar
                AtualizarCadastro()

            elif(escolha == 4):
                print("-=-=-=-=-=-Remover Disciplina-=-=-=-=-=-\n")
                #Chamando a função excluir
                ExcluirCadastro()
                
            elif(escolha == 5):
                print("\nVocê voltou ao menu principal \n")
                break
            else:
                print("\nOpção invalida\n")
    #turmas
    elif(opcao == 4):
        while(True):
            print("\n-=-=-=-=-=-Turmas-=-=-=-=-=-\n")
            print("1- Incluir")
            print("2- Listar")
            print("3- Atualizar")
            print("4- Excluir")
            print("5- Voltar ao menu principal")
            escolha = int(input("Escolha uma das opções acima: "))
            if(escolha == 1):
                print("-=-=-=-=-=-Incluir Turma-=-=-=-=-=-\n")
                #Chamando a função incluir
                IncluirCadastro()

            elif(escolha == 2):
                print("-=-=-=-=-=-Lista das Turmas-=-=-=-=-=-\n")
                #Chamando a função listar
                ListarCadastro()

            elif(escolha == 3):
                print("-=-=-=-=-=-Atualizar Turma-=-=-=-=-=-\n")
                #Chamando a função atualizar
                AtualizarCadastro()

            elif(escolha == 4):
                print("-=-=-=-=-=-Remover Turma-=-=-=-=-=-\n")
                #Chamando a função excluir
                ExcluirCadastro()
            elif(escolha == 5):
                print("\nVocê voltou ao menu principal \n")
                break
            else:
                print("\nOpção invalida\n")
    #matriculas
    elif(opcao == 5):
        while(True):
            print("\n-=-=-=-=-=-Matriculas-=-=-=-=-=-\n")
            print("1- Incluir")
            print("2- Listar")
            print("3- Atualizar")
            print("4- Excluir")
            print("5- Voltar ao menu principal")
            escolha = int(input("Escolha uma das opções acima: ")) 
            if(escolha == 1):
                print("-=-=-=-=-=-Incluir Matricula-=-=-=-=-=-\n")
                #Chamando a função incluir
                IncluirCadastro()

            elif(escolha == 2):
                print("-=-=-=-=-=-Lista das Matricula-=-=-=-=-=-\n")
                #Chamando a função listar
                ListarCadastro()

            elif(escolha == 3):
                print("-=-=-=-=-=-Atualizar Matricula-=-=-=-=-=-\n")
                #Chamando a função atualizar
                AtualizarCadastro()

            elif(escolha == 4):
                print("-=-=-=-=-=-Remover Matricula-=-=-=-=-=-\n")
                #Chamando a função excluir
                ExcluirCadastro()
            elif(escolha == 5):
                print("\nVocê voltou ao menu principal \n")
                break
            else:
                print("\nOpção invalida\n")
    #Bloco para encerrar o programa
    elif(opcao == 6):
        print("\nPrograma encerrado com sucesso")
        break
    #Bloco caso todos os if/elif falhem 
    else:
        print("\nOpção invalida")