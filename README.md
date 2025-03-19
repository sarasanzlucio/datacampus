
Sigue los pasos enumerados a continuación sobre este repositorio para completar la formación y evaluación del Data Campus BBVA - Analytics.

## 1. Clónate el repositorio en tu ordenador 
Para trabajar con este repositorio debes tener configurado tu API token. 

Si aún no lo has hecho, dirígete a tu perfil > API Token Authentication: 

![API Token authentication](api_token_auth.png)

Y genera un API Token con el botón "New API token". 

![New API Token](new_api_token.png)

De esta manera, a partir de ahora cuando tengas que autenticarte para realizar acciones sobre el repositorio como clonártelo (git clone) o subir cambios (git push) bastará con que introduzcas tu ID de accenture como nombre de usuario y tu API token como contraseña.

Finalmente, para clonarte el repositorio basta que te instales la aplicación [Git Bash](https://gitforwindows.org/) en tu ordenador para poder trabajar con Git fácilmente. Sitúate en el directorio de tu ordenador donde quieras ubicar este repositorio y abre la terminal de Git Bash donde ejecutarás el siguiente comando:

<code> git clone https://innersource.accenture.com/scm/~s.sanz.lucio/data_campus_bbva_wow.git</code>

Cuando ejecutes el comando se te abrirá automáticamente una nueva ventana de *Git Credential Manager* que te pedirá tu usuario y contraseña donde tendrás de introducir tu *ID de Accenture* y tu *API Token*.


## 2. Crea una rama 
Crea una nueva rama a partir de la rama actual cuyo nombre sea tu *ID de Accenture* para trabajar en ella.

## 3. Sitúate en tu rama y completa los ejercicios 
Sitúate en la rama que acabas de crear y dirígete a las carpetas:
- Ejercicios Engines
- Ejercicios Models
- Ejercicios QA

En cada una de estas carpetas encontrarás un Jupyter Notebook con los enunciados de los ejercicios correspondientes a cada módulo que deberás completar.

## 4. Haz commit y push de los cambios
Una vez hayas completado los ejercicios propuestos en el fichero ejercicios.py deberás subirlos al repositorio en la rama que acabas de crear de manera que estos sean visibles para su evaluación.

<code>git add <ejercicios_completados></code>

<code>git commit -m <Mensaje_de_subida></code>

<code>git push</code>