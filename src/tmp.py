#!/usr/bin/python3

import qiskit as q
from qiskit.algorithms.amplitude_amplifiers import Grover, AmplificationProblem
from qiskit.circuit.library.phase_oracle import PhaseOracle
from qiskit.quantum_info import Statevector

#1) Make something
aer_simulator = q.Aer.get_backend('aer_simulator')

#2) Oracle expression
expression = '(~a & ~b & c & ~d & ~e & ~f & ~g & h)'
'''values= [
	0b10000001,
	0b00100010,
	0b00100000,
	0b00000001,
	0b00101000,
	0b00100010,
	0b10000100,
	0b00001000,
	0b10000000,
	0b01000001,
	0b00100001,
	0b01000001,
	0b00000010,
	0b01000010,
	0b00010010,
	0b00000010,
	0b01001000,
	0b00000000,
	0b01001000,
	0b00000010,
	0b00100010,
	0b00001000
]'''
gs      = ['00100001']
good_state = ['110', '101']
oracle = Statevector([0,0,0,0,0,1,1,0])
grover = Grover(oracle, good_state=good_state)
my_gate=grover.grover_operator.to_gate()
#oracle  = PhaseOracle(expression)
#problem = AmplificationProblem(
#	oracle,
#	is_good_state=gs
#)

#g  = Grover(
#	quantum_instance=aer_simulator
#)

#result = g.amplify(problem)
#print(result)
