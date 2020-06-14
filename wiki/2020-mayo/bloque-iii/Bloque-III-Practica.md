# Bloque III: Entrega de ejercicios

## Enrutamiento IP


Descomprime el escenario disponible en el fichero escenario-test.zip y ábrelo con Netgui. Arranca todas las máquinas

1. Obtén las tablas de enrutamiento de TODAS las máquinas que estén configuradas e indica el comando que hay que usar. Adjunta pantallazos de los resultados en el terminal en todas las máquinas

2. Comprueba si pc2 y pc4 pueden intercambiar datagramas. Indica el comando que has usado para ello, la salida que produce y porqué deduces que hay conectividad

3. Los paquetes enviados de pc2 a pc4, ¿Qué ruta siguen?. Justifícalo indicando los comandos que hay que ejecutar para saberlo, y las salidas que producen

4. Los paquetes enviados de pc4 a pc2, ¿Qué ruta siguen?. Justifícalo indicando los comandos que hay que ejecutar para saberlo, y las salidas que producen

5. Configura la IP de PC1 para que haya conectividad con PC2. Los paquetes de pc1 a pc2 deben seguir la ruta pc1=>r2=>PC2. Sin cambiar ninguna tabla de enrutamiento del resto de máquinas, ¿Qué ruta siguen los paquetes que van de PC2 a PC1?

6. Apaga r1, r2, r3 y r4. Configura las máquinas restantes para que haya conectividad entre todas ellas. Muestra la información del comando traceroute desde PC1 al resto de máquina, y justifica que tu configuración está funcionando. Guarda esta configuración de forma persistente

## ARP

7. Partimos del escenario que ya tenías configurado en el apartado 6. Asegúrate que hay conectividad entre PC2 y PC4 a través de r5. Cierra todas las máquinas y arranca sólo PC2, PC4 y r5. Completa la siguiente tabla:

| Máquina  |  Direccion Ethernet | Dirección IP |
|----------|---------------------|--------------|
|   PC2    |                     |              |
|   PC4    |                     |              |
|   R5     |                     |              |

8. Partiendo de estado inicial, antes de haber ejecutado ningún comando ping, comprueba el estado de las cachés de arp. Saca una captura de la terminal de cada máquina (pc2, pc4 y r5) con el comando que has usado y el resultado.

9. Arranca tcpdump para capturar el tráfico en pc4 y en r5 (en su interfaz eth2). Realiza un único ping desde pc2 a pc4. Guarda las capturas en los ficheros cap-pc4-xxx.cap y cap-r5-xxx.cap donde xxx son tus iniciales (iguales que las que usaste en los ejercicios del bloque II). Toma una caputara de pantalla del terminal en pc4 y r5 donde se vea el comando tcpdump lanzado

10. Comprueba de nuevo el estado de las cachés de ARP y saca las capturas de la terminal de cada máquina (pc2, pc4 y r5). Compáralas con lo obtenido en 8 y explica qué ha ocurrido

11. Abre las dos capturas en wireshark, toma un pantallazo de cada una y adjúntalos como respuesta a este apartado

12. Explica cada una de las tramas que aparecen en la captura tomada en r5, indicando el protocolo, quién la envía, quien la recibe y el propósito


## UDP

13. Partimos del mismo escenario anterior, en el que hay conectividad entre PC2 y PC4 a través de r5. Arranca sólo PC2, PC4 y r5. Queremos enviar el mensaje "Hola, soy xxx", donde xxx son tus iniciales (iguales que en los ejercicios previos) desde PC2 a PC4, mediante el protocolo UDP. Para ello usaremos el comando nc. Como primer paso arranca el comando tcpdump en r5 para que se realice una captura del tráfico que pasa por su interfaz eth0. Guárdalo en el fichero udp-xxx.cap, donde xxx son tus iniciales. Lanza tcpump y toma una captura del terminal y adjúntala como respuesta a esta pregunta

14. Para recibir el mensaje en PC4 deberás lanzar nc en modo escucha desde un puerto que comience por el número 40 y termine con los dos primeros dígitos de tu DNI. Así, si tu dni es 32531021T, el puerto será 4032. Desde pc2 lanza el comando nc en modo cliente usando un puerto origen que comience por 20 y termine con los primeros dígitos de tu DNI. Como puerto destino usa el mismo que has empleado en el comando usado en pc4. Una vez lanzados ambos comandos, toma una captura de pantalla de los dos termines y adjúntalos como respuesta a esta pregunta. Todavía no hemos enviado el mensaje de texto

15. Desde pc2 escribe el mensaje "Hola, soy xxx", donde xxx son tus iniciales. Interrumpe el comando nc del ordenador pc2. Interrumpte la captura en r5, y adjunta pantallazos de los terminales de pc2 y pc4. ¿Se ha recibido en pc4 el mensaje enviado?

16. Abre la captura con Wireshark. Saca un pantallazo de todas las tramas recibidas y adjúntalo como respuesta a esta pregunta

17. Indica de entre todas las tramas capturadas cuáles son de apertura de la conexión, y cuáles de cierre

18. Busca la trama que envía los datos. Toma una captura de wiresark en la que se puedan ver los datos enviados de PC2 a PC4

19. Repite el experimento, pero ahora el comando nc del terminal pc2 debe conectarse al puerto destino 8000. Comienza una captura nueva, en el fichero udp2-xxx.cap (donde xxx son tus inciiales), envía el mensaje "Probando" (desde pc2 a pc4) y cierra la captura. Abre el fichero con wiresark y envía un pantallazo con las tramas capturadas

20. Explica cada una de las tramas, y qué es lo que ha sucedido. ¿PC4 ha recibido el mensaje?


## TCP

21. Partimos del mismo escenario anterior. Queremos enviar el mismo mensaje desde pc2 a pc4: "Hola, soy xxx", donde xxx son tus iniciales. Pero ahora usaremos el protocolo TCP. Arranca el comando tcpdump en r5 para realizar una captura en su interfaz eth0. Guárdalo en elfichero tcp-xxx.cap, donde xxx son tus iniciales. Lanza tcpdump y toma una captura del termina y adjúntala como resputa a esta pregunta

22. Lanza nc en PC4 en modo escucha, desde un puerto que comience por el número 40 y termine con los dos primeros dígitos de tu DNI (igual que en el apartado de UDP). Desde pc2 lanza el comando nc en modo cliente un puerto origen que comience por 20 y termine con los primeros dígitos de tu DNI. Como puerto destino usa el mismo que has empleado en el comando usado en pc4. Una vez lanzamos ambos comandos, toma una captura de pantalla de los dos termines y adjúntalos como respuesta a esta pregunta. Todavía no hemos enviado el mensaje de texto

23. Desde pc2 escribe el mensaje "Hola, soy xxx", donde xxx son tus iniciales. Interrumpe el comando nc del ordenador pc2. Interrumpte la captura en r5, y adjunta pantallazos de los terminales de pc2 y pc4. ¿Se ha recibido en pc4 el mensaje enviado?

24. Abre la captura con Wireshark. Saca un pantallazo de todas las tramas recibidas y adjúntalo como respuesta a esta pregunta

25. Indica de entre todas las tramas capturadas cuáles son de apertura de la conexión, y cuáles de cierre

26. Explica cada una de las tramas, y qué es lo que ha sucedido
