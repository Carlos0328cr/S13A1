def calcular_multa(tipolivro, multa, quant):
    if tipolivro not in [1, 2, 3]:
        return "Tipo de livro inválido!"

    if multa.lower() == "sim":
        if tipolivro == 1:
            valor_multa = quant * 0.5
            return f"Valor da multa: R$ {valor_multa}"
        elif tipolivro == 2:
            valor_multa = quant * 0.6
            return f"Valor da multa: R$ {valor_multa}"
        elif tipolivro == 3:
            valor_multa = quant * 0.7
            return f"Valor da multa: R$ {valor_multa}"
    else:
        return "Não haverá multa!"

# Testando diferentes cenários
print(calcular_multa(1, "Sim", 5))  # Teste com livro de ficção e 5 dias de atraso
print(calcular_multa(2, "Sim", 3))  # Teste com livro de não ficção e 3 dias de atraso
print(calcular_multa(3, "Não", 0))  # Teste com livro de referência e sem atraso
print(calcular_multa(4, "Sim", 5))  # Teste com tipo de livro inválido
