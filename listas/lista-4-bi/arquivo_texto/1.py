nome_arquivo = input("Digite o nome do arquivo HTML (sem a extensão): ") + ".html"
titulo_pagina = input("Digite o título da página: ")  

print("Digite o conteúdo da página (você pode usar tags HTML):")
print("Para finalizar a inserção do texto, digite 'FIM' e pressione Enter.")
    
linhas = []
while True:
    linha = input()
    if linha.upper() == "FIM":
        break
    linhas.append(linha)
conteudo_html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo_pagina}</title>
</head>
<body>
    {" ".join(linhas)}
</body>
</html>
"""
arquivo = open(nome_arquivo, "w")
arquivo.write(conteudo_html)
    
print(f"Arquivo {nome_arquivo} criado com sucesso!")

