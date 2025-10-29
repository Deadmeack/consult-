from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, CPF, contato, endereco, idade):
        super().__init__(nome, CPF, contato)
        self._endereco = endereco
        self._idade = idade

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
    

    def agendar_consulta(self):
        print("---- Agendar Consulta ----")
        print("Informe os dados da consulta:")
        data = input("Data (DD/MM/AAAA): ")
        hora = input("Hora (HH:MM): ")