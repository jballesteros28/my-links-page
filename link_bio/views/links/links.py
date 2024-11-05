import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.styles.styles as styles
import link_bio.views.links.constant as constant



def links() -> rx.Component:
    return rx.vstack(
        title("links de interes"),
        link_button(
            "Linkedin",
            "Mi perfil profesional",
            rx.color_mode_cond(
                light="icons/linkedin_light.svg",
                dark="icons/linkedin.svg"
            ),
            constant.LINKEDIN_URL
        ),
        link_button(
            "Github",
            "Codigo completo de todos mis proyectos",
            rx.color_mode_cond(
                light="icons/github_light.svg",
                dark="icons/github.svg"
            ),
            constant.GITHUB_URL
        ),
        link_button(
            "Portafolio",
            "Podras ver una parte mas completa sobre mi y mis proyectos",
            rx.color_mode_cond(
                light="icons/portafolio_light.svg",
                dark="icons/portafolio.svg"
            ),
            constant.FACEBOOK_URL
        ),
        link_button(
            "CV",
            "Mi cv profesional actualizado",
            rx.color_mode_cond(
                light="icons/cv_light.svg",
                dark="icons/cv.svg"
            ),
            constant.CV_URL
        ),
        title("contacto"),
        link_button(
            "Gmail",
            "juandavidballesterosbayona@gmail.com",
            rx.color_mode_cond(
                light="icons/mail_light.svg",
                dark="icons/mail.svg"
            ),
            constant.EMAIL_URL
        ),
        width="100%",
        spacing=styles.Size.MEDIUM.value
    )