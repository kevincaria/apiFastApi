# apiFastApi
Mi primer acercamiento a FastApi

# API de Usuarios

Esta es una API de usuarios que permite realizar operaciones CRUD sobre usuarios. Proporciona endpoints para administrar usuarios, autenticación y generación de tokens de acceso.

## Requisitos funcionales

- **Registro de usuarios**: Los clientes pueden registrar nuevos usuarios.
- **Inicio de sesión**: Pueden iniciar sesión con usuario y contraseña.
- **Obtener información de usuario**: Los usuarios autenticados pueden obtener información sobre su propio perfil.
- **Obtener lista de usuarios**: Pueden obtener una lista de todos los usuarios registrados.
- **Obtener usuario por ID**: Pueden obtener información de un usuario mediante su ID.
- **Actualizar usuario**: Pueden actualizar su propia información de perfil.
- **Eliminar usuario**: Pueden eliminar usuarios registrados.

## Requisitos no funcionales

- **Seguridad**: La API garantiza la seguridad de los datos y la autenticación de usuarios mediante el uso de JWT y Oauth2.
- **Documentación**: La API debe estar documentada utilizando Swagger (http://127.0.0.1:8000/docs) y Redocly (http://127.0.0.1:8000/redoc)
- **Pruebas unitarias**: Se deben desarrollar pruebas unitarias para garantizar la funcionalidad correcta de los endpoints y los casos de uso principales.
