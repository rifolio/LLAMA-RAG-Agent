import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader

'''
 checking if index exists/creating index usig llama_index vector storage
 from llama index documetation: https://docs.llamaindex.ai/en/stable/getting_started/starter_example/ and https://docs.llamaindex.ai/en/stable/examples/vector_stores/AsyncIndexCreationDemo/
'''

def get_index(data, index_name):
    index = None #initial state
    if not os.path.exists(index_name):
        print(f"creating index: {index_name}")
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


pdf_path = os.path.join("data/Ukraine.pdf")
ukraine_pdf = PDFReader().load_data(file=pdf_path) # https://llamahub.ai/l/readers/llama-index-readers-file?from=readers
ukraine_index = get_index(ukraine_pdf, "ukraine")
ukraine_engine = ukraine_index.as_query_engine()