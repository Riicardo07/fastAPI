# OpenSpec 02: Flujo de Carta y Navegación del Camarero

## 1. Contexto y Conexión
- Conexión contra el servidor MySQL existente del aula usando variables de entorno de .env.
- Driver: SQLAlchemy con PyMySQL mediante URL.create (según patrón indicado).
- Las tablas YA EXISTEN: Grupos, Carta, Tipos, Mesas. No crear tablas desde código.

## 2. Endpoints a Implementar
1. GET /tables: Listado de mesas dadas de alta.
2. GET /categories: Listado de grupos/categorías de la carta.
3. GET /categories/{category_id}/products: Productos pertenecientes a esa categoría.
4. GET /products/{product_id}: Detalle completo de un producto por su ID.
5. GET /products/{product_id}/presentations: Presentaciones activas o disponibles para ese producto concreto (unidad, tapa, media, ración según marque la tabla Carta o Tipos).

## 3. Requerimientos de Código
- Modelos Pydantic de entrada/salida para serializar y validar respuestas JSON limpias.
- Código directo, sin clases complejas innecesarias ni patrones sobrecargados.
- Validación de errores: si una categoría o producto no existe, responder HTTP 404 Not Found con mensaje claro.

## 4. Criterios de Aceptación
1. Todos los endpoints responden código HTTP 200 con datos reales del MySQL del aula.
2. Respuestas validadas desde Swagger UI (/docs).
3. Commit semántico y push a la rama feature/spec-02-catalog en GitHub.
