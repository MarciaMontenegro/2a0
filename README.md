# PERMANENTE 20A

 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
#INTEGRANTES:  

              JOAQUIN MUÑOZ RODRIGUEZ
              
              MARCIA MONETENEGRO CAVAGNARO
              
              JOSUE CARPIO PEÑA

 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
1.- PREGUNTA 1: Generar todos los primos de 3, 4 y 5 cifras.

    Utilizamos las siguentes funciones:
    
      -EXPMOD(a,x,n):
      
          Aplicamos exponenciacion modular.
          
      -ES_COMPUESTO(a, n, t, u):
      
          Determinamos si es un numero compuesto.
          
      -MILLER_RABIN(n,s):
      
          Determinamos si es un numero compuesto o pseudoprimo. 
          
  ---> Para generar los numeros de :
  
              3 cifras ---> Utilizamos un for con parametros que utilice por cada iteracion MILLER_RABIN; desde:100 - hasta:1000
              
              4 cifras ---> Utilizamos un for con parametros que utilice por cada iteracion MILLER_RABIN; desde:1000 - hasta:10000
              
              5 cifras ---> Utilizamos un for con parametros que utilice por cada iteracion MILLER_RABIN; desde:10000 - hasta:100000
              
 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
  -------> Utilizamos s=40, ya que para certificar un numero primo es necesario repetir la prueba MILLER_RABIN para disminuir la probabilidad de un error. 
 Seleccionamos este valor, de acuerdo con BRINCH HANSEN 92B.
 
 Un numero pequeño hace menos comprobaciones, es por esto que se debe poner un numero alto, pero no lo suficiente para que sea absurdo comprobar tantas veces.
 
 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
          
2.- PREGUNTA 2: Implementar un programa que genere de manera aleatoria al menos 10 primos distintos de 16, 32 y 64 bits.

    Utilizamos las siguentes funciones:
    
      -Nos basamos en las funcionas ya mencionadas, es por esto que las utilizamos dentro de las nuevas funciones:
      
        -RANDOMBITS(b)
        
        -RANDOMGEN_PRIMOS(b)
        
  ---> Para generar los 10 primos:
  
            Utilizamos un for con 10 iteraciones las cuales actuan segun el numero de bits que ingresamos, utilizando la funcion RANDOMGEN_PRIMOS(b).
            
------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------> Utilizamos s=40, debido a que al trabajar con numeros grandes por el numero de bits, nos parecio aceptable el tiempo de ejecucion aceptable , ademas de que se haga un correcto analisis y comprobacion de los numeros primos.
 Ademas, no es muy grande la probabilidad de que falle.

      
      
      
    
    
