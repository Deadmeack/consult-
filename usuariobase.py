from abc import ABC, abstractmethod

class UsuarioBase(ABC):
    def __init__(self, id, nome, CPF, contato, endereco, data_nasc, senha, email):
        super().__init__(CPF, contato)
        self._id= id
        self._nome = nome
        self._endereco = endereco
        self._data_nasc = data_nasc
        self._senha = senha
        self._email = email
        self._CPF = CPF
        self._contato = contato
        

    
    @property
    def CPF(self):
        return self._CPF
    @CPF.setter
    def CPF(self, CPF):
        self._CPF = CPF
    @property
    def contato(self):
        return self._contato
    @contato.setter
    def contato(self, contato):
        self._contato = contato

    @abstractmethod
    def Cadastrar(self):
        pass

    @abstractmethod
    def Autenticar(self):
        pass

    @abstractmethod
    def Agendar_Consulta(self):
        pass
    @abstractmethod
    def Ver_Agenda(self):
        pass
    @abstractmethod
    def Cancelar_Consulta(self):
        pass
    @abstractmethod
    def Listar_Consultas(self):
        pass
    @abstractmethod
    def Reagendar_Consulta(self):
        pass

   
    