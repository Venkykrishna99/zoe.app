import streamlit as st

st.title("🎬 Media Preview")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎧 Audio")
    st.audio("lokiverse.mp3")

with col2:
    st.subheader("🎥 Video")
    st.video("video.mp4")

st.balloons()
