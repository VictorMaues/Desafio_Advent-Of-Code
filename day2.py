import os

def ids_validos():
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados2.txt")

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()

    intervalos = conteudo.replace("\n", "").split(",")
    soma_invalidos = 0

    for item in intervalos:
        item = item.strip()
        if not item:
            continue

        inicio_str, fim_str = item.split("-")
        inicio = int(inicio_str)
        fim = int(fim_str)

        tam_min = len(inicio_str)
        tam_max = len(fim_str)

        for tamanho_total in range(tam_min, tam_max + 1):
            if tamanho_total % 2 != 0:
                continue

            tam_metade = tamanho_total // 2
            menor_metade = 10 ** (tam_metade - 1)
            maior_metade = (10 ** tam_metade) - 1

            for metade in range(menor_metade, maior_metade + 1):
                metade_str = str(metade)
                numero_invalido = int(metade_str + metade_str)

                if inicio <= numero_invalido <= fim:
                    soma_invalidos += numero_invalido

    print(soma_invalidos)

if __name__ == "__main__":
    ids_validos()