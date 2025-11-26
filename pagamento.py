from modails.consulta import Consulta
from modails.recibo import Recibo
import uuid
from datetime import datetime

class Pagamento(Consulta):
    def __init__(self, id_consulta, id_pagamento, consulta, valor, status="Pendente", metodo=None):
        Consulta.__init__(self, id_consulta, status)
        self._consulta = consulta
        self._valor = valor
        self._metodo = metodo
        self._id_pagamento = id_pagamento

    @property
    def consulta(self):
        return self._consulta
    @property
    def valor(self):
        return self._valor
    @consulta.setter
    def consulta(self, consulta):
        self._consulta = consulta
    @valor.setter
    def valor(self, valor):
        self._valor = valor
        
    def realizar_pagamento(self):

        print("\n---- Realizar Pagamento ----")
        print(f"Valor a pagar: R$ {self._valor:.2f}")
        print("Escolha o método de pagamento:")
        print("1. Cartão de Crédito/Débito")
        print("2. Pix")
        print("3. Dinheiro")
        
        opcao = input("Opção: ")
        
        if opcao == 'Cartão':
            input("Digite os dados do cartão... (Simulação)")
            self._metodo = "Cartão de Crédito/Débito"
            self._status = "Pago"
        elif opcao == 'Pix':
            # gera chave PIX aleatória
            chave_pix = str(uuid.uuid4())
            print(f"Chave Pix gerada: {chave_pix}")
            input("Pressione Enter após o pagamento... (Simulação)")
            self._metodo = "Pix"
            self._status = "Pago"
        elif opcao == 'Dinheiro':
            print("Pagamento em dinheiro será processado na clínica.")
            self._metodo = "Dinheiro"
            self._status = "Pago"
        else:
            print("❌ Opção de pagamento inválida.")
            self._metodo = "N/A"
            self._status = "Não Pago"
            return

        # Simula o processamento do pagamento
        if self._status == "Pago":
            print(f"\n🎉 Pagamento de R$ {self._valor:.2f} realizado com sucesso via {self._metodo}!")
            print("Gerando recibo...")
            paciente = None
            medico = None
            # tenta extrair paciente/medico se a consulta for um dicionário
            if isinstance(self._consulta, dict):
                paciente = self._consulta.get('paciente') or self._consulta.get('nome_paciente')
                medico = self._consulta.get('medico') or self._consulta.get('nome_medico')

            # instancia Recibo; Recibo gera id_recibo e data_emissao internamente
            recibo = Recibo(id_pagamento=self._id_pagamento,
                            id_consulta=getattr(self, '_id_consulta', None),
                            valor=self._valor,
                            metodo=self._metodo,
                            paciente=paciente,
                            medico=medico)
            # Gerar_Recibo() agora é responsável por formatar/retornar o recibo
            print(recibo.Gerar_Recibo())
        
        else:
            print("❌ Falha no pagamento. Tente novamente.")