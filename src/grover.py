#!/usr/bin/python3



# ---------------- IMPORTATION ----------------

#quantum lib
import qiskit as q






# ---------------- GROVER ----------------

#circuit
def getGroverCircuit(qbit_nbr):
	circuit = q.QuantumCircuit(qbit_nbr+1, qbit_nbr)

	#for each qbit
	for n in range(qbit_nbr):

		#set Hadamar gates
		circuit.h(n)

		#set grover gates
		#circuit.grover(n, last)

		#set measure
		circuit.measure(n,n)

	return circuit
