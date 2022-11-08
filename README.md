
- Se creará un contenedor con el estado activo (up), este contenedor tiene un cron que cada 1 hora ejecuta un script python

- El script realiza lo siguiente:

   A través de la API obtiene los datos del servicio de clima 
   
		(Cumplimiento de punto 1: Consumir cada hora del servicio)
   
   La infomación que obtiene cada hora lo almacena en un archivo con extensión CSV dentro de la "data"  
   
   El formato de los archivos generados es: YYYYmmdd_HH.csv
   
             YYYY 	representa el año
			 mm 	representa el mes
			 dd     representa el día
			 HH		representa la hora (formato 24 horas)
			
		(Cumplimiento de punto 2: Almacenar información historica/actual)
			 
	Se unen los resultados de las dos ultimas horas (correspondiente a los 2 ultimos CSV's), y se promedian las temperaturas máximas y mínimas agrupadas por el municipio 
	
		(Cumplimiento de punto 3: tabla por municipio de promedios de temperaturas)

     Para dejar en evidencia el punto 3 se almacena en un archivo con extensión CSV dentro de la "avg"
	 
	 Cuando se tiene el resultado de los promedios de las dos ultimas horas por municipio, se ha realizado un left join con la ultima actualizacion de archivo dentro la carpeta que  
	 me compartieron "data_municipios", esto lo realizo buscando buscando la fecha más reciente ya que los nombres de las carpetas estan con una nomenclatura de tipo fecha,
	 He tomado como campo de union "idmun" (Id de estado) e "ides" (Id de municipio) con las columnas de los archivos "Cve_Ent" (Id Estado) "Cve_Mun" (Id Municipio) 
	 El resultado de esto se deja en una carpeta llamada "current" 
	 
	    (Cumplimiento de punto 4:  Se une la tabla por municipio de temperaturas con el último archivo )

El repositorio esta en github de acceso publico

		https://github.com/jamirhuamancampos/reto_dd360
		
		Para descargar:

		$ git clone -b main https://github.com/jamirhuamancampos/reto_dd360

		(Cumplimiento de punto 5)

La solucion fue entregada con Docker y Docker Compose 

		(Cumplimiento de punto 6)
		
La cuenta con logs:

		Los logs que se genereran son por hora en la carpeta: /var/logs/app/

		(Cumplimiento de punto 6)		
		
Forma de ejecución:

	# se creará el contenedor que estara en modo activo (up)
	$ docker-compose up --build -d
	
	# para ingresar al contenedor y verificar la carpeta de archivos (todo se crea dentro de la carpeta de la aplicacion: /usr/app/src)	
	$ docker exec -i -t $(docker ps --format '{{.Names}}' --filter="ancestor=reto_dd360_python:latest") bash
	
	Si se desea ejecutar de forma manual y no esperar el resultado cada una hora
	$ python3.9 /usr/app/src/app.py >> /var/log/app/$(date +'%Y-%m-%d-%H').log

##################################################
