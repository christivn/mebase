## 🗃️✨ Mebox - 🙌 Open Source Knowledge Management para Agentes de IA

[![US](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/us.png "Canada") English](/readme/en.md) -
[![Spain](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/es.png "Spain") Español](/readme/es.md) -
[![France](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/fr.png "France") Français](/readme/fr.md) -
[![Germany](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/de.png "Germany") Deutschland](/readme/de.md) -
[![China](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/cn.png "China") 中国](/readme/cn.md) -
[![India](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/in.png "China") हिंदी](/readme/in.md) -
[![Korea](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/kr.png "Korea") 한국어](/readme/kr.md)

<img src="https://github.com/christivn/mebox/blob/main/img/mebox.jpg?raw=true">  

Mebox es una alternativa de código abierto a la herramienta `file_search` de OpenAI, diseñada para procesar, almacenar y recuperar información basada en archivos de manera eficiente utilizando Supabase y embeddings.  

🔹 **Extraer** texto de archivos subidos  
🔹 **Generar** chunks para almacenamiento y recuperación eficiente  
🔹 **Embed** datos de texto para búsqueda semántica  
🔹 **Almacenar** y **consultar** embeddings utilizando Supabase Vector DB  
🔹 **Soporte multilingüe** para mejorar la accesibilidad en diferentes idiomas  
🔹 **Formatos de archivos soportados:** `pdf`, `json`, `csv`, `xlsx`, `txt`, `md`, `xml`, `yaml`, `ini`, `log`, `bat`, `py`, `js`, `java`, `cpp`, `html`   
🔹 **Modelos de IA disponibles:** +300 modelos  

### Índice  

- [📖 Sobre Mebox](#-sobre-mebox)  
- [💡 ¿Por qué usar Mebox?](#-por-que-usar-mebox)  
- [🔧 Casos de uso](#-casos-de-uso)  
- [📝 Documentación](#-documentacion)  
  - [⬆️ Cargar Archivo](#️-cargar-archivo)  
  - [📄 Transformar Archivo a Texto](#-transformar-archivo-a-texto)  
  - [🧩 Generación de Chunks](#-generacion-de-chunks)  
  - [🔗 Embeddings de los Chunks](#-embeddings-de-los-chunks)  
  - [💾 Base de Datos](#-base-de-datos)  
  - [🔎 Búsqueda y Recuperación](#-busqueda-y-recuperacion)  
- [🛠️ Instalación y Configuración](#%EF%B8%8F-instalacion-y-configuracion)  
- [🤝 Contribuir](#-contribuir)  
- [📜 Licencia](#-licencia)  

<br>

## 💡 ¿Por qué usar Mebox?  

💰 **Código abierto y rentable** - No depende de APIs propietarias.  
⚡ **Rápido y escalable** - Usa Supabase Vector para una recuperación de alto rendimiento.  
🔍 **Búsqueda precisa** - Compatible con búsqueda semántica mediante embeddings.  
📂 **Flexible y extensible** - Se integra fácilmente con diferentes formatos de archivos y bases de datos.  
🌐 **Soporte multilingüe** - Procesa y recupera información en varios idiomas.  

<br>

## 🔧 Casos de uso  

Mebox puede aplicarse en diversas áreas que requieren recuperación eficiente de información basada en archivos:  

📚 **Bots de conocimiento impulsados por IA** – Asistentes que responden preguntas con base en bases de datos de documentos.  
🎯 **Algoritmos de recomendación** – Sistemas de recomendación personalizados mediante búsqueda semántica.  
🔍 **Investigación legal y cumplimiento** – Recuperación rápida de documentos legales y jurisprudencia.  
📚 **Herramientas académicas e investigativas** – Búsqueda eficiente en colecciones de libros y artículos científicos.  
💼 **Gestión del conocimiento empresarial** – Organización y búsqueda de documentación interna.  
🤖 **Integración con chatbots** – Memoria documental para respuestas más informadas.  
📂 **Extracción automatizada de datos** – Procesamiento de datos estructurados y no estructurados.  
💬 **Bots de respuestas predefinidas** – Asistentes que responden basado en información almacenada.  
📈 **Análisis de mercado y detección de tendencias** – Análisis de grandes volúmenes de datos para insights de mercado.  
🏢 **Automatización del soporte al cliente** – Resolución automatizada de consultas.  

<br>

## 🛠️ Instalación y Configuración  

**Requisitos:**  

- Clave API de Openrouter  
- Supabase con `pgvector`  

```bash
# Clonar el repositorio
git clone https://github.com/christivn/mebox.git

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno (claves de Supabase, claves de API del modelo de embeddings, etc.)
export SUPABASE_URL=your_supabase_url
export SUPABASE_KEY=your_supabase_key

# Ejecutar la aplicación
python main.py
```  

<br><br>

---
---

<br><br>

## 📝 Documentación  

Este proyecto abarca la gestión y búsqueda de embeddings a través de varias etapas.  

<img src="https://github.com/christivn/mebox/blob/main/img/text_splitter.png?raw=true" width="600px">  

## 🔗 Embeddings de los Chunks  

Cada chunk se convierte en un embedding utilizando un modelo avanzado de embeddings.  

<img src="https://github.com/christivn/mebox/blob/main/img/embedding.jpg?raw=true" width="450px">  

<br>

## 💾 Base de Datos  

Utilizamos Supabase para almacenar y gestionar embeddings, indexados con **HNSW** para optimizar la búsqueda por similitud.  

<img src="https://github.com/christivn/mebox/blob/main/img/HNSW.png?raw=true" width="450px">  

<br>

## 🔎 Búsqueda y Recuperación  

Usa búsqueda semántica para encontrar información relevante basada en consultas del usuario.  

<img src="https://github.com/christivn/mebox/blob/main/img/chunks-strategies.jpg?raw=true" width="550px">  

<br>

---

<br>

## 🤝 Contribuir  

¡Las contribuciones son bienvenidas! Puedes abrir issues, enviar pull requests o sugerir mejoras.  

📩 **Contacto:** A través de Issues o Discussions en GitHub.  

<br>

## 📜 Licencia  

MIT License © 2025 Christian Ramos. Consulta [LICENSE](https://github.com/christivn/mebox/blob/main/LICENSE) para más detalles.  