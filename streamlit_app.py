import streamlit as st
import numpy as np
from PIL import Image
import os

st.title("YOLOv5 Object Detection")

if st.button("Detect Objects"):
    os.system('python phone_detector.py --weights phone_detector.pt --source 1')
