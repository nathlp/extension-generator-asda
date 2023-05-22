// -----------------------------------------------------------------------------
// Código gerado com o ASDA - Ambiente de Simulação Distribuída Automático
// -----------------------------------------------------------------------------

package com.javasim.teste.basic;

public class Main
{
    public static void main (String[] args)
    {

        //System.out.println("args[1]="+ args[0]);
        Controle m = new Controle(Long.parseLong("1"), Long.parseLong("1"));
       // Controle m = new Controle(1, 1);
        // Para a thread principal e da controle do programa para a classe Controle
        m.await();

        System.exit(0);
    }
}

