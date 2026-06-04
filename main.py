# Sistema de Monitoramento Energético Espacial

# GS2026.1 - SERS

def analisar_missao(temperatura, energia, comunicacao, modulo):

alertas = []

if temperatura > 80:
    alertas.append("Superaquecimento detectado")

if energia < 20:
    alertas.append("Nível crítico de energia")

if comunicacao == 0:
    alertas.append("Falha de comunicação")

print("\n===== RELATÓRIO DA MISSÃO =====")

print(f"Temperatura: {temperatura} °C")
print(f"Energia: {energia}%")
print(f"Módulo: {modulo}")

if comunicacao == 1:
    print("Comunicação: OK")
else:
    print("Comunicação: FALHA")

print("\nALERTAS:")

if len(alertas) == 0:
    print("Nenhum alerta detectado.")
else:
    for alerta in alertas:
        print("-", alerta)

print("\nAÇÃO RECOMENDADA:")

if energia < 20:
    print("- Ativar modo de economia energética")

if temperatura > 80:
    print("- Ativar sistema de resfriamento")

if comunicacao == 0:
    print("- Reiniciar sistema de comunicação")

if len(alertas) == 0:
    print("- Operação normal")
```

print("=== MONITORAMENTO DE MISSÃO ESPACIAL ===")

temperatura = float(input("Temperatura (°C): "))
energia = float(input("Energia (%): "))
comunicacao = int(input("Comunicação (1=OK / 0=Falha): "))
modulo = input("Status do módulo: ")

analisar_missao(
temperatura,
energia,
comunicacao,
modulo
)
