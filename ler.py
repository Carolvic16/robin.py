def ler_arquivo(nome_arquivo):
    processos = []
    with open('test.txt', 'r') as arquivo:
        linha = arquivo.readline()
        while linha:
            linha = linha.strip()
            id_processo = linha[:3]
            instrucoes = linha[3:]
            processos.append((id_processo, instrucoes))
            print(f"Processo adicionado: ID = {id_processo}, Instruções = {instrucoes}")  # Debug print
            linha = arquivo.readline()
    print(f"Total de processos lidos: {len(processos)}")  # Debug print
    return processos
    processos.close()
  






