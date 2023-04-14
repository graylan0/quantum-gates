import numpy as np
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.quantum_info import Operator

# Define the I-Gate matrix
i_gate_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, np.exp(1j * np.pi / 3), 0],
    [0, 0, 0, np.exp(1j * np.pi / 3)]
], dtype=complex)

# Create a custom I-Gate
i_gate = Operator(i_gate_matrix)

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2)

# Add the I-Gate to the quantum circuit
qc.append(i_gate, [0, 1])

# Visualize the quantum circuit
print(qc)

# Execute the quantum circuit
backend = Aer.get_backend("statevector_simulator")
result = execute(qc, backend).result()
statevector = result.get_statevector(qc)

print("\nStatevector after applying the I-Gate:")
print(statevector)