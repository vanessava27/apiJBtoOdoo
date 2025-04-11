# Jobboss-Odoo Connector

Este proyecto es un conector entre la base de datos de Jobboss y la API de Odoo, diseñado para facilitar la sincronización de datos entre ambas plataformas.

## Estructura del Proyecto

```
jobboss-odoo-connector
├── src
│   ├── app.py                # Punto de entrada de la aplicación
│   ├── jobboss
│   │   ├── __init__.py       # Inicializa el paquete Jobboss
│   │   └── client.py         # Cliente para interactuar con Jobboss
│   ├── odoo
│   │   ├── __init__.py       # Inicializa el paquete Odoo
│   │   └── client.py         # Cliente para interactuar con Odoo
│   ├── services
│   │   └── sync_service.py    # Servicio para sincronizar datos
│   └── utils
│       └── helpers.py        # Funciones utilitarias
├── requirements.txt           # Dependencias del proyecto
├── config.yaml                # Configuración de la aplicación
├── README.md                  # Documentación del proyecto
└── .gitignore                 # Archivos a ignorar por Git
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd jobboss-odoo-connector
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Configura el archivo `config.yaml` con las credenciales necesarias para Jobboss y Odoo.

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python src/app.py
```

## Ejemplos

- Sincronizar datos entre Jobboss y Odoo.
- Realizar operaciones CRUD en ambas plataformas.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cambios.

## Licencia

Este proyecto está bajo la Licencia MIT.