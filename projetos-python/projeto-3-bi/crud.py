from prettytable import PrettyTable
import mysql.connector
def abrebanco():
    try:
        #criando um objeto para conexão ao banco de dados
        #Devemos indicar em :
        # host = Servidor ou IP(caso esteja numa rede),
        # database = nome do banco de dados criado no workbenck
        # user = nome do usuário definido no momento de criação do banco de dados
        # password = senha de acesso do banco de dados
        global conexao
        conexao = mysql.connector.Connect(host='localhost',database='projetoalberson',
        user='root', password='')
        # testando se estamos conectado ao banco de dados
        if conexao.is_connected():
            informacaobanco = conexao.get_server_info()
            print(f'Conectado ao servidor banco de dados - Versão {informacaobanco}')
            print('Conexão ok')
            # criando objeto cursor, responsável para trabalharmos com registros retornados pela tabela fisica
            global comandosql
            comandosql = conexao.cursor()
            # Criando uma QUERY para mostrar as informações do banco de dados ao qual nos conectamos
            comandosql.execute('select database();')
            # usando método fetchone para buscar um dado do banco de dados e armazenálo na variável nomebanco
            nomebanco = comandosql.fetchone()
            print(f'Banco de dados acessado = {nomebanco}')
            print('='*80)
            return 1
        else:
            print('Conexão não realizada com banco')
        return 0
    except Exception as erro:
        print(f'Erro : {erro}')
    return 0

def mostratodas():
    # criando duas colunas para o grid que exibirá todas as diciplinas cadastradas
    grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])
    try:
        comandosql = conexao.cursor()
        # repare que NÃO USEI A CLÁUSULA WHERE, ou seja, todas as disciplinas gravadas serão consultadas
        comandosql.execute(f'select * from disciplinas;')
        # O MÉTODO fetchall() retornará todos os registros filtrados (um ou maisregistros) pelo comando
        selecttabela = comandosql.fetchall()
        # O método rowcount conta quantos registros foram filtrados, caso tenha registro filtrado entra no if
        if comandosql.rowcount > 0:
            # se existir pelo menos uma disciplina na tabela temporária, mostre-as no
            grid
        for registro in selecttabela:
            # criando as linhas do grid com os registros lidos da tabela temporária. Mostrando todas as disciplinas
            grid.add_row([registro[0], registro[1]])
            print(grid)
        else:
            print('Não existem disciplinas cadastradas!!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')

def consultardisciplina(cd=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from disciplinas where codigodisc = {cd};')
        tabela = comandosql.fetchall()
        # verivificando quanto registros de disciplinas de código igual ao digitado
        # filtrados pelo select foram guardados na tabela temporária
        if comandosql.rowcount > 0:
            # se existir pelo menos uma disciplina na tabela temporária, mostre os dados da coluna 1
            for registro in tabela:
                print(f'Nome da Disciplina: {registro[1]}')
            return 'c'
        else:
            return 'nc'
    except Exception as error:
        return (f'Ocorreu erro ao tentar consultar esta disciplina: Erro===>>> {error}')

def cadastrardisciplina(cd=0, nd=''):
    try:
        comandosql = conexao.cursor()
        #criando comando insert e concatenando os dados a serem gravados, recebimdos em cd e nd
        comandosql.execute(f'insert into disciplinas(codigodisc, nomedisc) values({cd},"{nd}") ;')
        #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
        conexao.commit()
        return 'Cadastro da disciplina realizado com sucesso !!!! '
    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível cadastrar esta disciplina !!!'

def alterardisciplina(cd=0, nomedisciplina=''):
    try:
        comandosql = conexao.cursor()
        #criando comando update para atulizar o nome da disciplina em questão
        comandosql.execute(f'Update disciplinas SET nomedisc="{nomedisciplina}" where codigodisc = {cd};')
        #método commit é responsável por REGRAVAR de fato o novo NOME DA DISCIPLINA disciplina na tabela
        conexao.commit()
        return 'Disciplina alterada com sucesso !!! '
    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível alterada esta disciplina'

def excluirdisciplina(cd=0):
    try:
        comandosql = conexao.cursor()
        #criando comando delete e concatenando o código da disciplina para ser escluída
        comandosql.execute(f'delete from disciplinas where codigodisc = {cd};')
        #método commit é responsável por gravar de fato o novo registro de disciplina na tabela
        conexao.commit()
        return 'Disciplina excluída com sucesso !!! '
    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível excluir esta disciplina'


#========================================= MÓDULO PRINCIPAL DO PROGRAMA ===============================================

if abrebanco() == 1:
    resp = input('Deseja entrar no módulo de Disciplinas? (1-Sim, ou qualquer tecla para sair) ==> ')
    while resp =='1':
        print('='*80)
        print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS'))
        print('='*80)

        while True:
            codigodisc = input('Código da Disciplina: (0- Mostra Todas) ')
            if codigodisc.isnumeric():
                codigodisc = int(codigodisc)
                break

        if codigodisc == 0:
            mostratodas()
            #o comando continue volta a executar o laço de repetição do início do laço de repetição
            continue
        #chamando função para consultardisciplina, se retornar 'nc' não está cadastrada
        if consultardisciplina(codigodisc) == 'nc':
            nomedisciplina = input('Nome da Disciplina: ')
            msg = cadastrardisciplina(codigodisc, nomedisciplina)
            print(msg)
        else:
            op = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ")
            while op!='A' and op!='E' and op!='C':
                op = input("ERRO !!! Escolha CORRETAMENTE : [A]-Alterar [E]-Excluir [C]- Cancelar Operações ==> ")
                if op=='A':
                    print('Atenção: Código da disciplina não pode ser alterado: ')
                    nomedisciplina = input('Informe novo nome da disciplina: ')
                    msg = alterardisciplina(codigodisc, nomedisciplina)
                    print(msg)
                elif op == 'E':
                    confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                    while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                        msg = excluirdisciplina(codigodisc)
                        print (msg)
                        print('\n\n')
                        print('='*80)
                        if input('Deseja continuar usando o programa? 1- Sim OU qualquer tecla para sair: ') == '1':
                            #o COMANDO CONTIUE ABAIXO, RETORNA PARA O WHILE QUE ESTÁ SENDO EXECUTADO
                            continue
                        else:
                            break
                    comandosql.close()
                    conexao.close()

else:
    print('FIM DO PROGRAMA!!! Algum problema existente na conexão com banco de dados.')