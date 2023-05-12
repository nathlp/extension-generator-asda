package com.javasim.teste.basic;

import java.io.IOException;

import org.javasim.RestartException;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;
import org.javasim.streams.ExponentialStream;

public class Chegadas extends SimulationProcess
{
    private ExponentialStream taxa;
    private int i = 0;

    public Chegadas(double media, long m, long l)
    {
        taxa = new ExponentialStream(media, 0 , m, l);
    }

    public void run ()
    {
        while (!terminated())
        {
            try
            {
                hold(taxa.getNumber());
            }
            catch (SimulationException e)
            {
            }
            catch (RestartException e)
            {
            }
            catch (IOException e)
            {
            }
            i=i+1;
            new Cliente(i);
        }
    }

}
