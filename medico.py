from usuariobase import UsuarioBase

class Medico(UsuarioBase):
    def __init__(self, id_medico, nome_medico, CPF, contato, especialidade, CRM):
        super().__init__(CPF, contato)
        self._nome_medico = nome_medico
        self._id_medico = id_medico
        self._especialidade = especialidade
        self._CRM = CRM
    @property
    def nome(self):
        return self._nome_medico
    @nome.setter
    def nome(self, nome_medico):
        self._nome_medico = nome_medico
    
    @property
    def id_medico(self):
        return self._id_medico
    @id_medico.setter
    def id_medico(self, id_medico):
        self._id_medico = id_medico

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self._especialidade = especialidade

    @property
    def CRM(self):
        return self._CRM

    @CRM.setter
    def CRM(self, CRM):
        self._CRM = CRM

    def Cadastrar(self):
        print("---- Cadastro Médico ----")
        nome = input("Nome: ")
        CPF = input("CPF: ")
        contato = input("Contato: ")
        especialidade = input("Especialidade: ")
        CRM = input("CRM: ")
        self._nome_medico = nome
        self._CPF = CPF
        self._contato = contato
        self._especialidade = especialidade
        self._CRM = CRM
        print("-------------------------------")
        print("Cadastro realizado com sucesso!\n")
        print("Dados do Médico:\n")
        print(f"Nome: {self._nome}\nCPF: {self._CPF}\nContato: {self._contato}\nEspecialidade: {self._especialidade}\nCRM: {self._CRM}")
        print("-------------------------------")
    
    def Autenticar(self):
        print("---- Autenticação Médico ----")
        nome = input("Nome: ")
        CRM = input("CRM: ")
        if nome == self._nome_medico and CRM == self._CRM:
            print("Autenticação bem-sucedida!")
            return True
        else:
            print("Falha na autenticação. Nome ou CRM incorretos.")
            return False

    def Ver_Agenda(self):
        print(f"Exibindo agenda do Dr(a). {self._nome_medico}...")
        print("-------------------------------")
        print("Agenda de Consultas:\n")

        print(f"2024-07-01': '09:00 - Consulta com {self._nome_paciente}")
        print(f"2025-01-01': '10:00 - Consulta com {self._nome_paciente}")
