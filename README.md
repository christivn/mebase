## 🗃️✨ Mebox - 🙌 Open Source Knowledge Base For AI Agents

[![US](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/us.png "Canada") English](/readme/en.md) -
[![Spain](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/es.png "Spain") Español](/readme/es.md) -
[![France](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/fr.png "France") Français](/readme/fr.md) -
[![Germany](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/de.png "Germany") Deutschland](/readme/de.md) -
[![China](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/cn.png "China") 中国](/readme/cn.md) -
[![India](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/in.png "China") हिंदी](/readme/in.md) -
[![Korea](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/kr.png "Korea") 한국어](/readme/kr.md)

<img src="https://github.com/christivn/mebox/blob/main/img/mebox.jpg?raw=true">



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
         -1.9758e-01, -8.4965e-01,  1.9042e-01, -1.7524e-01,  1.1326e-01,
         -2.6646e-01, -2.7709e-01,  2.7579e-01, -5.4489e-01,  4.3373e-01,
          1.9649e-01,  3.3793e-01, -1.6748e-01,  3.3312e-02, -1.9927e-01,
         -3.2299e-01, -1.0167e-01,  1.0132e-02,  1.0324e-01, -2.1002e-01,
          1.5399e-01, -1.4285e-01,  2.6127e-01,  9.9326e-02,  1.9539e-01,
          4.6980e-01,  5.7947e-01,  3.5410e-01,  9.3290e-02,  2.5050e-01,
          4.9606e-01,  1.3357e-01, -2.0109e+00,  7.1566e-01,  6.5512e-01,
          8.0377e-01, -4.4848e-01, -4.4690e-02,  2.7157e-01,  1.9462e-01,
         -2.6314e-01,  1.7381e-01, -7.8615e-03,  6.8398e-01, -2.3111e-01,
          2.1295e-01, -4.2364e-02,  3.7562e-02, -4.2941e-01, -5.5194e-02,
          1.6047e-01, -2.5684e-01, -4.7569e-02, -2.1670e-01, -2.6755e-01,
         -3.8005e-01,  1.4537e-01, -4.3677e-01,  7.7072e-01,  2.0751e-01,
         -2.1154e-01, -8.3376e-02,  4.3289e-02, -9.2434e-02, -4.3273e-01,
         -1.9870e-01,  4.9275e-01,  4.9985e-02, -3.4849e-01,  1.6855e+00,
         -4.2659e-01,  3.1654e-01,  4.4517e-01, -5.9527e-01,  4.8919e-01,
         -2.2216e-01,  1.8695e-01, -1.9529e-01,  2.1633e-03, -4.0735e-03,
         -2.3393e-01,  3.4128e-02,  2.7516e-01, -4.5366e-01,  8.6434e-02,
         -2.6836e-01,  4.0000e-01,  1.0023e-01,  8.7586e-02, -3.3230e-01,
         -8.8362e-02,  8.6175e-02,  4.8671e-01, -1.9182e-01,  3.2668e-01,
         -6.4897e-01,  1.6965e-01,  9.4835e-01,  3.9646e-01,  5.7152e-01,
          8.1860e-01, -4.8296e-02, -2.5810e-01, -1.1551e-01, -2.9543e-01,
          1.9518e-01, -3.2578e-02,  2.5739e-01, -4.8572e-02, -1.7763e-01,
         -1.7051e-01, -9.0778e-01, -3.6184e-01, -7.5396e-01, -5.5413e-01,
          6.0382e-01, -1.7270e-01,  6.5298e-01, -3.7640e-01, -4.8197e-02,
          1.5316e-01,  1.7199e-01, -3.9543e-01,  7.1377e-02,  4.4999e-02,
          5.1685e-01,  6.2633e-01,  6.8921e-01, -3.0760e-01,  1.0718e-01,
         -3.1525e-01, -6.0511e-01, -3.0862e-01,  1.1819e+00,  1.8970e-01,
         -1.3720e+00, -8.5109e-02,  1.7793e-01, -2.2821e-02, -2.6869e-01,
          1.8710e-01,  1.3146e-01, -2.7440e-01,  4.7443e-01,  8.5258e-01,
          4.1104e-01, -1.9401e-01, -3.7398e-02,  7.3833e-02,  3.5023e-01,
          3.9975e-01, -5.0942e-01, -2.6174e-01,  5.3036e-01, -2.6264e-02,
         -3.7464e-01,  1.9621e-01, -2.9206e-01,  4.7243e-01,  5.1139e-01,
         -3.0989e-01,  1.9188e-01, -3.3688e-01, -2.4675e-01, -4.4213e-01,
         -4.5052e-03, -1.5180e-01, -4.8270e-01,  1.9573e-01, -6.1070e-01,
          8.0719e-01,  7.7409e-02, -2.0491e-01, -2.3347e-01, -3.1348e-01,
          3.8012e-01, -8.3108e-02, -3.0339e-01,  1.9906e-01,  4.4955e-02,
         -5.5798e-01,  6.0864e-02,  1.8135e-01, -1.4787e-03, -1.4120e-01,
         -1.8128e-01,  2.4740e-01,  4.1475e-01,  3.9574e-01,  7.8404e-01,
          2.2304e-01, -3.3438e-01, -7.3206e-01, -2.1919e+00, -3.2135e-02,
         -1.6781e-01, -2.0253e-01,  4.4004e-01, -6.1304e-01,  2.4745e-01,
         -3.6635e-02,  1.4904e-02,  8.3244e-01,  1.1692e+00, -5.1180e-03,
          8.7908e-02, -1.6775e-01, -1.3079e-01,  1.4721e-01,  2.4864e-02,
          8.5185e-03,  3.8698e-01, -6.1313e-02, -2.3944e-01, -4.2810e-01,
          1.2165e-02, -6.9934e-01,  5.9511e-01,  6.5413e-02,  1.6517e+00,
          8.9990e-01,  2.6168e-01, -4.8059e-01,  2.3596e-01, -5.1618e-02,
         -8.0227e-02, -1.2266e+00,  3.1085e-01,  2.1843e-01,  7.5500e-01,
         -5.7570e-01,  2.8223e-01, -3.1907e-01, -2.7281e-01,  3.9883e-01,
          1.1388e-02, -7.5602e-01, -9.6344e-02, -1.2563e-01, -4.9292e-01,
          9.4711e-02, -6.0986e-01,  4.1158e-01,  1.8875e-01, -6.1414e-02,
          1.4057e-01,  4.0303e-01, -5.1158e-02, -1.8982e-01, -5.1902e-01,
         -9.8264e-02, -1.4236e-01,  4.3964e-01, -3.0952e-01, -4.5934e-01,
          3.4544e-01, -4.4351e-01,  4.4216e-01,  3.1383e-01, -3.0202e-01,
         -4.8837e-01,  8.3990e-02, -1.9483e-01, -2.1872e-01,  9.9306e-01,
          1.1118e-01, -5.4962e-02,  1.4239e-01,  9.7149e-03,  1.1514e-01,
         -4.1445e-01, -1.9103e-01, -2.7038e-01,  3.1524e-01,  1.1208e-01,
          4.2210e-01,  1.9307e-01,  1.0504e-01,  1.8221e-01,  4.8074e-01,
         -4.3912e-01,  4.5956e-01, -5.2105e-01, -2.5036e-01, -9.0323e-02,
         -6.3154e-01, -1.1177e-01,  3.6770e-02, -2.9274e-02, -3.0610e+00,
          4.4054e-01, -6.6310e-02,  5.5437e-01, -4.3245e-01,  3.1124e-01,
          1.7902e-01, -1.8815e-02, -4.5971e-01, -8.8597e-02,  1.6969e-01,
          1.2811e-01,  2.6628e-01, -2.0147e-01,  1.1808e-01,  4.5060e-01,
         -3.6103e-02, -2.8650e-01,  5.5448e-01, -4.8320e-01,  2.6156e-01,
          3.3975e-01,  1.9953e+00, -5.0235e-01,  1.9914e-01,  3.7423e-01,
         -3.6149e-01, -1.6496e-03,  4.2861e-01, -1.3479e-01, -1.2919e-01,
          2.2807e-01,  7.0579e-01, -4.6841e-01, -4.2355e-02,  3.6810e-01,
         -4.2379e-01,  7.9615e-02,  1.4543e-01, -2.2441e-01, -4.1462e-01,
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

**CSV & XLSX:**
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
