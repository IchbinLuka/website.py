from __future__ import annotations

from html_dsl.element import css
from html_dsl.html import a, div, h1, header, img

from portfolio.constants import GITHUB_PROFILE_URL


def header_section():
    return header(css("header"))[
        div(
            css(
                display="flex",
                flex_direction="row",
                justify_content="space-between",
                align_items="center",
                padding="15px",
            )
        )[
            h1(css(font_weight="normal"))["LUKA BORN"],
            a(href=GITHUB_PROFILE_URL)[
                img(
                    css(width="50px", height="50px"),
                    src="icons/github-mark-white.svg",
                    alt="Link to my GitHub profile",
                )
            ],
        ]
    ]
