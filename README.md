## 🗃️✨ Mebox - 🙌 Gestión de Conocimiento Open Source para Agentes de IA

[![US](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/us.png "Canada") English](/readme/en.md) -
[![Spain](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/es.png "Spain") Español](/readme/es.md) -
[![France](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/fr.png "France") Français](/readme/fr.md) -
[![Germany](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/de.png "Germany") Deutschland](/readme/de.md) -
[![China](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/cn.png "China") 中国](/readme/cn.md) -
[![India](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/in.png "China") हिंदी](/readme/in.md) -
[![Korea](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/kr.png "Korea") 한국어](/readme/kr.md)

<img src="https://github.com/christivn/mebox/blob/main/img/mebox.jpg?raw=true">

Mebox es una alternativa open-source a la herramienta `file_search` de OpenAI, diseñada para procesar, almacenar y recuperar información basada en archivos de manera eficiente utilizando Supabase y embeddings.

🔹 **Extrae** texto de archivos subidos  
🔹 **Genera** chunks para almacenamiento y recuperación eficiente  
🔹 **Embed** datos de texto para búsqueda semántica  
🔹 **Almacena** y **consulta** embeddings utilizando Supabase Vector DB  
🔹 **Soporte multilingüe** para mejorar la accesibilidad en diferentes idiomas  

### Índice

- [📖 Acerca de Mebox](#-acerca-de-mebox)  
- [💡 ¿Por qué usar Mebox?](#-por-que-usar-mebox)  
- [🔧 Casos de Uso](#-casos-de-uso)  
- [📝 Documentación](#-documentacion)
  - [⬆️ Subir Archivo](#️-subir-archivo)  
  - [📄 Transformar Archivo a Texto](#-transformar-archivo-a-texto)  
  - [🧩 Generación de Chunks](#-generacion-de-chunks)  
  - [🔗 Embedding de Chunks](#-embedding-de-chunks)  
  - [💾 Base de Datos](#-base-de-datos)  
  - [🔎 Búsqueda y Recuperación](#-busqueda-y-recuperacion)  
- [🛠️ Instalación y Configuración](#%EF%B8%8F-instalacion-y-configuracion)  
- [🤝 Contribuir](#-contribuir)  
- [📜 Licencia](#-licencia)  

<br>

## 💡 ¿Por qué usar Mebox?

💰 **Open-source y económico** - Sin dependencia de APIs propietarias.  
⚡ **Rápido y escalable** - Utiliza Supabase Vector para recuperación de alta eficiencia.  
🔍 **Búsqueda precisa** - Compatible con búsqueda semántica mediante embeddings.  
📂 **Flexible y extensible** - Se integra fácilmente con diferentes formatos de archivos y bases de datos.  
🌐 **Soporte multilingüe** - Procesa y recupera información en múltiples idiomas.  

<br>

## 🔧 Casos de Uso

Mebox se puede utilizar en diversas aplicaciones que requieren recuperación eficiente de información basada en archivos:

📚 **Bots de conocimiento con IA** – Crea asistentes de IA que pueden responder preguntas basadas en bases de datos de documentos personalizadas.  
🎯 **Algoritmos de recomendación** – Construye sistemas de recomendación personalizados con búsqueda semántica.  
🔍 **Investigación legal y cumplimiento** – Recupera documentos y leyes relevantes de manera rápida.  
📚 **Herramientas académicas e investigación** – Facilita la búsqueda en grandes colecciones de artículos y libros.  
💼 **Gestión del conocimiento empresarial** – Organiza y busca documentación interna con facilidad.  
🤖 **Integración con chatbots** – Mejora los chatbots con memoria basada en documentos para respuestas más informadas.  
📂 **Extracción automatizada de datos** – Procesa y analiza datos estructurados y no estructurados en varios formatos.  
💬 **Bots de respuesta predefinida** – Desarrolla bots que proporcionan respuestas basadas en información almacenada.  
📈 **Análisis de mercado y detección de tendencias** – Analiza grandes volúmenes de datos para detectar tendencias e insights.  
🏢 **Automatización de soporte al cliente** – Mejora el soporte al cliente con resolución automatizada de consultas.  

<br>

## 🛠️ Instalación y Configuración

**Requisitos:**

- API Key de Openrouter  
- Supabase con `pgvector`  

```bash
# Clonar el repositorio
git clone https://github.com/christivn/mebox.git

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno (Supabase keys, embedding model API keys, etc.)
export SUPABASE_URL=your_supabase_url
export SUPABASE_KEY=your_supabase_key

# Ejecutar la aplicación
python main.py
```

<br><br>

---
---

<br><br>

# 📝 Documentación

Este proyecto cubre todo el proceso de gestión y búsqueda de embeddings a través de varias etapas. Comienza con la carga de archivos, que luego se transforman en texto para extraer información relevante. El texto se divide en *chunks* para su posterior procesamiento, y cada *chunk* se convierte en un **embedding** utilizando un modelo de aprendizaje automático. Estos embeddings se almacenan en **Supabase**, donde se indexan usando **HNSW** para optimizar la búsqueda de similitud. Finalmente, el sistema permite realizar búsquedas rápidas y precisas mediante **similitud de coseno**, facilitando la recuperación de información relevante en grandes volúmenes de datos.

## ⬆️ Subir Archivo
Los usuarios pueden subir varios formatos de archivo (por ejemplo, `.pdf`, `.txt`, `.csv`). El sistema extrae el contenido de texto para su procesamiento posterior.

## 📄 Transformar Archivo a Texto
Extrae texto significativo del archivo subido utilizando diferentes métodos de análisis según el tipo de archivo.

## 🧩 Generación de Chunks
Divide el texto extraído en chunks para optimizar el rendimiento en la búsqueda y recuperación.

**Configuraciones por defecto:**
- 📏 **Tamaño de chunk:** 512 tokens
- 🔢 **Máximo de chunks en contexto:** 20

## 🔗 Embedding de Chunks
Cada chunk se convierte en un embedding utilizando un modelo avanzado, lo que permite búsquedas eficientes basadas en similitud.

## 💾 Base de Datos
Se usa Supabase para almacenar embeddings e indexarlos con **HNSW**, lo que permite realizar búsquedas rápidas con **similitud de coseno**.

## 🔎 Búsqueda y Recuperación
Utiliza búsqueda semántica para encontrar información relevante basada en consultas del usuario.

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Puedes abrir issues, enviar pull requests o sugerir mejoras.

📩 **Contacto:** A través de GitHub Issues o Discussions.

## 📜 Licencia

Licencia MIT (c) 2025 Christian Ramos. Ver [LICENSE](https://github.com/christivn/mebox/blob/main/LICENSE) para más detalles.
