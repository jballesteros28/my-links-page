import reflex as rx
import link_bio.styles.styles as styles
def title(text: str) -> rx.Component:
    return rx.flex(
        rx.heading(
            text,
            size="6",
            style=styles.color_text_tittle
        ),
        
    )