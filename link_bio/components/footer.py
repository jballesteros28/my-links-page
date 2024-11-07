import reflex as rx
import datetime
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor

def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.box(
                rx.image(
                    src="/logo.svg",
                    width="70px",
                    height="auto",
                    weight="auto",
                    margin_left="auto",
                    margin_right= "auto",
                    alt="logotipo de juandev. una \"eme\"entre llaves"
                ),
                width="100%",
            ),
            rx.text(
                f"AÑO:{datetime.date.today().year}",
                font_size=styles.Size.DEFAULT.value,
                width="100%",
                align="center"
            ),
            rx.text(
                "BUILDING SOFWARE WITH ❤️ FROM COLOMBIA TO THE WORLD",
                font_size=styles.Size.DEFAULT.value
                ),
            margin_bottom=styles.Size.BIG.value,
            color= TextColor.FOOTER.value,
            margin_x=styles.Size.BIG.value
        )
    )