from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome, CPF, contato):
        self._nome = nome
        self._CPF = CPF
        self._contato = contato

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
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
    def cadastrar(self):
        pass

   
    