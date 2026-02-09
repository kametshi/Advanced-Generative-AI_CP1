import os
import gradio as gr
from dotenv import load_dotenv

from ingest import ingest_all_pdfs, chroma_count
from rag import retrieve
from ticketing import create_trello_ticket

load_dotenv()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_LIST_ID = os.getenv("TRELLO_LIST_ID")

# -------------------------
# INDEX
# -------------------------

def build_index(progress=gr.Progress()):
    def callback(msg):
        progress(0.1, desc=msg)

    total = ingest_all_pdfs(progress_callback=callback)
    return f"Index built. Total chunks: {total}"


# -------------------------
# CHAT
# -------------------------

def chat(message, history, state):
    # Авто-индексация если база пустая
    if chroma_count() == 0:
        ingest_all_pdfs()

    results = retrieve(message)

    if not results:
        answer = (
            "I couldn't find relevant information in the documents.\n"
            "You can create a support ticket."
        )
    else:
        answer = ""
        for r in results:
            answer += (
                f"Source: {r['source']} (page {r['page']})\n\n"
                f"{r['text'][:500]}\n\n---\n\n"
            )

    history.append((message, answer))
    state.append((message, answer))

    return history, state


# -------------------------
# CREATE TICKET
# -------------------------

def create_ticket(state):
    if not state:
        return "No conversation available."

    if not (TRELLO_API_KEY and TRELLO_TOKEN and TRELLO_LIST_ID):
        return "Trello secrets missing."

    description = ""
    for q, a in state:
        description += f"USER: {q}\n\nASSISTANT: {a}\n\n"

    try:
        create_trello_ticket(
            title="Customer Support Request (RAG)",
            description=description
        )
        return "Support ticket created successfully."
    except Exception as e:
        return f"Error creating ticket: {str(e)}"


# -------------------------
# UI
# -------------------------

with gr.Blocks() as demo:
    gr.Markdown("# Customer Support Chat (RAG)")

    # INDEX
    with gr.Row():
        index_button = gr.Button("Build / Rebuild Index")
        index_status = gr.Textbox(label="Index status")

    index_button.click(
        fn=build_index,
        outputs=index_status
    )

    # CHAT
    chatbot = gr.Chatbot()
    chat_state = gr.State([])

    msg = gr.Textbox(label="Ask a question")
    send = gr.Button("Send")

    send.click(
        fn=chat,
        inputs=[msg, chatbot, chat_state],
        outputs=[chatbot, chat_state]
    )

    # TICKET
    ticket_button = gr.Button("Create support ticket")
    ticket_status = gr.Textbox(label="Ticket status")

    ticket_button.click(
        fn=create_ticket,
        inputs=chat_state,
        outputs=ticket_status
    )

demo.launch()
