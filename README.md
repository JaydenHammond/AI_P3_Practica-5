# AI_P3_Practica-5

## ¿Qué es?

Imagina que tienes un montón de islas (vértices) y quieres unirlas con puentes (aristas), cada uno con un coste de construcción diferente.  
El algoritmo de **Kruskal** es como un ingeniero brillante que te ayuda a elegir qué puentes construir para lograr dos objetivos:

- 🔹 **Mínimo coste**: Conectar todas las islas gastando lo mínimo posible.  
- 🔸 **Máximo coste**: Crear la red más cara o robusta deliberadamente (¡sí, a veces queremos eso!).

---

## ¿Cómo lo hace?

**Kruskal** sigue un plan simple pero poderoso:

1. **Ordena los puentes**: De baratos a caros (para mínimo coste) o de caros a baratos (para máximo coste).
2. **Construye paso a paso**: Añade puentes uno por uno, pero nunca forma un circuito (evita rutas redundantes).  
   Para esto, usa una técnica llamada **Union-Find**, que detecta al instante si un puente crearía un "atajo innecesario".

---

## ¿Para qué sirve?

### Mínimo Coste (MST):

- **Optimizar recursos**: Como diseñar una red de fibra óptica con el menor cable posible, o conectar ciudades con carreteras usando el mínimo asfalto.
- **Ahorrar en grande**: Ideal para proyectos de infraestructura (electricidad, agua) donde cada metro de tubería cuenta.

### Máximo Coste:

- **Prepararse para lo peor**: Simular la red más vulnerable (ej.: en ciberseguridad) para fortalecer puntos débiles.
- **Invertir en fortaleza**: Crear redes de comunicación ultra-resistentes, o identificar las conexiones más valiosas en una red social (como los *influencers* clave).

---

> Este proyecto demuestra cómo aplicar el algoritmo de Kruskal para resolver problemas reales con un enfoque práctico y visual.
