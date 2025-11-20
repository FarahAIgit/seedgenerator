import streamlit as st
import time
import datetime

def generate_flux_seed(ritual_factor):
    now = time.time()
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    raw_seed = int((now + day_of_year) * ritual_factor)
    return raw_seed % 4294967295

st.title("Flux Seed Generator")
st.write("A cosmic seed born from time, daylight drift and the ritual factor.")

ritual_factor = st.number_input("Ritual Factor", min_value=1, max_value=9999, value=7, step=1)

if st.button("Cast the Seed"):
    seed = generate_flux_seed(ritual_factor)
    st.success(f"Your Flux Seed: {seed}")
    st.code(str(seed))
st.markdown(
    "Created by [@Farah_ai_](https://x.com/Farah_ai_)",
    unsafe_allow_html=True
)
