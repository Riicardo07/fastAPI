# Restaurant API

API REST para la gestión de un restaurante: consulta de la carta (mesas, categorías,
productos y presentaciones) y gestión de pedidos. Está construida con **FastAPI**,
**SQLAlchemy** y **MySQL**, siguiendo una arquitectura sencilla por capas
(Routers -> Services/Repositories -> Models).

> **Restricción de negocio:** este servicio está asignado **exclusivamente a la Mesa 7**.
> La creación, consulta y borrado de pedidos solo se permite para esa mesa. Cualquier
> operación sobre otra mesa responde `403 Forbidden`.

---

## Tecnologías

- **Python 3.11+**
- **FastAPI** – framework web y documentación automática (Swagger UI).
- **SQLAlchemy 2.x** – ORM y acceso a datos.
- **PyMySQL** – driver de MySQL.
- **Pydantic v2** – validación y serialización de datos.
- **MySQL** – base de datos del aula (remota).
- **python-dotenv** – carga de variables de entorno desde `.env`.

---

## Estructura del proyecto

```
restaurant-api/
├── app/
│   ├── core/
│   │   ├── config.py          # Variables de entorno (CORS, mesas permitidas)
│   │   └── database.py        # Motor SQLAlchemy, sesión y Base
│   ├── models/
│   │   ├── reflected.py       # Tablas reflejadas con automap (carta, mesas...)
│   │   └── order.py           # Modelo Order -> tabla pedidos
│   ├── schemas/
│   │   ├── catalog.py         # Esquemas Pydantic de la carta
│   │   └── order.py           # Esquemas Pydantic de pedidos
│   ├── repositories/
│   │   ├── catalog_repository.py  # DAO de mesas, categorías, carta y presentaciones
│   │   └── order_repository.py    # DAO de pedidos (crear, listar, borrar)
│   ├── services/
│   │   └── order_service.py   # Lógica de negocio y validación de la Mesa 7
│   ├── routers/
│   │   ├── health.py          # / y /health
│   │   ├── catalog.py         # Endpoints de catálogo
│   │   └── orders.py          # Endpoints de pedidos
│   └── main.py                # Aplicación FastAPI y registro de routers
├── openspec/                  # Especificaciones del proyecto
├── requirements.txt
├── .env.example
└── README.md
```

---

## Requisitos e instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Riicardo07/fastAPI.git
   cd restaurant-api
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux / macOS
   source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuración del `.env`

Copia el ejemplo y rellena tus credenciales del servidor MySQL:

```bash
cp .env.example .env
```

| Variable                 | Descripción                                        | Ejemplo                              |
| ------------------------ | -------------------------------------------------- | ------------------------------------ |
| `DB_HOST`                | Host del servidor MySQL                            | `82.223.102.153`                     |
| `DB_PORT`                | Puerto MySQL                                       | `3306`                               |
| `DB_NAME`                | Nombre de la base de datos                         | `2DAMRestaurante`                    |
| `DB_USER`                | Usuario de la base de datos                        | `2DAMRestaurante`                    |
| `DB_PASSWORD`            | Contraseña de la base de datos                     | `********`                           |
| `ALLOWED_TABLES`         | Número(s) de mesa asignados (separados por comas)  | `7`                                  |
| `BACKEND_CORS_ORIGINS`   | Orígenes permitidos por CORS (separados por comas) | `http://localhost:4200`              |

> La conexión se realiza con `URL.create` de SQLAlchemy + PyMySQL. No se crean ni
> levantan bases de datos locales: se usa la base de datos MySQL ya existente.

---

## Ejecución

Arranca el servidor en modo desarrollo:

```bash
uvicorn app.main:app --reload
```

- API: <http://127.0.0.1:8000>
- Documentación interactiva (Swagger UI): <http://127.0.0.1:8000/docs>

---

## Endpoints

### Core

| Método | Ruta      | Descripción                          |
| ------ | --------- | ------------------------------------ |
| GET    | `/`       | Mensaje de bienvenida de la API      |
| GET    | `/health` | Estado del servicio y mesas asignadas|

