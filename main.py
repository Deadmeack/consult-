from modails.paciente import Paciente
from modails.medico import Medico
from modails.pagamento import Pagamento
from modails.consulta import Consulta
from modails.recibo import Recibo

if __name__ == "__main__":
    # Exemplo de uso das classes
    paciente = Paciente(
        "João Silva",
        12345678900,
        11999999999,
        "Rua A, 123",
        "01/01/1990",
        "senha123",
        "joao@example.com",
    )
    # Teste não interativo: exibe os dados criados
    print("Paciente criado:")
    print(f"ID: {paciente.id_paciente}")
    print(f"Nome: {paciente.nome_paciente}")
    print(f"Email: {paciente._email}")

    medico = Medico(
        "Dr. Carlos",
        98765432100,
        11988887777,
        "senhaMed",
        12345,
        "Cardiologia",
    )
    print("\nMédico criado:")
    print(f"ID: {medico.id_medico}")
    print(f"Nome: {medico.nome_medico}")

    # Gerar recibo de exemplo
    recibo = Recibo(id_pagamento=1, id_consulta=1, valor=150.0, metodo="Pix", paciente={'nome': paciente.nome_paciente}, medico={'nome': medico.nome_medico})
    print("\nRecibo de exemplo:")
    print(recibo.Gerar_Recibo())