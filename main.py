pos = 50
senha = 0


with open('teste.txt') as arquivo:
   for linha in arquivo:
       direcao = linha.strip()[0]
       distancia = int(linha.strip()[1:])


       if direcao == "R":
           print(f"posição: {pos}, Direção: {direcao}, Distancia: {distancia}")
           pos += distancia
          
           senha += pos // 100
           pos %= 100
           print(f"Movendo para a direita: {distancia}, nova posição: {pos}")




       elif direcao == "L":
           print(f"posição: {pos}, Direção: {direcao}, Distancia: {distancia}")
           pos -= distancia
           senha += abs(pos) // 100
           pos %= 100
           print(f"Movendo para a esquerda: {distancia}, nova posição: {pos}")




       if pos == 0:
          senha += 1


print(f"senha: {senha}")