### Catálogo (solo lectura)

| Método | Ruta                                | Descripción                                      |
| ------ | ----------------------------------- | ------------------------------------------------ |
| GET    | `/tables`                           | Lista de mesas dadas de alta                     |
| GET    | `/categories`                       | Lista de categorías de la carta                  |
| GET    | `/categories/{category_id}/products`| Productos de una categoría (404 si no existe)    |
| GET    | `/products/{product_id}`            | Detalle de un producto (404 si no existe)        |
| GET    | `/products/{product_id}/presentations` | Presentaciones disponibles de un producto     |
| GET    | `/presentations`                    | Lista de presentaciones disponibles              |

### Pedidos (restringidos a la Mesa 7)

| Método | Ruta                        | Descripción                                          | Códigos          |
| ------ | --------------------------- | ---------------------------------------------------- | ---------------- |
| POST   | `/orders`                   | Crea una línea de pedido                             | 201, 403, 404    |
| GET    | `/tables/{table_id}/orders` | Lista los pedidos de la mesa                         | 200, 403         |
| DELETE | `/orders/{order_id}`        | Borra una línea de pedido                            | 204, 403, 404    |

> **Mesa 7:** `table_id` debe ser `7`. Internamente se traduce al identificador real
> de la mesa `"Mesa 07"` (id `1098`). Cualquier otro valor devuelve `403`.
> El campo `cantidad` se acepta en la petición pero **no se persiste**, porque la
> tabla `pedidos` no dispone de esa columna.

---

## Ejemplos de petición y respuesta

### Listar categorías

```http
GET /categories
```

```json
[
  { "id": 1, "nombre_categoria": "Bebidas" },
  { "id": 12, "nombre_categoria": "Carnes" }
]
```

### Productos de una categoría

```http
GET /categories/3/products
```

```json
[
  {
    "id": 8,
    "id_categoria": 3,
    "producto": "Croquetas",
    "unidad": 0,
    "tapa": 0,
    "media": 1,
    "racion": 1
  }
]
```

### Presentaciones disponibles de un producto

```http
GET /products/8/presentations
```

```json
[
  { "id": 3, "nombre_presentacion": "Media Ración" },
  { "id": 4, "nombre_presentacion": "Ración" }
]
```

### Crear un pedido (Mesa 7)

```http
POST /orders
Content-Type: application/json
```

```json
{
  "table_id": 7,
  "product_id": 8,
  "presentation_id": 3,
  "cantidad": 2
}
```

Respuesta `201 Created`:

```json
{
  "id": 1890,
  "table_id": 7,
  "product_id": 8,
  "presentation_id": 3
}
```

### Crear un pedido en otra mesa (error)

```http
POST /orders
```

```json
{
  "table_id": 3,
  "product_id": 8,
  "presentation_id": 3,
  "cantidad": 1
}
```

Respuesta `403 Forbidden`:

```json
{ "detail": "Operación permitida únicamente en la Mesa 7" }
```

### Listar los pedidos de la Mesa 7

```http
GET /tables/7/orders
```

```json
[
  {
    "id": 1890,
    "table_id": 7,
    "product_id": 8,
    "presentation_id": 3
  }
]
```

### Borrar un pedido

```http
DELETE /orders/1890
```

Respuesta `204 No Content` (sin cuerpo).

---

## Arquitectura por capas

1. **Routers** (`app/routers/`): reciben la petición HTTP, delegan en el servicio o
   repositorio y devuelven esquemas Pydantic. No contienen consultas a la base de datos.
2. **Services** (`app/services/`): contienen las reglas de negocio (validación estricta
   de la Mesa 7 y existencia de producto/presentación).
3. **Repositories / DAO** (`app/repositories/`): centralizan las consultas de SQLAlchemy.
4. **Models / DB** (`app/models/`, `app/core/database.py`): mapeo y conexión a MySQL.

---

## Autor

Proyecto académico del módulo de desarrollo de APIs con FastAPI.
