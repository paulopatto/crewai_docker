#!/usr/bin/env python

import gradio as Gradio
from dotenv import load_dotenv 

from app.crew import MyCrew
import app.settings

load_dotenv()


def run(input):
    inputs = { 'topic': input }
    return MyCrew().crew().kickoff(inputs=inputs)

iface = Gradio.Interface(
    fn=run, 
    inputs=Gradio.Textbox(label="Insira aqui seu comando:"), 
    outputs="markdown",
    title="CrewAI",
    description=("")
)

iface = Gradio.Interface(
    fn=run, 
    inputs=Gradio.Textbox(label="Insira aqui seu comando:"),
    outputs="markdown",
    title="CrewAI",
    description=(""),
    css="footer{display:none !important}"
)
iface.launch()

