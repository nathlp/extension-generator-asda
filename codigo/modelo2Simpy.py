# -----------------------------------------------------------------------------
# Código gerado com o ASDA - Ambiente de Simulação Distribuída Automático
# -----------------------------------------------------------------------------

import random
import simpy

contaChegada = 0
contaTerminos = 0
tempoServico = [0]*9
tempoResposta = [0]*9

# função que armazena as distribuições utilizadas no modelo
def distributions(tipo):
	return {
		'chegadas': random.expovariate(1.0/1), 
		'front': random.expovariate(1.0/0.1), 
		'cpu1': random.expovariate(1.0/0.325), 
		'cpu2': random.expovariate(1.0/0.325), 
		'cpu3': random.expovariate(1.0/0.325), 
		'cpu4': random.expovariate(1.0/0.325), 
		'disco1': random.expovariate(1.0/3.250), 
		'disco2': random.expovariate(1.0/3.250), 
		'disco3': random.expovariate(1.0/3.250), 
		'disco4': random.expovariate(1.0/3.250), 
	}.get(tipo, 0.0)

# função de chegada de clientes de acordo com os lugares que os clientes chegam
def chegadaClientes(env, recursos):
	global contaChegada
	while True:
		contaChegada+=1
		yield env.timeout(distributions('chegadas'))	

		env.process(processoFront(env, recursos))


# funções que realizam o processamento dos demais nodes

def processoFront(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(front)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('front'))
	tempoServico[0] = tempoServico[0] + (env.now - inicio)
	tempoResposta[0] = tempoResposta[0] + tempoFila + tempoServico[0]

	recursos[recursos.index(front)].release(req)

	x = random.randint(1,10000)

	if 0 < x and x < 2501:
		env.process(processoCPU1(env, recursos))

	if 2500 < x and x < 5001:
		env.process(processoCPU2(env, recursos))

	if 5000 < x and x < 7501:
		env.process(processoCPU3(env, recursos))

	if 7500 < x and x < 10001:
		env.process(processoCPU4(env, recursos))


def processoCPU1(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(cpu1)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('cpu1'))
	tempoServico[1] = tempoServico[1] + (env.now - inicio)
	tempoResposta[1] = tempoResposta[1] + tempoFila + tempoServico[1]

	recursos[recursos.index(cpu1)].release(req)

	env.process(processoDISCO1(env, recursos))


def processoCPU2(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(cpu2)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('cpu2'))
	tempoServico[2] = tempoServico[2] + (env.now - inicio)
	tempoResposta[2] = tempoResposta[2] + tempoFila + tempoServico[2]

	recursos[recursos.index(cpu2)].release(req)

	env.process(processoDISCO2(env, recursos))


def processoCPU3(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(cpu3)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('cpu3'))
	tempoServico[3] = tempoServico[3] + (env.now - inicio)
	tempoResposta[3] = tempoResposta[3] + tempoFila + tempoServico[3]

	recursos[recursos.index(cpu3)].release(req)

	env.process(processoDISCO3(env, recursos))


def processoCPU4(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(cpu4)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('cpu4'))
	tempoServico[4] = tempoServico[4] + (env.now - inicio)
	tempoResposta[4] = tempoResposta[4] + tempoFila + tempoServico[4]

	recursos[recursos.index(cpu4)].release(req)

	env.process(processoDISCO4(env, recursos))


def processoDISCO1(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(disco1)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('disco1'))
	tempoServico[5] = tempoServico[5] + (env.now - inicio)
	tempoResposta[5] = tempoResposta[5] + tempoFila + tempoServico[5]

	recursos[recursos.index(disco1)].release(req)

	contaTerminos+=1

def processoDISCO2(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(disco2)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('disco2'))
	tempoServico[6] = tempoServico[6] + (env.now - inicio)
	tempoResposta[6] = tempoResposta[6] + tempoFila + tempoServico[6]

	recursos[recursos.index(disco2)].release(req)

	contaTerminos+=1

def processoDISCO3(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(disco3)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('disco3'))
	tempoServico[7] = tempoServico[7] + (env.now - inicio)
	tempoResposta[7] = tempoResposta[7] + tempoFila + tempoServico[7]

	recursos[recursos.index(disco3)].release(req)

	contaTerminos+=1

def processoDISCO4(env, recursos):

	global contaTerminos, tempoServico, tempoResposta

	chegada = env.now
	req = recursos[recursos.index(disco4)].request()
	yield req
	tempoFila = env.now - chegada

	inicio = env.now
	yield env.timeout(distributions('disco4'))
	tempoServico[8] = tempoServico[8] + (env.now - inicio)
	tempoResposta[8] = tempoResposta[8] + tempoFila + tempoServico[8]

	recursos[recursos.index(disco4)].release(req)

	contaTerminos+=1

# define a semente ultizada para a geração aleatoria de numeros
random.seed(10)

# cria o ambiente de simulação
env = simpy.Environment()

# cria todos os recursos = facility
front = simpy.Resource(env, capacity = 1)
cpu1 = simpy.Resource(env, capacity = 1)
cpu2 = simpy.Resource(env, capacity = 1)
cpu3 = simpy.Resource(env, capacity = 1)
cpu4 = simpy.Resource(env, capacity = 1)
disco1 = simpy.Resource(env, capacity = 1)
disco2 = simpy.Resource(env, capacity = 1)
disco3 = simpy.Resource(env, capacity = 1)
disco4 = simpy.Resource(env, capacity = 1)

recursos = [
	front,
	cpu1,
	cpu2,
	cpu3,
	cpu4,
	disco1,
	disco2,
	disco3,
	disco4,
]

