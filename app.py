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
bounds = [coord for coord in locations.values()] 
folium.FitBounds(bounds).add_to(m)

# Add markers for clinics
for clinic, coord in locations.items():
    folium.Marker(coord, popup=clinic).add_to(m)

# Render map
st_folium(m, width=700, height=500)

st.header("🏥 Clinic Images")

# Clinic Images in a Grid Layout
clinic_images = [
    {
        "url": "https://res.cloudinary.com/dy0nzogyx/image/upload/v1736591998/WhatsApp_Image_2025-01-11_at_3.54.05_PM_1_eogvxy.jpg",
        "alt": "Clinic 1",
    },
    {
        "url": "https://res.cloudinary.com/dy0nzogyx/image/upload/v1736591998/WhatsApp_Image_2025-01-11_at_3.54.04_PM_auwiqz.jpg",
        "alt": "Clinic 2",
    },
    {
        "url": "https://res.cloudinary.com/dy0nzogyx/image/upload/v1736591997/WhatsApp_Image_2025-01-11_at_3.54.04_PM_1_latfyp.jpg",
        "alt": "Clinic 3",
    },
]

image_width = 300
image_height = 200

# Create a grid layout with 3 columns
cols = st.columns(3)

for idx, clinic in enumerate(clinic_images):
    with cols[idx % 3]:  # Dynamically assign images to columns
        st.image(
            clinic["url"],
            caption=clinic["alt"],
            width=image_width,
            output_format="JPEG",
        )
# Footer
st.write("© 2025 Dr. Manish Gupta. All rights reserved.")
