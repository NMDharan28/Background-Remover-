import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO



def removebg(img):
    input=Image.open (img)
    return remove(input)

def main():
    st.title ("BackGround Remover App")
    uploadfile= st.file_uploader("choose an Image...",type=["jpg","jpeg","png"])

    if uploadfile is not None:
        st.image(uploadfile, caption='Uploaded image')
        result=removebg(uploadfile)

        result_image_io=BytesIO()
        result.save(result_image_io, format='PNG')
        st.image (result, caption="Successfully removed")

        st.download_button(
            label="Download Result Image",
            data=result_image_io.getvalue(),
            file_name="background_removed_image.png",
            key="download_button"
        )


if __name__=='__main__':
    main()