
# Principio de Inversión de Dependencias: Sistema de Pag

## Ejercicio de Principio de Inversión de Dependencias para Bootcamp IA - Factoria F5

Este repositorio contiene un ejemplo práctico del principio SOLID de Inversión de Dependencias (Dependency Inversion Principle) aplicado a un sistema de procesamiento de pagos.

### ¿Qué es el Principio de Inversión de Dependencias?

Es el último principio del acrónimo SOLID y establece dos reglas fundamentales:

1. Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.
2. Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.

### Sobre este ejercicio

En este proyecto demostramos cómo aplicar correctamente el principio de Inversión de Dependencias en Python, utilizando un sistema de procesamiento de pagos como ejemplo. El sistema permite cambiar fácilmente entre diferentes métodos de pago (tarjeta de crédito, PayPal) sin modificar el código del procesador principal.

### Estructura del código

- `abstraction.py`: Contiene la interfaz abstracta para los métodos de pago
- `implementations.py`: Implementaciones concretas para diferentes métodos de pago
- `processor.py`: El procesador de pagos que depende de la abstracción
- `main.py`: Ejemplo de uso del sistema

### Objetivos de aprendizaje

- Comprender cómo las dependencias pueden invertirse mediante abstracciones
- Aprender a diseñar código más flexible y mantenible
- Practicar la implementación de interfaces abstractas en Python
- Entender cómo la inyección de dependencias favorece el código desacoplado

### Beneficios del principio aplicado

- **Flexibilidad**: El sistema puede adaptarse fácilmente a nuevos métodos de pago
- **Testabilidad**: Facilita la creación de pruebas unitarias mediante mocks
- **Mantenibilidad**: Los cambios en una parte del sistema no afectan a otras partes
- **Extensibilidad**: Se pueden añadir nuevas funcionalidades sin modificar el código existente

### Instrucciones

1. Clona este repositorio
2. Examina el código fuente para entender la implementación
3. Ejecuta `python main.py` para ver el sistema en acción
4. Intenta añadir un nuevo método de pago sin modificar el procesador existente
5. Reflexiona sobre cómo este principio mejora la calidad del código

---

Ejercicio desarrollado para el Bootcamp de Inteligencia Artificial de Factoria F5.
