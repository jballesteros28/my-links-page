import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor
from link_bio.styles.fonts import FontWeight
import link_bio.styles.styles as styles


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f" {body}",
        font_size=FontWeight.CLASIC.value,
        style=styles.color_text_body
    )