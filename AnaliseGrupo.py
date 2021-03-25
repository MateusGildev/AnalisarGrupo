quant_mulheres = 0 
maior_idade = 0
quant_homens = 0

while True:
    print("-"*30)
    print("CADASTRE UMA PESSOA")
    print("-"*30)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip() .upper() [0]
        if idade > 18:
            maior_idade += 1
        if sexo == "F":
            if idade < 20:
                quant_mulheres += 1
        if sexo == "M":
            quant_homens += 1
        
    continuar = ' '
    while continuar  not in "SN":
        print("-"*30)
        continuar = str(input("Quer continuar? [S/N] ")).strip() .upper() [0]
    if continuar == "S":
        continue
    if continuar == "N":
        print("O total de pessoas com mais de 18 anos: {}".format(maior_idade))
        print("Ao todo temos {} homens cadastrados".format(quant_homens))
        print("E temos {} mulheres com menos de 20 anos".format(quant_mulheres))
        break
        