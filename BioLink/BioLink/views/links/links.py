import reflex as rx
from BioLink.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
       link_button("Instagram","https://instagram.com"),
       link_button("Youtube","https://youtube.com"),
       link_button("Twitch","https://twitch.tx/tjdariox")
    )