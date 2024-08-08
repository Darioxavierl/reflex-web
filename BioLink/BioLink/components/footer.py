import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            rx.text(f"{datetime.date.today().year} Developer - Dario Portilla"),
            href="#",
            is_external=True
        ),
        rx.text("Estudiante - Freelancer")
    )