# -----------------------------------------------------------------------------
# Código gerado com o ASDA - Ambiente de Simulação Distribuída Automático
# -----------------------------------------------------------------------------

library(simmer)

set.seed(10)

env <- simmer("modelo2")
env

# Configurar trajetória 

cliente <- trajectory() %>%
	seize("front", 1) %>%
	timeout(function() rexp(1, 0.1)) %>%
	release("front", 1) %>%
	set_attribute("queue_front", function() get_queue_count(env, "front")) %>%
	set_attribute("x", function() sample(1:4, 1, prob=c(25, 25, 25, 25), replace=TRUE)) %>%
	branch(
		function() get_attribute(env, "x"), continue=c(TRUE, TRUE, TRUE, TRUE),
		 trajectory() %>%
			seize("cpu1", 1) %>%
			timeout(function() rexp(1, 0.325)) %>%
			release("cpu1", 1) %>%
			set_attribute("queue_cpu1", function() get_queue_count(env, "cpu1"))%>%
			seize("disco1", 1) %>%
			timeout(function() rexp(1, 3.250)) %>%
			release("disco1", 1) %>%
			set_attribute("queue_disco1", function() get_queue_count(env, "disco1")), 
		 trajectory() %>%
			seize("cpu2", 1) %>%
			timeout(function() rexp(1, 0.325)) %>%
			release("cpu2", 1) %>%
			set_attribute("queue_cpu2", function() get_queue_count(env, "cpu2"))%>%
			seize("disco2", 1) %>%
			timeout(function() rexp(1, 3.250)) %>%
			release("disco2", 1) %>%
			set_attribute("queue_disco2", function() get_queue_count(env, "disco2")), 
		 trajectory() %>%
			seize("cpu3", 1) %>%
			timeout(function() rexp(1, 0.325)) %>%
			release("cpu3", 1) %>%
			set_attribute("queue_cpu3", function() get_queue_count(env, "cpu3"))%>%
			seize("disco3", 1) %>%
			timeout(function() rexp(1, 3.250)) %>%
			release("disco3", 1) %>%
			set_attribute("queue_disco3", function() get_queue_count(env, "disco3")), 
		 trajectory() %>%
			seize("cpu4", 1) %>%
			timeout(function() rexp(1, 0.325)) %>%
			release("cpu4", 1) %>%
			set_attribute("queue_cpu4", function() get_queue_count(env, "cpu4"))%>%
			seize("disco4", 1) %>%
			timeout(function() rexp(1, 3.250)) %>%
			release("disco4", 1) %>%
			set_attribute("queue_disco4", function() get_queue_count(env, "disco4")))


# criando os recursos 

env %>%
add_resource("front", 1) %>%
add_resource("cpu1", 1) %>%
add_resource("cpu2", 1) %>%
add_resource("cpu3", 1) %>%
add_resource("cpu4", 1) %>%
add_resource("disco1", 1) %>%
add_resource("disco2", 1) %>%
add_resource("disco3", 1) %>%
add_resource("disco4", 1) %>%
add_generator("cliente", cliente, function() rexp(1, 1), mon=2)

# tempo total de execução
env %>% 
	run(600) %>%
 	now()
# dados da simulação

chegadas <- get_mon_arrivals(env, TRUE) 
recursos <- get_mon_resources(env) 
fila <- get_mon_attributes(env)

sprintf("Total de Clientes Processados = %d", nrow(get_mon_arrivals(env)))
sprintf("Thoughput = %f", (nrow(get_mon_arrivals(env))/600))

sprintf("Tempo de Serviço Front =  %f", sum(chegadas[chegadas$resource == "front", c("activity_time")]))
sprintf("Tempo Médio de Serviço Front =  %f", sum(chegadas[chegadas$resource == "front", c("activity_time")])/nrow(chegadas[chegadas$resource == "front", c("resource", "name")]))
sprintf("Utilização CPU Front = %f", sum(chegadas[chegadas$resource == "front", c("activity_time")])/600)
sprintf("Tempo de resposta Front = %f", sum(chegadas[chegadas$resource == "front", c("end_time")])-sum(chegadas[chegadas$resource == "front", c("start_time")]))
sprintf("Tempo Médio de resposta Front = %f", (sum(chegadas[chegadas$resource == "front", c("end_time")])-sum(chegadas[chegadas$resource == "front", c("start_time")]))/nrow(chegadas[chegadas$resource == "front", c("resource", "name")]) )
sprintf("Tempo Médio em Fila Front = %f ", ((sum(chegadas[chegadas$resource == "front", c("end_time")])-sum(chegadas[chegadas$resource == "front", c("start_time")]))/nrow(chegadas[chegadas$resource == "front", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "front", c("activity_time")])/nrow(chegadas[chegadas$resource == "front", c("resource", "name")])))
sprintf("Comprimento Médio de Fila Front =  %f", sum(fila[fila$key == "queue_front",c("value")])/nrow(fila[fila$key == "queue_front",c("value", "key")]))

