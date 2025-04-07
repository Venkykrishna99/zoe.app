import streamlit as st
import base64

st.set_page_config(page_title="Electrogadgedc", layout="wide")

# Sidebar theme switcher
mode = st.sidebar.radio("🎨 Theme", ["Light", "Dark"])

# Background image
def set_bg(local_image_file):
    with open(local_image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
        st.markdown(f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: {'white' if mode == 'Dark' else 'black'};
            }}
            </style>
        """, unsafe_allow_html=True)

set_bg("WhatsApp.jpg")

# Particle animation
st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/tsparticles@2.11.1/tsparticles.bundle.min.js"></script>
<div id="tsparticles" style="position:fixed; z-index:0; top:0; left:0; width:100%; height:100%;"></div>
<script>
    tsParticles.load("tsparticles", {
        fullScreen: { enable: true, zIndex: 0 },
        particles: {
            number: { value: 50 },
            color: { value: "#ffffff" },
            shape: { type: "circle" },
            opacity: { value: 0.5 },
            size: { value: { min: 1, max: 5 }},
            move: { enable: true, speed: 1 }
        }
    });
</script>
""", unsafe_allow_html=True)

# App intro
st.title("⚡ Electrogadgedc Dashboard")
st.markdown("Welcome to your interactive dashboard. Use the left sidebar to explore different pages.")

# Floating button
st.markdown("""
<style>
.fab {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #00b4d8;
  color: white;
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  font-size: 28px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.3);
  z-index: 9999;
  transition: 0.3s;
}
.fab:hover {
  background-color: #0096c7;
  cursor: pointer;
}
</style>
<button class="fab" onclick="alert('Add New!')">+</button>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("Crafted with ❤️ using Streamlit")
