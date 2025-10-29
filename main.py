from medico import Medico
from paciente import Paciente
from consulta import Consulta


def main():
    print("Bem-vindo ao sistema de agendamento de consultas!\n")


    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar Paciente")
        print("2. Cadastrar Médico")
        print("3. Agendar Consulta")
        print("4. Ver Agenda de um Médico")
        print("5. Sair")
        escolha = input("Opção: ")

        if escolha == '1':
            paciente = Paciente("", "", "", "", "")
            paciente.cadastrar()
            
            

        elif escolha == '2':
            medico = Medico("", "", "", "", "")
            medico.cadastrar()
            
            
        elif escolha == '3':
            if not pacientes or not medicos:
                print("⚠️ Cadastre pelo menos 1 paciente e 1 médico antes de agendar.")
                continue

            print("\nEscolha o paciente:")
            for i, p in enumerate(pacientes, start=1):
                print(f"{i}. {p.nome}")
            escolha_p = int(input("Número do paciente: ")) - 1

            if escolha_p < 0 or escolha_p >= len(pacientes):
                print("Opção inválida.")
                continue

            paciente_escolhido = pacientes[escolha_p]
            paciente_escolhido.agendar_consulta(medicos)

        elif escolha == '4':
            if not medicos:
                print("⚠️ Nenhum médico cadastrado.")
                continue

            print("\nEscolha o médico:")
            for i, m in enumerate(medicos, start=1):
                print(f"{i}. Dr(a). {m.nome} - {m.especialidade}")
            escolha_m = int(input("Número do médico: ")) - 1

            if escolha_m < 0 or escolha_m >= len(medicos):
                print("Opção inválida.")
                continue

            medicos[escolha_m].ver_agenda()

        elif escolha == '5':
            print("Encerrando o sistema... 👋")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()