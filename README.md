# Fase-2-credit-risk-and-recovery-

## Datos Generales

| Campo | Detalle |
| --- | --- |
| **Materia:** | Gestión de proyectos de inteligencia artificial |
| **Actividad:** | Fase 2 |
| **Alumno(a):** | María Fernanda Olvera Pegueros |
| **Matrícula:** | AL07154082 |
| **Docente:** | Luis Ariel Vázquez Piña |
| **Fecha de entrega:** | 12 / 07 / 2026 |

**Introducción:** En actividades previas se analizó el comportamiento de distintos modelos de clasificación, destacando entre ellos XGBoost, capaz de identificar relaciones complejas entre variables y ofrecer un desempeño sólido en la categorización de riesgo. Con el objetivo de ampliar el análisis hacia una perspectiva monetaria, se decidió incorporar un modelo de regresión lineal, comparándolo con la regresión logística, para estimar el monto de recuperación esperado en cuentas por cobrar.

Este enfoque no solo permite contrastar la capacidad predictiva de modelos de clasificación y regresión, sino también fortalecer la interpretación de resultados en términos financieros. Asimismo, se asegura una correcta codificación, documentación y despliegue en la nube, de manera que el proyecto esté preparado para una presentación más adecuada y profesional, integrando tanto la parte técnica como la práctica de implementación.

**Instrucciones**

**Debes realizar lo siguiente:**

**1.Repositorio en GitHub.**

Se estableció un repositorio público bajo la plataforma GitHub para el control de versiones del proyecto.

<img width="920" height="683" alt="image" src="https://github.com/user-attachments/assets/b2701bfc-5833-4415-bf0e-88d21b16ce4b" />

Ilustración 1. Estructura del repositorio del proyecto en GitHub.

a.  **Código fuente completo del proyecto.**

El código fuente principal (`app.py`) utiliza FastAPI e incorpora la carga dinámica de artefactos y la redirección automática del tráfico de red:
<img width="964" height="372" alt="image" src="https://github.com/user-attachments/assets/bfe7f1ea-6d72-4031-8645-28614660d037" />
<img width="964" height="360" alt="image" src="https://github.com/user-attachments/assets/8eddd77f-ac2f-4ac9-adfb-8e5876ad9448" />
<img width="943" height="403" alt="image" src="https://github.com/user-attachments/assets/85695e38-f90a-4069-9567-b2c423934f58" />


Ilustración 2. Código fuente completo en app.py

b.  **Dockerfile funcional.**

Para empaquetar la aplicación, se configuró un archivo Dockerfile optimizado que utiliza imágenes base oficiales y define de manera clara los puertos de comunicación en producción:

<img width="748" height="474" alt="image" src="https://github.com/user-attachments/assets/fcbe61f4-b7f3-4b75-8fd6-695e2e96b0e9" />

Ilustración 3. Dockerfile

c.  **Archivos de configuración necesarios.**

La orquestación de las librerías necesarias del ecosistema Python se gestiona a través del archivo de configuración estándar requirements.txt. Este archivo asegura que las dependencias operen en versiones validadas y compatibles:

-   flask
-   scikit-learn
-   pandas
-   numpy
-   joblib
-   matplotlib
-   seaborn
-   mlflow

_(Nota: Adicionalmente para el despliegue de la API con FastAPI se contemplan fastapi y uvicorn para asegurar que corra el entorno del servidor web rápido y de baja latencia)._

d  **Evidencia de integración (API, _endpoints_, entre otros).**

Se implementaron de forma satisfactoria las rutas del servidor encargadas de unificar el backend con los modelos matemáticos en formato `.pkl`. Esto permite procesar de manera simultánea peticiones lógicas e interpretaciones en formato numérico financiero bajo una misma arquitectura técnica clara.

La API funcionó correctamente. El endpoint `/predict_risk` procesó los datos y regresó un nivel de riesgo de `2`, mientras que el endpoint `/predict_recovery` calculó una recuperación estimada de `7476.01` sobre una factura de prueba de $10,000.

Respuesta devuelta por endpoints:

<img width="975" height="104" alt="image" src="https://github.com/user-attachments/assets/778acd2b-3665-4089-a633-37196239f938" />
<img width="975" height="98" alt="image" src="https://github.com/user-attachments/assets/7d9897b2-3adc-4306-bf6a-59904981b5f2" />


Ilustración 4. Respuesta devuelta por endpoints.

**2.Contenedor Docker funcional.**

e.  **Imagen construida correctamente.**

La imagen de Docker se compiló localmente de manera satisfactoria. Empaquetando todas las librerías requeridas.


<img width="978" height="95" alt="image" src="https://github.com/user-attachments/assets/50d090b7-c299-46e9-9348-393bcbc09247" />

Ilustración 5. Docker build -t mi-api-ar .

f.  **Ejecución local comprobable.**

Para validar el software antes de su distribución final en la nube, se levantó el contenedor localmente mapeando el puerto 8000. Los logs del sistema confirmaron un inicio limpio indicando el mensaje _"Application startup complete"_, respondiendo sin errores a las llamadas HTTP internas.


<img width="979" height="246" alt="image" src="https://github.com/user-attachments/assets/e9c10079-c473-4c1a-970c-5ffbaae6b0a9" />

Ilustración 6. Ejecución de comandos tag y push para subir la imagen del contenedor a Docker Hub.

<img width="665" height="678" alt="image" src="https://github.com/user-attachments/assets/ed5e56c4-17ed-4e6c-8b30-7be5039635c6" />


Ilustración 7. Interfaz interactiva de Swagger UI cargada localmente para la API de Cuentas por Cobrar.

**3.Manual de despliegue en la nube.**

g.  **Descripción del proceso paso a paso.**

2.**Subir la imagen:** Se compilaron los últimos cambios en la imagen local y se subió a Docker Hub usando el comando `push`.
<img width="979" height="202" alt="image" src="https://github.com/user-attachments/assets/0167563b-95dc-4b0e-acde-f66e39a3dcde" />

Ilustración 8. Confirmación del envío exitoso de las capas de la imagen hacia el repositorio de Docker Hub.

3. **Configurar en Render:** Se creó un nuevo _Web Service_ apuntando directo a la URL del contenedor en Docker Hub.


<img width="979" height="522" alt="image" src="https://github.com/user-attachments/assets/6fe2e182-af36-4e03-a4f7-c197257256fc" />

Ilustración 9. Configuración del nuevo servicio web en Render apuntando a la imagen del contenedor y selección del plan gratuito.

4. **Seleccionar el plan:** Elegí el plan gratuito (Free) de $0 USD/mes para mantener el control de costos del proyecto.

<img width="979" height="472" alt="image" src="https://github.com/user-attachments/assets/01147b78-101d-43d2-a116-2149fe5b9c35" />


Ilustración 10. Selección del tipo de instancia asignando el plan Free para el entorno de pruebas.

5. **Configurar variables:** En la sección _Advanced Settings_, agregué la variable `PORT = 8000`. Esto es clave para que Render pueda comunicarse con el puerto interno de la aplicación.


<img width="979" height="479" alt="image" src="https://github.com/user-attachments/assets/f924afad-5156-4e03-998b-af3b534f883c" />

Ilustración 11. Sección de configuración para la inyección de variables de entorno en Render.

<img width="979" height="535" alt="image" src="https://github.com/user-attachments/assets/32f952a6-49f8-4fc0-826d-f817113c3d3d" />


Ilustración 12. Logs del servidor remoto confirmando el despliegue exitoso de la aplicación con estatus Live.

6.**Desplegar:** Se ejecutó el despliegue y la API quedó activa y funcionando en internet.

