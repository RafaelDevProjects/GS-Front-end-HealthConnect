from datetime import datetime
import re
import sqlite3
from funcoes import *


def main():
    imprimir_linha_bonita("agendamento de exame e ficha do paciente")

    global ficha_paciente
    ficha_paciente = []

    # pega o nome do paciente
    nome = input("Nome do paciente:")
    lista_append(nome)

    # pega a idade do paciente
    idade = verifica_num(input("Idade do paciente:"), "Idade do paciente:",
                         "A idade deve ser cadastrada em números inteiros (1, 10, 55, 80 etc...)")
    lista_append(idade)

    # pega a data de nascimento
    while True:
        data_nascimento = input("Data de nascimento do paciente DD-MM-YYYY:")
        if verifica_data(data_nascimento):
            break
        else:
            print("Data de nascimento inválida, deve ser preenchida neste formato: DD-MM-YYYY")
    lista_append(data_nascimento)

    # pega o endereço
    endereco = input("Endereço do paciente:")
    lista_append(endereco)

    # pega o telefone
    telefone = input("Telefone para contato do paciente ex (dd) 92118-4570:")
    telefone_formatado = verifica_telefone(telefone)
    while telefone_formatado is None:
        telefone = input("Telefone para contato do paciente (dd) 92118-4570:")
        telefone_formatado = verifica_telefone(telefone)
    lista_append(telefone_formatado)

    # Sexo do Paciente
    lista_sexo = ["masculino", "feminino"]
    sexo = escolher_opcao(input("Sexo do paciente:"), lista_sexo, "Sexo do paciente:",
                          f"O sexo deve ser uma opção válida ex:{lista_sexo}")
    lista_append(sexo)

    # pega o tipo sanguíneo
    imprimir_tabela_tipos_sanguineos()
    lista_sangue = ["a-", "a+", "b+", "b-", "ab+", "ab-", "o+", "o-"]
    tipo_sanguineo = escolher_opcao(input("Tipo Sanguíneo do paciente:"), lista_sangue,
                                    "Tipo Sanguíneo do paciente:",
                                    f"O tipo sanguíneo deve ser uma opção existente ex:{lista_sangue}")
    lista_append(tipo_sanguineo)

    # pergunta se o paciente tem alergia
    opcao_alergia = input("O paciente tem alguma alergia?").strip().lower()
    opcao_alergia = escolher_opcao(opcao_alergia[0], ["s", "n"], "O paciente tem alguma alergia?",
                                   "Digite uma resposta válida!")
    if opcao_alergia == "s":
        alergia = input("Qual?")
    else:
        alergia = "vazio"
    lista_append(alergia)

    # pergunta se tem problema crônico
    opcao_saude_cronico = input("O paciente tem algum problema de saúde crônico?").strip().lower()
    opcao_saude_cronico = escolher_opcao(opcao_saude_cronico[0], ["s", "n"],"O paciente tem algum problema de saúde crônico?","Digite uma resposta válida!")

    if opcao_saude_cronico == "s":
        saude_cronico = input("Qual?")
    else:
        saude_cronico = "vazio"
    lista_append(saude_cronico)

    # pergunta se é prioritário
    lista_prioritario = ["pcd", "idoso", "gestante"]
    opcao_prioridade = input("O paciente é prioritário?").strip().lower()
    opcao_prioridade = escolher_opcao(opcao_prioridade[0], ["s", "n"],
                                      "O paciente é prioritário?", "Digite uma resposta válida!")
    if opcao_prioridade == "s":
        prioritario = escolher_opcao(input(f"Qual das categorias ({', '.join(lista_prioritario)}): "),
                                      lista_prioritario,
                                      f"Qual das categorias ({', '.join(lista_prioritario)}):",
                                      f'A opção deve ser uma destas: {", ".join(lista_prioritario)}')
    else:
        prioritario = "vazio"
    lista_append(prioritario)

    # pergunta o exame que ele irá fazer
    lista_exames = ["raio-x", "ultrassom", "tomografia", "ressonancia", "ecocardiograma"]
    exame = escolher_opcao(input(f"Exame que deseja realizar ({', '.join(lista_exames)}): "), lista_exames,
                            f"Exame que deseja realizar ({', '.join(lista_exames)}):",
                            "Escolha entre uma das opções apresentadas!")
    lista_append(exame)

    # pergunta a data do exame
    while True:
        data_exame = input("Data para realização do exame DD-MM-YYYY:")
        if verifica_data_futura(data_exame):
            print("Agendamento realizado com sucesso!")
            break
        else:
            print("Data inválida, deve ser preenchido neste formato: DD-MM-YYYY (dia-mês-ano).")
    lista_append(data_exame)

    criar_tabela()  # Certifica-se de que a tabela existe no banco de dado
    inserir_ficha_no_banco()  # Insere a ficha do paciente no banco de dados

    imprimir_ficha_completa()
    print(f"Muito Obrigado por utilizar os serviços da {Cor.ROSA}Healt{Cor.RESET}{Cor.AZUL}Connect{Cor.RESET}")

if __name__ == "__main__":
    main()
