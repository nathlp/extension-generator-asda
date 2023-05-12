import graphviz 
 
#criar o modelo de grafo direcionado 
modelo = graphviz.Digraph(name='modelo2', directory='modelos/') 

# Especifica caracteristicas para o grafo e passa as principais informaçoes do grafo
# (tempo total, numero de ciclos, tamanho do batch, numero maximo de entidades,
# tipo do modelo, warmup, tamanho warmup, semente)
modelo.attr(rankdir='LR', comment=' 2000 0 0 0 True False 0 10 ')

# Especifica as caracteristicas dos centros de serviço
# (tipo do node, tipo da distribuição de chegada, tipo da distribuição de serviço,
# média das chegadas, média de serviço)
modelo.node('0', 'Source', image='Rsource.gif', shape='plaintext', labelloc='t', comment='1')

modelo.node('1', 'Front', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 1 1 1 0.1 ') 
modelo.node('2', 'CPU1', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ') 
modelo.node('3', 'CPU2', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ') 
modelo.node('4', 'CPU3', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ') 
modelo.node('5', 'CPU4', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ') 

modelo.node('6', 'DISCO1', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 3.250 ') 
modelo.node('7', 'DISCO2', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 3.250 ')
modelo.node('8', 'DISCO3', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 3.250 ')
modelo.node('9', 'DISCO4', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 3.250 ')

modelo.node('10', 'Destination', image='REnd.gif', shape='plaintext', labelloc='t', comment='3')

# Especifica as caracteristicas dos ligações 
#(node de origem, node de destino e probabilidade)
modelo.edge('0', '1', comment='100')

modelo.edge('1', '2', comment='25') 
modelo.edge('1', '3', comment='25')
modelo.edge('1', '4', comment='25')
modelo.edge('1', '5', comment='25')

modelo.edge('2', '6', comment='100')
modelo.edge('3', '7', comment='100')
modelo.edge('4', '8', comment='100')
modelo.edge('5', '9', comment='100')

modelo.edge('6', '10', comment='100')
modelo.edge('7', '10', comment='100')
modelo.edge('8', '10', comment='100')
modelo.edge('9', '10', comment='100')

modelo.render(format='png')
