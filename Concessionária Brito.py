
    # Tabela que vou pegar o preço dos carros de acordo com a tabela fipe de cada carro
tabela_fipe = {
    "Nissan": {"R34": 950000,"370z":277148,"Silvia s15":122472},
    "Toyota": {"Supra mk4": 980000,"Corola": 180000,"SW4":384190},
    "Volkswagen": {"Polo":87990,"Jetta":250990,"ID. Buzz":840000},
    "Fiat": {"Uno":32426, "Palio": 31866, "Toro": 152453},
    "Mercedez": {"CLA Coupé": 295900,"GLE":729900,"GLS":979900}
}
    # Está tabela serve para mostrar as opções de marcas e carros disponíveis
veiculos_empresa= {
    "Nissan": {"R34","370z","Silvia s15"},
    "Toyota": {"Supra mk4","Corola","SW4"},
    "Volkswagen": {"Polo","Jetta","ID. Buzz"},
    "Fiat": {"Uno", "Palio", "Toro" },
    "Mercedez": {"CLA Coupé","GLE","GLS"}
}
   # Aqui eu pego os dados necessarios para o usuário continuar o código
print("---Cadastro do cliente---\n")
cliente = input("Digite seu nome: ")
telefone = int(input("Digite seu número: "))
saldo = float(input("Digite o seu saldo: "))
   # O while serve para conseguir colocar o código em loop até o momento que o usuário desejar sair
