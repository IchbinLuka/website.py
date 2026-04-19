from __future__ import annotations

from portfolio.components import (
    SourceCodeHost,
    section_title,
    project_element,
    InteractionItem,
    source_code_interaction_item,
    play_interaction_item,
    download_interaction_item,
)
from portfolio.constants import (
    GITHUB_PROFILE_URL,
    TANK_GAME_URL,
    SPACE_GAME_SOURCE_CODE,
    SPACE_GAME_URL,
    SPACE_GAME_RELEASES,
    RAYTRACER_SOURCE_CODE,
    RUVOLA_SOURCE_CODE,
)
from portfolio.html_dsl import a, div, img
from portfolio.element import css

SESAM_ARTICLE_LINK = (
    "https://web.archive.org/web/20250218041836/https://www.telekom.com/en/blog/careers/article/"
    "deutsche-telekom-and-bielefeld-university-developing-solutions-for-digital-identities-1053432"
)


def work_projects():
    return div[
        section_title("Work & Study Projects"),

        project_element(
            title="Web Client for the Cooperative Cuisine Environment",
            image="images/cocu_web_screenshot.png",
            interaction_items=[
                source_code_interaction_item(
                    link="https://gitlab.ub.uni-bielefeld.de/scs/cocosy/cooperative-cuisine",
                    host=SourceCodeHost.GITLAB,
                )
            ],
        )[
            "A web client for the Cooperative Cuisine Environment, developed by the "
            "Social Cognitive Systems Group at Bielefeld University. This implementation "
            "was written in TypeScript with PIXI.js for rendering and allows users to "
            "interact with the environment directly from their browser. This opens the "
            "possibility for online user studies and integrations into other study "
            "platforms, such as oTree."
        ],

        project_element(
            title="UNO P2P",
            image="images/uno_p2p.png",
            interaction_items=[
                source_code_interaction_item(link="https://github.com/IchbinLuka/p2p-uno"),
            ],
        )[
            "A peer-to-peer clone of the popular UNO card game implemented with "
            "TypeScript and React. To prevent cheating I designed a lightweight "
            "cryptographic protocol that lets players prove card plays and draws "
            "without revealing their hands. The networking is built on WebRTC data "
            "channels to achieve true peer-to-peer communication between players."
        ],

        project_element(
            title="CoCu VoiceChat",
            image=None,
            interaction_items=[
                source_code_interaction_item(link="https://gitlab.ub.uni-bielefeld.de/scs/cocosy/cocu-voicechat"),
            ],
        )[
            "A WebRTC-based voice chat system built for the Cooperative Cuisine Environment. "
            "The project contains both client and server parts — clients for browser and Python "
            "environments and a server implementation written in Python using FastAPI. "
            "The server can be mounted into existing FastAPI apps, which makes integration "
            "into research platforms straightforward."
        ],

        project_element(
            title="Bachelor Thesis",
            image="images/bachelor_thesis_screenshot.png",
            interaction_items=[
                InteractionItem(title="PDF", link="misc/bachelor_thesis.pdf", icon="icons/pdf-icon.svg"),
                source_code_interaction_item(link="https://gitlab.ub.uni-bielefeld.de/IchbinLuka/coop_cuisine_ba"),
            ],
        )[
            "My Bachelor's thesis evaluated the performance of several reinforcement learning "
            "algorithms in a simulated multi-agent environment. The work uses the ",
            a(href="https://gitlab.ub.uni-bielefeld.de/scs/cocosy/cooperative-cuisine")["Cooperative Cuisine Environment"],
            ", similar to the game Overcooked, while incrementally increasing the complexity "
            "of the environment across experiments. The thesis includes source code, algorithm "
            "implementations and trained model weights — all available on the University's GitLab."
        ],

        project_element(
            title="SESAM",
            image=(
                "https://web.archive.org/web/20231207111946im_/https://www.telekom.com/resource/image/1053434/"
                "landscape_ratio4x3/320/240/88f5400de646ef82eeb8c18bd1ea9f72/0A4C37323EE8EE6F16C9B55D9D8990B0/"
                "bi-20231120-hochschulkoop-sesam-artikel.jpg"
            ),
            interaction_items=[
                InteractionItem(title="Blog Post", link=SESAM_ARTICLE_LINK, icon="icons/earth.svg"),
            ],
        )[
            "In 2023, as part of a collaboration between Bielefeld University and Deutsche Telekom, "
            "our student team developed SESAM — an access-management software for buildings. Our team "
            "was one of the winning teams in the competition. The project was implemented with Java "
            "(Spring Boot) on the backend and TypeScript + Vue on the frontend. ",
            a(href=SESAM_ARTICLE_LINK)["Read more"]
        ],

        project_element(
            title="pya_agen",
            image="images/pya_agen_screenshot.png",
            interaction_items=[
                source_code_interaction_item(link="https://github.com/interactive-sonification/pya/tree/feature-agen"),
            ],
        )[
            "An extension to the Python audio library 'pya' that introduces Audio Generators (AGens). "
            "AGens expose a composable, lazy-evaluated API for constructing audio signal graphs. The "
            "extension enables convenient combinations of generators to build complex audio processing "
            "trees and is available on the feature-agen branch of the pya repository."
        ],

        project_element(
            title='How do AI systems “see”? Image recognition explained simply',
            image="images/conv_demo.gif",
            interaction_items=[
                InteractionItem(
                    title="Web Demo (German)",
                    link="https://ki-akademieowl.de/autorenseite-bilderkennung-demonstrator/",
                    icon="icons/earth.svg",
                ),
            ],
        )[
            "A demonstrator intended to introduce middle-school learners to neural networks and "
            "image processing. The app visualizes convolutions and CNN concepts in a playful way. "
            "It was implemented using React and p5.js and is hosted on the KI-Akademie OWL website."
        ],
    ]