[**https://mi-api-ar-latest.onrender.com**](https://mi-api-ar-latest.onrender.com)


<img width="979" height="491" alt="image" src="https://github.com/user-attachments/assets/b1d873a0-28ea-4a28-8dea-aea71b5398af" />

Ilustración 13. Panel de administración en Render mostrando el histórico de despliegues exitosos y URL pública.

<img width="979" height="455" alt="image" src="https://github.com/user-attachments/assets/2b966905-57aa-4b31-9e27-02a6bbf801b5" />


Ilustración 14. Documentación interactiva de la API (Swagger UI) expuesta en producción mediante la URL de Render.

a.  **Requerimientos técnicos.**

-   **En el entorno de desarrollo:** se usó Python 3.12 (64-bit), Docker Desktop, Windows PowerShell y VS Code.
-   **En la nube (producción):** Una instancia virtualizada en Linux (servicios PaaS), configurada con 512 MB de memoria RAM y 0.1 de CPU.

b.  **Estrategia de despliegue (contenedores, _PaaS_, entre otros).**

Se diseñó una estrategia de despliegue continuo conectando el contenedor con la plataforma Render (PaaS). Como puente, se utilizó un repositorio público en Docker Hub para almacenar la imagen (`mariapegueros/mi-api-ar:latest`). Esto facilita hacer actualizaciones en producción rápidamente y sin interrupciones del servicio.

c.  **Uso de herramientas de documentación (por ejemplo, Copilot).**

Para el desarrollo de esta fase, utilicé herramientas de asistencia con Inteligencia Artificial (GitHub, Copilot, ChatGPT y Gemini) como soporte técnico, analítico y de documentación. Esto me permitió optimizar el código, validar la estructura de los datos y asegurar el despliegue correcto de la infraestructura mediante los siguientes aspectos clave:

-   **Optimización del modelo y código:** Apoyo en la revisión de la redacción del reporte, corrección de errores en el código.
-   **Mejora del Dataset sintético:** Sugerencias de mejora en el dataset (el cual fue generado inicialmente con IA generativa) para ajustar las variables, evitar sesgos y obtener mejores resultados en la simulación de los modelos.
-   **Claridad en los requerimientos:** Identificación exacta de las diferencias entre las entregas de la Actividad 6 y los objetivos específicos de esta Fase II.
-   **Entendimiento de la infraestructura:** Comprensión a fondo de qué es y cómo estructurar el archivo Dockerfile, además de asimilar el concepto de despliegue en la nube.
-   **Dominio del entorno de desarrollo:** Resolución de dudas prácticas sobre el uso de Visual Studio Code y el manejo de comandos específicos (Docker, Git y PowerShell) dentro de su terminal integrada.

**4.Documento de validación y pruebas.**

d.  **Pruebas funcionales realizadas.**

Hice las pruebas funcionales directamente en la nube usando la interfaz interactiva de Swagger UI en Render. Envié solicitudes HTTP `POST` a los endpoints `/predict_risk` y `/predict_recovery`, y el servidor respondió al instante con códigos de estado exitosos `200 OK`.

<img width="821" height="890" alt="image" src="https://github.com/user-attachments/assets/89d7fa92-bcfe-4f74-ba0b-6be4f95673e6" />


Ilustración 15. Ingreso de parámetros de prueba en formato JSON para el endpoint de clasificación de riesgo.

<img width="667" height="432" alt="image" src="https://github.com/user-attachments/assets/253fbe86-21ef-4ac8-9d48-0d8de0e1c2cd" />


Ilustración 16. Código de estado HTTP 200 y respuesta del JSON con el riesgo predicho devuelto por la API.

e.  **Casos extremos evaluados.**

Para evaluar la robustez del modelo se realizaron pruebas con valores extremos mediante solicitudes JSON a la API. En el modelo de clasificación, las etiquetas representan los siguientes niveles de riesgo:

-   **0:** Riesgo alto
-   **1:** Riesgo medio
-   **2:** Riesgo bajo

Se evaluaron los siguientes escenarios:

-   **Caso real del dataset**

"monto_factura": 6974,
"dias_atraso": 19,
"historial_pago": 13,
"frecuencia_disputas": 1

**Resultado:** riesgo_predicho = 0 (riesgo alto).

-   **Valores mínimos**
"monto_factura": 0,
"dias_atraso": 0,
"historial_pago": 0,
"frecuencia_disputas": 0

**Resultado:** riesgo_predicho = 2 (riesgo bajo). El modelo respondió correctamente sin generar errores.

-   **Monto de factura extremadamente alto**
"monto_factura": 5555550,
"dias_atraso": 0,
"historial_pago": 0,
"frecuencia_disputas": 0

**Resultado:** recuperacion_esperada = 2,727,662.83. La regresión extrapola la predicción para valores fuera del rango de entrenamiento.

-   **Factura alta sin atraso**
"monto_factura": 55550,
 "dias_atraso": 0,
 "historial_pago": 7,
"frecuencia_disputas": 0

**Resultado:** riesgo_predicho = 1 (riesgo medio).

-   **Historial de pago fuera del rango**
"monto_factura": 5000,
"dias_atraso": 0,
 "historial_pago": 1000,
 "frecuencia_disputas": 0

**Resultado:** recuperacion_esperada = -5929.04. Al utilizar un valor muy superior al observado durante el entrenamiento, la predicción pierde validez práctica.

En general, las pruebas demostraron que la API procesa correctamente entradas extremas; sin embargo, las predicciones de regresión pueden ser poco confiables cuando los datos están fuera del rango utilizado para entrenar el modelo.

f.  **Resultados y conclusiones.**

**Resultados de la muestra:** Al correr el script de entrenamiento con los 2,000 registros de control, la base de datos arrojó una media de facturación de $27,368.83 pesos y una recuperación esperada promedio de $12,273.31 pesos. Para evaluar visualmente qué tan bien están respondiendo los modelos, generé las siguientes métricas de rendimiento:

<img width="979" height="263" alt="image" src="https://github.com/user-attachments/assets/ac001d24-653d-4d9b-b162-50a1f84c5c55" />


Ilustración 17. Estadísticas descriptivas de los 2,000 registros de control para la validación de las variables del modelo.

**1.Rendimiento de la Clasificación (Riesgo):** Al revisar cómo el modelo categoriza el riesgo de los clientes en alto (_high_), bajo (_low_) y medio (_medium_), la matriz de confusión demuestra una efectividad muy alta para detectar cuentas críticas, logrando clasificar sin errores 195 casos reales de alto riesgo. Aunque hay pequeños detalles a pulir en las zonas de riesgo medio y bajo, el endpoint es totalmente estable, no satura la memoria y devuelve las respuestas en texto.


<img width="604" height="466" alt="image" src="https://github.com/user-attachments/assets/f94580d9-0550-46c7-ba20-be3a402924ac" />

Ilustración 18. Matriz de Confusión para la clasificación del nivel de riesgo.
**2.Rendimiento de la Regresión (Monto):** Al analizar la gráfica de dispersión que cruza los valores reales contra los predichos, se confirma una tendencia lineal positiva bastante clara. Además, el histograma que mide la distribución de errores (residuos) tiene una forma simétrica muy bien definida y centrada en cero, lo que valida estadísticamente que las predicciones del modelo no están sesgadas hacia arriba o hacia abajo.

<img width="366" height="345" alt="image" src="https://github.com/user-attachments/assets/28471369-0cfc-4ee5-9f4f-0f3f29e3541c" />

Ilustración 19. Regresión Lineal.

<img width="501" height="335" alt="image" src="https://github.com/user-attachments/assets/54879da5-c76d-4cd4-8706-528b325cf943" />

Ilustración 20. Distribución de errores.

**Conclusiones**

En el caso de la regresión lineal, las métricas alcanzaron un desempeño limitado con un R² cercano a 0.57. Para mejorar este resultado se aplicaron técnicas de regularización como Ridge y Lasso, aunque las mejoras obtenidas fueron marginales. Esto evidencia que, para futuros análisis, será necesario incorporar feature engineering, por ejemplo, transformar la variable fecha_factura en mes o trimestre y codificar sentiment_email como variable numérica, con el fin de capturar relaciones más complejas.

Por otro lado, se observa que en actividades previas los modelos de clasificación ya ofrecían resultados confiables, lo que permite utilizarlos como complemento en la toma de decisiones. Estos modelos, junto con la regresión, aportan estimaciones útiles para la planeación de presupuestos y la definición de objetivos mensuales y anuales, así como para el diseño de estrategias tanto a nivel general como individual.

Finalmente, con las pruebas en PowerShell y los accesos web interactivos, queda confirmado que el sistema funciona correctamente tanto en el entorno local como en la nube. Dejando un proyecto sólido, integrado y listo para un despliegue profesional.
