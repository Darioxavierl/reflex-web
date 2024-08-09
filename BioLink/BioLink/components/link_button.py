import reflex as rx
import BioLink.styles.styles as styles

def link_button(title: str, body: str, url: str) -> rx.Component:
    return  rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_right",
                    width=styles.Size.DEFAULT,
                    height=styles.Size.LARGE
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_tittle_style),
                    rx.text(body,style=styles.button_body_style)
                )
                
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )