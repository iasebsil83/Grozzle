#!/usr/bin/python3



# ---------------- CLASS ----------------
class Qomputer:

	#initialization
	def __init__(self, qbit_nbr, measure_nbr, shots):
		self.simulator = q.Aer.get_backend('qasm_simulator')
		self.circuit   = q.QuantumCircuit(qbit_nbr, measure_nbr)
		self.shots     = shots

	#console display
	def showCircuit(self):
		print( circuit.draw(output='text') )

	#execution
	def getResults(self):
		return q.execute(
			self.circuit,
			self.simulator,
			shots=self.shots
		).result().get_counts(
			self.circuit
		)
