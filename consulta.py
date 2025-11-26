from modails.paciente import Paciente
from modails.medico import Medico
import json
import os

class Consulta(Paciente, Medico):
    def __init__(self, id_consulta, data, hora, nome_paciente, nome_medico, consulta="consultas.json"):
        Paciente.__init__(self, nome_paciente)
        Medico.__init__(self, nome_medico)
        self._id_consulta = id_consulta
        self._data = data
        self._hora = hora
        self._status = "Pendente"
        self._consulta = consulta
        

    def Lista_Consultas(self):
        consultas = []
        consultas.append({
            "data": self._data,
            "hora": self._hora,
            "paciente": self._nome_paciente,
            "medico": self._nome_medico,
            "status": self._status
        })
        print("---- Lista de Consultas ----")
        print(f"Data: {self._data}")
        print(f"Hora: {self._hora}")
        print(f"Paciente: {self._nome_paciente}")
        print(f"Médico: {self._nome_medico}")
        print(f"Status: {self._status}")
        print("----------------------------")