
Sigue los pasos enumerados a continuación sobre este repositorio para completar la formación y evaluación del Data Campus BBVA - Analytics.

## 1. Clónate el repositorio en tu ordenador 

El repositorio con el que trabajaremos se encuentra público en la plataforma [Github repository](https://github.com/sarasanzlucio/datacampus). 
De esta manera, podrás realizar acciones sobre el repositorio como clonártelo (git clone) o subir cambios (git push).

Finalmente, para clonarte el repositorio basta que te instales la aplicación [Git Bash](https://gitforwindows.org/) en tu ordenador para poder trabajar con Git fácilmente. Sitúate en el directorio de tu ordenador donde quieras ubicar este repositorio y abre la terminal de Git Bash donde ejecutarás el siguiente comando:

<code> git clone https://github.com/sarasanzlucio/datacampus.git </code>

Cuando ejecutes el comando se clonará este repositorio como una carpeta más en la ubicación que hayas seleccionado. Para empezar a trabajar sobre este puedes ubicarte en él con el siguiente comando:

<code>cd datacampus</code>

## 2. Crea una rama 
Crea una nueva rama a partir de la rama actual cuyo nombre sea tu *ID de Accenture* para trabajar en ella.

<code>git checkout -b <mi_id_accenture></code>

## 3. Sitúate en tu rama y completa los ejercicios 
Sitúate en la rama que acabas de crear y dirígete a las carpetas:
- Ejercicios Engines
- Ejercicios Models
- Ejercicios QA

En cada una de estas carpetas encontrarás un Jupyter Notebook con los enunciados de los ejercicios correspondientes a cada módulo que deberás completar.

Puedes consultar el estado de los ficheros que has modificado con respecto al repositorio ejecutando el siguiente comando:

<code>git status</code>

## 4. Haz commit y push de los cambios
Una vez hayas completado los ejercicios propuestos en el fichero ejercicios.py deberás subirlos al repositorio en la rama que acabas de crear de manera que estos sean visibles para su evaluación.

<code>git add .</code>

<code>git commit -m "<Mensaje_de_subida>"</code>

<code>git push</code>