sprintf("Tempo de Serviço CPU1 =  %f", sum(chegadas[chegadas$resource == "cpu1", c("activity_time")]))
sprintf("Tempo Médio de Serviço CPU1 =  %f", sum(chegadas[chegadas$resource == "cpu1", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu1", c("resource", "name")]))
sprintf("Utilização CPU CPU1 = %f", sum(chegadas[chegadas$resource == "cpu1", c("activity_time")])/600)
sprintf("Tempo de resposta CPU1 = %f", sum(chegadas[chegadas$resource == "cpu1", c("end_time")])-sum(chegadas[chegadas$resource == "cpu1", c("start_time")]))
sprintf("Tempo Médio de resposta CPU1 = %f", (sum(chegadas[chegadas$resource == "cpu1", c("end_time")])-sum(chegadas[chegadas$resource == "cpu1", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu1", c("resource", "name")]) )
sprintf("Tempo Médio em Fila CPU1 = %f ", ((sum(chegadas[chegadas$resource == "cpu1", c("end_time")])-sum(chegadas[chegadas$resource == "cpu1", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu1", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "cpu1", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu1", c("resource", "name")])))
sprintf("Comprimento Médio de Fila CPU1 =  %f", sum(fila[fila$key == "queue_cpu1",c("value")])/nrow(fila[fila$key == "queue_cpu1",c("value", "key")]))

sprintf("Tempo de Serviço CPU2 =  %f", sum(chegadas[chegadas$resource == "cpu2", c("activity_time")]))
sprintf("Tempo Médio de Serviço CPU2 =  %f", sum(chegadas[chegadas$resource == "cpu2", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu2", c("resource", "name")]))
sprintf("Utilização CPU CPU2 = %f", sum(chegadas[chegadas$resource == "cpu2", c("activity_time")])/600)
sprintf("Tempo de resposta CPU2 = %f", sum(chegadas[chegadas$resource == "cpu2", c("end_time")])-sum(chegadas[chegadas$resource == "cpu2", c("start_time")]))
sprintf("Tempo Médio de resposta CPU2 = %f", (sum(chegadas[chegadas$resource == "cpu2", c("end_time")])-sum(chegadas[chegadas$resource == "cpu2", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu2", c("resource", "name")]) )
sprintf("Tempo Médio em Fila CPU2 = %f ", ((sum(chegadas[chegadas$resource == "cpu2", c("end_time")])-sum(chegadas[chegadas$resource == "cpu2", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu2", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "cpu2", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu2", c("resource", "name")])))
sprintf("Comprimento Médio de Fila CPU2 =  %f", sum(fila[fila$key == "queue_cpu2",c("value")])/nrow(fila[fila$key == "queue_cpu2",c("value", "key")]))

sprintf("Tempo de Serviço CPU3 =  %f", sum(chegadas[chegadas$resource == "cpu3", c("activity_time")]))
sprintf("Tempo Médio de Serviço CPU3 =  %f", sum(chegadas[chegadas$resource == "cpu3", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu3", c("resource", "name")]))
sprintf("Utilização CPU CPU3 = %f", sum(chegadas[chegadas$resource == "cpu3", c("activity_time")])/600)
sprintf("Tempo de resposta CPU3 = %f", sum(chegadas[chegadas$resource == "cpu3", c("end_time")])-sum(chegadas[chegadas$resource == "cpu3", c("start_time")]))
sprintf("Tempo Médio de resposta CPU3 = %f", (sum(chegadas[chegadas$resource == "cpu3", c("end_time")])-sum(chegadas[chegadas$resource == "cpu3", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu3", c("resource", "name")]) )
sprintf("Tempo Médio em Fila CPU3 = %f ", ((sum(chegadas[chegadas$resource == "cpu3", c("end_time")])-sum(chegadas[chegadas$resource == "cpu3", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu3", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "cpu3", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu3", c("resource", "name")])))
sprintf("Comprimento Médio de Fila CPU3 =  %f", sum(fila[fila$key == "queue_cpu3",c("value")])/nrow(fila[fila$key == "queue_cpu3",c("value", "key")]))

sprintf("Tempo de Serviço CPU4 =  %f", sum(chegadas[chegadas$resource == "cpu4", c("activity_time")]))
sprintf("Tempo Médio de Serviço CPU4 =  %f", sum(chegadas[chegadas$resource == "cpu4", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu4", c("resource", "name")]))
sprintf("Utilização CPU CPU4 = %f", sum(chegadas[chegadas$resource == "cpu4", c("activity_time")])/600)
sprintf("Tempo de resposta CPU4 = %f", sum(chegadas[chegadas$resource == "cpu4", c("end_time")])-sum(chegadas[chegadas$resource == "cpu4", c("start_time")]))
sprintf("Tempo Médio de resposta CPU4 = %f", (sum(chegadas[chegadas$resource == "cpu4", c("end_time")])-sum(chegadas[chegadas$resource == "cpu4", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu4", c("resource", "name")]) )
sprintf("Tempo Médio em Fila CPU4 = %f ", ((sum(chegadas[chegadas$resource == "cpu4", c("end_time")])-sum(chegadas[chegadas$resource == "cpu4", c("start_time")]))/nrow(chegadas[chegadas$resource == "cpu4", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "cpu4", c("activity_time")])/nrow(chegadas[chegadas$resource == "cpu4", c("resource", "name")])))
sprintf("Comprimento Médio de Fila CPU4 =  %f", sum(fila[fila$key == "queue_cpu4",c("value")])/nrow(fila[fila$key == "queue_cpu4",c("value", "key")]))

sprintf("Tempo de Serviço DISCO1 =  %f", sum(chegadas[chegadas$resource == "disco1", c("activity_time")]))
sprintf("Tempo Médio de Serviço DISCO1 =  %f", sum(chegadas[chegadas$resource == "disco1", c("activity_time")])/nrow(chegadas[chegadas$resource == "disco1", c("resource", "name")]))
sprintf("Utilização CPU DISCO1 = %f", sum(chegadas[chegadas$resource == "disco1", c("activity_time")])/600)
sprintf("Tempo de resposta DISCO1 = %f", sum(chegadas[chegadas$resource == "disco1", c("end_time")])-sum(chegadas[chegadas$resource == "disco1", c("start_time")]))
sprintf("Tempo Médio de resposta DISCO1 = %f", (sum(chegadas[chegadas$resource == "disco1", c("end_time")])-sum(chegadas[chegadas$resource == "disco1", c("start_time")]))/nrow(chegadas[chegadas$resource == "disco1", c("resource", "name")]) )
sprintf("Tempo Médio em Fila DISCO1 = %f ", ((sum(chegadas[chegadas$resource == "disco1", c("end_time")])-sum(chegadas[chegadas$resource == "disco1", c("start_time")]))/nrow(chegadas[chegadas$resource == "disco1", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "disco1", c("activity_time")])/nrow(chegadas[chegadas$resource == "disco1", c("resource", "name")])))
sprintf("Comprimento Médio de Fila DISCO1 =  %f", sum(fila[fila$key == "queue_disco1",c("value")])/nrow(fila[fila$key == "queue_disco1",c("value", "key")]))

sprintf("Tempo de Serviço DISCO2 =  %f", sum(chegadas[chegadas$resource == "disco2", c("activity_time")]))
sprintf("Tempo Médio de Serviço DISCO2 =  %f", sum(chegadas[chegadas$resource == "disco2", c("activity_time")])/nrow(chegadas[chegadas$resource == "disco2", c("resource", "name")]))
sprintf("Utilização CPU DISCO2 = %f", sum(chegadas[chegadas$resource == "disco2", c("activity_time")])/600)
sprintf("Tempo de resposta DISCO2 = %f", sum(chegadas[chegadas$resource == "disco2", c("end_time")])-sum(chegadas[chegadas$resource == "disco2", c("start_time")]))
sprintf("Tempo Médio de resposta DISCO2 = %f", (sum(chegadas[chegadas$resource == "disco2", c("end_time")])-sum(chegadas[chegadas$resource == "disco2", c("start_time")]))/nrow(chegadas[chegadas$resource == "disco2", c("resource", "name")]) )
sprintf("Tempo Médio em Fila DISCO2 = %f ", ((sum(chegadas[chegadas$resource == "disco2", c("end_time")])-sum(chegadas[chegadas$resource == "disco2", c("start_time")]))/nrow(chegadas[chegadas$resource == "disco2", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "disco2", c("activity_time")])/nrow(chegadas[chegadas$resource == "disco2", c("resource", "name")])))
sprintf("Comprimento Médio de Fila DISCO2 =  %f", sum(fila[fila$key == "queue_disco2",c("value")])/nrow(fila[fila$key == "queue_disco2",c("value", "key")]))

sprintf("Tempo de Serviço DISCO3 =  %f", sum(chegadas[chegadas$resource == "disco3", c("activity_time")]))
sprintf("Tempo Médio de Serviço DISCO3 =  %f", sum(chegadas[chegadas$resource == "disco3", c("activity_time")])/nrow(chegadas[chegadas$resource == "disco3", c("resource", "name")]))
sprintf("Utilização CPU DISCO3 = %f", sum(chegadas[chegadas$resource == "disco3", c("activity_time")])/600)
sprintf("Tempo de resposta DISCO3 = %f", sum(chegadas[chegadas$resource == "disco3", c("end_time")])-sum(chegadas[chegadas$resource == "disco3", c("start_time")]))
sprintf("Tempo Médio de resposta DISCO3 = %f", (sum(chegadas[chegadas$resource == "disco3", c("end_time")])-sum(chegadas[chegadas$resource == "disco3", c("start_time")]))/nrow(chegadas[chegadas$resource == "disco3", c("resource", "name")]) )
sprintf("Tempo Médio em Fila DISCO3 = %f ", ((sum(chegadas[chegadas$resource == "disco3", c("end_time")])-sum(chegadas[chegadas$resource == "disco3", c("start_time")]))/nrow(chegadas[chegadas$resource == "disco3", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "disco3", c("activity_time")])/nrow(chegadas[chegadas$resource == "disco3", c("resource", "name")])))
sprintf("Comprimento Médio de Fila DISCO3 =  %f", sum(fila[fila$key == "queue_disco3",c("value")])/nrow(fila[fila$key == "queue_disco3",c("value", "key")]))

sprintf("Tempo de Serviço DISCO4 =  %f", sum(chegadas[chegadas$resource == "disco4", c("activity_time")]))
sprintf("Tempo Médio de Serviço DISCO4 =  %f", sum(chegadas[chegadas$resource == "disco4", c("activity_time")])/nrow(chegadas[chegadas$resource == "disco4", c("resource", "name")]))
sprintf("Utilização CPU DISCO4 = %f", sum(chegadas[chegadas$resource == "disco4", c("activity_time")])/600)
sprintf("Tempo de resposta DISCO4 = %f", sum(chegadas[chegadas$resource == "disco4", c("end_time")])-sum(chegadas[chegadas$resource == "disco4", c("start_time")]))
sprintf("Tempo Médio de resposta DISCO4 = %f", (sum(chegadas[chegadas$resource == "disco4", c("end_time")])-sum(chegadas[chegadas$resource == "disco4", c("start_time")]))/nrow(chegadas[chegadas$resource == "disco4", c("resource", "name")]) )
sprintf("Tempo Médio em Fila DISCO4 = %f ", ((sum(chegadas[chegadas$resource == "disco4", c("end_time")])-sum(chegadas[chegadas$resource == "disco4", c("start_time")]))/nrow(chegadas[chegadas$resource == "disco4", c("resource", "name")]))-(sum(chegadas[chegadas$resource == "disco4", c("activity_time")])/nrow(chegadas[chegadas$resource == "disco4", c("resource", "name")])))
sprintf("Comprimento Médio de Fila DISCO4 =  %f", sum(fila[fila$key == "queue_disco4",c("value")])/nrow(fila[fila$key == "queue_disco4",c("value", "key")]))

