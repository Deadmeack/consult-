from datetime import datetime
import uuid


class Recibo:
    def __init__(self, id_recibo=None, id_pagamento=None, id_consulta=None, valor=None, metodo=None, data_emissao=None, paciente=None, medico=None):
        # gera id_recibo se não fornecido
        self._id_recibo = id_recibo or str(uuid.uuid4())
        self._id_pagamento = id_pagamento
        self._id_consulta = id_consulta
        self._valor = valor
        self._metodo = metodo
        # gera data_emissao se não fornecida
        self._data_emissao = data_emissao or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # paciente/medico podem ser strings, dicionários ou objetos; aceitamos ambos
        self.paciente = paciente
        self.medico = medico

    def Gerar_Recibo(self):
        paciente_nome = None
        medico_nome = None
        # tenta extrair nomes se objetos forem passados
        if isinstance(self.paciente, dict):
            paciente_nome = self.paciente.get('nome') or self.paciente.get('nome_paciente')
        elif self.paciente is not None:
            paciente_nome = getattr(self.paciente, 'nome', None) or getattr(self.paciente, 'nome_paciente', None)

        if isinstance(self.medico, dict):
            medico_nome = self.medico.get('nome') or self.medico.get('nome_medico')
        elif self.medico is not None:
            medico_nome = getattr(self.medico, 'nome', None) or getattr(self.medico, 'nome_medico', None)

        paciente_nome = paciente_nome or 'N/A'
        medico_nome = medico_nome or 'N/A'

        return (
            "\n*** RECIBO DE PAGAMENTO ***"
            f"\nData de Emissão: {self._data_emissao}"
            f"\nID Recibo: {self._id_recibo}"
            f"\nID Pagamento: {self._id_pagamento}"
            f"\nID Consulta: {self._id_consulta}"
            f"\n-----------------------------"
            f"\nPaciente: {paciente_nome}"
            f"\nMédico: {medico_nome}"
            f"\n-----------------------------"
            f"\nValor Pago: R$ {self._valor if self._valor is not None else 0:.2f}"
            f"\nMétodo de Pagamento: {self._metodo or 'N/A'}"
            "\n*****************************\n"
        )