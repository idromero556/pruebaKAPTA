# pruebaKAPTA

Se utilizó python versión 3.6.8.

En el settings deben colocarse las credenciales para la base de datos en postgres y la apikey not secured de freedcamp.

Luego en la terminal se coloca python manage.py makemigrations.

Luego en la terminal se coloca python manage.py migrate.

Para correrlo se usa el comando python manage.py runserver.

Para poblar la BD con la información de freedcamp, usar el link localhost/freedcamp/listarProyectos/

y el link de las tareas(para cada id de proyecto): localhost/freedcamp/verListasTareas/<id_proyecto>/

Luego ingresar a para navegar la aplicación: localhost/freedcamp/


#Modelo base de datos
![alt text](https://www.lucidchart.com/publicSegments/view/b0631609-07d1-4683-bf98-26d020160ca6/image.png)

