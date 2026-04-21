from __future__ import annotations

from html_dsl.element import css
from html_dsl.html import a, div, img

from portfolio.components import (
    InteractionItem,
    SourceCodeHost,
    download_interaction_item,
    play_interaction_item,
    project_element,
    section_title,
    source_code_interaction_item,
)
from portfolio.constants import (
    GITHUB_PROFILE_URL,
    RAYTRACER_SOURCE_CODE,
    RUVOLA_SOURCE_CODE,
    SPACE_GAME_RELEASES,
    SPACE_GAME_SOURCE_CODE,
    SPACE_GAME_URL,
    TANK_GAME_URL,
    WEBSITE_SOURCE_CODE_URL,
)

SESAM_ARTICLE_LINK = (
    "https://web.archive.org/web/20250218041836/https://www.telekom.com/en/blog/careers/article/"
    "deutsche-telekom-and-bielefeld-university-developing-solutions-for-digital-identities-1053432"
)


def work_projects():
    return div[
        section_title["Work & Study Projects"],
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
            "A web client for the Cooperative Cuisine Environment, developed by the Social Cognitive Systems Group at ",
            "Bielefeld University. This implementation was written in TypeScript with PIXI.js for rendering and",
            "allows users to interact with the environment directly from their browser. This opens the possibility for",
            "online user studies and integrations into other study platforms, such as oTree.",
        ],
        project_element(
            title="UNO P2P",
            image="images/uno_p2p.png",
            interaction_items=[
                source_code_interaction_item(
                    link="https://github.com/IchbinLuka/p2p-uno"
                ),
            ],
        )[
            "A peer-to-peer clone of the popular UNO game, implemented using TypeScript and React. ",
            "To avoid cheating, I implemented a custom cryptographic protocol that allows players to verify card plays/draws without revealing their hand to the other players.",
            " The P2P communication is done via WebRTC Datachannels to achieve true Peer-to-Peer communication.",
        ],
        project_element(
            title="CoCu VoiceChat",
            image=None,
            interaction_items=[
                source_code_interaction_item(
                    link="https://gitlab.ub.uni-bielefeld.de/scs/cocosy/cocu-voicechat",
                    host=SourceCodeHost.GITLAB,
                ),
            ],
        )[
            "A Web-RTC based voice chat server & client implementation built for the Cooperative Cuisine Environment.",
            " We provide the client implementation for both the Python and Browser ecosystems. ",
            "The server is written in Python, using FastAPI and can also be directly mounted to your own FastAPI Apps.",
        ],
        project_element(
            title="Bachelor Thesis",
            image="images/bachelor_thesis_screenshot.png",
            interaction_items=[
                InteractionItem(
                    title="PDF",
                    link="misc/bachelor_thesis.pdf",
                    icon="icons/pdf-icon.svg",
                ),
                source_code_interaction_item(
                    link="https://gitlab.ub.uni-bielefeld.de/IchbinLuka/coop_cuisine_ba",
                    host=SourceCodeHost.GITLAB,
                ),
            ],
        )[
            "My Bachelor's thesis in which I evaluated the performance of multiple reinforcement learning algorithms in",
            " the ",
            a(href="https://gitlab.ub.uni-bielefeld.de/scs/cocosy/cooperative-cuisine")[
                "Cooperative Cuisine Environment"
            ],
            ", similar to the game Overcooked,",
            " while incrementally increasing the complexity of the environment along various dimensions. ",
            "The source code of the bachelor thesis, the algorithms, and the trained weights of the models are available",
            " on the GitLab of the University of Bielefeld.",
        ],
        project_element(
            title="SESAM",
            image=(
                "https://web.archive.org/web/20231207111946im_/https://www.telekom.com/resource/image/1053434/"
                "landscape_ratio4x3/320/240/88f5400de646ef82eeb8c18bd1ea9f72/0A4C37323EE8EE6F16C9B55D9D8990B0/"
                "bi-20231120-hochschulkoop-sesam-artikel.jpg"
            ),
            interaction_items=[
                InteractionItem(
                    title="Blog Post", link=SESAM_ARTICLE_LINK, icon="icons/earth.svg"
                ),
            ],
        )[
            "In 2023, as part of a collaboration between Bielefeld University and Deutsche Telekom, ",
            "our student team developed SESAM — an access-management software for buildings. Our team ",
            "was one of the winning teams in the competition. The project was implemented with Java ",
            "(Spring Boot) on the backend and TypeScript + Vue on the frontend. ",
            a(href=SESAM_ARTICLE_LINK)["Read more"],
        ],
        project_element(
            title="pya_agen",
            image="images/pya_agen_screenshot.png",
            interaction_items=[
                source_code_interaction_item(
                    link="https://github.com/interactive-sonification/pya/tree/feature-agen"
                ),
            ],
        )[
            f"An extension for the Python library {a(href='https://pypi.org/project/pya/')['pya']}"
            " that adds the concept of Audio Generators (AGens), which provide a simple and flexible way of generating audio signals."
            " Pya_agen enables various ways of combining these generators, effectively"
            " allowing for the creation of complex trees of nodes that are lazily evaluated on demand."
            " This extension is now integrated into the base pya library on the feature-agen branch of the repository."
        ],
        project_element(
            title="How do AI systems “see”? Image recognition explained simply",
            image="images/conv_demo.gif",
            interaction_items=[
                InteractionItem(
                    title="Web Demo (German)",
                    link="https://ki-akademieowl.de/autorenseite-bilderkennung-demonstrator/",
                    icon="icons/earth.svg",
                ),
            ],
        )[
            "A demonstrator aimed to introduce middle-school level learners into the world of Neural Networks and Image "
            "Processing by providing a playful explanation of convolutions and Convolutional Neural Networks. "
            "This application was written with React and p5.js and is available on the website of the KI-Akademie OWL."
        ],
    ]


