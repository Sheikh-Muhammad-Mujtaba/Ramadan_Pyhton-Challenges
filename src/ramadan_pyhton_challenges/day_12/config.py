import chainlit as cl

# App metadata & UI customization
cl.set_app_name("CyberSheikh AI")  # App name in the sidebar
cl.set_logo("./assets/logo_dark.png")  # Logo URL (transparent PNG recommended)
cl.set_author("Sheikh Mujtaba")  # Author name

# Theme customization (Light/Dark)
cl.set_theme(
    light=cl.Theme(
        primary_color="#4F46E5",  # Purple (tailwind indigo-600)
        background_color="#FFFFFF",  # White
        text_color="#1F2937",  # Gray-800
    ),
    dark=cl.Theme(
        primary_color="#7C3AED",  # Dark purple
        background_color="#1F2937",  # Dark gray
        text_color="#FFFFFF",  # White
    ),
)

# Chat settings
cl.set_chat_settings(
    max_chat_messages=100,  # Limit chat history length
    enable_audio=False,  # Disable microphone input
)


