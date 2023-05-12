envs <- lapply(1:20, function(i) {
  simmer("Mm1") %>%
    add_resource("cpu", 1) %>%
    add_generator("cliente", cliente, function() rexp(1, 0.050)) %>%
    run(600)
})

resources <- get_mon_resources(envs[[1]])
arrivals <- get_mon_arrivals(envs[[1]])

plot(resources, metric="usage", "cpu", items = "server", steps = TRUE) 

fila[fila$key == "queue_cpu",c("key", "value")]