def free_time_projects():
    return div[
        section_title("Free Time Projects"),

        project_element(
            title="Space Game",
            image="images/space_game_screenshot.png",
            interaction_items=[
                source_code_interaction_item(SPACE_GAME_SOURCE_CODE),
                download_interaction_item(SPACE_GAME_RELEASES),
                play_interaction_item(SPACE_GAME_URL),
            ],
        )[
            "A small top-down space shooter in which you defend stations from enemy ships. Enemies "
            "can drop power-ups such as shields, bombs, or turrets. The game is implemented in Rust "
            "using the Bevy engine and features an online leaderboard for competitive play.",
            " This game also features an online leaderboard, where you can compete with others for "
            f"the highest score. The leaderboard server is written in Rust using {a(href='https://rocket.rs/')['Rocket']}.",
            "The server source code is not public to avoid exposing anti-cheat mechanisms."
        ],

        project_element(
            title="Tanks 3D",
            image="images/tank_game_screenshot.png",
            interaction_items=[
                play_interaction_item(TANK_GAME_URL),
            ],
        )[
            "A multiplayer browser game where you control a tank and battle other players in an arena. "
            "The client uses Three.js, the codebase leverages Kotlin/JS, and the server is implemented "
            "with Ktor. The game is available to play on my GitHub pages."
        ],

        project_element(
            title="RuVoLA",
            image="images/ruvola.gif",
            interaction_items=[
                source_code_interaction_item(RUVOLA_SOURCE_CODE),
            ],
        )[
            "RuVoLA is a terminal-based vocabulary learning tool that encourages typing practice rather than "
            "recognition. Vocabulary is stored in TSV files to allow versioning with git. The app is written "
            f"in Rust and uses the {a(href='https://ratatui.rs/')['ratatui']} TUI library. The source code is available on GitHub.",
        ],

        project_element(
            title="raytracer.rs",
            image="images/raytracer_screenshot.png",
            interaction_items=[
                source_code_interaction_item(RAYTRACER_SOURCE_CODE),
            ],
        )[
            "A compact raytracer written in Rust (with WGSL for GPU shading). The implementation follows "
            "'Ray Tracing in One Weekend' and demonstrates basic global illumination and material models. "
            "Source code is available on GitHub."
        ],

        project_element(
            title="This Website",
            image="images/website_screenshot.png",
            interaction_items=[
                InteractionItem(title="Open", link="/", icon="icons/earth.svg"),
            ],
        )[
            "This website is implemented with Kotlin/JS and React. The backend uses Ktor. The site's source "
            "code and related projects are available on my GitHub."
        ],

        a(
            css(classes=["normalTextLink"], display="flex", flex_direction="row", align_items="center", justify_content="center", padding="30px"),
            href=GITHUB_PROFILE_URL,
        )[
            img(css(width="50px", height="50px", margin_right="10px"), src="icons/github-mark-white.svg", alt="GitHub Logo"),
            div(css(text_decoration="solid", color="#fff", font_size="xx-large"))["Other projects can be found on my GitHub"]
        ],
    ]


def projects():
    return div[work_projects(), free_time_projects()]
