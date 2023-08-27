import reflex as rx 
from rxconfig import config

class State(rx.State):
    """The app state."""
    email: str = ''
    pw: str = ''
    user_logged_in: bool = False
    
    def set_email(self, email: str):
        self.email = email.upper()
    def set_pw(self, pw: str):
        self.pw = pw.upper()


def log_in() -> rx.Component:
    return rx.container(
        rx.fragment(
            rx.center(
                rx.vstack(
                    rx.heading("Log In", font_size="2em", font_weight="800"),
                    # Email
                    rx.box(
                        rx.text("Email", color_scheme="green"),
                        rx.input(on_change=State.set_email), width="20vw"
                    ),
                    rx.Divider(),
                    # PW
                    rx.box(
                        rx.text("Password", color_scheme="green"),
                        rx.input(on_change=State.set_pw), width="20vw"
                    ),
                    spacing="1.5em",
                    font_size="2em",
                    padding_top="10%",
                ),
            )
        )
    )

def empty() -> rx.Component:
    return rx.container()

def index() -> rx.Component:
    return rx.container(
        rx.cond(
            State.user_logged_in,
            navbar(),
            empty()
        ),
        rx.fragment(
            rx.center(
                rx.vstack(
                    rx.heading("Log In", font_size="2em", font_weight="800"),

                    # Email
                    rx.box(
                        rx.text("Email", color_scheme="green"),
                        rx.input(on_change=State.set_email), width="20vw"
                    ),
                    rx.Divider(),

                    # PW
                    rx.box(
                        rx.text("Password", color_scheme="green"),
                        rx.input(on_change=State.set_pw), width="20vw"
                    ),
                    spacing="1.5em",
                    font_size="2em",
                    padding_top="10%",
                ),
            )
        )
    )

def navbar():
    return rx.box(
            rx.hstack(
                rx.menu(
                    rx.menu_button("Menu", class_name='left-text'),
                    rx.menu_list(
                        rx.menu_item("Home"),
                        rx.menu_divider(),
                        rx.menu_item("About"),
                        rx.menu_item("Contact"),
                    ),
                    padding="1rem",
                ),
                rx.color_mode_button(rx.color_mode_icon(), padding="1rem", class_name="right-text"),
            ),
            padding="1rem",
    )

def user_home() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Home", font_size="2em", font_weight="800"),
            rx.box(
                rx.accordion(
                    rx.accordion_item(
                        rx.accordion_button(
                            rx.heading("Example"),
                            rx.accordion_icon(),
                        ),
                        rx.accordion_panel(
                            rx.text(
                                "This is an example of an accordion component."
                            )
                        ),
                    ),
                    allow_toggle=True,
                    width="100%",
                )
            ),
        padding="1rem"
        )
    )



# def navbar():
#     return rx.box(
#         rx.hstack(
#             rx.image(src="favicon.ico"),
#             rx.heading("My App"),
#         ),
#         rx.spacer(),
#         rx.menu(
#             rx.menu_button("Menu"),
#         ),
#         position="fixed",
#         width="100%",
#         top="0px",
#         z_index="5",
#     )