import streamlit as st
from ai_service import generate_ai_response



#sidebar

st.sidebar.subheader("Controls")
images = st.sidebar.file_uploader("upload the photos of your notes",type=["png","jpg","jpeg"],accept_multiple_files=True)

st.sidebar.subheader("Uploaded photos")
if images:
    cols = st.sidebar.columns(len(images[:5]))
    for i ,img in enumerate(images[:5]):
        with cols[i]:
            st.image(img)


difficulty = st.sidebar.selectbox("Enter the difficulty of Quize",["Easy","Medium","Hard"],index=None)
conframationsbutton = st.sidebar.button("Click the button to initiate Ai",type="primary")






# main body start from where

st.title("Note Summary and Quiz Generator", anchor=False)
st.text("upload upto 3 images to generate Note summary and Auiz")
st.divider()



#where implement the warning and error message for user undustanding

if conframationsbutton:
    if not images:
        st.error("You must upload at least one image")
    elif not difficulty:
        st.warning("you are not select the difficulty")
    else:
        result = generate_ai_response(images, difficulty)
        st.markdown(result)

    




