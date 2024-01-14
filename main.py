import streamlit as st
from rembg import remove
from PIL import Image



def removebg(img):
    input=Image.open (img)
    return remove(input)

def main():
    st.title ("BackGround Remover App")
    uploadfile= st.file_uploader("choose an Image...",type=["jpg","jpeg","png"])

    if uploadfile is not None:
        st.image(uploadfile, caption='Uploaded image')
        st.write ("Processing.... please wait")
        result=removebg(uploadfile)
        st.image (result, caption="Successfully removed")


if __name__=='__main__':
    main()