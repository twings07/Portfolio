import streamlit as st

# Define your social media links
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/edward-twingstan",
    "GitHub": "https://github.com/twings07",
    "Behance": "https://www.behance.net/twingsEdward",
}

# Define icons for each social media platform
SOCIAL_MEDIA_ICONS = {
    "LinkedIn": "fab fa-linkedin",
    "GitHub": "fab fa-github",
    "Behance": "fab fa-behance",
}

# Create HTML markup for social media links with icons
social_media_html = ""
for platform, link in SOCIAL_MEDIA.items():
    icon_class = SOCIAL_MEDIA_ICONS.get(platform, "fab fa-link")
    social_media_html += f'<a href="{link}" target="_blank"><i class="{icon_class}"></i></a>&nbsp;&nbsp;'

# Render HTML markup using st.markdown
st.markdown(social_media_html, unsafe_allow_html=True)