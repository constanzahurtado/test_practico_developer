# test_practico_developer

Generalidades:

- Se crea un ambiente virtual, en donde se intala Django 4, junto con los requerimientos que se mencionan para cada tarea.
- Se realiza una conexión con Postgre para guardar los datos. 
- Se crea una cuenta de super usuario, en donde se pueden ver los modelos junto a sus datos guardados. 
- Las funciones en viwes fueron ejecutadas en consola: 
Para tarea 1:

python manage.py shell
>>from App.views import get_data_API
>>get_data_API()

Para tarea 2:
>>python manage.py shell
>>from App.views import web_scrapping()
>>web_scrapping()

>>python manage.py shell
>>from App.views import get_data_json
>>get_data_json()

tarea 1:
requerimientos: biblioteca requests
En esta se obtiene los datos de la API indicada a través de la biblioteca requests, y a través de sus llaves se obtiene cada dato, se guardan en base de datos
Postgres y se despligan los datos en la página tarea1.html, principalmente las estaciones.  

tarea 2:
requerimietos: biliotecas selenium, pandas y json
Selenium es utilizado para obtener los datos del sitio web (Web Scrapping), pandas para crear un dataframe para se convertido posteriormente en un archivo json. 
Los datos de este archivo son guardados en la base de datos. 

'C:/proyectos/PruebaTecnica/Proyecto/App/mydata.json'
