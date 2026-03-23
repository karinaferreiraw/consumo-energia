# Calculadora de Consumo Elétrico Inteligente
# Autor: Karina Wachi

# Entrada
nome = input("Digite o nome do Aparelho: ")
potencia = float(input("Digite a Potência do aparelho em Watts (W): "))
horasDia = float(input("Digite o tempo médio de uso diário desse aparelho em horas: "))

# Processamento
consumoMensal = (potencia * horasDia * 30) / 1000

# Saída
print(f"\nAparelho: {nome}")
print(f"Consumo Estimado: {consumoMensal:.0f}kWh/mês")