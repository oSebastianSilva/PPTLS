import random
import getpass
gameTrue = True

print("Jogo da Sorte - PPTLS \n\n- MENU -\n\nCOMEÇAR [1] \nSAIR [0]")
STEX = int(input(""))

def game():
    while gameTrue:

      print("pedra (1) - papel (2) - tesoura (3) - lagarto (4) - spock (5)")
      player = int(input("selecione o elemento para jogar: "))

      opcoes = ["pedra","papel","tesoura","lagarto","spock"]

      try:
        if player < 0: 
          raise Exception()
        player = opcoes[player - 1]
      except:
        print("opção inexistente.")
        continue


      element = random.choice(opcoes)
      print("\no bot escolheu: ",element)

      if player == element:
        print("empate!\n")


      elif player == "pedra" and (element == "tesoura" or element == "lagarto"):
        if element == "tesoura":
          print("pedra quebra tesoura, você ganhou!")
          break
        elif element == "lagarto":
          print("pedra esmaga lagarto... você ganhou!")
          break
          
      elif element == "pedra" and (player == "tesoura" or element == "lagarto"):
        if player == "tesoura":
          print("pedra quebra tesoura, você perdeu!")
          break
        elif player == "lagarto":
          print("pedra esmaga lagarto... você perdeu!")
          break



      elif player == "papel" and (element == "pedra" or element == "spock"):
        if element == "pedra":
          print("papel cobre pedra, você ganhou!")
          break
        elif element == "spock":
          print("papel refuta spock... você ganhou!")
          break

      elif element == "papel" and (player == "pedra" or player == "spock"):
        if player == "pedra":
          print("papel cobre pedra, você perdeu!")
          break
        elif player == "spock":
          print("papel refuta spock... você perdeu!")
          break



      elif player == "tesoura" and (element == "papel" or element == "lagarto"):
        if element == "papel":
          print("tesoura corta papel, você ganhou!")
          break
        elif element == "lagarto":
          print("tesoura decapita lagarto... você ganhou!")
          break

      elif element == "tesoura" and (player == "papel" or player == "lagarto"):
        if player == "papel":
          print("tesoura corta papel, você perdeu!")
          break
        elif player == "lagarto":
          print("tesoura decapita lagarto... você perdeu!")
          break



      elif player == "lagarto" and (element == "spock" or element == "papel"):
        if element == "spock":
          print("lagarto envenena spock... você ganhou!")
          break
        elif element == "papel":
          print("lagarto come papel... você ganhou!")
          break

      elif element == "lagarto" and (player == "spock" or player == "papel"):
        if player == "spock":
          print("lagarto envenena spock... você perdeu!")
          break
        elif player == "papel":
          print("lagarto come papel... você perdeu!")
          break



      elif player == "spock" and (element == "tesoura" or element == "pedra"):
        if element == "tesoura":
          print("spock derrete tesoura... você ganhou!")
          break
        elif element == "pedra":
          print("spock vaporiza pedra. você ganhou!")
          break

      elif element == "spock" and (player == "tesoura" or player == "pedra"):
        if player == "tesoura":
          print("spock derrete tesoura... você perdeu!")
          break
        elif player == "pedra":
          print("spock vaporiza pedra... você perdeu!")
          break


