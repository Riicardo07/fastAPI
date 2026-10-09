from sqlalchemy.ext.automap import automap_base

from app.core.database import engine

AutomapBase = automap_base()
AutomapBase.prepare(autoload_with=engine)

Categoria = AutomapBase.classes.categorias
Carta = AutomapBase.classes.carta
Mesa = AutomapBase.classes.mesas
Presentacion = AutomapBase.classes.presentaciones
