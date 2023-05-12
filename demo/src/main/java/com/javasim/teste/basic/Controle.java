package com.javasim.teste.basic;

import org.javasim.RestartException;
import org.javasim.Simulation;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;

public class Controle extends SimulationProcess
{

	public static CPU cpu = null;
	public static Fila filaDoCPU = new Fila();


    public static double tempoRespostaTotal = 0.0;
    public static long totalClientes = 0;
    public static double clientesProcessados = 0;
    public static double totalServico = 0.0;
    
    private long Lsemente = 0;
    private long Msemente = 0;


    public Controle(long m, long l)
    {
        this.Msemente = m;
        this.Lsemente = l;
    }

    public void run ()
    {
        try
        {
			Chegadas chegadas = new Chegadas(1.5, Msemente, Lsemente);
            Controle.cpu = new CPU(0.9, Msemente, Lsemente);
            chegadas.activate();

            Simulation.start();

            //while(Controle.totalClientes < 6 || currentTime() < 600)
			    hold(600);
            
            System.out.printf("%.0f %.3f %.3f %.3f %.3f %.3f %.3f %.3f %.3f %.3f \n", 
                clientesProcessados, clientesProcessados/600, totalServico, (totalServico / clientesProcessados), 
                Controle.cpu.tempoDeServico/600, tempoRespostaTotal, (tempoRespostaTotal / clientesProcessados), 
                ((tempoRespostaTotal / clientesProcessados)-(totalServico / clientesProcessados)),
                tempoRespostaTotal/600, ((tempoRespostaTotal/600) - (totalServico/600)));



          //  System.out.println("Tempo total = "+currentTime());
           // System.out.println("Total de clientes presentes no sistema = " + totalClientes);
           // System.out.printf("Total de clientes processados = \n", clientesProcessados);
           // System.out.printf("Throughput = %f\n", clientesProcessados/600);
           /// System.out.println("Tempo de Serviço total = " + totalServico);
           // System.out.println("Tempo médio de serviço = "
           //     + (totalServico / clientesProcessados));
           // System.out.println("Utilização do CPU = " + Controle.cpu.tempoDeServico/600);
          //  System.out.println("Tempo de resposta total = " + tempoRespostaTotal);
          //  System.out.println("Tempo médio de resposta = "
         //       + (tempoRespostaTotal / clientesProcessados));
          //  
          //  System.out.println("Tempo Médio em fila = " + ((tempoRespostaTotal / clientesProcessados)-(totalServico / clientesProcessados)));
		//	System.out.println("Número médio no sistema = "+ tempoRespostaTotal/600);
         //   System.out.println("Número médio na fila = "+ ((tempoRespostaTotal/600) - (totalServico/600)));
            
			
			//System.out.println("Comprimento médio de filaCPU = "+ (Controle.filaDoCPU.clientesEmFila / Controle.filaDoCPU.checkFila));

            Simulation.stop();

            chegadas.terminate();
			Controle.cpu.terminate();

            SimulationProcess.mainResume();
        }
        catch (SimulationException e)
        {
        }
        catch (RestartException e)
        {
        }
    }
    public void await ()
    {
        this.resumeProcess();
        SimulationProcess.mainSuspend();
    }

   
}
