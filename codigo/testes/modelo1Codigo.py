# -----------------------------------------------------------------------------
# Código gerado com o ASDA - Ambiente de Simulação Distribuída Automático
# -----------------------------------------------------------------------------

import random
import simpy

contaChegada = 0
contaTerminos = 0
tempoServico = 0
tempoResposta = 0

# função que armazena as distribuições utilizadas no modelo
def distributions(tipo):
	return {
		'chegadas': random.expovariate(1.0/2.0), 
		'front': random.expovariate(1.0/1.0), 
		'cpu': 5, 
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
	comeco = env.now  

	yield env.timeout(distributions('front'))

	fim = env.now - comeco
	tempoServico = tempoServico + fim
	tempoResposta = tempoResposta + tempoFila + tempoServico
	
	recursos[recursos.index(front)].release(req)
	contaTerminos+=1
	
	env.process(processoCPU(env, recursos))

def processoCPU(env, recursos):

	req = recursos[recursos.index(cpu)].request()
	yield req
	yield env.timeout(distributions('cpu'))
	recursos[recursos.index(cpu)].release(req)


# define a semente ultizada para a geração aleatoria de numeros
random.seed(10)

# cria o ambiente de simulação
env = simpy.Environment()

# cria todos os recursos = facility
front = simpy.Resource(env, capacity = 1)
cpu = simpy.Resource(env, capacity = 1)

recursos = [
	front,
	cpu,
]

# iniciar os processos de chegada 
env.process(chegadaClientes(env, recursos))

# define o tempo total de execução da simulação
env.run(until=60)

# gera os relatorios finais
saida = open("modelo1.txt","w+")

print('Total de Clientes processados = ', contaTerminos)
print('Throughput = ', contaTerminos/600)
print('Tempo de Serviço = ', tempoServico)
print('Tempo Médio de Serviço = ', tempoServico/contaTerminos)
print('Utilização = ',tempoServico/600)
print('Tempo de resposta = ', tempoResposta)
print('Tempo Médio de resposta = ', tempoResposta/contaTerminos)
print('Tempo Médio em Fila = ',(tempoResposta/contaTerminos)-(tempoServico/contaTerminos))
print('Numero Médio no Sistema = ',tempoResposta/600)
print('Numero médio na fila = ', (tempoResposta/600)-(tempoServico/600))

saida.close()
