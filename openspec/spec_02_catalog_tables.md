# OpenSpec 02: Catálogo de Carta y Mesas (MySQL Aula)

## 1. Contexto y Conexión
- Conectar a la base de datos MySQL existente del aula usando credenciales del archivo .env.
- NO usar XAMPP ni levantar bases de datos locales: la base de datos ya está montada y operativa en el host/puerto especificado en .env.
- Usar SQLAlchemy con PyMySQL mediante URL.create.
- Las tablas YA EXISTEN en MySQL con datos reales: NO crear tablas desde código (no usar Base.metadata.create_all).

## 2. Tablas Existentes de MySQL a Consultar
- Grupos: Categorías de la carta.
- Carta: Productos asociados a un grupo.
- Tipos: Tipos de presentación (unidad, tapa, media, ración).
- Mesas: Mesas dadas de alta en el sistema.

## 3. Endpoints a Implementar (Solo Lectura)
- GET /tables: Listado de mesas disponibles.
- GET /categories: Listado de categorías/grupos.
- GET /categories/{category_id}/products: Productos filtrados por categoría.
- GET /presentations: Listado de tipos de presentación disponibles.

## 4. Criterios de Aceptación
1. Conexión limpia y directa sin sobreingeniería.
2. Cada endpoint responde código 200 con la lista de registros en JSON.
3. Probar que responde en /docs y hacer commit + push a GitHub.
