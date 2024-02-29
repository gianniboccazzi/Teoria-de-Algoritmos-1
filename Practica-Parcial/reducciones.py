#Se requiere realizar un viaje a través de un territorio de difícil acceso. 
#El mismo se encuentra dividido en zonas por las que se debe pasar. 
#Existen m facciones que controlan algunas de esas zonas. 
#Una facción puede controlar más de 1 zona y una zona puede ser controlada por más de una. 
#Para poder realizar el viaje se debe pactar con alguna de estas. 
#Cada pacto con una facción nos asegura el paso seguro por todas las zonas que controlan independientemente de si alguna de sus zonas son 
#también controladas por otras facciones. 
#Deseamos saber si es posible pactar con no más de k facciones para poder concretar el viaje de forma segura.
#Se pide: Demostrar que el problema es NP-Completo.
#HINT: Se puede utilizar Vertex Cover.



#Para demostrar que el problema es NP Completo, primeramente debe estar en NP
#Esto se resuelve facilmente, ya que se verifica cada zona viendo si en la solución
#alguna de las facciones la cubre. siendo O(k*z), polinómico.

#luego, cada vertice del grafo será una facción, y cada arista será una zona, blablabla.







# #Un instituto de enseñanza debe coordinar las fechas de exámenes finales de sus respectivos cursos.
#  En cada curso se anotaron
# #varios alumnos. Y un alumno puede estar en varios cursos. En total se cuenta con "k" fechas
#  posibles de examen. Se desea generar un
# #procedimiento eficiente para decidir si es posible cumplir con ese requerimiento. En caso 
# afirmativo, dar una posible asignación de
# #exámenes por fecha. Se pide: Demostrar que el problema es NP-Completo.
# #HINT: Se puede utilizar K-coloreo de grafos.


#Primero, para que sea NP completo, debe estar en NP. Esto significa que debe poder
#validarse en tiempo polinomial. Esto se facil ya que se debe recorrer cada curso
#y ver cuantos tienen interseccion de alumnos. Se realiza eso por cada curso y si es <=k
#es correcto. Esto seria polinomial

#La reduccion consiste en poner a  cada vertice como un curso y a cada arista como 
#un alumno perteneciente a ese curso. De esa forma funciona.






# La organización de un workshop internacional debe coordinar las
#fechas de paneles de exposición. En cada panel se presentan un
#conjunto de oradores. Un orador puede estar en varios paneles. Se
#cuenta con un total "j" jornadas diferentes donde se pueden
#establecer paneles. Se desea generar un procedimiento eficiente
#para decidir si es posible cumplir con cumplir con todos los
#paneles con todos sus oradores. En caso afirmativo, dar una
#posible asignación de paneles por jornada.
#Se pide: Demostrar que el problema es NP-Completo.
#HINT: Se puede utilizar K-coloreo de grafos.


#Mismo que el anterior, los paneles son los vertices y los oradores las aristas











# Para un evento a realizar se requiere conformar una selección
# musical entre el conjunto A de "n" canciones. Podemos enumerar a
# los elementos de A como a1,a2,...,an. Por otra parte, contamos con
# un conjunto "B" de "m" personas. Cada una de ellas con un subsets
# de esas canciones que le gustan. Deseamos saber si podemos
# seleccionar un subconjunto de no más de "k" canciones, de tal
# forma que existe al menos 1 canción que le gusta a cada uno.
# Se pide: Demostrar que el problema es NP-Completo.
# HINT: Se puede utilizar Vertex Cover.

#Es hitting set problem, por cada arista se crea una persona y sus canciones seran
#los dos vertices de dicha arista.





# Un almacén registra en una matriz qué productos compra cada uno de sus clientes. 
# Un conjunto de clientes es diverso si cada uno de ellos compra cosas diferentes (tiene
#  intersección vacía con lo que compran los demás). Definimos al problema de los clientes
# diversos como: Dada una matriz de registro, de tamaño m (clientes) x n (productos), y un
# número k<=m, ¿existe un subconjunto de tamaño al menos k de los clientes que sea diverso? 
# Probar que el problema es NP-completo. Sugerencia: Reducir polinomialmente conjuntos 
# independientes a clientes diversos.



#Está en Np ya que por cada cliente de la solución, se puede ver si comparte algun producto en comun
#Lo cual es polinómico. O(N²) en el peor de los casos
#LA reduccion consiste en que los vertices van a ser los clientes y las aristas los productos.






# Nos piden que organicemos una jornada de apoyo de estudio para exámenes. Tenemos que poder dar
# apoyo a "n" materias y hemos recibido currículos de "m" postulantes para ser potenciales ayudantes. 
# Cada ayudante puede ayudar en un determinado subconjunto de materias. Para cada una de las 
# materias hay un subconjunto de postulantes que pueden dar apoyo en ella. 
# La pregunta es: dado un número k < m, ¿es posible seleccionar a lo sumo "k" ayudantes de modo 
# tal que siempre haya un ayudante que pueda dar consultas en alguna de las n materias? 
# Este problema se llama Contratación Eficiente. Probar que "Contratación Eficiente" es NP-completo. Sugerencia: se puede tratar de usar Cubrimiento de Vértices.


#HITTING SET PROBLEM


