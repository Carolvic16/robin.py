def escalonador(fila_de_processos, quantum):
    tempos_processos = {
        "A": 5,
        "B": 7,
        "C": 9,
        "D": 10
    }

    # Dicionário para controlar o número de reencaminhamentos de cada processo
    max_reencaminhamentos = 10
    reencaminhamentos = {}

    while fila_de_processos:
        processo_atual = fila_de_processos.pop(0)
        id_processo, instrucoes = processo_atual

        # Inicializa o contador de reencaminhamentos para este processo
        if id_processo not in reencaminhamentos:
            reencaminhamentos[id_processo] = 0

        print(f"Entrada de processo no processador: Processo {id_processo}")

        instrucoes_restantes = []
        for instrucao in instrucoes:
            tempo_instrucao = tempos_processos[instrucao]
            while tempo_instrucao > 0:
                if tempo_instrucao <= quantum:
                    print(f"Processando {instrucao} do processo {id_processo} por {tempo_instrucao} segundos")
                    tempo_instrucao = 0
                else:
                    print(f"Processando {instrucao} do processo {id_processo} por {quantum} segundos")
                    tempo_instrucao -= quantum
                    instrucoes_restantes.append(instrucao)
                    break  # Sai do loop para passar para a próxima instrução

