# InstaFollower

Este script de Python utiliza Selenium para automatizar interacciones en Instagram, como seguir y dejar de seguir a los seguidores de una cuenta específica.

## Requisitos

- Python 3.x
- Selenium
- WebDriver (en este caso, se utiliza ChromeDriver)

## Instalación

1. Instala Python 3.x desde [python.org](https://www.python.org/downloads/)
2. Instala Selenium usando pip: pip install selenium
3. Descarga el WebDriver correspondiente para tu navegador (en este caso, se utiliza ChromeDriver) y asegúrate de añadirlo al PATH del sistema.

## Uso

1. Abre el archivo `instafollower.py` en un editor de texto.
2. Modifica las variables `similiar_account`, `USERNAME` y `PASSWORD` con la cuenta que deseas analizar y tus credenciales de inicio de sesión de Instagram.
3. Ejecuta el script `instafollower.py` desde tu terminal o IDE de Python.

## Funcionalidades

- **login()**: Inicia sesión en Instagram.
- **find_followers()**: Busca y carga la lista de seguidores de la cuenta especificada.
- **follow()**: Sigue a los usuarios que aparecen en la lista de seguidores cargada.
- **unfollow()**: Deja de seguir a los usuarios que aparecen en la lista de seguidores cargada.

## Aviso Legal

Este script se proporciona únicamente con fines educativos y de aprendizaje. El uso de este script para automatizar acciones en Instagram puede violar los términos de servicio de Instagram. Úsalo con responsabilidad y bajo tu propio riesgo.

## Créditos

Este script fue creado por Rafael Grande y se basa en el módulo Selenium para Python.