while True:
    # Aqui eu apresento as opções que o usuário poderá usar no código
    print("----Bem-vindo a concessionária Brito.----\n")
    print("\n1. Vender veículo.")
    print("2. Alugar veículo.")
    print("3. Comprar veículo.")
    print("4. Sair.")
    
    opcao = int(input("Selecione uma das opções: "))   #Aqui eu pego a opção que o usuário desejar

    match opcao: # Aqui eu uso match para ir para a opção que o usuário digitou 

        case 1:
  
            i = 0 # Contador apenas para mostrar as opções com os números
            print("Marcas disponíveis para venda: ")

            for escolha_marca in veiculos_empresa: # For para mostrar as opções de marcas 

                print("{}. {}".format(i + 1,escolha_marca))
                i += 1

            escolha_marca = int(input("Escolha a marca (1-{}): ".format(i))) # Aqui eu pego a opção de marca que o usuário selecionou
                           
            if escolha_marca >= 1 and escolha_marca <= 5:  # If para conferir se a opção de marca que o usuário digitou é valída

                i = 0 # Contador apenas para mostrar as opções com os números
                print("Modelos disponíveis da marca:")
                marca_selecionada = list(veiculos_empresa)[escolha_marca - 1] # Aqui eu pego a opçao que o usuário digitou só que na lista, sem ser int

                for modelos in veiculos_empresa[marca_selecionada]: # For para mostrar os modelos de carro disponível

                    print("{}. {}".format(i + 1,modelos))
                    i += 1

                modelos = int(input("Escolha um carro (1-{}): ".format(i))) # Aqui eu pego a opção de carro que o usuário selecionou
                
                if modelos >= 1 and modelos <= 3: # If para conferir se a opção de marca que o usuário digitou é valída

                    carro_selecionado = list(veiculos_empresa[marca_selecionada])[modelos-1] # Aqui eu pego a opçao que o usuário digitou só que na lista, sem ser int

                    # Calculo do valor do carro com o desconto de venda de carro
                    valor = tabela_fipe[marca_selecionada][carro_selecionado]
                    valor_desconto = valor * 0.12
                    valor = valor - valor_desconto

                    print("Nossa proposta para venda deste carro ficará em R${:.2f}".format(valor)) # Aqui eu mostro a proposta da concessionária para a venda do veiculo

                    continuar = input("Deseja continuar a venda? (S/N):\n") 

                    if continuar == 'S' or continuar == 's': # Confirmação para ver se o usuário continuará a compra

                        saldo += valor_desconto # Conta para adicionar o valor da venda ao saldo do usuário
                        print("Seu saldo atual é R${:.2f}".format(saldo))


                    else: # else para venda cancelada
                        print("Venda cancelada!!") 

                else: # erro caso o usuário digite um opção invalída
                    print("Opção invalída! Tente outra.")   

            else: # erro caso o usuário digite um opção invalída
                print("Opção invalída! Tente outra.")         
            
        case 2:
            i = 0 # Contador apenas para mostrar as opções com os números

            print("Marcas disponíveis para alugar: ")

            for escolha_marca in veiculos_empresa: # For para mostrar as opções de marcas 
                print("{}. {}".format(i + 1,escolha_marca))
                i += 1

            escolha_marca = int(input("Escolha a marca (1-{}): ".format(i))) # Aqui eu pego a opção de marca que o usuário selecionou

            if escolha_marca >= 1 and escolha_marca <= 5:  # If para conferir se a opção de marca que o usuário digitou é valída

                i = 0 # Contador apenas para mostrar as opções com os números
                marca_selecionada = list(veiculos_empresa)[escolha_marca - 1] # Aqui eu pego a opçao que o usuário digitou só que na lista, sem ser int
                                 
                print("Modelos disponíveis da marca:")
                for modelos in veiculos_empresa[marca_selecionada]: # For para mostrar os modelos de carro disponível
                    print("{}. {}".format(i + 1,modelos))
                    i += 1

                modelos = int(input("Escolha um carro (1-{}): ".format(i)))# Aqui eu pego a opção de carro que o usuário selecionou
                            
                if modelos >= 1 and modelos <= 3: # If para conferir se a opção de marca que o usuário digitou é valída

                    carro_selecionado = list(veiculos_empresa[marca_selecionada])[modelos-1] # Aqui eu pego a opçao que o usuário digitou só que na lista, sem ser int

                    # Aqui pergunto qunatos dias o usuário deseja ficar com o carro e já faço o calculo do aluguel
                    dias = int(input("Digite a quantidade de dias que deseja alugar o carro: "))
                    aluguel = 77 * dias

                    print("A o valor do aluguel por {} dias ficará em R${:.2f}".format(dias,aluguel)) # Aqui mostro quanto ficará para alugar o carro de acordo com a quantidade de dias que o usuário escolheu 

                    continuar = input("Deseja continuar para alugar? (S/N):\n") 

                    if continuar == 'S' or continuar == 's': # Confirmação para ver se o usuário continuará a compra

                        if saldo >= aluguel: # Confirmaçao para ver se o saldo do usuário é maior que a divida que ele terá com o valor do aluguel
                            # Aqui subtraio o valor do aluguel no saldo do usuário 
                            saldo -= aluguel
                            veiculos_empresa[marca_selecionada].remove(carro_selecionado)
                            print("Aluguel feito com sucesso.")
                            print("Seu saldo atual é R${:.2f}".format(saldo)) # Aqui mostro o saldo atual depois dele ter alugado o carro

                        else:
                            print("Saldo insuficiente") # Erro caso o usuário não tenha saldo
                    else:
                        print("Venda cancelada!!")   # Else caso ele não queira mais alugar
                else:
                    print("Opção invalída! Tente outra.")   # Erro para opção invalida
            else:
                    print("Opção invalída! Tente outra.")    # Erro para opção invalida                

        case 3: 
            i = 0# Contador apenas para mostrar as opções com os números
            print("Marcas disponíveis para compra: ")
            for escolha_marca in veiculos_empresa: # For para mostrar as opções de marcas 
                print("{}. {}".format(i + 1,escolha_marca))
                i += 1
            escolha_marca = int(input("Escolha a marca (1-{}): ".format(i))) # Aqui eu pego a opção de marca que o usuário selecionou

            if escolha_marca >= 1 and escolha_marca <= 5: # If para conferir se a opção de marca que o usuário digitou é valída
            
                marca_selecionada = list(veiculos_empresa)[escolha_marca - 1] # Aqui eu pego a opçao que o usuário digitou só que na lista, sem ser int
                i = 0
                
                print("Modelos disponíveis da marca:")
                for modelos in veiculos_empresa[marca_selecionada]: # For para mostrar os modelos de carro disponível
                    print("{}. {}".format(i + 1,modelos))
                    i += 1

                modelos = int(input("Escolha um carro (1-3): ")) # Aqui eu pego a opção de marca que o usuário selecionou

                if modelos >= 1 and modelos <= 3: # If para conferir se a opção de marca que o usuário digitou é valída

                    carro_selecionado = list(veiculos_empresa[marca_selecionada])[modelos-1] # Aqui eu pego a opçao que o usuário digitou só que na lista, sem ser int

                    # Aqui eu faço o calculo de acrescimo no valor do carro para compra dele
                    valor = tabela_fipe[marca_selecionada][carro_selecionado]
                    valor_acrescimo = valor * 0.25
                    valor_acrescimo += valor

                    print("O valor deste carro na tabela fipe é de R${:.2f}".format(tabela_fipe[marca_selecionada][carro_selecionado])) # Aqui mostro o valor do carro na tabela fipe
                    print("Nossa proposta para venda deste carro ficará em R${:.2f}".format(valor_acrescimo)) # Aqui mostro o valor da proposta de compra do carro
                    continuar = input("Deseja continuar a venda? (S/N):\n")

                    if continuar == 'S' or continuar == 's': # Confirmação para ver se o usuário continuará a compra
                        if saldo > valor_acrescimo: # Confirmaçao para ver se o saldo do usuário é maior que a divida que ele terá com o valor do aluguel
                            # Aqui eu faço o calculo para subtrair o valor da compra ao saldo do usuário
                            saldo -= valor_acrescimo
                            print("Seu saldo atual é R${:.2f}".format(saldo)) # Mostro o saldo do usuário depois da compra do carro
                        
                        else: 
                            print("Saldo insuficiente!") # Erro caso o usuário não tenha saldo

                    else:
                        print("Venda cancelada") # Else caso ele não queira mais alugar

                else:
                    print("Opção invalída! Tente outra.")    # Erro para opção invalida

            else:
                    print("Opção invalída! Tente outra.")    # Erro para opção invalida

        case 4:
            
            print("Código finalizado")  # Case para quando o usuário selecionar a opção 4 o código parar o loop
            break    
                 
        case _:
            print("Opção invalída! Tente outro.") # Erro caso o usuário tente uma opção invalida