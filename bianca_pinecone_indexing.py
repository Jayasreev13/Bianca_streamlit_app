

!pip install --upgrade langchain openai  -q

!pip install sentence_transformers -q

!apt-get install poppler-utils

!pip install unstructured -q
!pip install unstructured[local-inference] -q
!pip install detectron2@git+https://github.com/facebookresearch/detectron2.git@v0.



from google.colab import drive
drive.mount('/content/drive')

!pip install langchain

! pip install unstructured

from langchain.document_loaders import DirectoryLoader

#directory = '/content/drive/MyDrive/data/'
directory = '/data/*'
def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

documents = load_docs(directory)
len(documents)

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(documents,chunk_size=500,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

docs = split_docs(documents)
print(len(docs))

print(docs[8].page_content)

!pip install sentence_transformers

from langchain.embeddings import SentenceTransformerEmbeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

query_result = embeddings.embed_query("Hi Binaca!")
len(query_result)

!pip install pinecone-client -q

import pinecone
from langchain.vectorstores import Pinecone
# initialize pinecone
pinecone.init(
    api_key="7aa80980-98cc-47b4-b3f9-6ff582e41f9e",  
    environment="gcp-starter"  
)

index_name = "bianca-chatbot"

index = Pinecone.from_documents(docs, embeddings, index_name=index_name)

def get_similiar_docs(query,k=1,score=False):
  if score:
    similar_docs = index.similarity_search_with_score(query,k=k)
  else:
    similar_docs = index.similarity_search(query,k=k)
  return similar_docs

query = "List the behaviours that turn girls off"
similar_docs = get_similiar_docs(query)
similar_docs
