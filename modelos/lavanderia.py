import graphviz 
 
#criar o modelo de grafo direcionado 
modelo = graphviz.Digraph(name='lavanderia', directory='modelos/') 

# Especifica caracteristicas para o grafo e passa as principais informaçoes do grafo
# (tempo total, numero de ciclos, tamanho do batch, numero maximo de entidades,
# tipo do modelo, warmup, tamanho warmup, semente)
modelo.attr(rankdir='LR', comment=' 600 0 0 0 True False 0 10 ')

# Especifica as caracteristicas dos centros de serviço
# (tipo do node, tipo da distribuição de chegada, tipo da distribuição de serviço,
# média das chegadas, média de serviço)
modelo.node('0', 'Source', image='Rsource.gif', shape='plaintext', labelloc='t', comment='1')

modelo.node('1', 'Lavadora', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 1 1 1 0.1 ') 
modelo.node('2', 'CestoRetirar', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ') 
modelo.node('2', 'CestoColocar', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ')  
modelo.node('3', 'Secadora', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ') 

modelo.node('4', 'Destination', image='REnd.gif', shape='plaintext', labelloc='t', comment='3')

# Especifica as caracteristicas dos ligações 
#(node de origem, node de destino e probabilidade)
modelo.edge('0', '1', comment='100')

modelo.edge('1', '2', comment='25') 
modelo.edge('1', '3', comment='25')
modelo.edge('1', '4', comment='25')
modelo.edge('1', '5', comment='25')

modelo.edge('2', '6', comment='100')


modelo.render(format='png')
