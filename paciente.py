from usuariobase import UsuarioBase
from abc import ABC, abstractmethod
import json
import os


class Paciente(UsuarioBase, ABC):
    def __init__(self, id_paciente, nome_paciente, CPF, contato, endereco, data_nasc, senha, email, consulta="consultas.json"):
        super().__init__(CPF, contato, endereco, data_nasc, senha, email)
        self._id_paciente = id_paciente
        self._nome_paciente = nome_paciente
        self._consulta = consulta
        self.consultas = []
        self._carregar_consultas()
        

    @property
    def nome_paciente(self):
        return self._nome_paciente
    @nome_paciente.setter
    def nome_paciente(self, nome_paciente):
        self._nome_paciente = nome_paciente

    @property
    def id_paciente(self):
        return self._id_paciente
    @id_paciente.setter
    def id_paciente(self, id_paciente):
        self._id_paciente = id_paciente
    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha

    def Cadastrar(self):
        print("---- Cadastro Cliente ----")
        nome_paciente = input("Nome: ")
        CPF_paciente = input("CPF: ")
        contato_paciente = input("Contato: ")
        endereco_paciente = input("Endereço: ")
        data_nasc_paciente = input("Idade: ")
        self._nome_paciente = nome_paciente
        self._CPF = CPF_paciente
        self._contato = contato_paciente
        self._endereco = endereco_paciente
        self._data_nasc = data_nasc_paciente
        print("-------------------------------")
        print("Cadastro realizado com sucesso!\n")
        print("Dados do Cliente:\n")
        print(f"Nome: {self._nome_paciente}\nCPF: {self._CPF}\nContato: {self._contato}\nEndereço: {self._endereco}\nIdade: {self._idade}")
        print("-------------------------------")
    
    def Autenticar(self):
        print("---- Autenticação Cliente ----")
        nome = input("Nome: ")
        CPF = input("CPF: ")
        if nome == self._nome_paciente and CPF == self._CPF:
            print("Autenticação bem-sucedida!")
            return True
        else:
            print("Falha na autenticação. Nome ou CPF incorretos.")
            return False


    def Agendar_Consulta(self):
        print("---- Agendar Consulta ----")
        print("Informe os dados da consulta:")
        data = input("Data (DD/MM/AAAA): ")
        hora = input("Hora (HH:MM): ")
        print(f"Consulta agendada para {data} às {hora}.\n")

    def Cancelar_Consulta(self):
        print("---- Cancelar Consulta ----")
        id_consulta = input("Informe o ID da consulta a ser cancelada: ")
        if id_consulta == self._id_consulta:
            print(f"Consulta com ID {id_consulta} cancelada com sucesso.")
        else:
            print(f"Nenhuma consulta encontrada com o ID {id_consulta}.")
        
    def Reagendar_Consulta(self):
        print("---- Reagendar Consulta ----")
        id_consulta = input("Informe o ID da consulta a ser reagendada: ")
        if id_consulta == self._id_consulta:
            nova_data = input("Nova Data (DD/MM/AAAA): ")
            nova_hora = input("Nova Hora (HH:MM): ")
            self._data = nova_data
            self._hora = nova_hora
            print(f"Consulta com ID {id_consulta} reagendada para {nova_data} às {nova_hora}.")
        else:
            print(f"Nenhuma consulta encontrada com o ID {id_consulta}.")
    
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
        with open(self._consulta, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar(self):
        if os.path.exists(self._consulta):
            with open(self._consulta, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                    self.consultas = [consulta.from_dict(d) for d in dados]
                except json.JSONDecodeError:
                    self.consultas = []