# TP1-AyP1
Trabajo Práctico 1 para la materia Algoritmos y Programación I (Cátedra Essaya) de la Facultad de Ingeniería de la Universidad de Buenos Aires.

Cursada el primer cuatrimestre del 2018.

### TP1 - Game of Life
El objetivo del trabajo práctico es implementar un simulador para el autómata celular Conway's Game of Life.

El "tablero de juego" es una malla formada por cuadrados ("células") que se extiende por el infinito en todas las direcciones. Cada célula tiene 8 células vecinas, que son las que están próximas a ella, incluidas las diagonales. Las células tienen dos estados: están "vivas" o "muertas" (o "encendidas" y "apagadas"). El estado de la malla evoluciona a lo largo de unidades de tiempo discretas (se podría decir que por turnos). El estado de todas las células se tiene en cuenta para calcular el estado de las mismas al turno siguiente. Todas las células se actualizan simultáneamente.

Las transiciones dependen del número de células vecinas vivas:

 - Una célula muerta con exactamente 3 células vecinas vivas "nace" (al turno siguiente estará viva).
  Una célula viva con 2 ó 3 células vecinas vivas sigue viva, en otro caso muere o permanece muerta (por "soledad" o "superpoblación").
