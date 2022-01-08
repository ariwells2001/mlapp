import pandas as pd
import numpy as np
import streamlit as st
from os import listdir
from os.path import isfile, join
from PIL import Image
import Training
import Testing
from keras.models import load_model
from keras import backend as K
from PIL import Image
from pathlib import Path
import os

showpred = 0
try:
	model_path = './models/model.h5'
	model_weights_path = './models/weights.h5'
except: 
	print("Need to train model")


# Ari Wells
def load_image(image_file):
    img = Image.open(image_file)
    return img


test_path = 'C:/Users/rkarm/Downloads/Data/Test'


target_dir = './ariwells/'

if not os.path.exists(target_dir):
      os.mkdir(target_dir)


#Load the pre-trained models
model = load_model(model_path)
model.load_weights(model_weights_path)
st.sidebar.title("About")

st.sidebar.info(
    "This is a demo application written to help you understand Streamlit. The application identifies the animal in the picture. It was built using a Convolution Neural Network (CNN).")

onlyfiles = [f for f in listdir("C:/Users/rkarm/Downloads/Data/Train/elephant") if isfile(join("C:/Users/rkarm/Downloads/Data/Train/elephant", f))]
#onlyfiles =str(onlyfiles)
#st.write(onlyfiles)
st.sidebar.title("Train Neural Network")
if st.sidebar.button('Train CNN'):
    Training.train()
    #st.write()
st.sidebar.title("Predict New Images")
#imageselect = st.sidebar.selectbox("Pick an image.", onlyfiles)


st.title('Living Organism Identification')
st.write("Pick an image from the left. You'll be able to view the image.")
st.write("When you're ready, submit a prediction on the left.")
st.write("Only detectable for cat, elephant, horse and human being")

st.write("")
image_file = st.sidebar.file_uploader("Upload Images",type=["png","jpg","jpeg"])
if image_file is not None:
    st.image(load_image(image_file),width=500)
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    #st.write(file_details)
    #img = load_image(image_file)
    #st.image(img,height=250,width=250)
    with open(os.path.join(target_dir,image_file.name),"wb") as f: 
      f.write(image_file.getbuffer())         
    #st.success("Saved File")
    #st.write(image_file.name)
    
#image = Image.open("C:/Users/rkarm/Downloads/Data/Train/elephant/" + imageselect)
#st.image(image, caption="Let's predict the animal!", use_column_width=True)
if st.sidebar.button('Predict a Living Organism'):
    showpred = 1
    #prediction = Testing.predict((model),"C:/Users/rkarm/Downloads/Data/Train/elephant/" + imageselect)
    #prediction = Testing.predict((model),image_file)
    prediction = Testing.predict((model),target_dir + image_file.name)
if showpred == 1:
    if prediction == 0:
        st.write("This is a **cat!**")
        image = Image.open("C:/Users/rkarm/Downloads/Data/mycat.jpg")
        st.image(image,width = 200)
    if prediction == 1:
        st.write("This is an **elephant!**")
        image = Image.open("C:/Users/rkarm/Downloads/Data/myelephant.png")
        st.image(image,width = 200)
    if prediction == 2:
        st.write("This is a **horse!**")
        image = Image.open("C:/Users/rkarm/Downloads/Data/myhorse.jpg")
        st.image(image,width = 200)
    if prediction == 3:
        st.write("This is a **human being**")
        image = Image.open("C:/Users/rkarm/Downloads/Data/myhuman.jpg")
        st.image(image,width = 200)