# -----------------------------------------------------------------------------
# Código gerado com o ASDA - Ambiente de Simulação Distribuída Automático
# -----------------------------------------------------------------------------

library(simmer)

set.seed(10)

env <- simmer("Mm1")
env

# Configurar trajetória 

cliente <- trajectory("clientes' path", TRUE) %>%
	seize("cpu", 1) %>%
	timeout(function() rexp(1, 0.1)) %>%
	release("cpu", 1) %>%
	set_attribute("queue_cpu", function() get_queue_count(env, "cpu")) %>%
	seize("disco", 1) %>%
	timeout(function() rexp(1, 0.5)) %>%
	release("disco", 1) %>%
	set_attribute("queue_disco", function() get_queue_count(env, "disco")) 

# criando os recursos 

env %>%
	add_resource("cpu", 1) %>%
	add_resource("disco", 1) %>%
	add_generator("cliente", cliente, function() rexp(1, 1), mon=2)

# tempo total de execução
env %>% 
	run(40) %>%
 	now()
# dados da simulação

chegadas <- get_mon_arrivals(env, TRUE) 
recursos <- get_mon_resources(env)

#library("plyr")



sprintf("Total de Clientes Processados = %d", nrow(chegadas))
sprintf("Thoughput = %f", (nrow(chegadas)/40))
sprintf("Tempo de Serviço =  %f", sum(chegadas[4]))
sprintf("Tempo Médio de Serviço =  %f", sum(chegadas[4])/nrow(chegadas))
sprintf("Utilização CPU = %f", sum(chegadas[4])/40)
sprintf("Tempo de resposta = %f", sum(chegadas[3])-sum(chegadas[2]))
sprintf("Tempo Médio de resposta = %f", (sum(chegadas[3])-sum(chegadas[2]))/nrow(chegadas) )
sprintf("Tempo Médio em Fila = %f ", ((sum(chegadas[3])-sum(chegadas[2]))/nrow(chegadas))-(sum(chegadas[4])/nrow(chegadas)))



  
