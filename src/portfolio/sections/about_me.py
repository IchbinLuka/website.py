from __future__ import annotations
from dataclasses import dataclass

from portfolio.html_dsl import a, div, h1, img, p
from portfolio.element import css
from portfolio.components import section_title

CONTACT_EMAIL = "contact@lukaborn.de"


def programming_lang_item(text: str, icon: str):
    return div(css(display="flex", flex_direction="row", align_items="center"))[
        img(css(width="20px", height="20px", margin_top="5px", margin_bottom="5px", margin_right="10px"), src=icon, alt=text),
        p(css(margin="0px"))[text],
    ]


def programming_section():
    items = [
        "Kotlin",
        "Ktor",
        "Three.js",
        "React",
        "Compose Multiplatform",
        "Python",
        "Rust",
        "Bevy",
        "Dart",
        "Flutter",
        "Java",
        "Spring Boot",
        "Android",
    ]

    # grid with 3 columns (using a simple style representation consistent with the rest of the DSL)
    children = tuple(div[item] for item in items)
    return div(css(display="grid", grid_template_columns="repeat(3, auto)"))[*children]


def about_me():
    return div[
        section_title("About Me"),
        div(css(font_size="large", margin_bottom="50px"))[
            p[
                (
                    "I recently graduated with a Bachelor's degree in Cognitive Computer Science at the University of Bielefeld "
                    "and am now pursuing a Master's degree in Intelligent Interactive Systems. "
                    "In my free time, I like to work on various projects, such as this website or small browser games."
                )
            ],
            p[f"I have previously worked as a student assistant at {a(href='https://www.kognihome.de/')['KogniHome']}, where I am developing a mobile application for {a(href='https://github.com/sharly-project')['SHARLY']}. Currently, I am working as a research assistant at the Social Cognitive Systems Group at the University of Bielefeld."],
            h1(css(font_weight="normal", margin_top="40px"))["Programming Languages / Technologies"],
            p["For my projects and at work, I mainly use the following programming languages and technologies:"],
            programming_lang_item("Kotlin + Ktor, Three.js, React, Compose Multiplatform", "icons/kotlin-logo.svg"),
            programming_lang_item("Python", "icons/python-logo.svg"),
            programming_lang_item("Rust + Bevy", "icons/rust-logo.svg"),
            programming_lang_item("Dart + Flutter", "icons/dart-logo.svg"),
            programming_lang_item("Java + Spring Boot", "icons/java-logo.svg"),

            h1(css(font_weight="normal", margin_top="40px"))["Contact"],
            p[f"You can reach me via email at {a(href=f'mailto:{CONTACT_EMAIL}')[CONTACT_EMAIL]}."],
        ],
    ]


# Export a module-level value that's ready to be inserted into the page
AboutMe = about_me()
