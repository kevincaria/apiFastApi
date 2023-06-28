# apiFastApi
Mi primer acercamiento a FastApi

# API de Usuarios

Esta es una API de usuarios que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre usuarios. Proporciona endpoints para administrar usuarios, autenticación y generación de tokens de acceso.

## Requisitos funcionales

- **Registro de usuarios**: Los clientes pueden registrar nuevos usuarios proporcionando un nombre de usuario, correo electrónico y contraseña.
- **Inicio de sesión**: Pueden iniciar sesión utilizando su nombre de usuario y contraseña.
- **Obtener información de usuario**: Los usuarios autenticados pueden obtener información sobre su propio perfil.
- **Obtener lista de usuarios**: Pueden obtener una lista de todos los usuarios registrados.
- **Obtener usuario por ID**: Pueden obtener información detallada de un usuario específico mediante su ID.
- **Actualizar usuario**: Pueden actualizar su propia información de perfil, como el nombre de usuario y la dirección de correo electrónico.
- **Eliminar usuario**: Pueden eliminar usuarios registrados.

## Requisitos no funcionales

- **Seguridad**: La API debe garantizar la seguridad de los datos y la autenticación de usuarios mediante el uso de tokens de acceso y contraseñas cifradas.
- **Documentación**: La API debe estar documentada utilizando Swagger y Redocly para facilitar su comprensión y uso.
- **Pruebas unitarias**: Se deben desarrollar pruebas unitarias para garantizar la funcionalidad correcta de los endpoints y los casos de uso principales.