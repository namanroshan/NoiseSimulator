# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Pauli Z (phase-flip) gate.
"""
import numpy
from qiskit.circuit import CompositeGate
from qiskit.circuit import Gate
from qiskit.circuit import QuantumCircuit
from qiskit.circuit import QuantumRegister
from qiskit.qasm import pi
from qiskit.extensions.standard.u1 import U1Gate


class ZGate(Gate):
    """Pauli Z (phase-flip) gate."""

    def __init__(self, label=None):
        """Create new Z gate."""
        super().__init__("z", 1, [], label=label)

    def _define(self):
        definition = []
        q = QuantumRegister(1, "q")
        rule = [
            (U1Gate(pi), [q[0]], [])
        ]
        for inst in rule:
            definition.append(inst)
        self.definition = definition

    def inverse(self):
        """Invert this gate."""
        return ZGate()  # self-inverse

    def to_matrix(self):
        """Return a Numpy.array for the X gate."""
        return numpy.array([[1, 0],
                            [0, -1]], dtype=complex)


def z(self, q):
   # return self.append(ZGate(), [q], [])
    """
        Apply Z to qubit q in density matrix register self.
        Density matrix remains in the same register.
        Args:
            q (int): q is the qubit where the gate Z is applied.
    """

        # update density matrix
    self._densitymatrix = np.reshape(self._densitymatrix,(4**(q),4,4**(self._number_of_qubits-q-1)))
    for j in range(4**(self._number_of_qubits-q-1)):
        for i in range(4**(q)):
            self._densitymatrix[i,1,j] = -self._densitymatrix[i,1,j]
            self._densitymatrix[i,2,j] = -self._densitymatrix[i,2,j]

QuantumCircuit.z = z
CompositeGate.z = z
