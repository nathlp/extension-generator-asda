package com.javasim.teste.basic;

import org.javasim.RestartException;
import org.javasim.Simulation;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;

public class Controle extends SimulationProcess
{

	public static Front front = null;
	public static Fila filaDoFront = new Fila();

	public static CPU1 cpu1 = null;
	public static Fila filaDoCPU1 = new Fila();

	public static CPU2 cpu2 = null;
	public static Fila filaDoCPU2 = new Fila();

	public static CPU3 cpu3 = null;
	public static Fila filaDoCPU3 = new Fila();

	public static CPU4 cpu4 = null;
	public static Fila filaDoCPU4 = new Fila();

	public static DISCO1 disco1 = null;
	public static Fila filaDoDISCO1 = new Fila();

	public static DISCO2 disco2 = null;
	public static Fila filaDoDISCO2 = new Fila();

	public static DISCO3 disco3 = null;
	public static Fila filaDoDISCO3 = new Fila();

	public static DISCO4 disco4 = null;
	public static Fila filaDoDISCO4 = new Fila();


    public static double tempoRespostaTotal = 0.0;
    public static long totalClientes = 0;
    public static long clientesProcessados = 0;
    public static double totalServico = 0;


    public Controle()
    {
        
    }

    public void run ()
    {
        try
        {
			Chegadas chegadas = new Chegadas(1);
			Controle.front = new Front(0.1);
			Controle.cpu1 = new CPU1(0.1);
			Controle.cpu2 = new CPU2(0.1);
			Controle.cpu3 = new CPU3(0.1);
			Controle.cpu4 = new CPU4(0.1);
			Controle.disco1 = new DISCO1(0.1);
			Controle.disco2 = new DISCO2(0.1);
			Controle.disco3 = new DISCO3(0.1);
			Controle.disco4 = new DISCO4(0.1);
            chegadas.activate();

            Simulation.start();

			hold(600);

            System.out.println("Tempo total = "+currentTime());
            System.out.println("Total de clientes presentes no sistema = " + totalClientes);
            System.out.println("Total de clientes processados = " + clientesProcessados);
            System.out.println("Tempo de resposta total = " + tempoRespostaTotal);
            System.out.println("Tempo médio de resposta = "
                + (tempoRespostaTotal / clientesProcessados));
            
			System.out.println("Utilização do Front = " + Controle.front.tempoDeServico);
			System.out.println("Comprimento médio de filaFront = "+ (Controle.filaDoFront.clientesEmFila / Controle.filaDoFront.checkFila));
			System.out.println("Utilização do CPU1 = " + Controle.cpu1.tempoDeServico);
			System.out.println("Comprimento médio de filaCPU1 = "+ (Controle.filaDoCPU1.clientesEmFila / Controle.filaDoCPU1.checkFila));
			System.out.println("Utilização do CPU2 = " + Controle.cpu2.tempoDeServico);
			System.out.println("Comprimento médio de filaCPU2 = "+ (Controle.filaDoCPU2.clientesEmFila / Controle.filaDoCPU2.checkFila));
			System.out.println("Utilização do CPU3 = " + Controle.cpu3.tempoDeServico);
			System.out.println("Comprimento médio de filaCPU3 = "+ (Controle.filaDoCPU3.clientesEmFila / Controle.filaDoCPU3.checkFila));
			System.out.println("Utilização do CPU4 = " + Controle.cpu4.tempoDeServico);
			System.out.println("Comprimento médio de filaCPU4 = "+ (Controle.filaDoCPU4.clientesEmFila / Controle.filaDoCPU4.checkFila));
			System.out.println("Utilização do DISCO1 = " + Controle.disco1.tempoDeServico);
			System.out.println("Comprimento médio de filaDISCO1 = "+ (Controle.filaDoDISCO1.clientesEmFila / Controle.filaDoDISCO1.checkFila));
			System.out.println("Utilização do DISCO2 = " + Controle.disco2.tempoDeServico);
			System.out.println("Comprimento médio de filaDISCO2 = "+ (Controle.filaDoDISCO2.clientesEmFila / Controle.filaDoDISCO2.checkFila));
			System.out.println("Utilização do DISCO3 = " + Controle.disco3.tempoDeServico);
			System.out.println("Comprimento médio de filaDISCO3 = "+ (Controle.filaDoDISCO3.clientesEmFila / Controle.filaDoDISCO3.checkFila));
			System.out.println("Utilização do DISCO4 = " + Controle.disco4.tempoDeServico);
			System.out.println("Comprimento médio de filaDISCO4 = "+ (Controle.filaDoDISCO4.clientesEmFila / Controle.filaDoDISCO4.checkFila));

            Simulation.stop();

            chegadas.terminate();
			Controle.front.terminate();
			Controle.cpu1.terminate();
			Controle.cpu2.terminate();
			Controle.cpu3.terminate();
			Controle.cpu4.terminate();
			Controle.disco1.terminate();
			Controle.disco2.terminate();
			Controle.disco3.terminate();
			Controle.disco4.terminate();

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
