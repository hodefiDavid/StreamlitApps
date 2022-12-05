import random
import streamlit as st
import math

# from sklearn.externals import joblib
import time
from PIL import Image

def load_images(file_name):
  img = Image.open(file_name)
  return st.image(img,width=300)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)
# need to change to our actual code
def algo_to_det(doration, sent, recived)-> int:
    ans = 0 
    dot = [sent,recived]
    # k cluster info embeded here
    centroids = [[ 487 , 2868 ],[ 248 , 4910544 ],[ 238 , 30046 ],[ 245 , 343635 ]]
    distance = 4000
    arr = []
    arr.append(math.dist(centroids[0], dot))
    arr.append(math.dist(centroids[1], dot))
    arr.append(math.dist(centroids[2], dot))
    arr.append(math.dist(centroids[3], dot))
    arr.sort()
    if arr[0] < distance:
      ans += 1 
    avgSent = 474.2478980792457 
    distSent = 150 
    avgRecive = 4473.532613862158 
    medianRecive = 1661.0
    medianSent = 249.0 
    distRecive = 1500 

    if abs(dot[0] - avgSent) < distSent or abs(dot[0] - medianSent) < distSent:
      ans += 1 
    if abs(dot[1] - avgRecive) < distRecive or abs(dot[1] - medianRecive) < distRecive:
      ans  += 0.7 #this is the result that we get 
    return ans

def main():
  """anomaly Classifier App
    With Streamlit

  """

  st.title("Anomaly Classifier")
  html_temp = """
  <div style="background-color:blue;padding:10px">
  <h2 style="color:grey;text-align:center;">Streamlit App </h2>
  </div>

  """
  st.markdown(html_temp,unsafe_allow_html=True)
#   load_css('icon.css')
#   load_icon('people')

  sent_packets = st.number_input("Enter sent packets",min_value=0)
  recive_packets = st.number_input("Enter recive packets",min_value=0)
  duration = st.number_input("Enter duration",min_value=0)
  
  if st.button("Predict"):
    result = algo_to_det(duration,sent_packets,recive_packets)
    if result < 1:
      prediction = 'Bad'
      img = 'bad.png'
    else:
      prediction = 'Good'
      img = 'good.png'

    st.success('The data: sent packets: {}\trevive packets {}\t douratrion:{} \nwas classified as {}'.format(sent_packets,recive_packets,duration,prediction))
    load_images(img)

print("#hetchlno")
main()