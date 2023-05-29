

# CI-CD project

Este proyecto es una aplicación web que implementa un sistema de registro y inicio de sesión utilizando tecnologías como Node.js, MySQL y Docker. Proporciona una API para registrar usuarios y realizar el inicio de sesión con validación de credenciales.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:

- Docker: [Instrucciones de instalación](https://docs.docker.com/get-docker/)
- Docker Compose: [Instrucciones de instalación](https://docs.docker.com/compose/install/)

## Configuración

1. Clona este repositorio en tu máquina local:
      git@github.com:juanesvelez/ci-cd.git


2. Accede al directorio del proyecto:
      cd ci-cd
 
3. Crea un archivo `.env` en el directorio raíz del proyecto y configura las variables de entorno necesarias.


4. Actualiza las variables de entorno en el archivo `.env` según sus preferencias. Asegúrate de proporcionar la configuración adecuada para la conexión a la base de datos MySQL.

## Uso

5.  Abre una terminal y ejecuta el siguiente comando para construir las imágenes de Docker y levantar los contenedores:

    docker-compose up

    Esto iniciará los contenedores de la base de datos MySQL y el backend de la aplicación.

6. Una vez que los contenedores estén en funcionamiento, podrás acceder a la aplicación desde postman en la siguiente dirección:

    http://localhost:3000

	Ejemplo de uso:	
	
    1. Este endpoint es usado parara realizar la creacion de usuario http://localhost:3000/register.

	

			{

			"email":  "juanesvelez@otro.com",

			"password":  "clavesupersecret"

			}    
    
    2. Este endpoint es usado para el inicio de sesion del usuario
	    http://localhost:3000/login
		
				{

			"email":  "juanesvelez@otro.com",

			"password":  "clavesupersecret"

			}    
		
 
    
 ## Video explicativo
    
    https://poligran-my.sharepoint.com/:v:/g/personal/juvelezm3_poligran_edu_co/Eb-lVHBRNfxGm8qIlSZG8VkBB4BRo9bK8rSJgKcMrZgHEA?e=SZEzli
    

 
