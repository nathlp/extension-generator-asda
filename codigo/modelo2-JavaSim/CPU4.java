package com.javasim.teste.basic;

import java.io.IOException;
import java.util.Random;

import org.javasim.RestartException;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;
import org.javasim.streams.ExponentialStream;

public class CPU4 extends SimulationProcess
{
    private ExponentialStream taxa;
    private Cliente cliente;
    public double tempoDeServico = 0.0;
    
	public CPU4(double media)
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
			while (!Controle.filaDoCPU4.isEmpty())
			{
				inicioAtividade = currentTime();

				Controle.filaDoCPU4.checkFila++;
				Controle.filaDoCPU4.clientesEmFila += Controle.filaDoCPU4.queueSize();
				cliente = Controle.filaDoCPU4.dequeue();

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

				vazio = Controle.filaDoDISCO4.isEmpty();
				Controle.filaDoDISCO4.enqueue(cliente);

				if (vazio)
				{
					try
					{
						Controle.disco4.activate();
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
