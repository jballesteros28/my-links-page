import reflex as rx
from enum import Enum
from .colors import Color
from .colors import TextColor
from .fonts import Font,FontWeight


#constans
MAX_WIDTH= "500px"

STYLESHEETS=[
    "https://fonts.googleapis.com/css2?family=roboto:wght@0,300;0,500&display=swap"
]

#sizes

class Size(Enum):
    ZERO="0em"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    VERY_BIG="2.5em"
    
#styles

DARK_STYLE= {
    "font_family":Font.DEFAULT.value,
    "font_weight":FontWeight.LIGHT.value,
    rx.button:{
        "width":"100%",
        "height":"100%",
        "padding":Size.SMALL.value,
        "color":TextColor.HEADER.value,
        "white_space": "normal",
        "text_align":"start",
        "_hover":{
            "border_style":"solid",
            "border_width":"1px",
            "border_color":Color.PRIMARY.value,
            "text_decoration":"none",
        },
        "border_radius":Size.DEFAULT.value
    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
    },
    rx.heading:{
        "font_family":Font.TITTLE.value,
        "font_weight":FontWeight.MEDIUM.value,
        "width":"100%",
        "height":"100%"
    },
}


navbar_tittle_style= dict(
    font_size=Size.BIG.value,
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value
)
tittle_style= dict(
    font_size=FontWeight.CLASIC.value,
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value
)
boddy_style= dict(
    font_size=FontWeight.SUB_CLASIC.value,
    font_family=Font.LOGO.value,
    font_weight=FontWeight.LIGHT.value,
    color= TextColor.FOOTER.value
)

navbar_style= dict(
        position="sticky",
        bg= rx.color_mode_cond(
            light="#e8e8e8",
            dark=Color.BACKGROUND.value
        ),
        box_shadow= rx.color_mode_cond(
            light="2px 2px 4px #c5c5c5",
            dark="2px 2px 4px #000",
        ),
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
)

background_base_style= dict(
    bg=rx.color_mode_cond(
        light=Color.BACKGROUND_LIGHT.value,
        dark=Color.BACKGROUND.value
    ),
)

background_button_style= dict(
    bg=rx.color_mode_cond(
        light=Color.BACKGROUND_LIGHT.value,
        dark=Color.BACKGROUND.value
    ),
    color=rx.color_mode_cond(
        light= TextColor.BODY_LIGHT.value,
        dark=TextColor.HEADER.value
    ),
    box_shadow= rx.color_mode_cond(
            light="2px 2px 4px #c5c5c5,-2px -2px 4px #ffffff",
            dark="2px 2px 4px #000,-2px -2px 4px #222222",
        ),
    _hover={
            "border_style":"solid",
            "border_width":"1px",
            "border_color":Color.PRIMARY.value,
            "text_decoration":"none",
        },
    
)

color_text_body=dict(
    color=rx.color_mode_cond(
        light= TextColor.BODY_LIGHT.value,
        dark=TextColor.FOOTER.value
    )
)

color_text_tittle=dict(
    color=rx.color_mode_cond(
        light= TextColor.BODY_LIGHT.value,
        dark=TextColor.HEADER.value
    )
)