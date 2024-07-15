def int_flo():
    while True:
        try: 
            inteiro = int(input("Digite um número inteiro: "))
            ponto_flutuante = float(input("Digite um número: "))
            res = f"A resposta obtida foi:\n inteiro = {inteiro} e\n flutuante = {ponto_flutuante}"
            return res
        except Exception as erro:
            res = "ERRO INDENTIFICADO!!! " 

res = int_flo()
print(res)