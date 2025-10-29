from usuario import Usuario

class Medico(Usuario):
    def __init__(self, id_medico, nome, CPF, contato, especialidade, crm):
        super().__init__(nome, CPF, contato)
        self._especialidade = especialidade
        self._crm = crm
        self._id_medico = id_medico
    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self._especialidade = especialidade

    @property
    def crm(self):
        return self._crm

    @crm.setter
    def crm(self, crm):
        self._crm = crm

    def cadastrar(self):
        print("---- Cadastro Médico ----")
        nome = input("Nome: ")
        CPF = input("CPF: ")
        contato = input("Contato: ")
        especialidade = input("Especialidade: ")
        crm = input("CRM: ")
        self._nome = nome
        self._CPF = CPF
        self._contato = contato
        self._especialidade = especialidade
        self._crm = crm
        print("-------------------------------")
        print("Cadastro realizado com sucesso!\n")
        print("Dados do Médico:\n")
        print(f"Nome: {self._nome}\nCPF: {self._CPF}\nContato: {self._contato}\nEspecialidade: {self._especialidade}\nCRM: {self._crm}")
        print("-------------------------------")

    def adicionar_consulta(self, consulta):
        self.agenda.append(consulta)
        print(f"Consulta adicionada na agenda do Dr(a). {self.nome}.")

    def ver_agenda(self):
        print(f"\n---- Agenda do Dr(a). {self.nome} ----")
        if not self.agenda:
            print("Nenhuma consulta agendada.")
        else:
            for i, consulta in enumerate(self.agenda, start=1):
                print(f"{i}. {consulta.data} | {consulta.hora} | Paciente: {consulta.paciente.nome} | Status: {consulta.status}")
        print("--------------------------------------")

    def cancelar_consulta(self, data, hora):
        for consulta in self.agenda:
            if consulta.data == data and consulta.hora == hora:
                consulta.cancelar_consulta()
                return
        print("Consulta não encontrada para essa data/hora.")