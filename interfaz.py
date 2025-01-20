from bot import consulta
import gradio

iface = gradio.ChatInterface(type="messages",
    fn = consulta,
    chatbot = gradio.Chatbot(height=300, type="messages"),
    textbox = gradio.Textbox(placeholder="Hazme una pregunta", container=False, scale=7),
    title="Medisur",
    description="Escribe tu consulta")

if __name__ == "__main__":
    iface.launch(inbrowser=True, share=True)