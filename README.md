## 🗃️✨ Mebox - 🙌 Open Source Knowledge Base For AI Agents

[![US](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/us.png "Canada") English](/readme/en.md) -
[![Spain](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/es.png "Spain") Español](/readme/es.md) -
[![France](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/fr.png "France") Français](/readme/fr.md) -
[![Germany](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/de.png "Germany") Deutschland](/readme/de.md) -
[![China](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/cn.png "China") 中国](/readme/cn.md) -
[![India](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/in.png "China") हिंदी](/readme/in.md) -
[![Korea](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/kr.png "Korea") 한국어](/readme/kr.md)

<img src="https://github.com/christivn/mebox/blob/main/img/mebox.jpg?raw=true">

| **ⓘ INFO** |
|---------|
| This repository is under development, it is likely that you will find bugs and incomplete parts. |

<br>

Mebox is an open-source alternative to OpenAI's `file_search` tool, designed to efficiently process, store, and retrieve file-based information using Supabase and embeddings.

🔹 **Extract** text from uploaded files  
🔹 **Generate** chunks for efficient storage and retrieval  
🔹 **Embedding** text data for semantic search  
🔹 **Store** and **query** embeddings using Supabase Vector DB  

🔹 **Multiple file formats:** `pdf`, `json`, `csv`, `xlsx`, `txt`, `md`, `xml`, `yaml`, `ini`, `log`, `bat`, `py`, `js`, `java`, `cpp`, `html`  
🔹 **Multilingual support:** +12 languages supported  
🔹 **Multiple AI:** +300 models  

### Index

