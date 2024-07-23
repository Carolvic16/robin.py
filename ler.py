import re

# Abrir o arquivo para leitura
ler = open("Teste.txt", "r")

# Ler todas as linhas do arquivo e processá-las
linha = ler.readline()
while linha != "":
  # Imprimir a linha atual
  print(linha.strip())  # .strip() remove espaços em branco no início e no fim da linha

  # Dividir a linha em ID do processo e instruções
  # Supondo que o ID tenha sempre 3 caracteres e o restante são instruções
  id_processo = linha[:3]
  instrucoes = linha[3:]
  
  # Imprimir ID do processo e instruções (apenas para verificação)
  print(f"ID do processo: {id_processo}")
  print(f"Instruções: {instrucoes}")
  
  # Ler a próxima linha
  linha = ler.readline()

# Fechar o arquivo
ler.close()


