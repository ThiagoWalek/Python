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
    grid = PrettyTable(['Código', 'Código Disciplina', 'Código Professor', 'Curso', 'Carga Horária', 'Ano Letivo'])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from disciplinasxprofessores;')
        selecttabela = comandosql.fetchall()
        if comandosql.rowcount > 0:
            for registro in selecttabela:
                grid.add_row([registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]])
            print(grid)
        else:
            print('Não existem registros cadastrados!!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')

def consultardisciplinaprofessor(cd=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from disciplinasxprofessores where codigosdisciplinanocurso = {cd};')
        tabela = comandosql.fetchall()
        if comandosql.rowcount > 0:
            for registro in tabela:
                print(f"Disciplina: {registro[1]}, Professor: {registro[2]}")
            return 'c'
        else:
            return 'nc'
    except Exception as error:
        return (f'Ocorreu erro ao tentar consultar: Erro===>>> {error}')

def cadastrardisciplinaprofessor(cd=0, cod_disciplina=0, cod_professor=0, curso=0, cargahoraria=0, anoletivo=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'insert into disciplinasxprofessores(codigosdisciplinanocurso, coddisciplina, codprofessor, curso, cargahoraria, anoletivo) values({cd},{cod_disciplina},{cod_professor},{curso},{cargahoraria},{anoletivo}) ;')
        conexao.commit()
        return 'Cadastro realizado com sucesso !!!! '
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível cadastrar esta relação !!!'

def alterardisciplinaprofessor(cd=0, cod_disciplina=0, cod_professor=0, curso=0, cargahoraria=0, anoletivo=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'Update disciplinasxprofessores SET coddisciplina={cod_disciplina}, codprofessor={cod_professor}, curso={curso}, cargahoraria={cargahoraria}, anoletivo={anoletivo} where codigosdisciplinanocurso = {cd};')
        conexao.commit()
        return 'Relação alterada com sucesso !!! '
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível alterar esta relação'

def excluirdisciplinaprofessor(cd=0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'delete from disciplinasxprofessores where codigosdisciplinanocurso = {cd};')
        conexao.commit()
        return 'Relação excluída com sucesso !!! '
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível excluir esta relação'

# MÓDULO PRINCIPAL DO PROGRAMA
if abrebanco() == 1:
    resp = input('Deseja entrar no módulo de DisciplinasxProfessores? (1-Sim, ou qualquer tecla para sair) ==> ')
    while resp == '1':
        print('='*80)
        print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS X PROFESSORES'))
        print('='*80)
        
        while True:
            codigodiscprof = input('Código da relação Disciplina x Professor: (0- Mostra Todas) ')
            if codigodiscprof.isnumeric():
                codigodiscprof = int(codigodiscprof)
                break

        if codigodiscprof == 0:
            mostratodas()
            continue

        if consultardisciplinaprofessor(codigodiscprof) == 'nc':
            cod_disciplina = int(input('Código da Disciplina: '))
            cod_professor = int(input('Código do Professor: '))
            curso = int(input('Código do Curso: '))
            cargahoraria = int(input('Carga Horária: '))
            anoletivo = int(input('Ano Letivo: '))
            msg = cadastrardisciplinaprofessor(codigodiscprof, cod_disciplina, cod_professor, curso, cargahoraria, anoletivo)
            print(msg)
        else:
            op = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ")
            while op != 'A' and op != 'E' and op != 'C':
                op = input("ERRO !!! Escolha CORRETAMENTE : [A]-Alterar [E]-Excluir [C]- Cancelar Operações ==> ")
            
            if op == 'A':
                print('Atenção: Código da relação não pode ser alterado: ')
                cod_disciplina = int(input('Informe o novo código da disciplina: '))
                cod_professor = int(input('Informe o novo código do professor: '))
                curso = int(input('Informe o novo código do curso: '))
                cargahoraria = int(input('Informe a nova carga horária: '))
                anoletivo = int(input('Informe o novo ano letivo: '))
                msg = alterardisciplinaprofessor(codigodiscprof, cod_disciplina, cod_professor, curso, cargahoraria, anoletivo)
                print(msg)
            elif op == 'E':
                confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                while confirma != 'S' and confirma != 'N':
                    confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                if confirma == 'S':
                    msg = excluirdisciplinaprofessor(codigodiscprof)
                    print(msg)
        
        print('\n\n')
        print('='*80)
        if input('Deseja continuar usando o programa? 1- Sim OU qualquer tecla para sair: ') != '1':
            break
    comandosql.close()
    conexao.close()
else:
    print('FIM DO PROGRAMA!!! Algum problema existente na conexão com banco de dados.')
