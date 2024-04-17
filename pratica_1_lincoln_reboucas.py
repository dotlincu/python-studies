# -*- coding: utf-8 -*-
__author__ = "Lincoln Rebouças"

import json

def main():
    dict_times = {}

    dict_times['001'] = {'nome': 'Flamengo', 'esporte': 'Futebol', 'cidade': 'Rio de Janeiro', 'fundacao': '1895-11-17', 'membros': 30}
    dict_times['002'] = {'nome': 'Real Madrid', 'esporte': 'Futebol', 'cidade': 'Madrid', 'fundacao': '1902-03-06', 'membros': 28}
    dict_times['003'] = {'nome': 'Sada Cruzeiro', 'esporte': 'Vôlei', 'cidade': 'Betim', 'fundacao': '2006-06-14', 'membros': 16}
    # dict_times['004'] = {}

    print("##################### DADOS DO DICIONARIO INICIAL ######################")             
    print("Quantidade de elementos: %d" % len(dict_times))  
    for time_id in dict_times:
        print('**************** TIME ****************')
        print('\tcodigo: %s' % time_id)
        print('\tnome: %s' % dict_times[time_id]['nome'])
        print('\tesporte: %s' % dict_times[time_id]['esporte'])
        print('\tcidade: %s' % dict_times[time_id]['cidade'])
        print('\tfundacao: %s' % dict_times[time_id]['fundacao'])
        print('\tmembros: %d' % dict_times[time_id]['membros'])
            
    # print("Todo o dicionario: %s" % dict_times)
    
    # SALVANDO EM JSON
    print("\n\n##################### SALVANDO O DICIONARIO EM FORMATO JSON #####################")
    input("TECLE ENTER")
    with open('dict_times.json', 'w') as f:
        json.dump(dict_times, f)
        # f.write(json.dumps(dict_times))
    
    # LENDO O JSON
    print("\n\n##################### LENDO O DICIONARIO EM FORMATO JSON #####################")
    input("TECLE ENTER")
    dicionario_lido = {}
    with open('dict_times.json') as f:
        dicionario_lido = json.load(f)
        # dicionario_lido = json.loads(f.read())
        
        for time_id in dicionario_lido:
            print('**************** TIME ****************')
            print('\tcodigo: %s' % time_id)
            print('\tnome: %s' % dicionario_lido[time_id]['nome'])
            print('\tesporte: %s' % dicionario_lido[time_id]['esporte'])
            print('\tcidade: %s' % dicionario_lido[time_id]['cidade'])
            print('\tfundacao: %s' % dicionario_lido[time_id]['fundacao'])
            print('\tmembros: %d' % dicionario_lido[time_id]['membros'])

    # SALVANDO O JSON LINHA POR LINHA
    print("\n\n##################### SALVANDO O DICIONARIO EM FORMATO JSON LINHA POR LINHA #####################")
    input("TECLE ENTER")
    with open('dict_times_linha.json', 'w') as f:
        for time_id in dicionario_lido:
            f.write('%s\n' % (json.dumps({time_id: dicionario_lido[time_id]})))

    # LENDO O JSON LINHA POR LINHA
    print("\n\n##################### LENDO O DICIONARIO EM FORMATO JSON LINHA POR LINHA #####################")
    input("TECLE ENTER")
    with open('dict_times_linha.json', 'r') as f:
        for line in f:
            line = line.strip()
            json_line = json.loads(line)
            print(json_line.keys())
            time_id = list(json_line.keys()).pop()
            time_data = json_line[time_id]
            print("%s:%s" % (time_id, time_data))

    # SALVANDO COMO TSV
    print("\n\n##################### SALVANDO O DICIONARIO EM FORMATO TSV #####################")
    input("TECLE ENTER")
    with open('dict_times_tsv.tsv', 'w') as f:
        f.write("time_id\ttime_nome\ttime_esporte\ttime_cidade\ttime_fundacao\ttime_membros\n")
        for time_id in dicionario_lido:
            f.write("%s\t%s\t%s\t%s\t%s\t%d\n" % (
                time_id,
                dicionario_lido[time_id]['nome'],
                dicionario_lido[time_id]['esporte'],
                dicionario_lido[time_id]['cidade'],
                dicionario_lido[time_id]['fundacao'],
                dicionario_lido[time_id]['membros']
            ))

    # LENDO O TSV
    print("\n\n##################### LENDO O DICIONARIO EM FORMATO TSV #####################")
    input("TECLE ENTER")
    with open('dict_times_tsv.tsv') as f:
        for line in f:
            print(line.strip())
            elements = line.strip().split('\t')
            print(elements)
    
if __name__ == "__main__":   
    main()
    