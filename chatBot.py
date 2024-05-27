


import os
from llmware.library import Library
from llmware.retrieval import Query
from llmware.setup import Setup
from llmware.status import Status
from llmware.prompts import Prompt
from llmware.configs import LLMWareConfig




    
####################### SETUP #######################

LLMWareConfig().set_active_db("sqlite")


embedding_model_name = "industry-bert-contracts"


vector_db = "faiss"

# pick any name for the library
library_name = "example5_library"

example_models = ["llmware/bling-1b-0.1", "llmware/bling-tiny-llama-v0", "llmware/dragon-yi-6b-gguf"]


llm_model_name = example_models[2]


change=0

####################### END SETUP ###################



####################### LIBRARY SETUP #####################################



print ("\nupdate: Step 1 - Creating library: {}".format(library_name))

library = Library().create_new_library(library_name)


print ("update: Step 2 - Get Files")

sample_files_path = "/Users/jimgrillakis/Documents/llm/data"
contracts_path = os.path.join(sample_files_path, "Harvard_Handbook")


print("update: Step 3 - Parsing and Text Indexing Files")

library.add_files(input_folder_path=contracts_path)

# Install the embeddings
print("\nupdate: Step 4 - Generating Embeddings in {} db - with Model- {}".format(vector_db, embedding_model_name))

library.install_new_embedding(embedding_model_name=embedding_model_name, vector_db=vector_db)

####################### END LIBRARY SETUP #####################################




def Ask(q):


    ##................................RAG START................................##

    # RAG steps start here ...

    print("\nupdate: Loading model for LLM inference - ", llm_model_name)

    prompter = Prompt().load_model(llm_model_name)

    query = q

    

    
    results = Query(library).semantic_query(query, result_count=50, embedding_distance_threshold=1.0)

    #   if you want to look at 'results', uncomment the two lines below
    #   for i, res in enumerate(results):
    #       print("update: ", i, res["file_source"], res["distance"], res["text"])

    for i, contract in enumerate(os.listdir(contracts_path)):

        qr = []

        if contract != ".DS_Store":

            print("\nContract Name: ", i, contract)

            
            for j, entries in enumerate(results):

                library_fn = entries["file_source"]
                if os.sep in library_fn:
                    # it handles difference in windows file formats vs. mac / linux
                    library_fn = library_fn.split(os.sep)[-1]

                if library_fn == contract:
                    print("Top Retrieval: ", j, entries["distance"], entries["text"])
                    qr.append(entries)

            #   we will add the query results to the prompt
            source = prompter.add_source_query_results(query_results=qr)

            #   run the prompt
            response = prompter.prompt_with_source(query, prompt_name="default_with_context", temperature=0.3)

            #   note: prompt_with_resource returns a list of dictionary responses
            #   -- depending upon the size of the source context, it may call the llm several times
            #   -- each dict entry represents 1 call to the LLM

            for resp in response:
                if "llm_response" in resp:
                    print("\nupdate: llm answer - ", resp["llm_response"])
                    return resp["llm_response"]

            # start fresh for next document
            prompter.clear_source_materials()

            

            ##................................RAG END..................................##



def Ask2(q,New_library,New_contracts_path):


    ##................................RAG START................................##

    # RAG steps start here ...

    print("\nupdate: Loading model for LLM inference - ", llm_model_name)

    prompter = Prompt().load_model(llm_model_name)

    query = q

   

    
    results = Query(New_library).semantic_query(query, result_count=50, embedding_distance_threshold=1.0)

    #   if you want to look at 'results', uncomment the two lines below
    #   for i, res in enumerate(results):
    #       print("update: ", i, res["file_source"], res["distance"], res["text"])

    for i, contract in enumerate(os.listdir(New_contracts_path)):

        qr = []

        if contract != ".DS_Store":

            print("\nContract Name: ", i, contract)

            
            for j, entries in enumerate(results):

                library_fn = entries["file_source"]
                if os.sep in library_fn:
                    # it handles difference in windows file formats vs. mac / linux
                    library_fn = library_fn.split(os.sep)[-1]

                if library_fn == contract:
                    print("Top Retrieval: ", j, entries["distance"], entries["text"])
                    qr.append(entries)

            #   we will add the query results to the prompt
            source = prompter.add_source_query_results(query_results=qr)

            #   run the prompt
            response = prompter.prompt_with_source(query, prompt_name="default_with_context", temperature=0.3)

            #   note: prompt_with_resource returns a list of dictionary responses
            #   -- depending upon the size of the source context, it may call the llm several times
            #   -- each dict entry represents 1 call to the LLM

            for resp in response:
                if "llm_response" in resp:
                    print("\nupdate: llm answer - ", resp["llm_response"])
                    return resp["llm_response"]

            # start fresh for next document
            prompter.clear_source_materials()

            

            ##................................RAG END..................................##