def mult():
  while gameTrue:

    print("pedra (1) - papel (2) - tesoura (3) - lagarto (4) - spock (5)")
    player_1 = int(getpass.getpass("\njogador 1 selecionando: "))
    player_2 = int(getpass.getpass("vez de jogador 2: "))

    opcoes = ["pedra","papel","tesoura","lagarto","spock"]

    try:
      if player_1 < 0 or player_2 < 0:
        raise Exception()
      player_1 = opcoes[player_1 - 1]
      player_2 = opcoes[player_2 - 1]
    except:
      print("opção inexistente.")
      continue


    if player_1 == player_2:
      print("empate!\n")


    elif player_1 == "pedra" and (player_2 == "tesoura" or player_2 == "lagarto"):
      if player_2 == "tesoura":
        print("pedra quebra tesoura, player 1 ganhou!")
        break
      elif player_2 == "lagarto":
        print("pedra esmaga lagarto... player 1 ganhou!")
        break
        
    elif player_2 == "pedra" and (player_1 == "tesoura" or player_2 == "lagarto"):
      if player_1 == "tesoura":
        print("pedra quebra tesoura, player 2 ganhou!")
        break
      elif player_1 == "lagarto":
        print("pedra esmaga lagarto... player 2 ganhou!")
        break



    elif player_1 == "papel" and (player_2 == "pedra" or player_2 == "spock"):
      if player_2 == "pedra":
        print("papel cobre pedra, player 1 ganhou!")
        break
      elif player_2 == "spock":
        print("papel refuta spock... player 1 ganhou!")
        break

    elif player_2 == "papel" and (player_1 == "pedra" or player_1 == "spock"):
      if player_1 == "pedra":
        print("papel cobre pedra, player 2 ganhou!")
        break
      elif player_1 == "spock":
        print("papel refuta spock... player 2 ganhou!")
        break



    elif player_1 == "tesoura" and (player_2 == "papel" or player_2 == "lagarto"):
      if player_2 == "papel":
        print("tesoura corta papel, player 1 ganhou!")
        break
      elif player_2 == "lagarto":
        print("tesoura decapita lagarto... player 1 ganhou!")
        break

    elif player_2 == "tesoura" and (player_1 == "papel" or player_1 == "lagarto"):
      if player_1 == "papel":
        print("tesoura corta papel, player 2 ganhou!")
        break
      elif player_1 == "lagarto":
        print("tesoura decapita lagarto... player 2 ganhou!")
        break



    elif player_1 == "lagarto" and (player_2 == "spock" or player_2 == "papel"):
      if player_2 == "spock":
        print("lagarto envenena spock... player 1 ganhou!")
        break
      elif player_2 == "papel":
        print("lagarto come papel... player 1 ganhou!")
        break

    elif player_2 == "lagarto" and (player_1 == "spock" or player_1 == "papel"):
      if player_1 == "spock":
        print("lagarto envenena spock... player 2 ganhou!")
        break
      elif player_1 == "papel":
        print("lagarto come papel... player 2 ganhou!")
        break



    elif player_1 == "spock" and (player_2 == "tesoura" or player_2 == "pedra"):
      if player_2 == "tesoura":
        print("spock derrete tesoura... player 1 ganhou!")
        break
      elif player_2 == "pedra":
        print("spock vaporiza pedra. player 1 ganhou!")
        break

    elif player_2 == "spock" and (player_1 == "tesoura" or player_1 == "pedra"):
      if player_1 == "tesoura":
        print("spock derrete tesoura... player 2 ganhou!")
        break
      elif player_1 == "pedra":
        print("spock vaporiza pedra... player 2 ganhou!")
        break

    else: print("opção inexistente.")
    
    
if STEX == 1:
  print("Bem-vindo ao PPTLS. O jogo funciona da seguinte maneira: "
    +"\nCada elemento tem uma certa vatangem contra outros dois elementos. \nAs regras do jogo são as seguintes:\n\n"
    + "1. Tesoura corta Papel \n2. Papel cobre Pedra \n3. Pedra esmaga Lagarto \n"
    +"4. Lagarto envenena Spock \n5. Spock derrete Tesoura \n6. Tesoura decapita lagarto \n"
    +"7. Lagarto come papel \n8. Papel refuta Spock \n9. Spock vaporiza Pedra \n"
    +"10. Pedra amassa Tesoura.\n")

  modo_game = int(input("selecione o modo de jogo: \n\nPlayer VS Player [1] \nContra Bot [2] \n"))

  if modo_game == 1: mult()
  elif modo_game == 2: game()
  else: print("modo de jogo indisponível")


  restart = int(input("\nDeseja jogar novamente? \nSIM [1] \nNÃO [0]\n"))
  while restart != 0:
    if modo_game == 1: mult()
    else: game()

    restart = int(input("\nDeseja jogar novamente? \nSIM [1] \nNÃO [0]\n"))

  print("fechando...")
      

elif STEX == 0: print("fechando...")
else: print("opção inválida ou indisponível.")