import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width= styles.MAX_WIDTH,
                width="100%",
                align="center",
                margin_y= styles.Size.BIG.value,
                margin_x= styles.Size.BIG.value,
            )
        ),
        footer(),
        style=styles.background_base_style
    )


app= rx.App(
    style= styles.DARK_STYLE,
    stylesheets= styles.STYLESHEETS,
    
)
app.add_page(
    index,
    title="JuanDev | pagina de links"
            )


