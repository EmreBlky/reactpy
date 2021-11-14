from idom import component, html, run


@component
def Photo():
    return html.img(
        {
            "src": "https://i.pinimg.com/564x/d6/96/c4/d696c4d3db31609c1abb05c52f305ec1.jpg",
            "style": {"width": "70%", "marginLeft": "15%"},
            "alt": "Ray Charles",
        }
    )


run(Photo)