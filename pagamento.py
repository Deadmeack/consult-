from consulta import Consulta

class Pagamento(Consulta):
    def __init__(self, id_consulta, id_pagamento, consulta, valor):
        Consulta.__init__(self, id_consulta)
        self._consulta = consulta
        self._valor = valor
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
        
    def realizar_pagamento(self):

        print("\n---- Realizar Pagamento ----")
        print(f"Valor a pagar: R$ {self._valor:.2f}")
        print("Escolha o método de pagamento:")
        print("1. Cartão de Crédito/Débito")
        print("2. Pix")
        print("3. Dinheiro")
        
        opcao = input("Opção: ")
        metodo = ""
        
        if opcao == 'Cardão':
            metodo = "Cartão de Crédito/Débito"
            input("Digite os dados do cartão... (Simulação)")
            self._status = "Pago"
        elif opcao == 'Pix':
            metodo = "Pix"
            print("Chave Pix: 1234567890001 (CPF/CNPJ)")
            input("Pressione Enter após o pagamento... (Simulação)")
            self._status = "Pago"
        elif opcao == 'Dinheiro':
            metodo = "Dinheiro"
            print("Pagamento em dinheiro será processado na clínica.")
            self._status = "Pago"
        else:
            print("❌ Opção de pagamento inválida.")
            self._status = "Não Pago"
            return

        # Simula o processamento do pagamento
        if self._status == "Pago":
            print(f"\n🎉 Pagamento de R$ {self._valor:.2f} realizado com sucesso via {metodo}!")
            print("Gerando recibo...")
            print(self._recibo.Gerar_Recibo())
        
        else:
            print("❌ Falha no pagamento. Tente novamente.")