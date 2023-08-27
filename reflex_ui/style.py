import reflex as rx

accent_color = "#f81ce5"
style = {
    "::selection": {
        "background_color": accent_color,
    },
    ".some-css-class": {
        "text_decoration": "underline",
    },
    "#special-input": {"width": "20vw"},
    rx.Divider: {
        "margin_bottom": "1em",
        "margin_top": "0.5em",
    },
    rx.Heading: {
        "font_weight": "500",
    },
    rx.Code: {
        "color": accent_color,
    },
    rx.Input: {
        "width": "20vw",
    },
    ".right-text": {
        "position": 'absolute',
        'right': "5vw",
        'top': "2vw",
    },
    ".left-text": {
        "position": 'absolute',
        'left': "5vw",
        'top': "2vw",
    },
}