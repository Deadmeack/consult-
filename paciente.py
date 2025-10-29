from usuario import Usuario
from consulta import Consulta

class Paciente(Usuario):
    def __init__(self, id_paciente, nome, CPF, contato, endereco, idade):
        super().__init__(nome, CPF, contato)
        self._endereco = endereco
        self._idade = idade
        self._id_paciente = id_paciente

    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    def cadastrar(self):
        print("---- Cadastro Cliente ----")
        nome = input("Nome: ")
        CPF = input("CPF: ")
        contato = input("Contato: ")
        endereco = input("Endereço: ")
        idade = input("Idade: ")
        self._nome = nome
        self._CPF = CPF
        self._contato = contato
        self._endereco = endereco
        self._idade = idade
        print("-------------------------------")
        print("Cadastro realizado com sucesso!\n")
        print("Dados do Cliente:\n")
        print(f"Nome: {self._nome}\nCPF: {self._CPF}\nContato: {self._contato}\nEndereço: {self._endereco}\nIdade: {self._idade}")
        print("-------------------------------")
    

    def agendar_consulta(self, medicos):
        print("---- Agendar Consulta ----")
        print("Escolha um médico disponível:")

        for i, m in enumerate(medicos, start=1):
            print(f"{i}. {m.nome} - {m.especialidade}")

        escolha = int(input("Número do médico: ")) - 1
        if escolha < 0 or escolha >= len(medicos):
            print("Opção inválida.")
            return None

        medico_escolhido = medicos[escolha]
        data = input("Data (AAAA-MM-DD): ")
        hora = input("Hora (HH:MM): ")

     
        consulta = Consulta(data, hora, self, medico_escolhido)

        self.consultas.append(consulta)
        medico_escolhido.adicionar_consulta(consulta)

        print("\nConsulta agendada com sucesso!")
        print(consulta.gerar_relatorio())
        return consulta