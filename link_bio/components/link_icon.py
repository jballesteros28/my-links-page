import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size

def link_icon( url: str,image: str,alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            height=styles.Size.LARGE.value,
            margin=styles.Size.SMALL.value
        ),
        href= url,
        is_external= True
    )