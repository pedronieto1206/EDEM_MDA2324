# ¿Nos hacemos ricos?

<div align=center><img src=https://territoriocat.files.wordpress.com/2014/07/gifs-animados-tio-gilito-1287111.jpg /></div>

A caminar se aprende andando por lo que, la idea de este proyecto es daros la oportunidad de afrontar un reto según vayáis adquiriendo conocimientos durante el master. El objetivo, es que al finalizar el master, seáis capaces de afrontar un problema real, desde la definición del problema, hasta la entrega de una solución y de paso que si podemos nos hagamos ricos con ello.

## ¿En qué consiste el reto?

Si tenemos que elegir una manera de hacerse ricos, seguramente todos penséis en la loteria pero... no hay manera de predecir los números de la loteria, ¿o sí?. Bueno en este reto no intentaremos predecir los números ya que estos asumiendo que el juego está bien hecho son equiprobables.

El objetivo de este reto es predecir la jornada de la quiniela de fútbol.

<div align=center><img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfDLOz9oD7Cjbtj2imXph3CrwbPCWCKmC4o0px3UG-x2ZEYLAFpk6IpfJECFs5x5Qr3eI&usqp=CAU /></div>

Para ello, trabajaremos todos para predecir cada semana en base a los datos y estratégias que definamos la jornada de la quiniela. 

## ¿Cómo se organizará el reto?

En este repositorio hay un código que una vez a la semana se ejecutará y generará un resultado, este resultado será la predicción de la jornada de la quiniela. Para ello debemos de dotar al código de la lógica necesaria para que sea capaz de predecir la jornada de la quiniela. 

Ahora mismo tenemos una fase inicial que es que el código simplemente hace un random de 15 resultados, es decir, 15 resultados aleatorios de 1, X o 2. 

Pero más adelante quizá podamos hacerlo mejor...

- Recuperando datos de partidos anteriores
- Recuperando datos de jugadores
- Recuperando datos de entrenadores
- Recuperando datos de la prensa
- Recueprando datos de casas de apuestas
- Usando machine learning
...

## ¿Cómo se organizará el reto?

En este reto usaremos las discussions de github para organizar el reto, donde cada uno de vosotros es libre de crear una discusión sobre el tema que queráis, por ejemplo, si queréis proponer una estrategia de predicción, podéis crear una discusión con el título "Estrategia de predicción: XXXX" y en el cuerpo de la discusión explicar la estrategia que proponéis.

Una vez que la estrategia la tengáis clara, debéis crear una rama y hacer una PR sobre la carpeta PetProject. Para realizar esta estrategia será obligatorio lo siguiente:

- Hacer una PR explicando vuestra estratégia y el código que la implementa
- Crear una carpeta dentro de DATA con los datos que aportáis para la estrategia
- Ejecutar vuestra estratégia contra el histórico para ver que tal funciona

## ¿Cómo se evaluará el reto?

La estrategía se evaluará de la siguiente manera. Primero cargaremos un histórico de resultados y ejecutaremos vuestra estrategia contra el histórico. Una vez ejecutada la estrategia, se evaluará el resultado de la estrategia contra el histórico y se calculará el porcentaje de acierto de la estrategia. 

Si la estrategia es mejor que la actual, sobretodo para los últimos años, nos la quedamos!!

## Y qué hacemos con los resultados...

Pues una vez que tengamos una estrategia que funcione, la usaremos para predecir la jornada de la quiniela y si acertamos, nos haremos ricos!! Una vez a al semana yo realizaré la apuesta y si ganamos, repartiremos los beneficios entre todos los que hayan participado en el reto.
