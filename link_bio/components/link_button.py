import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size
from link_bio.styles.styles import Font
import link_bio.views.links.constant as constant

def link_button(tittle: str, body: str,image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src= image,
                    margin_top=styles.Size.SMALL,
                    height=styles.Size.VERY_BIG.value,
                    alt=tittle
                ),
                rx.vstack(
                    rx.text(
                        tittle,
                        style= styles.tittle_style
                    ),
                    rx.text(
                        body,
                        style= styles.boddy_style
                    ),
                    spacing="1",

                ),
                width="100%",
                align="start"
            ),
            width="100%",
            style=styles.background_button_style
        ),
        href= url, 
        is_external= True,
        width="100%"
    )



