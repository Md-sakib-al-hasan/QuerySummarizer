# import streamlit as st
# from ai_service import generate_ai_response



# #sidebar

# st.sidebar.subheader("Controls")
# images = st.sidebar.file_uploader("upload the photos of your notes",type=["png","jpg","jpeg"],accept_multiple_files=True)

# st.sidebar.subheader("Uploaded photos")
# if images:
#     cols = st.sidebar.columns(len(images[:5]))
#     for i ,img in enumerate(images[:5]):
#         with cols[i]:
#             st.image(img)


# difficulty = st.sidebar.selectbox("Enter the difficulty of Quize",["Easy","Medium","Hard"],index=None)
# conframationsbutton = st.sidebar.button("Click the button to initiate Ai",type="primary")






# # main body start from where

# st.title("Note Summary and Quiz Generator", anchor=False)
# st.text("upload upto 3 images to generate Note summary and Auiz")
# st.divider()



# #where implement the warning and error message for user undustanding

# if conframationsbutton:
#     if not images:
#         st.error("You must upload at least one image")
#     elif not difficulty:
#         st.warning("you are not select the difficulty")
#     else:
#         result = generate_ai_response(images, difficulty)
#         st.markdown(result)



import streamlit as st 
from api_calling import note_generator ,quiz_generator , audio_transcription
from PIL import Image



#title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()


with st.sidebar:
    st.header("Controls")

    #image
    images = st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    pil_images =[]
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded images")
            
            col = st.columns(len(images))

            

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #difficulty 
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index = None
    )

    pressed= st.button("Click the button to initiate AI",type="primary")


if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty")
    
    if images and selected_option:

        #note 

        with st.container(border=True):
            st.subheader("Your note")

            #the portion below will be replaced by API Call

            with st.spinner("Ai is writing nodes for you"):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)
           




        #Audio transcipt
        with st.container(border=True):
            st.subheader("Audio Transcription")



            #the portion below will be replaced by API Call 
            with st.spinner("Voice  translate"):
                 
                audio = audio_transcription(generated_notes)
                st.audio(audio)


        #quiz

        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")

            #the portion below will be replaced by API Call 

            with st.spinner("AI is geratin the quizzes"):
                quizzes = quiz_generator(pil_images,selected_option)
                st.markdown(quizzes)






    




