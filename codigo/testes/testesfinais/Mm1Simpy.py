# -----------------------------------------------------------------------------
# Código gerado com o ASDA - Ambiente de Simulação Distribuída Automático
# -----------------------------------------------------------------------------

import random
import simpy
import sys

contaChegada = 0
contaTerminos = 0
tempoServico = [0]*1
tempoResposta = [0]*1

# função que armazena as distribuições utilizadas no modelo
def distributions(tipo):
	return {
		'chegadas': random.expovariate(1.0/1.5), 
		'cpu': random.expovariate(1.0/0.9), 
	}.get(tipo, 0.0)

# função de chegada de clientes de acordo com os lugares que os clientes chegam
def chegadaClientes(env, recursos):
	global contaChegada
	while True:
		contaChegada+=1
		yield env.timeout(distributions('chegadas'))	

		env.process(processoCPU(env, recursos))


# funções que realizam o processamento dos demais nodes

def processoCPU(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(cpu)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('cpu'))
	
	tempoServicoParcial = env.now - inicio

	tempoServico[0] = tempoServico[0] + tempoServicoParcial

	tempoResposta[0] = tempoResposta[0] + tempoFila + tempoServicoParcial

	recursos[recursos.index(cpu)].release(req)

	contaTerminos+=1

# define a semente ultizada para a geração aleatoria de numeros

random.seed(2)

# cria o ambiente de simulação
env = simpy.Environment()

# cria todos os recursos = facility
cpu = simpy.Resource(env, capacity = 1)

recursos = [
	cpu,
]

# iniciar os processos de chegada 
env.process(chegadaClientes(env, recursos))

# define o tempo total de execução da simulação
env.run(until=600)

# gera os relatorios finais
print('Total de Clientes processados = ', contaTerminos)
print('Throughput = ', contaTerminos/600)

print('Tempo de Serviço CPU = ', tempoServico[0])
print('Tempo Médio de Serviço CPU = ', tempoServico[0]/contaTerminos)
print('Utilização CPU = ', tempoServico[0]/600)
print('Tempo de resposta CPU = ', tempoResposta[0])
print('Tempo Médio de resposta CPU = ', tempoResposta[0]/contaTerminos)
print('Tempo Médio em Fila CPU = ',(tempoResposta[0]/contaTerminos)-(tempoServico[0]/contaTerminos))
print('----------------------------------------------------')