# iniciar os processos de chegada 
env.process(chegadaClientes(env, recursos))

# define o tempo total de execução da simulação
env.run(until=600)

# gera os relatorios finais
print('Total de Clientes processados = ', contaTerminos)
print('Throughput = ', contaTerminos/600)

print('Tempo de Serviço Front = ', tempoServico[0])
print('Tempo Médio de Serviço Front = ', tempoServico[0]/contaTerminos)
print('Utilização Front = ', tempoServico[0]/600)
print('Tempo de resposta Front = ', tempoResposta[0])
print('Tempo Médio de resposta Front = ', tempoResposta[0]/contaTerminos)
print('Tempo Médio em Fila Front = ',(tempoResposta[0]/contaTerminos)-(tempoServico[0]/contaTerminos))
print('----------------------------------------------------')

print('Tempo de Serviço CPU1 = ', tempoServico[1])
print('Tempo Médio de Serviço CPU1 = ', tempoServico[1]/contaTerminos)
print('Utilização CPU1 = ', tempoServico[1]/600)
print('Tempo de resposta CPU1 = ', tempoResposta[1])
print('Tempo Médio de resposta CPU1 = ', tempoResposta[1]/contaTerminos)
print('Tempo Médio em Fila CPU1 = ',(tempoResposta[1]/contaTerminos)-(tempoServico[1]/contaTerminos))
print('----------------------------------------------------')

print('Tempo de Serviço CPU2 = ', tempoServico[2])
print('Tempo Médio de Serviço CPU2 = ', tempoServico[2]/contaTerminos)
print('Utilização CPU2 = ', tempoServico[2]/600)
print('Tempo de resposta CPU2 = ', tempoResposta[2])
print('Tempo Médio de resposta CPU2 = ', tempoResposta[2]/contaTerminos)
print('Tempo Médio em Fila CPU2 = ',(tempoResposta[2]/contaTerminos)-(tempoServico[2]/contaTerminos))
print('----------------------------------------------------')

print('Tempo de Serviço CPU3 = ', tempoServico[3])
print('Tempo Médio de Serviço CPU3 = ', tempoServico[3]/contaTerminos)
print('Utilização CPU3 = ', tempoServico[3]/600)
print('Tempo de resposta CPU3 = ', tempoResposta[3])
print('Tempo Médio de resposta CPU3 = ', tempoResposta[3]/contaTerminos)
print('Tempo Médio em Fila CPU3 = ',(tempoResposta[3]/contaTerminos)-(tempoServico[3]/contaTerminos))
print('----------------------------------------------------')

print('Tempo de Serviço CPU4 = ', tempoServico[4])
print('Tempo Médio de Serviço CPU4 = ', tempoServico[4]/contaTerminos)
print('Utilização CPU4 = ', tempoServico[4]/600)
print('Tempo de resposta CPU4 = ', tempoResposta[4])
print('Tempo Médio de resposta CPU4 = ', tempoResposta[4]/contaTerminos)
print('Tempo Médio em Fila CPU4 = ',(tempoResposta[4]/contaTerminos)-(tempoServico[4]/contaTerminos))
print('----------------------------------------------------')

print('Tempo de Serviço DISCO1 = ', tempoServico[5])
print('Tempo Médio de Serviço DISCO1 = ', tempoServico[5]/contaTerminos)
print('Utilização DISCO1 = ', tempoServico[5]/600)
print('Tempo de resposta DISCO1 = ', tempoResposta[5])
print('Tempo Médio de resposta DISCO1 = ', tempoResposta[5]/contaTerminos)
print('Tempo Médio em Fila DISCO1 = ',(tempoResposta[5]/contaTerminos)-(tempoServico[5]/contaTerminos))
print('----------------------------------------------------')

print('Tempo de Serviço DISCO2 = ', tempoServico[6])
print('Tempo Médio de Serviço DISCO2 = ', tempoServico[6]/contaTerminos)
print('Utilização DISCO2 = ', tempoServico[6]/600)
print('Tempo de resposta DISCO2 = ', tempoResposta[6])
print('Tempo Médio de resposta DISCO2 = ', tempoResposta[6]/contaTerminos)
print('Tempo Médio em Fila DISCO2 = ',(tempoResposta[6]/contaTerminos)-(tempoServico[6]/contaTerminos))
print('----------------------------------------------------')

print('Tempo de Serviço DISCO3 = ', tempoServico[7])
print('Tempo Médio de Serviço DISCO3 = ', tempoServico[7]/contaTerminos)
print('Utilização DISCO3 = ', tempoServico[7]/600)
print('Tempo de resposta DISCO3 = ', tempoResposta[7])
print('Tempo Médio de resposta DISCO3 = ', tempoResposta[7]/contaTerminos)
print('Tempo Médio em Fila DISCO3 = ',(tempoResposta[7]/contaTerminos)-(tempoServico[7]/contaTerminos))
print('----------------------------------------------------')

print('Tempo de Serviço DISCO4 = ', tempoServico[8])
print('Tempo Médio de Serviço DISCO4 = ', tempoServico[8]/contaTerminos)
print('Utilização DISCO4 = ', tempoServico[8]/600)
print('Tempo de resposta DISCO4 = ', tempoResposta[8])
print('Tempo Médio de resposta DISCO4 = ', tempoResposta[8]/contaTerminos)
print('Tempo Médio em Fila DISCO4 = ',(tempoResposta[8]/contaTerminos)-(tempoServico[8]/contaTerminos))
print('----------------------------------------------------')

