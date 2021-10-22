#!/usr/bin/python3



import qiskit as qk
from qiskit.circuit.library import *
from qiskit import QuantumCircuit, execute
from qiskit.algorithms import AmplificationProblem
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.circuit import QuantumRegister
from qiskit.circuit import ClassicalRegister
from qiskit.algorithms import Grover
from qiskit.circuit.library import PhaseOracle



#Create register
qIndexRegister   = QuantumRegister(5, 'bit_indexe')
qValueRegister   = QuantumRegister(4, 'bit_side')
qIndexMeasure    = ClassicalRegister(5, 'indexMeasure')
qValueMeasure    = ClassicalRegister(4, 'valueMeasure')

#Simulator
backend = Aer.get_backend('qasm_simulator')

#Displayer
from operator import itemgetter
from collections import defaultdict

def display(values):
    values = sorted(values.items(), key=lambda x: x[1], reverse=True)
    for v in values:
        print(v[0]+" :", v[1])



qData = {
    '00':'0010', # 0 => 2
    '01':'1101', # 1 => 13
    '10':'0001', # 2 => 1
    '11':'0110', # 3 => 6
}

def circuit():

    #Create circuit and add different register
    circuit = QuantumCircuit()
    circuit.add_register(qIndexRegister)
    circuit.add_register(qValueRegister)
    circuit.add_register(qIndexMeasure)
    circuit.add_register(qValueMeasure)

    #Hadamart on index register
    circuit.h([0,1,2,3,4])

    #load data
    gate = XGate()

    gate0 = gate.control(5, ctrl_state='00000')
    circuit.append(gate0, [0,1,2,3,4, 5])

    gate1 = gate.control(5, ctrl_state='00001')
    circuit.append(gate1, [0,1,2,3,4, 6])

    gate2 = gate.control(5, ctrl_state='00011')
    circuit.append(gate2, [0,1,2,3,4, 7])

    gate3 = gate.control(5, ctrl_state='00100')
    circuit.append(gate3, [0,1,2,3,4, 8])

    gate3 = gate.control(5, ctrl_state='00101')
    circuit.append(gate3, [0,1,2,3,4, 8])
    gate3 = gate.control(5, ctrl_state='00101')
    circuit.append(gate3, [0,1,2,3,4, 5])

    #Grover oracle
    #We are looking for value 0010 (on index 0001)
    oracle = PhaseOracle('~a & b & ~c & ~d')
    backend = Aer.get_backend('qasm_simulator')
    quantum_instance = QuantumInstance(backend)

    problem = AmplificationProblem(oracle=oracle, is_good_state=oracle.evaluate_bitstring)
    grover = Grover(quantum_instance=quantum_instance, iterations=3)
    grover.amplify(problem)
    circuit.append(
        grover.construct_circuit(problem),
        [5,6,7,8]                          #values lines
    )
    grover.amplify(problem)

    return circuit



'''
OUTPUT 1 :
                ┌───┐                                                 ┌─┐                        
  bit_indexe_0: ┤ H ├──o────■────■────o────■────■─────────────────────┤M├────────────────────────
                ├───┤  │    │    │    │    │    │                     └╥┘┌─┐                     
  bit_indexe_1: ┤ H ├──o────o────■────o────o────o──────────────────────╫─┤M├─────────────────────
                ├───┤  │    │    │    │    │    │                      ║ └╥┘┌─┐                  
  bit_indexe_2: ┤ H ├──o────o────o────■────■────■──────────────────────╫──╫─┤M├──────────────────
                ├───┤  │    │    │    │    │    │                      ║  ║ └╥┘┌─┐               
  bit_indexe_3: ┤ H ├──o────o────o────o────o────o──────────────────────╫──╫──╫─┤M├───────────────
                ├───┤  │    │    │    │    │    │                      ║  ║  ║ └╥┘┌─┐            
  bit_indexe_4: ┤ H ├──o────o────o────o────o────o──────────────────────╫──╫──╫──╫─┤M├────────────
                └───┘┌─┴─┐  │    │    │    │  ┌─┴─┐┌─────────────────┐ ║  ║  ║  ║ └╥┘┌─┐         
    bit_side_0: ─────┤ X ├──┼────┼────┼────┼──┤ X ├┤0                ├─╫──╫──╫──╫──╫─┤M├─────────
                     └───┘┌─┴─┐  │    │    │  └───┘│                 │ ║  ║  ║  ║  ║ └╥┘┌─┐      
    bit_side_1: ──────────┤ X ├──┼────┼────┼───────┤1                ├─╫──╫──╫──╫──╫──╫─┤M├──────
                          └───┘┌─┴─┐  │    │       │  Grover circuit │ ║  ║  ║  ║  ║  ║ └╥┘┌─┐   
    bit_side_2: ───────────────┤ X ├──┼────┼───────┤2                ├─╫──╫──╫──╫──╫──╫──╫─┤M├───
                               └───┘┌─┴─┐┌─┴─┐     │                 │ ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐
    bit_side_3: ────────────────────┤ X ├┤ X ├─────┤3                ├─╫──╫──╫──╫──╫──╫──╫──╫─┤M├
                                    └───┘└───┘     └─────────────────┘ ║  ║  ║  ║  ║  ║  ║  ║ └╥┘
indexMeasure: 5/═══════════════════════════════════════════════════════╩══╩══╩══╩══╩══╬══╬══╬══╬═
                                                                       0  1  2  3  4  ║  ║  ║  ║ 
valueMeasure: 4/══════════════════════════════════════════════════════════════════════╩══╩══╩══╩═
                                                                                      0  1  2  3 
'''



#Measure index prob
from qiskit.tools.visualization import plot_histogram
indexCircuit = circuit()

#index measures
indexCircuit.measure(qIndexRegister[0], qIndexMeasure[0])
indexCircuit.measure(qIndexRegister[1], qIndexMeasure[1])
indexCircuit.measure(qIndexRegister[2], qIndexMeasure[2])
indexCircuit.measure(qIndexRegister[3], qIndexMeasure[3])
indexCircuit.measure(qIndexRegister[4], qIndexMeasure[4])

#values measures
indexCircuit.measure(qValueRegister[0], qValueMeasure[0])
indexCircuit.measure(qValueRegister[1], qValueMeasure[1])
indexCircuit.measure(qValueRegister[2], qValueMeasure[2])
indexCircuit.measure(qValueRegister[3], qValueMeasure[3])

job = qk.execute(indexCircuit, backend, shots=8000).result().get_counts(indexCircuit)
#print(indexCircuit.decompose())
print(indexCircuit)
display(job)
