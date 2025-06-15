import psycopg2

#Conectando ao banco de dados 
conexão = psycopg2.connect(
    host="localhost", # type: ignore
    database="cadastro_alunos",
    user="postgres",
    password="sofia123",
    port="5432"
)
print("✅ Conectado ao banco de dados com sucesso!")

# Criando cursor para executar comandos
cursor = conexão.cursor()

# Testando com SELECT
cursor.execute("SELECT * FROM alunos;")
alunos = cursor.fetchall()

# Exibindo resultados

dados_banco = cursor.fetchall()

for aluno in alunos:
    print(aluno)

# Fechando conexão
cursor.close()
conexão.close()


alunos = []

def calcular_media(n1, n2, n3):
    return round((n1 + n2 + n3) / 3, 2)

def verificar_status(media):
    return "APROVADO" if media >= 7 else "REPROVADO"

def cadastrar_aluno():
    print("\n=== Cadastro de Aluno ===")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    idade = input("Idade: ")

    try:
        nota1 = float(input("Nota 1 (Portugues): "))
        nota2 = float(input("Nota 2 (Matematica): "))
        nota3 = float(input("Nota 3 (Ingles): "))
    except ValueError:
        print("Notas inválidas. Use números.")
        return

    media = calcular_media(nota1, nota2, nota3)
    status = verificar_status(media)

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "idade": idade,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "status": status
    }

    alunos.append(aluno)
    print(f"\nAluno {nome} cadastrado com média {media} - {status}.\n")

def listar_alunos():
    if not alunos:
        print("\nNenhum aluno cadastrado.\n")
        return

    print("\n=== Lista de Alunos ===")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Notas: {aluno['nota1']}, {aluno['nota2']}, {aluno['nota3']}")
        print(f"Média: {aluno['media']}")
        print(f"Status: {aluno['status']}")
        print("-" * 30)

def menu():
    while True:
        print("\n===== Sistema de Cadastro de Alunos =====")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
