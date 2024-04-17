__author__ = "Lincoln"

import json

def main():
    dict_professores = {}

    dict_professores['c1'] = {'nome':'Filipe', 'departamento':'DECSI', 'disciplinas':['CSI001','CSI002']}
    dict_professores['b2'] = {'nome':'Joao', 'departamento':'DECEA', 'disciplinas':['CEA001','CEA002']}
    dict_professores['a1'] = {'nome':'Pedro', 'departamento':'DEENP', 'disciplinas':['ENP001','ENP002']}
    dict_professores['a2'] = {'nome':'Ana', 'departamento':'DEELT', 'disciplinas':['ELT001','ELT002']}

    print("Quantidade de elementos: %d" % len(dict_professores))
    for professor_id in dict_professores:
        print('****************PROFESSOR****************')
        print('\tcodigo: %s' % professor_id)
        print('\tnome: %s' % dict_professores[professor_id]['nome'])
        print('\tdisciplinas')
        lista_disciplinas = dict_professores[professor_id]['disciplinas']
        for disciplina in lista_disciplinas:
            print('\t\t%s' % disciplina)

    # print('\nTodo o dicionario: \n%s' % dict_professores)

    input("vai salvar o arquivo em formato json - Digite qualquer caracter e tecle enter")
    with open('dict_professores.json', 'w') as f:
        json.dump(dict_professores,f)
        # alternativa
        # f.write(json.dumps(dict_professores))
        
    input("vai ler o json - Tecle enter")
    print("\n\n****************LENDO O JSON SALVO****************")
    dicionario_lido = {}
    with open('dict_professores.json') as f:
        dicionario_lido = json.load(f)
        # alternativa
        # dicionario_lido = json.load(f.read())

        for professor_id in dicionario_lido:
            print('****************PROFESSOR****************')
            print('\tcodigo: %s' % professor_id)
            print('\tnome: %s' % dict_professores[professor_id]['nome'])
            print('\tdisciplinas')
            lista_disciplinas = dicionario_lido[professor_id]['disciplinas']
            # lista_disciplinas.append('EEE02')
            for disciplina in lista_disciplinas:
                print("\t\t%s" % disciplina)
        
    input("vai salvar o arquivo linha por linha json - Tecle enter")
    with open('dict_professores_linha.json','w') as f:
        for professor_id in dicionario_lido:
            f.write('%s\n' % (json.dumps({professor_id: dicionario_lido[professor_id]})))


    input("vai ler o arquivo linha por linha json - Tecle enter")
    print("\n\n****************LENDO JSON LINHA POR LINHA****************")
    with open('dict_professores_linha.json', 'r') as f:
        for line in f:
            line = line.strip()
            json_line = json.loads(line)
            print(json_line.keys())
            professor_id = list(json_line.keys()).pop()
            professor_data = json_line[professor_id]
            print("%s:%s" % (professor_id, professor_data))


    # SALVANDO COMO TSV
    with open('dict_professores_tsv.tsv', 'w') as f:
        f.write("prof_id\tprof_name\tprof_dpt\tprof_dic\n")
        for professor_id in dicionario_lido:
            lista_disciplinas = dicionario_lido[professor_id]['disciplinas']
            num_disciplinas = len(lista_disciplinas)
            f.write("%s\t%s\t%s\t%d\n" % (professor_id, dicionario_lido[professor_id]['nome']))


if __name__ == "__main__":
    main()