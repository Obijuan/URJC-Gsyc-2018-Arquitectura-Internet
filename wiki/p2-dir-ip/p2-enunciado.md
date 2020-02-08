![](https://github.com/Obijuan/URJC-Gsyc-2018-Arquitectura-Internet/raw/master/wiki/p2-dir-ip/Portada/Portada.png)

### Febrero de 2020
-----

## Contenido

1. [Configuración de direcciones IP: comando ifconfig](https://github.com/Obijuan/URJC-Gsyc-2018-Arquitectura-Internet/wiki/Practica-2:-Direcciones-IP#1-configuraci%C3%B3n-de-direcciones-ip-comando-ifconfig)
2. [Capturando y analizando tráfico](#2-capturando-y-analizando-tr%C3%A1fico)  
3. [Configuración de direcciones IP mediante ficheros de configuración](#3-configuraci%C3%B3n-de-direcciones-ip-mediante-ficheros-de-configuraci%C3%B3n)  
4. [Configurando un rúter](#4-configurando-un-r%C3%BAter)  


# Práctica 2: Direcciones IP

## Resumen

El **nivel de red** se encarga de que máquinas que están en **subredes diferentes**, y que por tanto **NO** comparten el mismo medio físico, se puedan comunicar entre sí. En esta práctica aprenderemos a configurar las **interfaces de red** de las máquinas para trabajar a nivel de red y comprobaremos la interconexión entre ellas usando el **comando ping**

**IMPORTANTE**: Toma nota de todo lo que hagas en un cuaderno de laboratorio, ya sea en papel o en formato electrónico. En él deberı́a constar lo que vas aprendiendo en cada apartado de la práctica, los pasos que has tenido que ir dando para obtener los resultados pedidos, los comandos que has empleado, las respuestas a las preguntas que se realizan en el enunciado, y cualquier otra información que consideres oportuna. Este cuaderno de laboratorio te será muy útil para repasar lo aprendido

## 1. Configuración de direcciones IP: comando ifconfig

Partiremos de un escenario que ya conocemos: **tres ordenadores** que comparten un mismo **medio físico**. Es lo que conocemos como una **red de área local** o una **subred**. Internet se construye mediante la **interconexión** de muchas subredes a través de unos elementos llamados **rúters** (que son también ordenadores)

1. Arranca **Netgui** y construye esta **subred**, formada por los tres odenadores pc1, pc2 y pc3

![](https://github.com/Obijuan/URJC-Gsyc-2018-Arquitectura-Internet/raw/master/wiki/p2-dir-ip/red-local-01.png)

* Cada máquina tiene una **interfaz de red** por donde se comunica con el resto de máquina. Esta interfaz tiene una **dirección física**, que ya conocemos, que le permite intercambiar información con las máquinas que comparten **su mismo medio físico** (las máquinas de su propia subred). Ya hemos trabajado con las direcciones físicas en las prácticas anteriores

* Además, cada interfaz de red tiene una **dirección IP**, que le permitirá comunicarse con **cualquier máquina** de toda la red, situada en cualquiera de las **subredes** que la componen. Por supuesto, con las direcciones IP tambień se comunican las máquinas de su propia subred (mismo medio físico)

* En la subred que hemos creado, asignaremos a cada **interfaz de red** de cada máquina su propia **dirección IP**. Utilizaremos las siguientes:

| Máquina | Interfaz de red | Dirección IP |
|---------|-----------------|--------------|
|  pc1    | eth0            | 10.0.100.1   |
|  pc2    | eth0            | 10.0.100.2   |
|  pc3    | eth0            | 10.0.100.3   |

* Las direcciones IP se dividen en **dos partes**: la primera es la **dirección de la subred**. Cada subred tiene su propio identificador. La segunda es la dirección de la propia interfaz de red de la máquina en cuestión

* Para configurar la dirección IP de la interfaz de una máquina necesitamos dos parámetros: La **dirección IP** completa y la **máscara de red**. La máscara de red nos sirve para obtener la dirección de la propia Subred. En la subred que hemos creado, la **máscara de red** será **255.255.255.0**

2. **Arrancar** las tres máquinas, una a una. Empezamos configurando la **dirección IP** de **pc1**

* Desde la **terminal** de pc1, ejecuta el **comando ifconfig**. ¿Cuántas interfaces de red están activas?
* Para configurar su **dirección IP**, debemos indicar la propia dirección IP de su interfaz eth0 y la **máscara de red**. Ejecutamos el comando ifconfig con estos parámetros:

```
ifconfig eth0 10.0.100.1 netmask 255.255.255.0
```
* Ejecuta de nuevo el **comando ifconfig sin parámetros**. ¿Cuantas interfaces de red están ahora activas?
* Localiza en la salida del comando ifconfig la **interfaz eth0** y mira su **dirección física**, su **dirección IP** y su **máscara de red**
* Siempre que necesites saber si una interfaz está o no configurada, y qué dirección IP y máscara de red se le han asignado, deberás usar *ifconfig*
* Observa que en la **interfaz gráfica de netgui**, cuando una máquina está **correctamente configurada** podremos ver en azúl su **dirección IP**, y en verde su **interfaz de red**

![](https://github.com/Obijuan/URJC-Gsyc-2018-Arquitectura-Internet/raw/master/wiki/p2-dir-ip/red-local-02.png)

3. El **comando ping** lo usamos para comprobar si hay **conectividad entres máquinas**. También lo podemos usar con la propia máquina, para saber si está bien configurada. Desde el terminal de pc1 ejecutamos el siguiente comando:

```
ping 10.0.100.1
```
Nos deberá aparecer algo como esto:

```
pc1:~# ping 10.0.100.1
PING 10.0.100.1 (10.0.100.1) 56(84) bytes of data.
64 bytes from 10.0.100.1: icmp_seq=1 ttl=64 time=0.024 ms
64 bytes from 10.0.100.1: icmp_seq=2 ttl=64 time=0.024 ms
64 bytes from 10.0.100.1: icmp_seq=3 ttl=64 time=0.024 ms
64 bytes from 10.0.100.1: icmp_seq=4 ttl=64 time=0.029 ms
64 bytes from 10.0.100.1: icmp_seq=5 ttl=64 time=0.027 ms
64 bytes from 10.0.100.1: icmp_seq=6 ttl=64 time=0.025 ms
64 bytes from 10.0.100.1: icmp_seq=7 ttl=64 time=0.024 ms
64 bytes from 10.0.100.1: icmp_seq=8 ttl=64 time=0.025 ms
...
```

Pulsamos **Ctrl-c** para terminar. Lo que hace el comando ping es enviar un mensaje a la dirección IP indicada y esperar la respuesta. En este caso estamos haciendo ping "a nosotros mismos". Desde pc1 enviamos un mensaje a pc1. En cada línea vemos el tiempo de respuesta: el tiempo en milisegundos que ha tardado el mensaje en ir y volver

* Desde **pc1**, ejecuta el comando ping usando la **dirección IP de pc2**:

```
ping 10.0.100.2
```

¿Qué sucede? ¿Por qué crees que pasa eso?

4. Sitúate en la terminal de pc2. Ejecuta un ping a la propia dirección de pc2

```
pc2:~# ping 10.0.100.2
```
¿Qué sucede?

Prueba también con un **ping a pc1**, desde el terminal de pc2

```
pc2:~# ping 10.0.100.2
```

¿Qué sucede?

5. Los **errores** que han sucedido en los apartados anteriores son debidos que **no hemos configurado** la dirección IP de pc2, todavía. Antes de poder comunicar las máquinas es necesario que estén bien configuradas. Ve al **terminal de pc2** y configura su **dirección IP** y **máscara de red** con el comando ifconfig que ya conocemos:

```
pc2:~# ifconfig eth0 10.0.100.2 netmask 255.255.255.0
```
* Haz un ping desde pc2 al propio pc2. ¿Qué sucede ahora?
* Haz un ping desde pc2 a pc1. ¿Hay conectividad?
* Ve al terminal de pc1, y haz un ping desde pc1 a pc2. Antes no había conectividad. ¿Qué ocurre ahora?

6. Seguimos experimentando. ¿Qué debería ocurrir si desde pc2 hacemos un ping a pc3?. Ejecuta el comando para comprobarlo
* Ve al terminal de **pc3** y configura su dirección IP y su máscara de red
* Ejecuta comandos **ping** hacia pc1 y pc2. ¿Hay conectividad?
* Comprueba lo mismo a la inversa: desde pc1 haz ping a pc3. ¿Hay conectividad?
* Comprueba la conectividad de pc2 a pc3

Desde la **interfaz gráfica de Netgui** podemos comprobar los ordenadores que están configurados, viendo sus **direcciones IP**:

![](https://github.com/Obijuan/URJC-Gsyc-2018-Arquitectura-Internet/raw/master/wiki/p2-dir-ip/red-local-03.png)

## 2. Capturando y analizando tráfico

Ya sabemos cómo **configurar** las **direcciones IP** de las interfaces de red de las máquina de una **subred**, y también sabemos **cómo generar tráfico** con el **comando ping** para comprobar la **conectividad** entre las máquinas

También sabemos cómo **capturar el tráfico** de una subred con el **comando tcpdump**

1. Usaremos la **misma subred** del aparatado anterior, configurada con las mismas direcciones IP. Vamos a **capturar el tráfico** de la subred desde **pc3**. Nos vamos al terminal de pc3 y lanzamos el **comando tcpdump** para iniciar una captura en el fichero **captura1.cap**:

```
pc3:~# tcpdump -i eth0 -s 0 -w /hosthome/captura1.cap
```

Ahora nos vamos a **pc1** y hacemos un **ping a pc2** y otro a pc3. El **parámetro -c** nos permite indicar el número de pings a realizar. Por defecto, si no se especifica este parámetro se hacen pings indefinidamente hasta que pulsemos Control-C. Lanzamos 2 pings de pc1 a pc2:

```
pc1:~# ping 10.0.100.2 -c 2
```

y otros dos de pc1 a pc3:

```
pc1:~# ping 10.0.100.3 -c 2
```

Finalizamos la captura en pc3 y abrimos el fichero **captura1.cap** con **wireshark**, desde el ordenador del laboratorio

* ¿Cuantos paquetes se han capturado en total? (Ignora los que ponga protocolo ARP, si hubiese alguno)
* Fíjate en la trama 1. ¿Cuántos protocolos se han detectado y a qué nivel pertenecen?
* ¿Cuál es la dirección IP origen y la IP destino de este paquete?
* Localiza en la trama el campo con la IP origen. ¿En qué protocolo está?
* Localiza el primer paquete de respuesta de pc2 a pc1
* A parte de las direcciones IP origen y destino, busca el campo del protocolo ICMP que permite diferenciar los mensajes de solicitud de los mensajes de respuesta. ¿Qué valor tiene para los mensajes de solicitud? ¿Y para los de respuesta?

## 3. Configuración de direcciones IP mediante ficheros de configuración

Aprenderemos a **configurar** un escenario de red de manera que las **direcciones IP** se queden de forma **permanente**. Con el comando *ifconfig* hacemos configuraciones en caliente, para realizar pruebas. Pero si reiniciamos las máquinas, esta configuración **se pierde**. Para que sea **permanente** debemos modificar algunos **archivos del sistema**

* Partimos del escenario anterior. **Apaga** todas las máquinas, una a continuación de la otra, y vuelve a **encenderlas**
* Haz un ping de pc1 a pc2. ¿Qué sucede?
* Comprobamos que la configuración de las direcciones IP se ha **perdido**. Para establecer la configuración de forma **permanente** hay que modificar el archivo **/etc/network/interfaces** de cada máquina. Es ahí donde pondremos los datos de la **IP** y la **máscara de red**
* Desde **pc1** editamos el fichero /etc/network/interfaces con el programa **mcedit**:

```
 mcedit /etc/network/interfaces
```
Añadimos las siguientes líneas:

```
auto eth0
iface eth0 inet static
    address 10.0.100.1
    netmask 255.255.255.0
```
Con ellas establecemos la **dirección IP**, la **máscara de red** y configuramos **eth0** para que arranque **automáticamente** al iniciarse el ordenador

Ahora **guardamos** el fichero (F2) y salimos del mcedit (F10)

* Ya lo tenemos configurado, pero todavía NO ha tenido efecto. Para que se active debemos bien iniciar la máquina o bien ejecutar este comando:

```
pc1:~# /etc/init.d/networking restart
```

Al cabo de unos segundos veremos cómo aparece la dirección IP en la **interfaz de Netgui**. Y podemos comprobar que ya sí hay conectividad entre de pc1 a pc1. Todo está bien configurado

En caso de que no hayamos escrito bien la configuración en el fichero /etc/network/interfaces, al ejecutar el comando networking nos aparecerá algún **mensaje de error** parecido a este:

```
pc1:~# /etc/init.d/networking restart
Reconfiguring network interfaces...Don't seem to be have all the variables for eth0/inet.
Failed to bring up eth0.
done.
```
2. Repetimos el proceso para el ordenador **pc2**, pero usando su dirección IP. Editamos le fichero /etc/network/interfaces y luego ejecutamos el programa /etc/init.d/networking restart

* Haz un ping de **pc2 a pc2** para comprobar que está todo bien configurado
* Comprueba la conectividad entre **pc1 y pc2**. El ping debería funcionar en ambos sentidos

3. Repite el proceso para **pc3**, usando su dirección IP

* Comprueba que hay conectividad con **pc1 y pc2**, mediante el comando ping

4. **¡Nuestra subred está configurada!**. Ahora **apagamos** las máquinas. Y las volvemos a **arrancar de nuevo**. Al cabo de unos segundos, tras el arranque, vemos que aparecen las **direcciones IP** que habíamos previamente configurado. Nuestros equipos ya **recuerdan** la configuración, y se configuran automáticamente al arrancar

* Comprueba que hay **conectividad** entre las máquinas, usando el comando **ping**

## 4. Configurando un rúter

1. Crear el siguiente **escenario de red**, que es una ampliación del anterior

![](https://github.com/Obijuan/URJC-Gsyc-2018-Arquitectura-Internet/raw/master/wiki/p2-dir-ip/red-01.png)

* Tenemos la **subred** anterior, formada por los ordenadores pc1, pc2 y pc3. Hay una **subred nueva**, compuesta por los ordenadores **pc4** y **pc5**. Ambas subredes están **interconectadas** mediante el **rúter r1**
* Nos fijamos que el rúter tiene **2 interfaces** de red: **eth0** y **eth1**. Con eth0 se conecta a la primera subred, y con eth1 a la segunda

2. El rúter tiene **2 direcciones IP**, una para cada una de sus interfaces. En estas tablas se ha resumido toda la información de cada una de las subredes

#### Subred 10.0.100.0

* **Máscara de red**: 255.255.255.0

| Máquina | Interfaz de red | Dirección IP |
|---------|-----------------|--------------|
|  pc1    | eth0            | 10.0.100.1   |
|  pc2    | eth0            | 10.0.100.2   |
|  pc3    | eth0            | 10.0.100.3   |
|  r1     | eth0            | 10.0.100.100 |

#### Subred 20.0.100.0

* **Máscara de red**: 255.255.255.0

| Máquina | Interfaz de red | Dirección IP |
|---------|-----------------|--------------|
|  pc4    | eth0            | 20.0.100.4   |
|  pc5    | eth0            | 20.0.100.5   |
|  r1     | eth1            | 20.0.100.100 |

3. **Arranca** todas las máquinas, incluido el rúter (el rúter es un ordenador más cualquiera). Configura las **direcciones** IP de los ordenadores **pc4** y **pc5**, usando **ficheros de configuración**. Comprueba que hay comunicación entre pc4 y pc5

* En el **escenario de netgui** deberías ver todas las IPs, salvo la del rúter, ya que todavía no lo hemos configurado

![](https://github.com/Obijuan/URJC-Gsyc-2018-Arquitectura-Internet/raw/master/wiki/p2-dir-ip/red-02.png)

4. Vamos a **configurar el rúter**. Como tiene **2 interfaces de red**, habrá que crear **dos configuraciones** en el fichero **/etc/network/interfaces**, una para **eth0** y otra para **eth1**

* Configura primero el **interfaz eth0** de **r1**, que está conectado a la subred 10.0.100.0. Hazlo como si se tratase de un ordenador cualquier, exactamente igual que has configurado los otros pcs

* Comprueba que desde **pc1** hay **conectividad con el rúter**, en ambos sentidos
* Lo mismo desde **pc2** y **pc3**. Tienen **conectividad con el rúter**. Compruébalo

5. Ahora configuramos la otra interfaz del rúter: **eth1**, que está conectada a la **subred 20.0.100.0**. Basta con que **añadamos** la siguiente información en el fichero **/etc/network/interfaces**:

```
auto eth1
iface eth1 inet static
    address 20.0.100.100
    netmask 255.255.255.0
```

* Ejecutamos el comando /etc/init.d/networking restart. Y comprobamos que hay conectividad entre r1 y pc4, así como entre r1 y pc5
* En nuestro **escenario de Netgui** veremos las **dos direcciones** IP del rúter

![](https://github.com/Obijuan/URJC-Gsyc-2018-Arquitectura-Internet/raw/master/wiki/p2-dir-ip/red-03.png)

6. El rúter, al estar conectado a ambas subredes, **comparte medio físico** con todos los ordenadores. Por tanto tiene conectividad con todos ellos. Desde **r1**, comprueba que puedes hacer **ping** a **pc1**, **pc2**, **pc3**, **pc4** y **pc5**

7. Desde el terminal **pc1**, haz un **ping** a **pc4**. ¿Qué ocurre? ¿Qué mensaje te sale?

8. Esto lo resolveremos en las prácticas siguientes. La razón por la que pc1 no llega a pc4 es porque **pc1 no conoce la red 20.0.100.0**. Y no sabe a **quién** debe enviar el paquete para alcanzar el destino (No sabe que existe r1, que está conectado a ambas redes)

9. Desde **r1**, ejecuta el comando **ifconfig** para ver todas sus interfaces activas
