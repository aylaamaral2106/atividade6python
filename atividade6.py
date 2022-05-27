#Crie um sistema que imprima um recibo de compras para o usuário. O sistema vai perguntar a quantidade de itens diferentes e depois vai perguntar qual o nome do item e a quantidade deste item. No final o programa exibe o recibo juntamente com o valor final da compra. Veja um exemplo de como o sistema deve funcionar: 

itensdiferentes = float(input(">>Quantidade de itens diferentes: "))

valortotal = 0

itens = []

i = 0 
while i < itensdiferentes:
    nome = input(">>Nome do item " + str(i+1) + ":")
    quantidade = input(">>Quantidade deste produto :")
    valor = input(">>Valor Unitário deste produto :")
    valortotal += float(valor)
    recibo = {
     nome,
     quantidade,
     valor
    }
    itens.append(quantidade)
    itens.append(nome)
    itens.append(valor)

    i += 1

linhaformatada = ("===================================")
print(linhaformatada)

reciboformatado = ("       Recibo:")
print(reciboformatado)

nomequantidadeformatado = (" Quantidade  | Nome  | Valor")
print(nomequantidadeformatado)

print(itens)

valortotalformatado = ("   Total: " + str(valortotal))

print(valortotalformatado)

linhasformatada = ("====================================")
print(linhasformatada)
