
# Principio de Inversión de Dependencias: Sistema de Pag

## Ejercicio de Principio de Inversión de Dependencias para Bootcamp IA - Factoria F5

Este repositorio contiene un ejemplo práctico del principio SOLID de Inversión de Dependencias (Dependency Inversion Principle) aplicado a un sistema de procesamiento de pagos.

### ¿Qué es el Principio de Inversión de Dependencias?

Es el último principio del acrónimo SOLID y establece dos reglas fundamentales:

1. Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.
2. Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.

### Sobre este ejercicio

En este proyecto demostramos cómo aplicar correctamente el principio de Inversión de Dependencias en Python, utilizando un sistema de procesamiento de pagos como ejemplo. El sistema permite cambiar fácilmente entre diferentes métodos de pago (tarjeta de crédito, PayPal) sin modificar el código del procesador principal.

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


---

Ejercicio desarrollado para el Bootcamp de Inteligencia Artificial de Factoria F5.
