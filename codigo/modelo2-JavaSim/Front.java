package com.javasim.teste.basic;

import java.io.IOException;
import java.util.Random;

import org.javasim.RestartException;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;
import org.javasim.streams.ExponentialStream;

public class Front extends SimulationProcess
{
    private ExponentialStream taxa;
    private Cliente cliente;
    public double tempoDeServico = 0.0;
    
	public Front(double media)
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
			while (!Controle.filaDoFront.isEmpty())
			{
				inicioAtividade = currentTime();

				Controle.filaDoFront.checkFila++;
				Controle.filaDoFront.clientesEmFila += Controle.filaDoFront.queueSize();
				cliente = Controle.filaDoFront.dequeue();

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
				Random x = new Random();
				int aleatorio;
				aleatorio = x.nextInt(1000);

				if (0 < aleatorio && aleatorio < 2500)
				{
					vazio = Controle.filaDoCPU1.isEmpty();
					Controle.filaDoCPU1.enqueue(cliente);

					if (vazio)
					{
						try
						{
							Controle.cpu1.activate();
						}
						catch (SimulationException e)
						{
						}
						catch (RestartException e)
						{
						}
				}
				if (2500 < aleatorio && aleatorio < 5000)
				{
					vazio = Controle.filaDoCPU2.isEmpty();
					Controle.filaDoCPU2.enqueue(cliente);

					if (vazio)
					{
						try
						{
							Controle.cpu2.activate();
						}
						catch (SimulationException e)
						{
						}
						catch (RestartException e)
						{
						}
				}
				if (5000 < aleatorio && aleatorio < 7500)
				{
					vazio = Controle.filaDoCPU3.isEmpty();
					Controle.filaDoCPU3.enqueue(cliente);

					if (vazio)
					{
						try
						{
							Controle.cpu3.activate();
						}
						catch (SimulationException e)
						{
						}
						catch (RestartException e)
						{
						}
				}
				if (7500 < aleatorio && aleatorio < 10000)
				{
					vazio = Controle.filaDoCPU4.isEmpty();
					Controle.filaDoCPU4.enqueue(cliente);

					if (vazio)
					{
						try
						{
							Controle.cpu4.activate();
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
