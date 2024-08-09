import reflex as rx 
from BioLink.components.navbar import navbar
from BioLink.views.header.header import header
from BioLink.views.links.links import links
from BioLink.components.footer import footer
import BioLink.styles.styles as styles
from BioLink.styles.styles import Size as Size


class State(rx.State):
    pass

def  index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=Size.LARGE.value
            )
        ),
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
