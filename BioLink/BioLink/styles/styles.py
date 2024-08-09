from enum import Enum
import reflex as rx


# Constants 
MAX_WIDTH = "600px"

# Sizes

class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="2em"


# Styles

BASE_STYLE = {
    rx.button: {
        "width"     : "100%",
        "height"    : "100%",
        "display"   : "block",
        "padding"   : Size.SMALL.value,
        "border_raduis" : Size.DEFAULT.value
    },
    rx.link : {
        "text_decoration" : "none",
        "_hover" : {}
    }
}

button_tittle_style = dict(
    font_size=Size.DEFAULT.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
)