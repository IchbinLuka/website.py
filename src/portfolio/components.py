from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from html_dsl.element import Child, Element, Fragment, component, css
from html_dsl.html import a, div, h1, img


@component
def section_title():
    return div(css(font_size="xxx-large", margin_bottom="20px", margin_top="30px"))


def background():
    """
    Background container that renders two background_circles instances.
    The second instance is flipped and given a large min-height to avoid
    circle positioning glitches while the page is loading.
    """
    return div(css("backgroundContainer"))[
        background_circles(),
        background_circles(
            style={"transform": "scale(-1, -1)", "min_height": "3000px"}
        ),
    ]


def background_circles(style: dict[str, str] | None = None):
    """
    Renders a background container element plus several dot elements that
    can be animated via CSS. `style` is a dict of style-like keys that
    are passed into the DSL `css` helper.
    """
    st = style or {}

    return div(css("background", **st))[
        *(div(css("dot", animation_delay=f"{-delay}s")) for delay in (1, 50, 120))
    ]


@dataclass
class InteractionItem:
    title: str
    link: str
    icon: str


@component
def content_element() -> Element:
    return div(css("contentElement"))


class SourceCodeHost(Enum):
    GITHUB = "icons/github-mark-white.svg"
    GITLAB = "icons/gitlab-logo.svg"

    @property
    def icon(self) -> str:
        return self.value


def source_code_interaction_item(
    link: str,
    host: SourceCodeHost = SourceCodeHost.GITHUB,
) -> InteractionItem:
    return InteractionItem(
        title="Source Code",
        link=link,
        icon=host.icon,
    )


def play_interaction_item(link: str) -> InteractionItem:
    return InteractionItem(
        title="Play",
        link=link,
        icon="icons/play_arrow.svg",
    )


def download_interaction_item(link: str) -> InteractionItem:
    return InteractionItem(
        title="Download",
        link=link,
        icon="icons/download.svg",
    )


def project_element(
    title: str,
    image: str | None,
    interaction_items: list[InteractionItem],
) -> Element:
    children: list[Child] = []

    # Optional image block
    if image is not None:
        children.append(
            div(css("projectImage", max_height="600px", text_align="center"))[
                img(
                    css(
                        "projectImage",
                        max_width="100%",
                        min_width="500px",
                        max_height="500px",
                    ),
                    src=image,
                    alt=title,
                )
            ]
        )

    interaction_children: list[Child] = []
    for item in interaction_items:
        interaction_children.append(
            a(css("overlayButton"), href=item.link)[
                img(src=item.icon, alt=item.title),
                item.title,
            ]
        )
    slot = Fragment()

    return content_element[
        h1(css(margin_top=0))[title],
        *children,
        div(css(display="flex", flex_direction="row"))[*interaction_children],
        slot,
    ].set_slot(slot)
