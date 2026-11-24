# Plantar · App Clientes (web)

Página pública de pedidos de Plantar (Netlify). Los pedidos llegan por Netlify Forms (formulario `pedido`) y una tarea automática los carga en Plantar · Gestión.

- `index.html`: la app (generada desde la App Clientes de Claude).
- `catalogo.json`, `cuits.json`, `f/`: se actualizan solos cada hora con `tools/actualizar.py`.
