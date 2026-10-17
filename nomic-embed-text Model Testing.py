from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(model = "nomic-embed-text")

text = "If you expect disappointment, then you can never really be disappointed."

vector = embedding_model.embed_query(text)

#print(vector)
print(len(vector))

docs = ["If you expect disappointment,", "then you can never really be disappointed."]

docs_vector = embedding_model.embed_documents(docs)
print(len(docs_vector))