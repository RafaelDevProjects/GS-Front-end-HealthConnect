from datetime import datetime
import re
import sqlite3

ficha_paciente = []
class Cor:
    RESET = '\033[0m'
    CINZA = '\033[37m'
    VERDE = '\033[36m'
    ROSA = '\033[95m'
    AZUL = '\033[94m'

def limpar_cores(texto_formatado):
    # Remove códigos de cor ANSI
    return re.sub(r'\033\[\d+m', '', texto_formatado)
def imprimir_linha_bonita(msg):
    print(f"{Cor.ROSA}{'*' * (len(msg) + 4)}{Cor.RESET}")
    print(f"{Cor.ROSA}* {msg} *{Cor.RESET}")
    print(f"{Cor.ROSA}{'*' * (len(msg) + 4)}{Cor.RESET}")
def imprimir_tabela_tipos_sanguineos():
    print(f"{Cor.CINZA}Tipos Sanguíneos{Cor.RESET}")
    print(f"{Cor.CINZA}--------------------------{Cor.RESET}")
    print(f"{Cor.CINZA}A- | A+ | B+ | B- | AB+ | AB- | O+ | O-{Cor.RESET}")


def criar_tabela():
    # Função para criar a tabela no banco de dados
    conn = sqlite3.connect('ficha_paciente.db')
    cursor = conn.cursor()

    # SQL para criar a tabela se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ficha_paciente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            data_nascimento TEXT,
            endereco TEXT,
            telefone TEXT,
            sexo TEXT,
            tipo_sanguineo TEXT,
            alergia TEXT,
            saude_cronico TEXT,
            prioritario TEXT,
            exame TEXT,
            data_exame TEXT
        )
    ''')

    conn.commit()
    conn.close()

def inserir_ficha_no_banco():
    # Função para inserir a ficha do paciente no banco de dados
    conn = sqlite3.connect('ficha_paciente.db')
    cursor = conn.cursor()

    # Limpa a formatação dos dados
    dados_limpos = [re.sub(r'\033\[\d+m', '', dado) for dado in ficha_paciente]

    # Inserindo os dados da ficha do paciente
    cursor.execute('''
        INSERT INTO ficha_paciente
        (nome, idade, data_nascimento, endereco, telefone, sexo, tipo_sanguineo, alergia, saude_cronico, prioritario, exame, data_exame)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        dados_limpos[0],  # Nome
        dados_limpos[1],  # Idade
        dados_limpos[2],  # Data de Nascimento
        dados_limpos[3],  # Endereço
        dados_limpos[4],  # Telefone
        dados_limpos[5],  # Sexo
        dados_limpos[6],  # Tipo Sanguíneo
        dados_limpos[7],  # Alergia
        dados_limpos[8],  # Saúde Crônico
        dados_limpos[9],  # Prioritário
        dados_limpos[10],  # Exame
        dados_limpos[11],  # Data do Exame
    ))

    conn.commit()
    conn.close()




def formata_numero_celular(numero):
    # Remover caracteres não numéricos
    numero = re.sub(r'\D', '', numero)

    # Formatar para (dd) 92118-4570
    return f'({numero[:2]}) {numero[2:7]}-{numero[7:]}'

def verifica_telefone(numero):
    # Formatar o número de celular
    numero_formatado = formata_numero_celular(numero)

    # Verificar se o número formatado está no padrão desejado
    if re.match(r'^\(\d{2}\) \d{5}-\d{4}$', numero_formatado):
        return numero_formatado
    else:
        print("Formato de número de celular inválido!")
        return None

def verifica_data(data):
    try:
        datetime.strptime(data, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def verifica_data_futura(data):
    try:
        # Converter a string para um objeto datetime
        data_formatada = datetime.strptime(data, '%d-%m-%Y')

        # Verificar se a data é no futuro em relação à data atual
        data_atual = datetime.now()
        if data_formatada > data_atual:
            return True
        else:
            print("A data deve ser no futuro.")
            return False

    except ValueError:
        print("Formato de data inválido. Deve ser preenchido neste formato: DD-MM-YYYY")
        return False

def verifica_num(var, msg, alerta):
    while not var.isnumeric():
        print(alerta)
        var = input(msg)
    return int(var)

def escolher_opcao(var, lista_opcoes, msg, alerta):
    while var.lower() not in lista_opcoes:
        print(alerta)
        erro = input(msg).strip().lower()
        var = erro[0]
    return var

def lista_append(var):
    ficha_paciente.append(f"{Cor.VERDE}{var}{Cor.RESET}")

def imprimir_ficha_completa():
    print(f"{Cor.VERDE}Ficha completa do paciente{Cor.RESET}")

    labels = [
        "Nome do paciente",
        "Data de nascimento",
        "Endereço",
        "Telefone(cel)",
        "Sexo",
        "Idade do paciente",
        "Tipo sanguíneo",
        "Alergia",
        "Problema de saúde crônico",
        "Atendimento prioritário",
        "Periodo de exame",
        "Data de exame"
    ]

    for label, valor in zip(labels, ficha_paciente):
        print(f"{Cor.CINZA}{label}:{Cor.RESET} {valor}")