def Ask3(q,llm_model_name):


    ##................................RAG START................................##

    # RAG steps start here ...

    print("\nupdate: Loading model for LLM inference - ", llm_model_name)

    prompter = Prompt().load_model(llm_model_name)

    query = q

  

    
    results = Query(library).semantic_query(query, result_count=50, embedding_distance_threshold=1.0)

    #   if you want to look at 'results', uncomment the two lines below
    #   for i, res in enumerate(results):
    #       print("update: ", i, res["file_source"], res["distance"], res["text"])

    for i, contract in enumerate(os.listdir(contracts_path)):

        qr = []

        if contract != ".DS_Store":

            print("\nContract Name: ", i, contract)

           
            for j, entries in enumerate(results):

                library_fn = entries["file_source"]
                if os.sep in library_fn:
                    # it handles difference in windows file formats vs. mac / linux
                    library_fn = library_fn.split(os.sep)[-1]

                if library_fn == contract:
                    print("Top Retrieval: ", j, entries["distance"], entries["text"])
                    qr.append(entries)

            #   we will add the query results to the prompt
            source = prompter.add_source_query_results(query_results=qr)

            #   run the prompt
            response = prompter.prompt_with_source(query, prompt_name="default_with_context", temperature=0.3)

            #   note: prompt_with_resource returns a list of dictionary responses
            #   -- depending upon the size of the source context, it may call the llm several times
            #   -- each dict entry represents 1 call to the LLM

            for resp in response:
                if "llm_response" in resp:
                    print("\nupdate: llm answer - ", resp["llm_response"])
                    return resp["llm_response"]

            # start fresh for next document
            prompter.clear_source_materials()

            

            ##................................RAG END..................................##

















from tkinter import *

# GUI
root = Tk()
root.title("PdfChatBot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function

def send():
    
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    global change
    global New_library,New_contracts_path

    user_q = e.get().lower()

    

    # /User/file1/file2/path
    
    if (user_q[0]=="/"):
        change= 1
        txt.insert(END, "\n" + "Bot -> changing file path to "+user_q)
        library = Library().create_new_library(library_name)
        sample_files_path = user_q
        contracts_path = os.path.join(sample_files_path, "Harvard_Handbook")
        library.add_files(input_folder_path=contracts_path)
        library.install_new_embedding(embedding_model_name=embedding_model_name, vector_db=vector_db)
        
    # ./Users/file1/file2/path,FOLDER

    elif (user_q[0]=="."):

        
        change= 1
        text = user_q.split(",")
        txt.insert(END, "\n" + "Bot -> changing file path to "+text[0][1:]+" And folder to "+text[1])
        New_library_name = text[1]
        New_library = Library().create_new_library(New_library_name)
        New_sample_files_path = text[0][1:]
        New_contracts_path = os.path.join(New_sample_files_path, text[1][0:])
        New_library.add_files(input_folder_path=New_contracts_path)
        New_library.install_new_embedding(embedding_model_name=embedding_model_name, vector_db=vector_db)
        print("done")
        
    elif (user_q == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
    elif(user_q == "how are you"):
        txt.insert(END, "\n" + "Bot -> i am fine , thanks for asking")
    elif(user_q == "tell me a joke"):
        txt.insert(END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.!")
    elif(user_q[0] == "g" and user_q[1]=="p" and user_q[2]=="t"):
        
        txt.insert(END, "\n" + "Bot -> GPT Mode Activated")
        #   text = user_q.split(",")
        #   change = 2
        #   to swap in a gpt-4 openai model - uncomment these two lines and the elif(change) == 2
        #   New_llm_model_name = "gpt-4"
        #   os.environ["USER_MANAGED_OPENAI_API_KEY"] = text[1] #"<insert-your-openai-key>"
    elif(change == 1):
        
        Bot_Ans = Ask2(user_q,New_library,New_contracts_path)
        txt.insert(END, "\n" + "Bot -> "+Bot_Ans)
    # elif(change == 2):
        
    #     Bot_Ans = Ask3(user_q,New_llm_model_name)
    #     txt.insert(END, "\n" + "Bot -> "+Bot_Ans)
    else:
        Bot_Ans = Ask(user_q)
        txt.insert(END, "\n" + "Bot -> "+Bot_Ans)
        


    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="AI ChatBot", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()
