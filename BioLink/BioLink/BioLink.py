import reflex as rx 
from BioLink.components.navbar import navbar
from BioLink.views.header.header import header
from BioLink.views.links.links import links
from BioLink.components.footer import footer


class State(rx.State):
    pass

def  index() -> rx.Component:
    return rx.box(
        rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
        )
    )


app = rx.App()
app.add_page(index)
