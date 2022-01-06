import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-logo.png')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!
***
""" )


st.header('Enter Dna Sequence')

sequence_input = ">DNA Query\nGAACAGGGGGGGGGGG\nDAEGGGGGGGGGGGGGGGGGGG\nTAGGGAAAAAAAAAAAAAAAA" 
sequence = st.text_area("Sequence Input",sequence_input, height=150)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('INPUT(DNA Query')
sequence

st.header('1. Print dictionary')

