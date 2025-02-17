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

- [📖 Acerca de Mebox](#-acerca-de-mebox)  
- [💡 ¿Por qué usar Mebox?](#-por-qué-usar-mebox)  
- [🔧 Casos de uso](#-casos-de-uso)  
- [📝 Documentación](#-documentación)  
  - [⬆️ Subir archivo](#️-subir-archivo)  
  - [📄 Transformar archivo a texto](#-transformar-archivo-a-texto)  
  - [🧩 Generación de chunks](#-generación-de-chunks)  
  - [🔗 Embedding de los chunks](#-embedding-de-los-chunks)  
  - [💾 Base de datos](#-base-de-datos)  
  - [🔎 Búsqueda y recuperación](#-búsqueda-y-recuperación)  
- [🛠️ Instalación y configuración](#%EF%B8%8F-instalación-y-configuración)  
- [🤝 Contribuir](#-contribuir)  
- [📜 Licencia](#-licencia)  

<br>  

## 💡 ¿Por qué usar Mebox?  

💰 **Código abierto y rentable** - No depende de APIs propietarias.  
⚡ **Rápido y escalable** - Utiliza Supabase Vector para una recuperación de alto rendimiento.  
🔍 **Búsqueda precisa** - Soporta búsqueda semántica con embeddings.  
📂 **Flexible y extensible** - Se integra fácilmente con distintos formatos de archivos y bases de datos.  
🌐 **Soporte multilingüe** - Procesa y recupera información en múltiples idiomas.  

<br>  

## 🔧 Casos de uso  

Mebox puede utilizarse en diversas aplicaciones que requieren recuperación eficiente de información basada en archivos y gestión del conocimiento:  

📚 **Bots de conocimiento impulsados por IA** – Crea asistentes de IA que respondan preguntas basadas en bases de datos documentales personalizadas.  
🎯 **Algoritmos de recomendación** – Construye sistemas de recomendación personalizados utilizando búsqueda semántica.  
🔍 **Investigación legal y de cumplimiento** – Recupera documentos y jurisprudencia relevante de manera rápida.  
📚 **Herramientas académicas e investigativas** – Facilita la búsqueda en grandes colecciones de artículos y libros.  
💼 **Gestión del conocimiento empresarial** – Organiza y consulta documentación interna de la empresa.  
🤖 **Integración con chatbots** – Mejora los chatbots con memoria basada en documentos para respuestas más informadas.  
📂 **Extracción automatizada de datos** – Procesa y analiza datos estructurados y no estructurados de distintos formatos.  
💬 **Bots de respuestas predefinidas** – Desarrolla bots que proporcionen respuestas basadas en información almacenada.  
📈 **Análisis de mercado y detección de tendencias** – Analiza grandes volúmenes de datos para obtener información de mercado.  
🏢 **Automatización del soporte al cliente** – Optimiza la atención al cliente con resolución automatizada de consultas.  

<br>  

## 🛠️ Instalación y configuración  

**Requisitos:**  

- API Key de Openrouter  
- Supabase con `pgvector`  

```bash  
# Clonar el repositorio  
git clone https://github.com/christivn/mebox.git  

# Instalar dependencias  
pip install -r requirements.txt  

# Configurar variables de entorno (claves de Supabase, API de embeddings, etc.)  
export SUPABASE_URL=your_supabase_url  
export SUPABASE_KEY=your_supabase_key  

# Ejecutar la aplicación  
python main.py  
```  

<br><br>  

---  

# 📝 Documentación  

Este proyecto abarca todo el proceso de gestión y búsqueda de embeddings a través de varias etapas. Comienza con la carga de archivos en el sistema, que luego se transforman en texto para extraer información relevante. El texto se divide en *chunks* (fragmentos) para su posterior procesamiento, y cada *chunk* es convertido en un **embedding** utilizando un modelo de aprendizaje automático. Estos embeddings se almacenan en **Supabase**, donde se indexan mediante **HNSW** para optimizar las búsquedas de similitud. Finalmente, el sistema permite realizar búsquedas rápidas y precisas utilizando **similitud de coseno**, facilitando la recuperación de información relevante a partir de grandes volúmenes de datos.  

<br>  

## ⬆️ Subir archivo  

Los usuarios pueden subir diversos formatos de archivos (e.g., `.pdf`, `.txt`, `.csv`). El sistema extrae el contenido de texto para su posterior procesamiento.  

<br>  

## 📄 Transformar archivo a texto  

Extrae texto significativo del archivo subido utilizando distintos métodos de análisis según el tipo de archivo.  

<br>  

## 🧩 Generación de chunks  

Divide el texto extraído en chunks manejables para optimizar la búsqueda y recuperación de información.  

**Configuraciones predeterminadas:**  
- 📏 **Tamaño del chunk:** 512 tokens  
- 🔢 **Máximo de chunks en contexto:** 20  

<br>  

## 🔗 Embedding de los chunks  

Cada chunk se convierte en un embedding mediante un modelo avanzado de embeddings, permitiendo una búsqueda eficiente basada en similitud.  

**Configuraciones predeterminadas:**  
- 🧠 **Modelo de embedding:** `thenlper/gte-small`  
- 📏 **Dimensiones:** 384  

<br>  

## 💾 Base de datos  

Se utiliza Supabase para almacenar y gestionar los embeddings generados, implementando un índice basado en el algoritmo HNSW para mejorar la búsqueda de similitud con embeddings.  

**Ventajas de HNSW:**  
- **Búsqueda eficiente:** Reduce significativamente el tiempo de consulta en grandes volúmenes de datos.  
- **Escalabilidad:** Apto para grandes bases de datos sin afectar el rendimiento.  
- **Precisión:** Resultados de alta calidad en búsqueda de similitud.  

<br>  

## 🔎 Búsqueda y recuperación  

Utiliza búsqueda semántica para encontrar información relevante basada en consultas del usuario.  

Siempre se mostrará en el chat el archivo fuente del cual se obtuvo la información y el chunk específico.  

---  

## 🤝 Contribuir  

¡Las contribuciones son bienvenidas! Puedes abrir issues, enviar pull requests o sugerir mejoras.  

📩 **Contacto:** A través de GitHub Issues o Discussions.  

<br>  

## 📜 Licencia  

Licencia MIT © 2025 Christian Ramos. Consulta [LICENSE](https://github.com/christivn/mebox/blob/main/LICENSE) para más detalles.  