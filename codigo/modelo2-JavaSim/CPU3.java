package com.javasim.teste.basic;

import java.io.IOException;
import java.util.Random;

import org.javasim.RestartException;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;
import org.javasim.streams.ExponentialStream;

public class CPU3 extends SimulationProcess
{
    private ExponentialStream taxa;
    private Cliente cliente;
    public double tempoDeServico = 0.0;
    
	public CPU3(double media)
    {
        taxa = new ExponentialStream(media);
        cliente = null;
    }

    public void run ()
    {
        double inicioAtividade, fimAtividade;
        boolean vazio = false;

        while (!terminated())
        {
			while (!Controle.filaDoCPU3.isEmpty())
			{
				inicioAtividade = currentTime();

				Controle.filaDoCPU3.checkFila++;
				Controle.filaDoCPU3.clientesEmFila += Controle.filaDoCPU3.queueSize();
				cliente = Controle.filaDoCPU3.dequeue();

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
                tempoDeServico += fimAtividade - inicioAtividade;
                Controle.totalServico += tempoDeServico;

				vazio = Controle.filaDoDISCO3.isEmpty();
				Controle.filaDoDISCO3.enqueue(cliente);

				if (vazio)
				{
					try
					{
						Controle.disco3.activate();
					}
					catch (SimulationException e)
					{
					}
					catch (RestartException e)
					{
					}
				}

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
