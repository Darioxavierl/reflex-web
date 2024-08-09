import reflex as rx
from BioLink.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
       link_button("Instagram","Link a Instagram","https://instagram.com"),
       link_button("Youtube","Link a Youtube","https://youtube.com"),
       link_button("Twitch","Link a Twitch","https://twitch.tx/tjdariox"),
       width = "100%"
    )