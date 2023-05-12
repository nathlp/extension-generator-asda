# -----------------------------------------------------------------------------
# Código gerado com o ASDA - Ambiente de Simulação Distribuída Automático
# -----------------------------------------------------------------------------

library(simmer)

set.seed(10)

env <- simmer("modelo1")
env

# Configurar trajetória 

cliente <- trajectory() %>%
	seize("Front", 1) %>%
	timeout(function() rexp(1, 1.0)) %>%
	release("Front", 1) %>%
	seize("CPU", 1) %>%
	timeout(function() rexp(1, 5.0)) %>%
	release("CPU", 1)

# criando os recursos 

env %>%
add_resource("front", 1) %>%
add_resource("cpu", 1) %>%
add_generator("cliente", cliente, function() rexp(1, 2.0))

# tempo total de execução
env %>% 
	run(600) %>%
 	now()
# dados da simulação

chegadas <- get_mon_arrivals(env, TRUE) %>%
recursos <- get_mon_resources(env) %>%
fila <- get_mon_attributes(env)

sprintf("Total de Clientes Processados = %d", nrow(chegadas))
sprintf("Thoughput = %f", (nrow(chegadas)/600))

sprintf("Tempo de Serviço Front =  %f", sum(chegadas[chegadas$resource == "Front", c("activity_time")]))
sprintf("Tempo Médio de Serviço Front =  %f", sum(chegadas[chegadas$resource == "Front", c("activity_time")])/nrow(chegadas[chegadas$resource == "Front", c("resource")]))
sprintf("Utilização CPU Front = %f", sum(chegadas[chegadas$resource == "Front", c("activity_time")])/600)
sprintf("Tempo de resposta Front = %f", sum(chegadas[chegadas$resource == "Front", c("end_time")])-sum(chegadas[chegadas$resource == "Front", c("start_time")]))
sprintf("Tempo Médio de resposta Front = %f", (sum(chegadas[chegadas$resource == "Front", c("end_time")])-sum(chegadas[chegadas$resource == "Front", c("start_time")]))/nrow(chegadas[chegadas$resource == "Front", c("resource")]) )
sprintf("Tempo Médio em Fila = %f ", ((sum(chegadas[chegadas$resource == "Front", c("end_time")])-sum(chegadas[chegadas$resource == "Front", c("start_time")]))/nrow(chegadas[chegadas$resource == "Front", c("resource")]))-(sum(chegadas[chegadas$resource == "Front", c("activity_time")])/nrow(chegadas[chegadas$resource == "Front", c("resource")])))

sprintf("Tempo de Serviço CPU =  %f", sum(chegadas[chegadas$resource == "CPU", c("activity_time")]))
sprintf("Tempo Médio de Serviço CPU =  %f", sum(chegadas[chegadas$resource == "CPU", c("activity_time")])/nrow(chegadas[chegadas$resource == "CPU", c("resource")]))
sprintf("Utilização CPU CPU = %f", sum(chegadas[chegadas$resource == "CPU", c("activity_time")])/600)
sprintf("Tempo de resposta CPU = %f", sum(chegadas[chegadas$resource == "CPU", c("end_time")])-sum(chegadas[chegadas$resource == "CPU", c("start_time")]))
sprintf("Tempo Médio de resposta CPU = %f", (sum(chegadas[chegadas$resource == "CPU", c("end_time")])-sum(chegadas[chegadas$resource == "CPU", c("start_time")]))/nrow(chegadas[chegadas$resource == "CPU", c("resource")]) )
sprintf("Tempo Médio em Fila = %f ", ((sum(chegadas[chegadas$resource == "CPU", c("end_time")])-sum(chegadas[chegadas$resource == "CPU", c("start_time")]))/nrow(chegadas[chegadas$resource == "CPU", c("resource")]))-(sum(chegadas[chegadas$resource == "CPU", c("activity_time")])/nrow(chegadas[chegadas$resource == "CPU", c("resource")])))

