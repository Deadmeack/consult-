from datetime import datetime
from abc import ABC, abstractmethod'

class Consulta:
    def __init__(self, data, hora, paciente, medico):
        self.data = data          
        self.hora = hora         
        self.paciente = paciente
        self.medico = medico
        self.status = "Pendente"  

    def confirmar_consulta(self):
        if self.status != "Cancelada":
            self.status = "Confirmada"
            print(f"Consulta de {self.paciente} com Dr(a). {self.medico} confirmada.")
        else:
            print("Não é possível confirmar uma consulta cancelada.")

    def cancelar_consulta(self):
        self.status = "Cancelada"
        print(f"Consulta de {self.paciente} foi cancelada.")

    def reagendar_consulta(self, nova_data, nova_hora):
        if self.status != "Cancelada":
            self.data = nova_data
            self.hora = nova_hora
            self.status = "Pendente"
            print(f"Consulta reagendada para {self.data} às {self.hora}.")
        else:
            print("Não é possível reagendar uma consulta cancelada.")

    def gerar_relatorio(self):
        return {
            "Paciente": self.paciente,
            "Médico": self.medico,
            "Data": self.data,
            "Hora": self.hora,
            "Status": self.status
        }

