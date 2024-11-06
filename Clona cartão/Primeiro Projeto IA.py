import os
from groq import groq

# Defina a chave de API diretamente no codigo ou garanta que ela esteja configurada corretamente no ambiente
os.environ["GROQ_API_KEY"] = "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"
Client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


# Inicializa a lista de mensagens para manter o contextoda conversa
messages = []

while true:
     usuario = input("Digite uma mensagem ou 'sair' para encerrar: ")

     if usuario.lower() == 'sair':
        print("Conversa encerrada.")
        break

    # Adiciona a mensagem do usuario à lista de mensagens
    messages.append(("role": "user", "content": usuario))
     chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-60b-versatile",
    )


    resposta = chat_completion.choices[0].messages.content
    print("Resposta:", resposta)

    # Adiciona a resposta do assistente à lista de mensagens para manter o contexto
    messages.append({"role": "assistant", "Content": resposta})