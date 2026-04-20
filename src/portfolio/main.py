from __future__ import annotations

import shutil

from html_dsl.element import css
from html_dsl.html import body, div, head, html, link, meta, title

from portfolio import PROJECT_ROOT, ROOT
from portfolio.components import background
from portfolio.sections.about_me import about_me
from portfolio.sections.header import header_section
from portfolio.sections.projects import projects


def app():
    return div(css(position="relative", width="100%", display="inline-block"))[
        background(),
        header_section(),
        content_section(),
    ]


def content_section():
    return div(css(display="flex", flex_direction="column", align_items="center"))[
        div(css("contentContainer"))[
            about_me(),
            projects(),
        ]
    ]


def index():
    # Mirror the contents of resources/index.html using the DSL
    return html(lang="en")[
        head[
            meta(charset="UTF-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            meta(
                name="description",
                content="Homepage showcasing my activity, interests and experience",
            ),
            title["Luka Born"],
            link(rel="stylesheet", href="stylesheet.css"),
            link(rel="preconnect", href="https://fonts.googleapis.com"),
            link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
            link(
                rel="stylesheet",
                href="https://fonts.googleapis.com/css2?family=Glory:ital,wght@0,100..800;1,100..800&display=swap",
            ),
        ],
        body[div[app()],],
    ]


def build_website():
    out_dir = PROJECT_ROOT / "out"
    out_dir.mkdir(exist_ok=True)

    with open(out_dir / "index.html", "w") as f:
        f.write(index().render())

    # for file in os.listdir(ROOT / "resources"):
    shutil.copytree(ROOT / "resources", out_dir, dirs_exist_ok=True)


def main():
    # Print the full HTML index page
    print(str(index()))


if __name__ == "__main__":
    main()
