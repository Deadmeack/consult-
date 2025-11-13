from recibo import Recibo
from abc import ABC, abstractmethod
from consulta import Consulta
from pagamento import Pagamento

class Pagamento(ABC):
    def __init__(self, id_consulta, id_pagamento, consulta, valor_consulta, status):
        super().__init__(id_consulta, id_pagamento)
        self._consulta = consulta
        self._valor = valor_consulta
        self._status = "Pendente"
        self._recibo = None
        self._id_consulta = id_consulta
        self._id_pagamento = id_pagamento
    


    @property
    def consulta(self):
        return self._consulta
    @property
    def valor(self):
        return self._valor
    @property
    def status(self):
        return self._status
    @property
    def recibo(self):
        return self._recibo
    @consulta.setter
    def consulta(self, consulta):
        self._consulta = consulta
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    @status.setter
    def status(self, status):
        self._status = status
    @recibo.setter
    def recibo(self, recibo):
        self._recibo = recibo
    @id_consulta.setter
    def id_consulta(self, id_consulta):
        self._id_consulta = id_consulta
        
    def realizar_pagamento(self):

        print("\n---- Realizar Pagamento ----")
        print(f"Valor a pagar: R$ {self.valor:.2f}")
        print("Escolha o método de pagamento:")
        print("1. Cartão de Crédito/Débito")
        print("2. Pix")
        print("3. Dinheiro")
        
        opcao = input("Opção: ")
        metodo = ""
        
        if opcao == '1':
            metodo = "Cartão de Crédito/Débito"
            input("Digite os dados do cartão... (Simulação)")
        elif opcao == '2':
            metodo = "Pix"
            print("Chave Pix: 1234567890001 (CPF/CNPJ)")
            input("Pressione Enter após o pagamento... (Simulação)")
        elif opcao == '3':
            metodo = "Dinheiro"
            print("Pagamento em dinheiro será processado na clínica.")
        else:
            print("❌ Opção de pagamento inválida.")
            return

        # Simula o processamento do pagamento
        if self.status == "Pago":
            print(f"\n🎉 Pagamento de R$ {self.valor:.2f} realizado com sucesso via {metodo}!")
        
    @abstractmethod
    def Gerar_Recibo(self):
        pass