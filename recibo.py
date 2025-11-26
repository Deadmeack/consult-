from abc import ABC, abstractmethod
from pagamento import Pagamento
from consulta import Consulta

class Recibo(Pagamento, Consulta):
    def __init__(self, id_pagamento, id_consulta, valor, metodo, data_emissao):
        Pagamento.__init__(self, id_pagamento, None, valor, metodo)
        Consulta.__init__(self, id_consulta, None, None, None, None)
        self._data_emissao = data_emissao
        self._valor = valor
        self._metodo = metodo
 
    @property
    def data_emissao(self):
        return self._data_emissao
    @property
    def valor(self):
        return self._valor
    @property
    def metodo(self):
        return self._metodo
   
    @data_emissao.setter
    def data_emissao(self, data_emissao):
        self._data_emissao = data_emissao
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    @metodo.setter
    def metodo(self, metodo):
        self._metodo = metodo

    def Gerar_Recibo(self):
        # Retorna uma string formatada com os detalhes do pagamento e da consulta
        return (
            "\n*** RECIBO DE PAGAMENTO ***"
            f"\nData de Emissão: {self.data_emissao}"
            f"\nID da Transação: {id(self.id_pagamento)}"
            f"\n-----------------------------"
            f"\nPaciente: {self.nome_paciente}"
            f"\nMédico: Dr(a). {self.nome_medico}"
            f"\nConsulta (Data/Hora): {self.pagamento.consulta.data} às {self.pagamento.consulta.hora}"
            f"\n-----------------------------"
            f"\nValor Pago: R$ {self.valor:.2f}"
            f"\nMétodo de Pagamento: {self.metodo}"
            "\n*****************************\n"
        )