from modails.usuariobase import UsuarioBase
from abc import ABC, abstractmethod
import json
import os


class Paciente(UsuarioBase, ABC):
    contador = 0
    
    def __init__(self, nome_paciente, CPF, contato, endereco, data_nasc, senha, email, consulta="consultas.json"):
        super().__init__(CPF, contato, endereco, data_nasc, senha, email)
        Paciente.contador += 1
        self._id_paciente = Paciente.contador
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
    

    def Cadastrar(self):
        print("---- Cadastro Cliente ----")
        nome_paciente = input("Nome: ")
        CPF_paciente = int(input("CPF: "))
        senha_paciente = input("Senha: ")
        email_paciente = input("Email: ")
        contato_paciente = int(input("Contato: "))
        endereco_paciente = input("Endereço: ")
        data_nasc_paciente = int(input("Data de Nascimento: "))
        self._email = email_paciente
        self._senha = senha_paciente
        self._nome_paciente = nome_paciente
        self._CPF = CPF_paciente
        self._contato = contato_paciente
        self._endereco = endereco_paciente
        self._data_nasc = data_nasc_paciente
        print("-------------------------------")
        print("Cadastro realizado com sucesso!\n")
        print("Dados do Cliente:\n")
        print(f"ID: {self._id_paciente}\nNome: {self._nome_paciente}\nCPF: {self._CPF}\nContato: {self._contato}\nEndereço: {self._endereco}\nIdade: {self._data_nasc}\nEmail: {self._email}")
        print("-------------------------------")
    
    def Autenticar(self):
        print("---- Autenticação Cliente ----")
        email_paciente = input("Email: ")
        senha_paciente = input("Senha: ")
        if email_paciente == self._email and senha_paciente == self._senha:
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
        # procura por consulta em formato de dicionário (salvo em JSON)
        found = False
        for i, c in enumerate(self.consultas):
            if isinstance(c, dict):
                cid = c.get('id') or c.get('id_consulta') or c.get('idConsulta')
                if cid is not None and str(cid) == str(id_consulta):
                    self.consultas.pop(i)
                    self.salvar()
                    print(f"Consulta com ID {id_consulta} cancelada com sucesso.")
                    found = True
                    break
        if not found:
            print(f"Nenhuma consulta encontrada com o ID {id_consulta}.")
        
    def Reagendar_Consulta(self):
        print("---- Reagendar Consulta ----")
        id_consulta = input("Informe o ID da consulta a ser reagendada: ")
        found = False
        for c in self.consultas:
            if isinstance(c, dict):
                cid = c.get('id') or c.get('id_consulta') or c.get('idConsulta')
                if cid is not None and str(cid) == str(id_consulta):
                    nova_data = input("Nova Data (DD/MM/AAAA): ")
                    nova_hora = input("Nova Hora (HH:MM): ")
                    c['data'] = nova_data
                    c['hora'] = nova_hora
                    self.salvar()
                    print(f"Consulta com ID {id_consulta} reagendada para {nova_data} às {nova_hora}.")
                    found = True
                    break
        if not found:
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
    def _carregar_consultas(self):
        if os.path.exists(self._consulta):
            with open(self._consulta, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                    # armazena os dados brutos (dicionários). Para desserializar em objetos,
                    # implemente Consulta.from_dict e ajuste aqui para usar essa função.
                    self.consultas = dados
                except json.JSONDecodeError:
                    self.consultas = []