import sqlite3

busca = input("Quem você está procurando? ").strip()

try:
    with sqlite3.connect("meubanco.db") as banco:
    # banco = sqlite3.connect("meubanco.db")
        banco.row_factory = sqlite3.Row # faz com que eu possa colocar o nome da tabela ao invés do indice, no for ali embaixo
        cur = banco.cursor()
        cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

        # lista = cur.fetchall()
        # print(lista)

        total = 0
        for total, amigo in enumerate(cur, start=1):
            print(f"[{amigo[0]}] {amigo["nome"]} nasceu em {amigo[2]}")
        print(f"Ao todo encontrei {total} amigos com '{busca}'")

except sqlite3.Error as e:
    print(f"Falha no banco: {e}")
except Exception as e:
    print(f"Algo deu errado: {e}")

# cur.close()
# banco.close()
print("ACABOU!")