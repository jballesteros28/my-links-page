import reflex as rx
from link_bio.styles.colors import Color
from link_bio.styles.styles import Size
import link_bio.styles.styles as styles
from reflex.style import toggle_color_mode




def dark_mode_toggle() -> rx.Component:
    return rx.flex(
                rx.color_mode_cond(
                    dark=rx.icon(tag="moon",size=20),
                    light=rx.icon(tag="sun",size=20)
                ),
                on_click=toggle_color_mode,
                cursor="pointer",
                padding="0.5em",
                border_radius= Size.DEFAULT.value,
                _hover={
                    "box_shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2)"
                },
                style=styles.background_button_style
                
            )
        
    

