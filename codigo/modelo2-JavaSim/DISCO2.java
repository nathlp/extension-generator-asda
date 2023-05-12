package com.javasim.teste.basic;

import java.io.IOException;
import java.util.Random;

import org.javasim.RestartException;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;
import org.javasim.streams.ExponentialStream;

public class DISCO2 extends SimulationProcess
{
    private ExponentialStream taxa;
    private Cliente cliente;
    public double tempoDeServico = 0.0;
    
	public DISCO2(double media)
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
			while (!Controle.filaDoDISCO2.isEmpty())
			{
				inicioAtividade = currentTime();

				Controle.filaDoDISCO2.checkFila++;
				Controle.filaDoDISCO2.clientesEmFila += Controle.filaDoDISCO2.queueSize();
				cliente = Controle.filaDoDISCO2.dequeue();

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
