'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
tipolivro = int(input("Qual tipo de livro voçê escoleu? 1-Ficção | 2- Não ficção | 3- Referência"))
multa = input("Devolveu o livro com atraso?")
if multa == "Sim":
        print("Haverá multa! Vamos calcular o valor da multa.")
        quant =  int(input("Quantos dias de atraso?"))
        if tipolivro == 1:
            livro1 = quant * 0.5
            print("Valor da multa: R$",livro1)
        elif tipolivro == 2:
            livro2 = quant * 0.6
            print("Valor da multa: R$",livro2)
        else:
            print("Não ouve multa")
else:
    print("Não haverá multa!")








