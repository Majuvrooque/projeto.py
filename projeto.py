# Solicita ao usuário que escolha a operação que deseja realizar
print("Selecione a operação que deseja realizar:")
print("1 - Converter decimal para binário, hexadecimal ou octal")
print("2 - Converter binário, hexadecimal ou octal para decimal")

operacao = int(input("Operação (1 ou 2): "))

# Realiza a operação de acordo com a escolha do usuário
if operacao == 1:
  decimal = int(input("Digite o número decimal que deseja converter: "))
  print("Selecione a base para a conversão:")
  print("1 - Binário")
  print("2 - Hexadecimal")
  print("3 - Octal")
  base = int(input("Base (1, 2 ou 3): "))
  if base == 1:
    resultado = bin(decimal)
  elif base == 2:
    resultado = hex(decimal)
  elif base == 3:
    resultado = oct(decimal)
  else:
    print("Opção inválida.")
    resultado = None

elif operacao == 2:
  numero = input("Digite o número que deseja converter: ")
  print("Selecione a base do número:")
  print("1 - Binário")
  print("2 - Hexadecimal")
  print("3 - Octal")
  base = int(input("Base (1, 2 ou 3): "))
  if base == 1:
    resultado = int(numero, 2)
  elif base == 2:
    resultado = int(numero, 16)
  elif base == 3:
    resultado = int(numero, 8)
  else:
    print("Opção inválida.")
    resultado = None

else:
  print("Opção inválida.")
  resultado = None

# Exibe o resultado para o usuário
if resultado is not None:
  print("Resultado: {}".format(resultado))