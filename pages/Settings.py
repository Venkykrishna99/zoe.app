import streamlit as st

st.title("⚙️ Settings")

st.text_input("✉️ Email Address")
st.date_input("📅 Select Date")
st.time_input("⏰ Select Time")
st.color_picker("🎨 Pick a Color")
st.file_uploader("📤 Upload a File")

if st.button("💾 Save Settings"):
    st.success("Settings saved!")
