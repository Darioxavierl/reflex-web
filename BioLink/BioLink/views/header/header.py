import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            fallback="Dariox",
            size="6"
        ),
        rx.text("@darioxavierpl"),
        rx.text("Hola soy Dario"),
        rx.text("Estudiante de ingeniria en Telecomunicaciones")
    )