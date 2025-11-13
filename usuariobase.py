from abc import ABC, abstractmethod

class UsuarioBase(ABC):
    def __init__(self, CPF, contato):
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

   
    