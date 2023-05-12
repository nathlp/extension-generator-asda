#!/bin/bash
for i in $(seq 1 20); do
	python3 Mm1Simpy.py $i >> saida.txt
done
