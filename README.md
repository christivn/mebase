# 🗃️✨ oFiles - Open Alternative to OpenAI `file_search`

[![US](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/us.png "Canada") English](/readme/en.md) -
[![Spain](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/es.png "Spain") Español](/readme/es.md) -
[![France](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/fr.png "France") Français](/readme/fr.md) -
[![Germany](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/de.png "Germany") Deutschland](/readme/de.md) -
[![China](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/cn.png "China") 中国](/readme/cn.md) -
[![India](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/in.png "China") हिंदी](/readme/in.md) -
[![Korea](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/kr.png "Korea") 한국어](/readme/kr.md)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Supabase Vector](https://img.shields.io/badge/Supabase%20Vector%20DB-000?style=for-the-badge&logo=supabase&logoColor=white)
![Embedding](https://img.shields.io/badge/EMBEDDING-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

<br>

## 📖 About oFile

oFile is an open-source alternative to OpenAI's `file_search` tool, designed to efficiently process, store, and retrieve file-based information using Supabase and embeddings.

🔹 **Extract** text from uploaded files
🔹 **Generate** chunks for efficient storage and retrieval
🔹 **Embed** text data for semantic search
🔹 **Store** and **query** embeddings using Supabase Vector DB
🔹 **Multilingual support** for better accessibility across different languages

### Index

- [📖 About oFile](#-about-ofile)  
- [💡 Why Use oFile?](#-why-use-ofile)  
- [🔧 Use Cases](#-use-cases)  
- [🚀 How It Works](#-how-it-works)  
- [📝 Documentation](#-documentation)  
  - [⬆️ Upload File](#️-upload-file)  
  - [📄 Transform File to Text](#-transform-file-to-text)  
  - [🧩 Chunks Generation](#-chunks-generation)  
  - [🔗 Embedding the Chunks](#-embedding-the-chunks)  
  - [🗄️ Upload to Supabase](#️-upload-to-supabase)  
  - [🔎 Search & Retrieval](#-search--retrieval)  
- [🛠️ Installation & Setup](#️-installation--setup)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  

<br>

## 💡 Why Use oFile?

💰 **Open-source & Cost-effective** - No reliance on proprietary APIs.
⚡ **Fast & Scalable** - Uses Supabase Vector for high-performance retrieval.
🔍 **Accurate Search** - Supports semantic search with embeddings.
📂 **Flexible & Extensible** - Easily integrates with different file formats and databases.
**🌐 Multilingual Support** - Process and retrieve information in multiple languages.

<br>

## 🔧 Use Cases

oFile can be used in various applications that require efficient file-based information retrieval and knowledge management:

📚 **AI-Powered Knowledge Bots** – Create AI assistants that can answer questions based on custom document databases.  
🎯 **Recommendation Algorithms** – Build personalized recommendation systems using semantic search.  
🔍 **Legal & Compliance Research** – Quickly retrieve relevant documents and case laws based on contextual search.  
📖 **Academic & Research Tools** – Enable efficient searching through large collections of research papers and books.  
💼 **Enterprise Knowledge Management** – Organize and search internal company documentation with ease.  
🤖 **Chatbot Integration** – Enhance chatbots with document-based memory for more informed responses.  
📂 **Automated Data Extraction** – Process and analyze structured and unstructured text data from various file formats.  

<br>

## 🚀 How It Works

oFile follows a structured process to ensure high-quality search and retrieval:

1. **Upload:** Accepts files and extracts text.
2. **Chunking:** Splits text into overlapping segments for better context.
3. **Embedding:** Converts text chunks into vector representations.
4. **Storage:** Saves embeddings in a vector database.
5. **Search & Retrieval:** Uses semantic search to find relevant information based on user queries.

<br><br>

---

<br><br>

## 📝 Documentation

### ⬆️ Upload File
Users can upload various file formats (e.g., `.pdf`, `.txt`, `.csv`). The system extracts text content for further processing.

<br>

### 📄 Transform File to Text
Extracts meaningful text from the uploaded file using different parsing methods based on file type.

<br>

### 🧩 Chunks Generation
Splits the extracted text into manageable chunks to optimize search and retrieval performance.

<br>

### 🔗 Embedding the Chunks
Each chunk is embedded using a powerful embedding model, allowing for efficient similarity-based search.

<br>

### 🗄️ Upload to Supabase
Stores the embedded chunks in Supabase's vector database for fast and accurate querying.

<br>

### 🔎 Search & Retrieval
Uses semantic search to find relevant information based on user queries.

<br><br>

---

<br><br>

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-repo/ofile.git

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (Supabase keys, embedding model API keys, etc.)
export SUPABASE_URL=your_supabase_url
export SUPABASE_KEY=your_supabase_key

# Run the application
python main.py
```

<br>

## 🤝 Contributing

We welcome contributions! Feel free to open issues, submit pull requests, or suggest improvements.

📩 **Contact:** Reach out via GitHub Issues or Discussions.

<br>

## 📜 License

MIT License. See `LICENSE` for details.

