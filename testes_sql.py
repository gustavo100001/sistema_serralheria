import sqlite3
conexao = sqlite3.connect("serralheria.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orcamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT,
    servico TEXT,
    valor REAL
)
""")

vcliente = input("Digite o nome do cliente: ")
vservico = input("Digite o serviço: ")
vvalor = float(input("Digite o valor do orçamento: "))

cursor.execute("insert into orcamentos (cliente, servico, valor) values (?, ?, ?)",
               (vcliente, vservico, vvalor))
conexao.commit()


print("Orçamento cadastrado com sucesso!")

cursor.execute("SELECT * FROM orcamentos")

meus_dados = cursor.fetchall()

for x in meus_dados:
   print(f"Pedido #{x[0]} | Cliente: {x[1]} | Serviço: {x[2]} | Valor: R$ {x[3]:.2f}")

id_pedido = input(" qual id quer mudar: ")
novo_valor = input(" Mudar preco: ")

cursor.execute("Update orcamentos set valor = ? WHERE id = ?", (novo_valor, id_pedido))

conexao.commit()

conexao.close()
