import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

class QuantumCard:
    """
    Representa una carta cuántica usando Qiskit.
    6 qubits: 2 para palo, 4 para valor.

    Nota importante:
    - Qiskit devuelve los bitstrings en orden clásico "reverso" respecto a q[0], q[1], ...
      Por eso invertimos el bitstring al medir para que:
        measured_state[0] corresponda a qr[0], etc.
    """

    PALOS = {
        '00': 'Oro',
        '01': 'Copa',
        '10': 'Espada',
        '11': 'Basto'
    }

    VALORES = {
        '0001': 1,
        '0010': 2,
        '0011': 3,
        '0100': 4,
        '0101': 5,
        '0110': 6,
        '0111': 7,
        '1000': 10,
        '1001': 11,
        '1010': 12
    }

    PALO_CODE = {
        'Oro': '00',
        'Copa': '01',
        'Espada': '10',
        'Basto': '11'
    }

    VALOR_CODE = {
        1: '0001', 2: '0010', 3: '0011', 4: '0100',
        5: '0101', 6: '0110', 7: '0111', 10: '1000',
        11: '1001', 12: '1010'
    }

    def __init__(self, palo: str, valor: int, card_id: int = 0):
        self.palo = palo
        self.valor = valor
        self.card_id = card_id
        self.simulator = AerSimulator()
        self.measured_state: str | None = None  # 6 bits (q0..q5)

    def to_dict(self):
        return {
            'palo': self.palo,
            'valor': self.valor,
            'card_id': self.card_id,
            'measured_state': self.measured_state,
            'repr': str(self)
        }
