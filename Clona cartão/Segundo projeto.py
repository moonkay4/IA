import os
import kivy
from kivy.app import app
from kivy.uix.boxlayout import boxlayout
from kivy.uix.textimput import textimput
from kivy.uix.button import button
from kivy.uix.scrollview import scrollview
from kivy.uix.label import label
from kivy.core.window import window
import requests
import json

# Configuração de cores (cores escuras, preto e azul ciano)
Window.clearcolor = (0.05, 0.05, 0.05, 1) # Cor de fundo (preto)

class ChatApp(App):
    def build(self):
        # Layout principal
        self.layout = boxlayout(orientation='vertical', padding=10, spacing=10)

        # ScrollView para eibir as mensagens
        self.scroll = ScrollView(size_hint=(1, 0.8))

