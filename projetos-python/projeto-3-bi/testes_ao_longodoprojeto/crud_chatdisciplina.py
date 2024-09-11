from prettytable import PrettyTable
import mysql.connector

def abrebanco():
    try:
        global conexao
        conexao = mysql.connector.Connect(host='localhost', database='projetoalberson', user='root', password='')
        if conexao.is_connected():
            informacaobanco = conexao.get_server_info()
            print(f'Conectado ao servidor banco de dados - Versão {informacaobanco}')
            print('Conexão ok')
            global comandosql
            comandosql = conexao.cursor()
            comandosql.execute('select database();')
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
    grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from disciplinas;')
        selecttabela = comandosql.fetchall()
        if comandosql.rowcount > 0:
            for registro in selecttabela:
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
        if comandosql.rowcount > 0:
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
        comandosql.execute(f'insert into disciplinas(codigodisc, nomedisc) values({cd},"{nd}") ;')
        conexao.commit()
        return 'Cadastro da disciplina realizado com sucesso !!!! '
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível cadastrar esta disciplina !!!'

def alterardisciplina(cd=0, nomedisciplina=''):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'Update disciplinas SET nomedisc="{nomedisciplina}" where codigodisc = {cd};')
        conexao.commit()
        return 'Disciplina alterada com sucesso !!! '
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível alterada esta disciplina'

def excluirdisciplina(cd=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'delete from disciplinas where codigodisc = {cd};')
        conexao.commit()
        return 'Disciplina excluída com sucesso !!! '
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível excluir esta disciplina'

def cadastrarprofessor(rg=0, np='', tp='', ip=0, sp=0.0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'insert into professores(registro, nomeprof, telefoneprof, idadeprof, salarioprof) values({rg},"{np}","{tp}",{ip},{sp}) ;')
        conexao.commit()
        return 'Cadastro do professor realizado com sucesso !!!! '
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível cadastrar este professor !!!'

def alterarprofessor(rg=0, nomeprofessor='', telefoneprof='', idadeprof=0, salarioprof=0.0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'Update professores SET nomeprof="{nomeprofessor}", telefoneprof="{telefoneprof}", idadeprof={idadeprof}, salarioprof={salarioprof} where registro = {rg};')
        conexao.commit()
        return 'Professor alterado com sucesso !!! '
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível alterar este professor'

def excluirprofessor(rg=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from disciplinasxprofessores where codigoprofessor = {rg};')
        if comandosql.rowcount == 0:
            comandosql.execute(f'delete from professores where registro = {rg};')
            conexao.commit()
            return 'Professor excluído com sucesso !!! '
        else:
            return 'Não foi possível excluir este professor, pois ele está relacionado com disciplinas.'
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível excluir este professor'

if abrebanco() == 1:
    resp = input('Deseja entrar no módulo de Disciplinas? (1-Sim, ou qualquer tecla para sair) ==> ')
    while resp == '1':
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
            continue

        if consultardisciplina(codigodisc) == 'nc':
            nomedisciplina = input('Nome da Disciplina: ')
            msg = cadastrardisciplina(codigodisc, nomedisciplina)
            print(msg)
        else:
            op = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ")
            while op != 'A' and op != 'E' and op != 'C':
                op = input("ERRO !!! Escolha CORRETAMENTE : [A]-Alterar [E]-Excluir [C]- Cancelar Operações ==> ")
            
            if op == 'A':
                print('Atenção: Código da disciplina não pode ser alterado: ')
                nomedisciplina = input('Informe novo nome da disciplina: ')
                msg = alterardisciplina(codigodisc, nomedisciplina)
                print(msg)
            elif op == 'E':
                confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                while confirma != 'S' and confirma != 'N':
                    confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                if confirma == 'S':
                    msg = excluirdisciplina(codigodisc)
                    print(msg)
        
        print('\n\n')
        print('='*80)
        if input('Deseja continuar usando o programa? 1- Sim OU qualquer tecla para sair: ') != '1':
            break
    comandosql.close()
    conexao.close()
else:
    print('FIM DO PROGRAMA!!! Algum problema existente na conexão com banco de dados.')