package com.javasim.teste.basic;

import java.io.IOException;
import java.util.Random;

import org.javasim.RestartException;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;
import org.javasim.streams.ExponentialStream;

public class CPU2 extends SimulationProcess
{
    private ExponentialStream taxa;
    private Cliente cliente;
    public double tempoDeServico = 0.0;
    
	public CPU2(double media)
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
			while (!Controle.filaDoCPU2.isEmpty())
			{
				inicioAtividade = currentTime();

				Controle.filaDoCPU2.checkFila++;
				Controle.filaDoCPU2.clientesEmFila += Controle.filaDoCPU2.queueSize();
				cliente = Controle.filaDoCPU2.dequeue();

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

				vazio = Controle.filaDoDISCO2.isEmpty();
				Controle.filaDoDISCO2.enqueue(cliente);

				if (vazio)
				{
					try
					{
						Controle.disco2.activate();
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
