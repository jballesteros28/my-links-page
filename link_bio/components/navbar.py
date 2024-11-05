import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color
from link_bio.styles.colors import TextColor
from link_bio.styles.modes import dark_mode_toggle

def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.text.span("Juan",color=Color.PRIMARY.value,as_="span"),
            rx.text.span("dev",color=Color.SECONDARY.value,as_="span"),
            style=styles.navbar_tittle_style,
        ),
        rx.spacer(),
        dark_mode_toggle(),
        style=styles.navbar_style
    )