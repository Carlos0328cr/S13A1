'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
tipolivro = int(input("Qual tipo de livro voçê escoleu? 1-Ficção | 2- Não ficção | 3- Referência"))
if tipolivro not in [1, 2, 3]:
        print("Tipo de livro inválido!")
else:
        multa = input("Devolveu o livro com atraso?")
        if multa == "Sim":
                print("Haverá multa! Vamos calcular o valor da multa.")
                quant =  int(input("Quantos dias de atraso?"))
                if tipolivro == 1:
                    valor_multa = quant * 0.5
                    print("Valor da multa: R$", valor-multa)
                elif tipolivro == 2:
                    valor_multa = quant * 0.6
                    print("Valor da multa: R$", valor_multa)
                else:
                    print("Não ouve multa")
        else:
            print("Não haverá multa!")








