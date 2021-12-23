print('Cadastro de usuário\n\nInformações para realizar o cadastro\n\n1º - O nome do usuário deve ter mais de 2 caracteres'
      '\n2º - A idade deve ser maior que 0 e menor que 150\n3º - O salário deve ser maior que 0\n4º - O sexo deve ser f ou m.'
      ' Onde f é feminino e m é masculino\n4º - O estado civil deve ser s, c, v ou d. Onde, s é solteiro, c casado, v viúvo e d divorciado')
nome = input('\n\nNome: ')
if len(nome) < 3:
    while len(nome) < 3:
        print('Nome inválido.')
        nome = input('Nome: ')
        
idade = int(input('Idade: '))
if idade < 0 or idade > 150:
    while idade < 0 or idade > 150:
        print('Idade inválida.')
        idade = int(input('Idade: '))

salario = float(input('Salário: '))
if salario <= 0:
    while salario <= 0:
        print('Salario inválido.')
        salario = float(input('Salário: '))
        
sexo = input('Sexo: ')
sex = ('f', 'm')
if sexo not in sex:
    while sexo not in sex:
        print('Sexo inválido.')
        sexo = input('Sexo: ')
    
estado_civil = input('Estado civil: ')
est = ('s', 'c', 'v', 'd')
if estado_civil not in est:
    while estado_civil not in est:
        print('Estado civil inválido.')
        estado_civil = input('Estado civil: ')

escolha = input(f'\nParabéns senhor(a) {nome} o seu cadastro foi realizado com sucesso. Se o senhor quiser '
                f' visualizar o seu cadastro pressione a tecla c, se quiser alterar seu cadastro \npressione a tecla a. Se'
                f' não quiser alterar nada pressione qualquer outra tecla: ')
if escolha == "c":
    print(f'\nO seu cadastro é:\nNome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}\nEstado civil: '
          f'{estado_civil} ')
    escolha_2 = input('\nGostaria de ver novamente o seu cadastro? Digite s para sim, ou n para não: ')
    if escolha_2 == "s":
        while escolha_2 == "s":
            print(f'\nO seu cadastro é:\nNome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}\nEstado civil: '
          f'{estado_civil} ')
            escolha_2 = input('\nGostaria de ver novamente o seu cadastro? Digite s para sim, ou n para não: ')
            if escolha_2 =="n":
                print(f'\nOk, obrigado por utilizar nosso sistema sr(a) {nome}')
    elif escolha_2 == "n":
        print(f'\nOk, obrigado por utilizar nosso sistema sr(a) {nome}')
    else:
        while escolha_2 != "s" or escolha_2 != "n":
            escolha_2 = input('\nResposta inválida. Por gentileza, digite s para sim ou n para não: ')
elif escolha == "a":
    while escolha == "a":
        nome = input('\n\nNome: ')
        if len(nome) < 3:
            while len(nome) < 3:
                print('Nome inválido.')
                nome = input('Nome: ')

        idade = int(input('Idade: '))
        if idade < 0 or idade > 150:
            while idade < 0 or idade > 150:
                print('Idade inválida.')
                idade = int(input('Idade: '))

        salario = float(input('Salário: '))
        if salario <= 0:
            while salario <= 0:
                print('Salario inválido.')
                salario = float(input('Salário: '))

        sexo = input('Sexo: ')
        sex = ('f', 'm')
        if sexo not in sex:
            while sexo not in sex:
                print('Sexo inválido.')
                sexo = input('Sexo: ')

        estado_civil = input('Estado civil: ')
        est = ('s', 'c', 'v', 'd')
        if estado_civil not in est:
            while estado_civil not in est:
                print('Estado civil inválido.')
                estado_civil = input('Estado civil: ')
        escolha = input(f'\nParabéns senhor(a) {nome} o seu cadastro foi alterado com sucesso. Se o senhor quiser '
                f' visualizar o seu cadastro pressione a tecla c, se quiser alterar seu cadastro \npressione a tecla a. Se'
                f' não quiser alterar nada pressione qualquer outra tecla: ')
        if escolha == "c":
            print(f'\nO seu cadastro é:\nNome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}\nEstado civil: '
                  f'{estado_civil} ')
            escolha_2 = input('\nGostaria de ver novamente o seu cadastro? Digite s para sim, ou n para não: ')
            if escolha_2 == "s":
                while escolha_2 == "s":
                    print(
                        f'\nO seu cadastro é:\nNome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}\nEstado civil: '
                        f'{estado_civil} ')
                    escolha_2 = input('\nGostaria de ver novamente o seu cadastro? Digite s para sim, ou n para não: ')
                    if escolha_2 == "n":
                        print(f'\nOk, obrigado por utilizar nosso sistema sr(a) {nome}')
            elif escolha_2 == "n":
                print(f'\nOk, obrigado por utilizar nosso sistema sr(a) {nome}')
            else:
                while escolha_2 != "s" or escolha_2 != "n":
                    escolha_2 = input('\nResposta inválida. Por gentileza, digite s para sim ou n para não: ')
else:
    print(f'\nOk, obrigado por utilizar nosso sistema sr(a) {nome}')








    
    
