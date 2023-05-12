package com.javasim.teste.basic;

import java.io.IOException;


import org.javasim.RestartException;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;
import org.javasim.streams.ExponentialStream;

public class CPU extends SimulationProcess
{
    private ExponentialStream taxa;
    private Cliente cliente;
    public double tempoDeServico = 0.0;
    
	public CPU(double media, long m, long l)
    {
        taxa = new ExponentialStream(media, 0 , m, l);
        cliente = null;
    }

    public void run ()
    {
        double inicioAtividade, fimAtividade;
        boolean vazio = false;

        while (!terminated())
        {
			while (!Controle.filaDoCPU.isEmpty())
			{
				inicioAtividade = currentTime();
                //System.out.println("INICIO SERVICO = "+ currentTime());
				Controle.filaDoCPU.checkFila++;
				Controle.filaDoCPU.clientesEmFila += Controle.filaDoCPU.queueSize();
				cliente = Controle.filaDoCPU.dequeue();

                try
                {
                    hold(serviceTime());
                }
                catch (SimulationException e)
                {
                }
                catch (RestartException e)
                {
                }

                fimAtividade = currentTime();
               // System.out.println("FIM SERVICO = "+ currentTime());
               // System.out.println("DISBUIÇÃO = " + serviceTime());
                tempoDeServico += fimAtividade - inicioAtividade;
                Controle.totalServico = tempoDeServico;
              //  System.out.println("SERVICO = "+ tempoDeServico);
              //  System.out.println(" valor do controle SERVICO = "+ Controle.totalServico);
				Controle.clientesProcessados++;
				cliente.finished();


            }

        
            try
            {
                cancel();
            }
            catch (RestartException e)
            {
            }
        }
    }

    public double serviceTime ()
    {
        try
        {
            return taxa.getNumber();
        }
        catch (IOException e)
        {
            return 0.0;
        }
    }

}