def free_time_projects():
    return div[
        section_title["Free Time Projects"],
        project_element(
            title="Space Game",
            image="images/space_game_screenshot.png",
            interaction_items=[
                source_code_interaction_item(SPACE_GAME_SOURCE_CODE),
                download_interaction_item(SPACE_GAME_RELEASES),
                play_interaction_item(SPACE_GAME_URL),
            ],
        )[
            "A small top down space shooter game where you need to defend space stations from enemy ships."
            " The enemies can drop power-ups like shields, bombs, or turrets, which can help you in your fight."
            " I am making this game using Rust and the Bevy game engine."
            " This game also features an online leaderboard, where you can compete with others for the highest score."
            f" The server hosting the leaderboard is written in Rust with {a(href='https://rocket.rs/')['Rocket']}"
            ". The source code of the leaderboard server is not available to not expose the anti-cheat mechanisms."
        ],
        project_element(
            title="Tanks 3D",
            image="images/tank_game_screenshot.png",
            interaction_items=[
                play_interaction_item(TANK_GAME_URL),
            ],
        )[
            "A multiplayer browser game in which you control a tank and try to destroy other tanks.",
            " It's built with Three.js and Kotlin/JS.",
            " The server is also written in Kotlin and uses Ktor.",
            " The source code is currently not public, however, you can play the game on my GitHub page.",
        ],
        project_element(
            title="RuVoLA",
            image="images/ruvola.gif",
            interaction_items=[
                source_code_interaction_item(RUVOLA_SOURCE_CODE),
            ],
        )[
            "A simple TUI application for learning vocabulary by actually typing the words, contrary to tools like ",
            "Anki or vocage. The vocabulary is stored in a simple TSV format, allowing it to be stored and managed using git. ",
            f"This application is written in Rust and uses the {a(href='')['ratatui']} library for the TUI. ",
            "The source code is available on GitHub.",
        ],
        project_element(
            title="raytracer.rs",
            image="images/raytracer_screenshot.png",
            interaction_items=[
                source_code_interaction_item(RAYTRACER_SOURCE_CODE),
            ],
        )[
            "A simple raytracer written in Rust.",
            " A Rust + WGSL implementation of Ray Tracing in One Weekend by Peter Shirley.",
            " The source code is available on GitHub.",
        ],
        project_element(
            title="This Website",
            image="images/website_screenshot.png",
            interaction_items=[
                InteractionItem(title="Open", link="/", icon="icons/earth.svg"),
                source_code_interaction_item(
                    link=WEBSITE_SOURCE_CODE_URL, host=SourceCodeHost.GITHUB
                ),
            ],
        )[
            "This website was built using a custom Python DSL that directly generates the HTML code ahead of time"
            ", avoiding the use of a templating engine, any external libraries, or JavaScript to be enabled at all"
        ],
        a(
            css(
                "normalTextLink",
                display="flex",
                flex_direction="row",
                align_items="center",
                justify_content="center",
                padding="30px",
            ),
            href=GITHUB_PROFILE_URL,
        )[
            img(
                css(width="50px", height="50px", margin_right="10px"),
                src="icons/github-mark-white.svg",
                alt="GitHub Logo",
            ),
            div(css(text_decoration="solid", color="#fff", font_size="xx-large"))[
                "Other projects can be found on my GitHub"
            ],
        ],
    ]


def projects():
    return div[work_projects(), free_time_projects()]
