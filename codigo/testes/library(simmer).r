library(simmer)

set.seed(10)

env <- simmer("Mm1")
env

# Configurar trajetória 

job <- trajectory("job' path") %>%
	seize("cpu1", 1) %>%
	timeout(function() rexp(1, 0.5)) %>%
	release("cpu1", 1) %>%
	set_attribute("queue_cpu1", function() get_queue_count(env, "cpu1")) %>%
	seize("disco1", 1) %>%
	timeout(function() rexp(1, 1)) %>%
	release("disco1", 1) %>%
	set_attribute("queue_disco1", function() get_queue_count(env, "disco1")) 


cliente <- trajectory("clientes' path") %>%
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

env %>%
	add_resource("cpu1", 1) %>%
	add_resource("disco1", 1) %>%
	add_generator("cliente", cliente, function() rexp(1, 1), mon=2)

# tempo total de execução
env %>% 
	run(40) %>%



    traj <- trajectory() %>%
  log_("hello!") %>%
  timeout(1) %>%
  rollback(1, 3)

simmer() %>%
  add_generator("hello_sayer", traj, at(0)) %>%
  run() %>% invisible



  cliente <- trajectory("clientes' path") %>%
    set_global("passou", -1, mod="+", init=2)%>%
    log_(get_global(env, "passou"))%>%
    seize("cpu", 1) %>%
    timeout(function() rexp(1, 0.1)) %>%
    release("cpu", 1) %>%
    branch(
        function() get_global(env, "passou"), continue=c(TRUE,TRUE),
        trajectory() %>%
            log_("entrou na branch")%>%
            seize("disco", 1) %>%
            timeout(function() rexp(1, 0.5)) %>%
            release("disco", 1),
        trajectory()%>%
            log_("aq"))%>%
    rollback(14, check=function() get_global(env, "passou") == 0) 
	 



traj <- trajectory() %>%
  set_global("path", 1, mod="+", init=-1) %>%
  log_(function() paste("Path", get_global(env, "path"), "selected")) %>%
  branch(
    function() get_global(env, "path"), continue=c(TRUE, FALSE),
    trajectory() %>%
      log_("following path 1"),
    trajectory() %>%
      log_("following path 2")) %>%
  log_("continuing after the branch (path 0)")
  rollback(9, 1)
