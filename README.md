# Testing-Python

En este repositorio voy a mostrar como testear una pila en Python. La importancia de testear radica en la confianza del producto con el cliente. Las ventajas son que permite probar que el programa funciona correctamente, se puede identificar variables que no existen o tipos esperados en las funciones y son una buena forma de documentar el código (no en forma directa, pero como los tests indican cómo es que se tiene que comportar el programa, viendo los tests se puede ver el resultado esperado para ciertas entradas del programa). Esto no excluye que se tenga que escribir la documentación del código.

Tenemos dos archivos que son los siguentes:

  * clasePila.py --> La clase pila junto con las funciones que vamos a testear
  * test.py --> Tenemos la clase TestPila que hereda de unittest. Cada metodo debe empezar con la palabra "test".
