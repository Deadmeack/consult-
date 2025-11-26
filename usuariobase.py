from abc import ABC, abstractmethod

class UsuarioBase(ABC):
    def __init__(self, CPF, contato, endereco, data_nasc, senha, email):
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
    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    @property
    def data_nasc(self):
        return self._data_nasc
    @data_nasc.setter
    def data_nasc(self, data_nasc):
        self._data_nasc = data_nasc
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha
    @property
    def email(self):
        return self._email

    @abstractmethod
    def Cadastrar(self):
        pass

    @abstractmethod
    def Autenticar(self):
        pass


   
    