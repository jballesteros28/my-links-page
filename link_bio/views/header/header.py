import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color
from link_bio.styles.colors import TextColor
import link_bio.views.links.constant as constant

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.flex(
                rx.avatar(
                    src="/juan.jpg",
                    fallback="juan",
                    size="8",
                    radius= "full",
                    padding="2px",
                    border=f"2px solid {Color.PRIMARY.value}",
                    margin_top=styles.Size.LARGE.value,
                    color_scheme="gray",
                    variant="soft",
                    width="100%"
                ),
            ),
            rx.vstack(
                rx.heading(
                    "Juan Ballesteros", 
                    size="7",
                    style=styles.color_text
                ),
                rx.hstack(
                    link_icon(
                        constant.INSTAGRAM_URL,
                        rx.color_mode_cond(
                            light="icons/instagram_light.svg",
                            dark="icons/instagram.svg"
                        ),
                        "instagram"
                    ),
                    link_icon(
                        constant.FACEBOOK_URL,
                        rx.color_mode_cond(
                            light="icons/facebook_light.svg",
                            dark="icons/facebook.svg"
                        ),
                        "facebook"
                    ),
                    link_icon(
                        constant.TWITTER_URL,
                        rx.color_mode_cond(
                            light="icons/twitter_light.svg",
                            dark="icons/twitter.svg"
                        ),
                        "twitter"
                    ),
                ),
                align_items="start",
                padding_top="40px",
                spacing="0"
            ),
            spacing=styles.Size.BIG.value
        ),
        rx.flex(
            info_text("+1","año de experiencia")  
        ),
        rx.text("Soy estudiante de ingenieria de sistemas y actualmente estoy disponible como back-end y front-end developer. aqui podras encontrar todos mis enlaces de interes ¡Bienbenid@!",
                width="100%",
                style=styles.color_text
        ),
        align_items="start",
        width="100%",
        spacing=styles.Size.BIG.value,
        color= TextColor.HEADER.value,
    )