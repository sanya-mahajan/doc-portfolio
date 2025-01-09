import streamlit as st
from streamlit_folium import st_folium
import folium

# Page Configuration
st.set_page_config(page_title="Dr. Manish Gupta, Dentist", layout="wide")

# Header Section with Image and Text Alignment
st.title("Dr. Manish Gupta")
col1, col2 = st.columns([1, 2])  

with col1:
    st.image("doc.jpeg", width=200)

with col2:
    st.header("Dental Surgeon")
    st.markdown("""
    **Jammu**
    

    - I specialize in providing advanced dental care with a focus on patient comfort and excellence.
    - 25+ years of experience in dental surgery and treatment.

    🕒 **Visiting Hours:**
    - **Monday - Saturday**: 10:00 AM - 1:30 PM, 5:00 PM - 8:00 PM
    - **Sunday**: Closed

    📞 **Contact Number**: [9419192109](tel:9419192109)
    """)

# Google Maps Section
st.header("Find My Clinics")

st.markdown("""
**📍 Locations:**

- [**Clinic 1**: Oral Care Dental and Implant Centre, Shop no. 12, Municipal Market, Bakshi Nagar, Jammu](https://maps.app.goo.gl/pcMTMzT7wYzuwDxq5)
- [**Clinic 2**: Opp. railway crossing, sec3, Channi Himat, Jammu](https://maps.app.goo.gl/hFnWiWAtpEXsuMpN7)
""")

# Coordinates for the clinics
locations = {
    "Clinic 1": (32.73869234413952, 74.85254710980048),  
    "Clinic 2": (32.68939288205767, 74.88599785420551) 
}

# Initialize map
m = folium.Map(location=[32.73869234413952, 74.85254710980048], zoom_start=6)

# Add markers for clinics
for clinic, coord in locations.items():
    folium.Marker(coord, popup=clinic).add_to(m)

# Render map
st_folium(m, width=300, height=200)

st.header("🏥 Clinic Images")
carousel_html = """
<div id="clinicCarousel" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://via.placeholder.com/700x400?text=Clinic+1" class="d-block w-100" alt="Clinic 1">
    </div>
    <div class="carousel-item">
      <img src="https://via.placeholder.com/700x400?text=Clinic+2" class="d-block w-100" alt="Clinic 2">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#clinicCarousel" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#clinicCarousel" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
"""

st.markdown(
    carousel_html,
    unsafe_allow_html=True
)


# Footer
st.write("© 2025 Dr. Manish Gupta. All rights reserved.")
