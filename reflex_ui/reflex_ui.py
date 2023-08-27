"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from .pages import State, index, user_home 
from .style import style

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

# Add state and page to the app.

app = rx.App(
    state=State,
    style=style,
)

app.add_page(index)
app.add_page(user_home, route="user-home")
app.compile()
