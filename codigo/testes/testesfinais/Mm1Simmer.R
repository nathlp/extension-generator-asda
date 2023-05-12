# -----------------------------------------------------------------------------
# Código gerado com o ASDA - Ambiente de Simulação Distribuída Automático
# -----------------------------------------------------------------------------

library(simmer)

set.seed(20)

env <- simmer("Mm1")
env

# Configurar trajetória 

cliente <- trajectory() %>%
	seize("cpu", 1) %>%
	timeout(function() rexp(1, 1/0.9)) %>%
	release("cpu", 1) %>%
	set_attribute("queue_cpu", function() get_queue_count(env, "cpu"))


# criando os recursos 

env %>%
add_resource("cpu", 1) %>%
add_generator("cliente", cliente, function() rexp(1, 1/1.5), mon=2)

# tempo total de execução
env %>% 
	run(600) %>%
 	now()
# dados da simulação

chegadas <- get_mon_arrivals(env, TRUE) 
recursos <- get_mon_resources(env) 
fila <- get_mon_attributes(env)

sprintf("%d %f %f %f %f %f %f %f %f", nrow(get_mon_arrivals(env)), (nrow(get_mon_arrivals(env))/600), sum(chegadas[chegadas$resource == "cpu", c("activity_time")]),
sum(chegadas[chegadas$resource == "cpu", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu", c("resource", "name")]), sum(chegadas[chegadas$resource == "cpu", c("activity_time")])/600,
sum(chegadas[chegadas$resource == "cpu", c("end_time")])-sum(chegadas[chegadas$resource == "cpu", c("start_time")]),
(sum(chegadas[chegadas$resource == "cpu", c("end_time")])-sum(chegadas[chegadas$resource == "cpu", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu", c("resource", "name")]),
((sum(chegadas[chegadas$resource == "cpu", c("end_time")])-sum(chegadas[chegadas$resource == "cpu", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "cpu", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu", c("resource", "name")])),
sum(fila[fila$key == "queue_cpu",c("value")])/nrow(fila[fila$key == "queue_cpu",c("value", "key")]))

sprintf("Total de Clientes Processados = %d", nrow(get_mon_arrivals(env)))
sprintf("Thoughput = %f", (nrow(get_mon_arrivals(env))/600))

sprintf("Tempo de Serviço CPU =  %f", sum(chegadas[chegadas$resource == "cpu", c("activity_time")]))
sprintf("Tempo Médio de Serviço CPU =  %f", sum(chegadas[chegadas$resource == "cpu", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu", c("resource", "name")]))
sprintf("Utilização CPU CPU = %f", sum(chegadas[chegadas$resource == "cpu", c("activity_time")])/600)
sprintf("Tempo de resposta CPU = %f", sum(chegadas[chegadas$resource == "cpu", c("end_time")])-sum(chegadas[chegadas$resource == "cpu", c("start_time")]))
sprintf("Tempo Médio de resposta CPU = %f", (sum(chegadas[chegadas$resource == "cpu", c("end_time")])-sum(chegadas[chegadas$resource == "cpu", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu", c("resource", "name")]) )
sprintf("Tempo Médio em Fila CPU = %f ", ((sum(chegadas[chegadas$resource == "cpu", c("end_time")])-sum(chegadas[chegadas$resource == "cpu", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "cpu", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu", c("resource", "name")])))
sprintf("Comprimento Médio de Fila CPU =  %f", sum(fila[fila$key == "queue_cpu",c("value")])/nrow(fila[fila$key == "queue_cpu",c("value", "key")]))

