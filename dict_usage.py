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

    # input("vai salvar o arquivo em formato json - Digite qualquer caracter e tecle enter")
    # with open('dict_professores.json', 'w') as f:


if __name__ == "__main__":
    main()