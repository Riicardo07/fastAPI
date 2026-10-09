# OpenSpec 04: Refactorización por Capas, Documentación y Cierre

## 1. Contexto y Objetivos
- Refactorizar el código para asegurar una arquitectura modular y desacoplada (Routers -> Services/DAO -> Models/DB).
- Evitar consultas directas a la base de datos dentro de los endpoints de FastAPI.
- Completar la documentación profesional del proyecto en el README.md para entrega y currículum.

## 2. Requerimientos de Refactorización
- Capa Repositories / DAO: Centralizar las queries de SQLAlchemy para catálogo y pedidos (\pp/repositories/\).
- Capa Services: Contener las validaciones de negocio (comprobación estricta de la Mesa 7, verificación de existencia de producto y tipo) (\pp/services/\).
- Capa Routers: Únicamente reciben peticiones HTTP, invocan servicios mediante \Depends\ y retornan esquemas Pydantic (\pp/routers/\).

## 3. Documentación del README.md
El README debe incluir:
- Descripción del proyecto y contexto del restaurante.
- Tecnologías empleadas (FastAPI, SQLAlchemy, PyMySQL, Pydantic, MySQL).
- Instrucciones claras de instalación con entorno virtual.
- Variables requeridas en el archivo .env (basadas en .env.example).
- Instrucciones para arrancar el servidor en local.
- Resumen de endpoints disponibles (Catálogo, Mesas y Pedidos de la Mesa 7) con ejemplos de petición/respuesta.

## 4. Criterios de Aceptación
1. El servidor arranca sin errores de importación circular o dependencias rotas.
2. Todos los endpoints siguen funcionando exactamente igual en /docs.
3. Se mantiene intacta la restricción: la creación y consulta de pedidos solo se permite en la Mesa 7.
4. README.md redactado en español, claro y completo.
5. Fusión (merge) de las ramas a la rama 'main' y subida limpia a GitHub.
