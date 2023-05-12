# -----------------------------------------------------------------------------
# Código gerado com o ASDA - Ambiente de Simulação Distribuída Automático
# -----------------------------------------------------------------------------

import random
import simpy
import sys

contaChegada = 0
contaTerminos = 0
tempoServico = 0
tempoResposta = 0

# função que armazena as distribuições utilizadas no modelo
def distributions(tipo):
	return {
		'chegadas': random.expovariate(1.0/50.0), 
		'cpu': random.expovariate(1.0/91.7), 
	}.get(tipo, 0.0)

# função de chegada de clientes de acordo com os lugares que os clientes chegam
def chegadaClientes(env, recursos):
	global contaChegada
	i = 0
#	while i<6:
	while True:
		contaChegada+=1
		
		yield env.timeout(distributions('chegadas'))	
#		print('Chegada do cliente %d = %.1f' % (contaChegada, env.now))

		env.process(processoCPU(env, 'cliente %d' % contaChegada, recursos))
		i+=1


# funções que realizam o processamento dos demais nodes

def processoCPU(env, nome, recursos):
	global contaTerminos, tempoServico, tempoResposta
	chegada = env.now 
	req = recursos[recursos.index(cpu)].request()
	yield req

	tempoFila = env.now - chegada 
	comeco = env.now             
#	print('%.1f Servidor inicia o atendimento do %s. Tempo em fila: %.1f' 
	#	% (env.now, nome, tempoFila))

	yield env.timeout(distributions('cpu'))

	fim = env.now - comeco
#	print('%.1f Servidor termina o atendimento do %s. Clientes em fila: %i' 
  #          % (env.now, nome, len(cpu.queue)))
	
	tempoServico = tempoServico + fim
#	print('TEMPO DE SERVIÇO = %.1f' % (tempoServico))
	tempoResposta = tempoResposta + tempoFila + tempoServico
	
	recursos[recursos.index(cpu)].release(req)
	contaTerminos+=1


# define a semente ultizada para a geração aleatoria de numeros
random.seed(1)
#print(int(sys.argv[1]))

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

print(' %d %.3f %.3f %.3f %.3f %.3f %.3f %.3f %.3f %.3f' %(contaTerminos, contaTerminos/600, tempoServico, tempoServico/contaTerminos, 
	+ tempoServico/600, tempoResposta, tempoResposta/contaTerminos,(tempoResposta/contaTerminos)-(tempoServico/contaTerminos),
	+ tempoResposta/600, (tempoResposta/600)-(tempoServico/600)))

#print('Total de Clientes processados = ', contaTerminos)
#print('Throughput = ', contaTerminos/600)
#print('Tempo de Serviço = ', tempoServico)
#print('Tempo Médio de Serviço = ', tempoServico/contaTerminos)
#print('Utilização = ',tempoServico/600)
#print('Tempo de resposta = ', tempoResposta)
#print('Tempo Médio de resposta = ', tempoResposta/contaTerminos)
#print('Tempo Médio em Fila = ',(tempoResposta/contaTerminos)-(tempoServico/contaTerminos))
#print('Numero Médio no Sistema = ',tempoResposta/600)
#print('Numero médio na fila = ', (tempoResposta/600)-(tempoServico/600))
# gera os relatorios finais
#saida = open("mm1.txt","w+")

#saida.close()
