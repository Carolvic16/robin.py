# CLASSE DO PROCESSO (feito pela vic)

def criar_array(tamanho):
    array = []
    for i in range(tamanho):
        valor = float(input(f"Entre com o valor da tarefa {i+1}: "))
        array.append(valor)
    return array

# Definir o tamanho do array
tarefas = int(input("Entre com a quantidade de processos: "))

# Criar o array com os valores do usuário
meu_array = criar_array(tarefas)

# Adicionar o último número ao array e estender a lista com esse número
if meu_array:
    ultimo_valor = meu_array[-1]
    meu_array.append(ultimo_valor)  # Adiciona o último número
    meu_array.extend([ultimo_valor])  # Estende a lista com o último número

# Exibir o array
print("Os valores do array são:", meu_array)
