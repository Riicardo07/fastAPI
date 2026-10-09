# OpenSpec 03: Gestión de Pedidos y Persistencia (Mesa 7)

## 1. Contexto y Reglas de Negocio
- Conexión a la base de datos MySQL existente mediante SQLAlchemy y PyMySQL.
- Tabla existente: \Pedidos\ (campos habituales: id, table_id / id_mesa, product_id / id_producto, presentation_id / id_tipo, cantidad / units).
- **Restricción estricta de mesa:** Solo se permiten operaciones sobre la **Mesa 7**. Cualquier intento de crear o consultar pedidos para otra mesa debe ser rechazado con un error HTTP 403 o 400.

## 2. Endpoints a Implementar
1. \POST /orders\: Crear una línea de pedido.
   - Entrada JSON: table_id, product_id, presentation_id, cantidad.
   - Validación: table_id debe ser obligatoriamente 7. Si no, retornar 403 Forbidden.
   - Validación: verificar que producto y presentación existan antes de guardar.
   - Respuesta: 201 Created con el objeto del pedido creado.
2. \GET /tables/{table_id}/orders\: Listar pedidos de una mesa.
   - Validación: solo se permite consultar la mesa 7 (si piden otra mesa, retornar 403 Forbidden).
   - Respuesta: 200 OK con la lista de pedidos abiertos de esa mesa.
3. \DELETE /orders/{order_id}\: Eliminar una línea de pedido existente.
   - Validación: si el id no existe, retornar 404 Not Found.
   - Validación: solo permitir eliminar pedidos pertenecientes a la mesa 7.
   - Respuesta: 204 No Content.

## 3. Criterios de Aceptación
1. Esquemas Pydantic OrderCreate y OrderResponse claros y validados.
2. Manejo de excepciones con HTTPException y códigos HTTP correctos (201, 204, 400, 403, 404).
3. Probado manualmente desde /docs realizando:
   - Inserción de un pedido en la mesa 7 (devuelve 201).
   - Intento de inserción en otra mesa (falla con 403).
   - Consulta de pedidos de la mesa 7 (devuelve 200 con el pedido anterior).
   - Eliminación del pedido (devuelve 204).
4. Subida a GitHub en rama feature/spec-03-orders y comprobación final.