- [📖 About Mebox](#-about-mebox)  
- [💡 Why Use Mebox?](#-why-use-mebox)  
- [🔧 Use Cases](#-use-cases)
- [🛠️ Installation & Setup](#%EF%B8%8F-installation--setup)  
- [📝 Documentation](#-documentation)
  - [⬆️ Upload File](#️-upload-file)  
  - [📄 Transform File to Text](#-transform-file-to-text)  
  - [🧩 Chunks Generation](#-chunks-generation)  
  - [🔗 Embedding the Chunks](#-embedding-the-chunks)  
  - [💾 Database](#-database) 
  - [🔎 Search & Retrieval](#-search--retrieval)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  

<br>

## 💡 Why Use Mebox?

💰 **Open-source & Cost-effective** - No reliance on proprietary APIs.  
⚡ **Fast & Scalable** - Uses Supabase Vector for high-performance retrieval.  
🔍 **Accurate Search** - Supports semantic search with embeddings.  
📂 **Flexible & Extensible** - Easily integrates with different file formats and databases.  
🌐 **Multilingual Support** - Process and retrieve information in multiple languages.  

<br>

## 🔧 Use Cases

Mebox can be used in various applications that require efficient file-based information retrieval and knowledge management:

📚 **AI-Powered Knowledge Bots** – Create AI assistants that can answer questions based on custom document databases.  
🎯 **Recommendation Algorithms** – Build personalized recommendation systems using semantic search.  
🔍 **Legal & Compliance Research** – Quickly retrieve relevant documents and case laws based on contextual search.  
📚 **Academic & Research Tools** – Enable efficient searching through large collections of research papers and books.  
💼 **Enterprise Knowledge Management** – Organize and search internal company documentation with ease.  
🤖 **Chatbot Integration** – Enhance chatbots with document-based memory for more informed responses.  
📂 **Automated Data Extraction** – Process and analyze structured and unstructured text data from various file formats.  
💬 **Predefined Response Bots** – Develop bots that provide predefined responses based on stored information.  
📈 **Market Analysis & Trend Detection** – Analyze large datasets for market trends and insights.  
🏢 **Customer Support Automation** – Streamline customer support by enabling automated query resolution.  

<br>

## 🛠️ Installation & Setup

**Requisitos:**

- Api Key de Openrouter
- Supabase con `pgvector`

```bash
# Clone the repository
git clone https://github.com/christivn/mebox.git

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (Supabase keys, embedding model API keys, etc.)
export SUPABASE_URL=your_supabase_url
export SUPABASE_KEY=your_supabase_key

# Run the application
python main.py
```

<br><br>

---
---

<br><br>

# 📝 Documentation
Este proyecto abarca todo el proceso de gestión y búsqueda de embeddings a través de varias etapas. Comienza con la carga de archivos en el sistema, que luego se transforman a texto para extraer la información relevante. El texto se divide en *chunks* (fragmentos) para su posterior procesamiento, y cada *chunk* es convertido en un **embedding** utilizando un modelo de aprendizaje automático. Estos embeddings son almacenados eficientemente en **Supabase**, donde se indexan utilizando **HNSW** para optimizar las búsquedas de similitud. Finalmente, el sistema permite realizar búsquedas rápidas y precisas mediante la **similitud de coseno**, facilitando la recuperación de información relevante a partir de grandes volúmenes de datos.

<br>

## ⬆️ Upload File
Users can upload various file formats (e.g., `.pdf`, `.txt`, `.csv`). The system extracts text content for further processing.

<br>

## 📄 Transform File to Text
Extracts meaningful text from the uploaded file using different parsing methods based on file type.

**getTextFromWebpage:** `website URL`

**getTextFromTXT:** `txt`, `md`, `xml`, `yaml`, `ini`, `log`, `bat`, `py`, `js`, `java`, `cpp`, `html`

**getTextFromPDF:** `pdf`

**getTextFromCSV:** `json`, `csv`, `xlsx`

**getTextFromMicrosoftOffice:** `doc`, `docx`, `pptx`

**getTextFromEmail:** `eml`

**getTextFromUnstructured:** Load files of many types

<br>

## 🧩 Chunks Generation
Splits the extracted text into manageable chunks to optimize search and retrieval performance.

**Default Settings:**
- 📏 **Chunk size:** 512 tokens
- 🔢 **Max chunks in context:** 20

<img src="https://github.com/christivn/mebox/blob/main/img/text_splitter.png?raw=true" width="600px">

<br>

## 🔗 Embedding the Chunks
Each chunk is embedded using a powerful embedding model, allowing for efficient similarity-based search.

**Default Settings:**
- 🧠 **Embedding model:** `thenlper/gte-small`
- 📏 **Dimensions:** 384

The GTE models are trained by **Alibaba DAMO Academy**. They are mainly based on the BERT framework and currently offer three different sizes of models, including GTE-large, GTE-base, and GTE-small. 

| Model Name | Model Size (GB) | Dimension | Sequence Length | Average (56) | Clustering (11) | Pair Classification (3) | Reranking (4) | Retrieval (15) | STS (10) | Summarization (1) | Classification (12) |
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**gte-small**](https://huggingface.co/thenlper/gte-small) | **0.07** | **384** | **512** | **61.36** | **44.89** | **83.54** | **57.7** | **49.46** | **82.07** | **30.42** | **72.31** |

**Comparison with other embedding models:**
| Model Name | Model Size (GB) | Dimension | Sequence Length | Average (56) | Clustering (11) | Pair Classification (3) | Reranking (4) | Retrieval (15) | STS (10) | Summarization (1) | Classification (12) |
|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| e5-large-v2 | 1.34 | 1024| 512 | 62.25 | 44.49 | 86.03 | 56.61 | 50.56 | 82.05 | 30.19 | 75.24 |
| e5-base-v2 | 0.44 | 768 | 512 | 61.5 | 43.80 | 85.73 | 55.91 | 50.29 | 81.05 | 30.28 | 73.84 |
| text-embedding-ada-002 | - | 1536 | 8192 | 60.99 | 45.9 | 84.89 | 56.32 | 49.25 | 80.97 | 30.8 | 70.93 |
| e5-small-v2 | 0.13 | 384 | 512 | 59.93 | 39.92 | 84.67 | 54.32 | 49.04 | 80.39 | 31.16 | 72.94 |

**Example `gte-small`embedding:**

```
tensor([[-4.8426e-01, -3.5470e-01,  2.5043e-01,  8.7683e-02,  1.0782e-01,
         -5.7016e-03, -8.1829e-02,  4.4422e-01, -9.2456e-03, -3.5152e-01,
          1.5013e-02, -4.2973e-01,  2.2862e-01,  4.3781e-01,  4.5499e-01,
          2.3649e-02,  1.0961e-01,  1.0125e-01, -4.1820e-01,  3.3270e-01,
          7.0393e-01, -9.8001e-03,  1.0716e-01, -4.6404e-01,  1.4286e-01,
         -9.9045e-03, -1.2405e-01, -1.5022e-01, -3.2292e-01, -1.2242e+00,
          ... more
          3.3178e-03, -7.0972e-01,  1.1175e-01,  6.8678e-01, -2.0580e-02,
          8.3930e-02, -5.8170e-01,  5.7685e-02,  3.8488e-01, -9.4733e-02,
         -2.3249e-01, -1.0366e-01,  1.0068e-01,  2.1887e-01,  1.5462e-01,
         -2.4715e-01, -3.2600e-01, -5.0547e-01, -5.0383e-01, -1.7109e-01,
         -2.3582e-01,  1.5043e-01,  7.6588e-02,  5.1266e-01]],
       grad_fn=<MeanBackward1>)
```

<br>

## 💾 Database

En este proyecto, utilizamos Supabase como base de datos para almacenar y gestionar los embeddings generados por un modelo de aprendizaje automático. Para facilitar la búsqueda eficiente de datos similares, implementamos un índice basado en el algoritmo HNSW (Hierarchical Navigable Small World) y utilizamos la similitud de coseno para medir la cercanía entre los vectores de embeddings.

**¿Por qué HNSW?**

HNSW (Hierarchical Navigable Small World) es un algoritmo de búsqueda eficiente de vecinos más cercanos en espacios de alta dimensión. Se utiliza para mejorar el tiempo de respuesta en la búsqueda de los embeddings más cercanos en grandes volúmenes de datos. En lugar de realizar una búsqueda exhaustiva a través de todos los vectores, HNSW organiza los datos en una estructura jerárquica, lo que permite realizar búsquedas rápidas con un número reducido de comparaciones.

<img src="https://github.com/christivn/mebox/blob/main/img/HNSW.png?raw=true" width="450px">

**Ventajas de HNSW:**
- **Búsqueda eficiente:** Reduce significativamente el tiempo de consulta en grandes volúmenes de datos.  
- **Escalabilidad:** Es adecuado para trabajar con grandes bases de datos de embeddings sin comprometer mucho el rendimiento.  
- **Precisión:** Ofrece resultados de alta calidad en la búsqueda de vecinos más cercanos, lo que es fundamental cuando se busca similitud entre embeddings.  

<br>

**Similitud de Coseno**

La similitud de coseno es una medida utilizada para calcular la similitud entre dos vectores en un espacio de alta dimensión. Se define como el coseno del ángulo entre dos vectores, lo cual indica qué tan similares son en términos de dirección, independientemente de su magnitud.

La fórmula de la similitud de coseno es:

<img src="https://github.com/christivn/mebox/blob/main/img/cosine-distance.png?raw=true" width="450px">
Donde:

AA y BB son los vectores de los embeddings que estamos comparando.  
∥A∥ y ∥B∥ son las normas (o longitudes) de los vectores.  

Un valor de similitud de coseno cercano a 1 indica que los vectores son muy similares, mientras que un valor cercano a 0 indica que los vectores son muy diferentes.

**Representación 3D simplificada (Similitud de Coseno de 2 embbedings):**

<img src="https://github.com/christivn/mebox/blob/main/img/cosine-similarity.png?raw=true" width="450px">

<br>

## 🔎 Search & Retrieval
Uses semantic search to find relevant information based on user queries.

Always show in the chat the source file from which the information was obtained and the specific chunk.

- **K-NN:** 2 (Default)
- **Neighboring Chunks Pairs:** 1 (Default)

**JSON, CSV & XLSX:**
- **K-NN:** 20 (Default)
- **Neighboring Chunks Pairs:** 0 (Default)
<img src="https://github.com/christivn/mebox/blob/main/img/chunks-strategies.jpg?raw=true" width="550px">

<br><br>

---

<br>

## 🤝 Contributing

Welcome contributions! Feel free to open issues, submit pull requests, or suggest improvements.

📩 **Contact:** Reach out via GitHub Issues or Discussions.

<br>

## 📜 License

MIT License Copyright (c) 2025 Christian Ramos. See [LICENSE](https://github.com/christivn/mebox/blob/main/LICENSE) for details.
