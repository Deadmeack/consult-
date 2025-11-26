from usuariobase import UsuarioBase
from abc import ABC, abstractmethod
import json
import os


class Medico(UsuarioBase, ABC):
    def __init__(self, id_medico, nome_medico, CPF, contato, endereco, data_nasc, senha, email, CRM, especialidade, consulta="consultas.json"):
        super().__init__(CPF, contato, endereco, data_nasc, senha, email)
        self._id_medico = id_medico
        self._nome_medico = nome_medico
        self._consulta = consulta
        self._CRM = CRM
        self._especialidade = especialidade
        self.consultas = []
        self._carregar_consultas()

    @property
    def nome_medico(self):
        return self._nome_medico
    @nome_medico.setter
    def nome_medico(self, nome_medico):
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
        nome_medico = input("Nome: ")
        CPF_medico = input("CPF: ")
        contato_medico = input("Contato: ")
        especialidade = input("Especialidade: ")
        CRM = input("CRM: ")
        self._nome_medico = nome_medico
        self._CPF = CPF_medico
        self._contato = contato_medico
        self._especialidade = especialidade
        self._CRM = CRM
        print("-------------------------------")
        print("Cadastro realizado com sucesso!\n")
        print("Dados do Médico:\n")
        print(f"Nome: {self._nome_medico}\nCPF: {self._CPF}\nContato: {self._contato}\nEspecialidade: {self._especialidade}\nCRM: {self._CRM}")
        print("-------------------------------")
    
    def Autenticar(self):
        print("---- Autenticação Médico ----")
        nome_medico = input("Nome: ")
        CRM = input("CRM: ")
        if nome_medico == self._nome_medico and CRM == self._CRM:
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

    
    def atualizar(self, indice, **kwargs):
        try:
            self.consultas[indice].atualizar(**kwargs)
            self.salvar()
        except IndexError:
            print("Produto não encontrado.")

    def deletar(self, indice):
        try:
            self.consultas.pop(indice)
            self.salvar()
        except IndexError:
            print("Produto não encontrado.")

    def salvar(self):
        dados = [p.to_dict() for p in self.consultas]
        with open(self.consulta, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar(self):
        if os.path.exists(self._consulta):
            with open(self.consulta, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                    self.consultas = [consulta.from_dict(d) for d in dados]
                except json.JSONDecodeError:
                    self.consultas = []
