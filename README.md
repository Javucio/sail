# Sailmaniac

**Sailmaniac** es un juego de simulación de navegación en el que controlas un barco de vela y debes aprovechar el viento para moverte. El objetivo es aprender a navegar utilizando conceptos básicos de navegación a vela, como el viento de popa, ceñida y viento de proa.

## Características

- Simulación de navegación con físicas básicas.
- Interfaz retro con fuente 8-bit.
- Selección de colores para el barco en el menú principal.
- Indicadores visuales para la dirección y fuerza del viento.
- Lógica de ceñida para navegar contra el viento.

## Requisitos

- Python 3.8 o superior.
- Biblioteca `pygame`.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/sailmaniac.git
   cd sailmaniac


2. Instala las dependencias:
   ```bash
   pip install pygame
   ```

3. Asegúrate de que la fuente retro `PressStart2P.ttf` esté en la carpeta `assets/fonts/`.

## Cómo jugar

1. Ejecuta el juego:
   ```bash
   python menu.py
   ```

2. En el menú principal:
   - Usa las **flechas izquierda y derecha** para seleccionar el color del barco.
   - Pulsa **ENTER** para comenzar el juego.

3. Durante el juego:
   - Usa las **flechas izquierda y derecha** para cambiar el ángulo del barco.
   - Pulsa **ESPACIO** para avanzar utilizando el viento.

## Controles

- **Flechas izquierda/derecha**: Cambiar el ángulo del barco.
- **Espacio**: Mover el barco.
- **ESC**: Salir del juego.

## Estructura del proyecto

```
sailmaniac/
├── assets/
│   └── fonts/
│       └── PressStart2P.ttf
├── menu.py
├── juego.py
└── README.md
```

## Créditos

- **Fuente retro**: [Press Start 2P](https://www.fontspace.com/press-start-2p-font-19318)

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
```