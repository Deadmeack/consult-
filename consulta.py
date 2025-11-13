from abc import ABC, abstractmethod
from usuariobase import UsuarioBase
from paciente import Paciente
from medico import Medico

class Consulta(UsuarioBase, Paciente, Medico):
    def __init__(self, id_consulta, data, hora, paciente, medico):
        super().__init__(nome_paciente, nome_medico,)
        self._id_consulta = id_consulta
        self._data = data
        self._hora = hora
        self._status = "Pendente"

    def Lista_Consultas(self):
        consultas = []
        consultas.append({
            "data": self._data,
            "hora": self._hora,
            "paciente": self._paciente.nome,
            "medico": self._medico.nome,
            "status": self._status
        })
        print("---- Lista de Consultas ----")
        print(f"Data: {self._data}")
        print(f"Hora: {self._hora}")
        print(f"Paciente: {self._nome_paciente}")
        print(f"Médico: {self._nome_medico}")
        print(f"Status: {self._status}")
        print("----------------------------")