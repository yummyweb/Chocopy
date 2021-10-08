# Chocopi

Chocopi introduces a new way to create declarative macOS applications efficiently. Chocopy utilizes the macOS Cocoa API under the hood.

All rendered UI elements are known as controllers, and they function using listeners, which is nothing but a function or a callback. Layouts are a combination of controllers and a system of positioning. 

The following layout constricts have been implemented:
- Panels
- Windows

The following controllers work:
- Button
- Label
- Text Input
- Slider
- Progress Bar
- Checkbox

## Installation

Install Chocopi using pip:

```
pip install chocopi
```

## API Reference

Chocopy: Main window object.

Args:
- title -> str
- location -> (x, y)
- size -> (width, height)

set_max_size: Sets the maximum size for a window

Args:
- size -> (width, height)

Check the `examples/` directory for more examples.
