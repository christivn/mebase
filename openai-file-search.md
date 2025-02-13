## 🔗 OpenAI - `file_search`

For reference, OpenAI provides `file_search` as part of their assistants:

🔗 [OpenAI File Search Documentation](https://platform.openai.com/docs/assistants/tools/file-search/quickstart#how-it-works)

The `file_search` tool enhances retrieval by:

✅ Rewriting queries for optimized search
✅ Running keyword and semantic searches
✅ Reranking results for improved relevance
✅ Supporting chunk-based retrieval

### Default Settings:
- 📏 **Chunk size:** 800 tokens
- 🔄 **Chunk overlap:** 400 tokens
- 🧠 **Embedding model:** `text-embedding-3-large` (256 dimensions)
- 🔢 **Max chunks in context:** 20
- 📊 **Ranker:** `auto`
- 🎯 **Score threshold:** 0 minimum ranking score
