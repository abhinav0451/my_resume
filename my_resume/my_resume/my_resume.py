import json
import nextpy as xt

json_file_path = "./resume.json"


def load_json_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


RESUME_DATA = load_json_data(json_file_path)


BASICS = RESUME_DATA["basics"]
WORK_EXPERIENCE = RESUME_DATA["work"]
EDUCATION_HISTORY = RESUME_DATA["education"]
SKILLS = RESUME_DATA["skills"]
PROJECTS = RESUME_DATA["projects"]


def social_img(src):
    return xt.box(
        xt.image(src=src, class_name="w-10 "),
        class_name="border-solid border w-10 h-10 flex items-center p-2 rounded-md border-[#6b7280]/12",
    )


def basic_section():
    layout = xt.box(
        xt.box(
            xt.text(
                BASICS["name"],
                class_name="font-bold text-2xl lg:text-3xl",
            ),
            xt.text(
                BASICS["label"],
                " focused on building products with extra attention to details",
                class_name="text-[#6b7280] text-base mt-2 lg:text-lg max-w-sm",
            ),
            xt.text(
                BASICS["location"]["address"],
                class_name="text-sm lg:text-base text-[#6b7280]",
            ),
            xt.box(
                social_img("/message.svg"),
                social_img("/github.svg"),
                social_img("/twitter.png"),
                social_img("/Linkedin.svg"),
                class_name="flex items-center gap-2 mt-2",
            ),
        ),
        xt.box(
            xt.image(src=BASICS["image"], class_name="rounded-lg w-32"),
        ),
        class_name="flex items-center justify-between",
    )
    return layout


def about():
    layout = xt.box(
        xt.box(
            xt.text("About", class_name="font-bold text-2xl lg:text-3xl"),
            xt.text(
                BASICS["summary"],
                class_name="text-sm lg:text-base max-w-2xl mt-2 text-[#6b7280]",
            ),
        ),
        class_name="mt-6",
    )
    return layout


def work_experience():
    layout = xt.box(
        xt.box(
            xt.text(
                "Work Experience",
                class_name="font-bold text-2xl lg:text-3xl",
            ),
            xt.box(
                xt.box(
                    xt.text(
                        WORK_EXPERIENCE[0]["name"], class_name="text-base font-bold "
                    ),
                    xt.text(
                        "Remote", class_name="text-sm px-3 font-medium bg-[#f3f4f6] rounded-md"
                    ),
                    class_name="flex gap-4 mt-2 items-center",
                ),
                xt.box(
                    xt.text(
                        WORK_EXPERIENCE[0]["startDate"], "-", class_name="text-base "
                    ),
                    xt.text(WORK_EXPERIENCE[0]["endDate"], class_name="text-base "),
                    class_name="flex items-center",
                ),
                class_name="flex justify-between items-center",
            ),
            xt.text(
                WORK_EXPERIENCE[0]["position"], class_name="text-base mt-1 font-medium "
            ),
            xt.text(
                WORK_EXPERIENCE[0]["summary"],
                class_name="text-sm lg:text-base text-[#6b7280]",
            ),
            xt.box(
                xt.box(
                    xt.box(
                        xt.text(
                            WORK_EXPERIENCE[1]["name"],
                            class_name="text-base font-bold ",
                        ),
                        xt.text(
                            "Remote",
                            class_name="text-sm font-medium px-3 bg-[#f3f4f6] rounded-md",
                        ),
                        class_name="flex gap-4 mt-2 items-center",
                    ),
                    xt.box(
                        xt.text(
                            WORK_EXPERIENCE[1]["startDate"],
                            "- ",
                            WORK_EXPERIENCE[1]["endDate"],
                        ),
                        class_name="flex text-base items-center",
                    ),
                    class_name="flex justify-between items-center",
                ),
                xt.text(
                    WORK_EXPERIENCE[2]["position"],
                    class_name="text-base mt-1 font-medium ",
                ),
                xt.text(
                    WORK_EXPERIENCE[2]["summary"],
                    class_name="text-sm lg:text-base text-[#6b7280]",
                ),
                class_name="mt-2",
            ),
            xt.box(
                xt.box(
                    xt.box(
                        xt.text(
                            WORK_EXPERIENCE[2]["name"],
                            class_name="text-base font-bold ",
                        ),
                    ),
                    xt.box(
                        xt.text(
                            WORK_EXPERIENCE[2]["startDate"],
                            " - ",
                            WORK_EXPERIENCE[2]["endDate"],
                        ),
                        class_name="flex text-base items-center",
                    ),
                    class_name="flex justify-between items-center",
                ),
                xt.text(
                    WORK_EXPERIENCE[1]["position"],
                    class_name="text-base mt-1 font-medium ",
                ),
                xt.text(
                    WORK_EXPERIENCE[1]["summary"],
                    class_name="text-sm lg:text-base text-[#6b7280]",
                ),
                class_name="mt-2",
            ),
            xt.box(
                xt.box(
                    xt.box(
                        xt.text(
                            WORK_EXPERIENCE[3]["name"],
                            class_name="text-base font-bold ",
                        ),
                    ),
                    xt.box(
                        xt.text(
                            WORK_EXPERIENCE[3]["startDate"],
                            " - ",
                            WORK_EXPERIENCE[3]["endDate"],
                        ),
                        class_name="flex text-base items-center",
                    ),
                    class_name="flex justify-between items-center",
                ),
                xt.text(
                    WORK_EXPERIENCE[3]["position"],
                    class_name="text-base mt-1 font-medium ",
                ),
                xt.text(
                    WORK_EXPERIENCE[3]["summary"],
                    class_name="text-sm lg:text-base text-[#6b7280]",
                ),
                class_name="mt-2",
            ),
        ),
        class_name="mt-6 ",
    )
    return layout


def education():
    layout = xt.box(
        xt.box(
            xt.text(
                "Education",
                class_name="font-bold text-2xl lg:text-3xl",
            ),
            xt.box(
                xt.box(
                    xt.box(
                        xt.text(
                            EDUCATION_HISTORY[0]["institution"],
                            class_name="text-base font-bold ",
                        ),
                    ),
                    xt.box(
                        xt.text(
                            EDUCATION_HISTORY[0]["startDate"],
                            " - ",
                            EDUCATION_HISTORY[0]["endDate"],
                        ),
                        class_name="flex text-base items-center",
                    ),
                    class_name="flex justify-between items-center",
                ),
                xt.text(
                    EDUCATION_HISTORY[0]["studyType"],
                    " in ",
                    EDUCATION_HISTORY[0]["area"],
                    class_name="text-base text-[#6b7280]",
                ),
                class_name="mt-2",
            ),
        ),
        class_name="mt-6",
    )
    return layout


def skills():
    layout = xt.box(
        xt.box(
            xt.text(
                "Skills",
                class_name="font-bold text-2xl lg:text-3xl",
            ),
            xt.box(
                xt.text(
                    SKILLS[0]["keywords"][0],
                    class_name="font-medium bg-[#414652] text-white px-3 lg:text-lg test-base rounded-md",
                ),
                xt.text(
                    SKILLS[0]["keywords"][1],
                    class_name="font-medium bg-[#414652] text-white px-3 lg:text-lg test-base rounded-md",
                ),
                xt.text(
                    SKILLS[0]["keywords"][2],
                    class_name="font-medium bg-[#414652] text-white px-3 lg:text-lg test-base rounded-md",
                ),
                xt.text(
                    SKILLS[0]["keywords"][3],
                    class_name="font-medium bg-[#414652] text-white px-3 lg:text-lg test-base rounded-md",
                ),
                xt.text(
                    SKILLS[0]["keywords"][4],
                    class_name="font-medium bg-[#414652] text-white px-3 lg:text-lg test-base rounded-md",
                ),
                xt.text(
                    SKILLS[0]["keywords"][5],
                    class_name="font-medium bg-[#414652] text-white px-3 lg:text-lg test-base rounded-md",
                ),
                xt.text(
                    SKILLS[0]["keywords"][2],
                    class_name="font-medium bg-[#414652] text-white px-3 lg:text-lg test-base rounded-md",
                ),
                class_name="flex items-center flex-wrap gap-2 mt-2",
            ),
        ),
        class_name="mt-6",
    )
    return layout


def projects():
    layout = xt.box(
        xt.box(
            xt.text(
                "Projects",
                class_name="font-bold text-2xl lg:text-3xl",
            ),
            xt.box(
                xt.box(
                    xt.box(
                        xt.text(
                            PROJECTS[0]["name"],
                            class_name="font-bold",
                            font_size="1.2em",
                        ),
                        xt.text(
                            PROJECTS[0]["description"],
                            class_name="max-w-[200px]",
                            font_size="1em",
                        ),
                        xt.box(
                            xt.text(
                                "Side Project",
                                class_name="font-medium bg-[#f3f4f6] text-sm px-2 rounded-md",
                            ),
                            xt.text(
                                SKILLS[0]["keywords"][1],
                                class_name="font-medium bg-[#f3f4f6] text-sm px-2 rounded-md",
                            ),
                            class_name="flex gap-1 items-center mt-4",
                        ),
                        xt.box(
                            xt.text(
                                "Next.js",
                                class_name="font-medium bg-[#f3f4f6] text-sm px-2 rounded-md",
                            ),
                            xt.text(
                                "Vite",
                                class_name="font-medium bg-[#f3f4f6] text-sm px-2 rounded-md",
                            ),
                            xt.text(
                                SKILLS[0]["keywords"][4],
                                class_name="font-medium bg-[#f3f4f6] text-sm px-2 rounded-md",
                            ),
                            class_name="flex gap-1 items-center mt-2",
                        ),
                        xt.text(
                            "React",
                            class_name="font-medium bg-[#f3f4f6] w-14 text-sm text-center  mt-2 rounded-md",
                        ),
                        class_name="border-solid border w-60 h-52 p-3 mt-2 rounded-md border-[#6b7280]/12",
                    ),
                    xt.box(
                        xt.text(
                            PROJECTS[1]["name"],
                            class_name="font-bold",
                            font_size="1.2em",
                        ),
                        xt.text(
                            PROJECTS[1]["description"],
                            class_name="max-w-[200px]",
                            font_size="1em",
                        ),
                        xt.box(
                            xt.text(
                                "Side Project",
                                class_name="font-medium bg-[#f3f4f6] px-2 text-sm rounded-md",
                            ),
                            xt.text(
                                SKILLS[0]["keywords"][1],
                                class_name="font-medium bg-[#f3f4f6] px-2 text-sm rounded-md",
                            ),
                            class_name="flex gap-1 items-center mt-2",
                        ),
                        xt.box(
                            xt.text(
                                "Next.js",
                                class_name="font-medium bg-[#f3f4f6] px-2 text-sm rounded-md",
                            ),
                            xt.text(
                                "Browser extension",
                                class_name="font-medium bg-[#f3f4f6] px-2 text-sm rounded-md",
                            ),
                            class_name="flex gap-1 items-center mt-2",
                        ),
                        class_name="border-solid border w-60 h-52  p-3 mt-2 rounded-md border-[#6b7280]/12",
                    ),
                    xt.box(
                        xt.text(
                            PROJECTS[2]["name"],
                            class_name="font-bold",
                            font_size="1.2em",
                        ),
                        xt.text(
                            PROJECTS[2]["description"],
                            class_name="max-w-[200px]",
                            font_size="1em",
                        ),
                        xt.box(
                            xt.text(
                                "Side Project",
                                class_name="font-medium bg-[#f3f4f6] px-2 text-sm rounded-md",
                            ),
                            xt.text(
                                "Next.js",
                                class_name="font-medium bg-[#f3f4f6] px-2 text-sm rounded-md",
                            ),
                            xt.text(
                                "MDX",
                                class_name="font-medium bg-[#f3f4f6] px-2 text-sm rounded-md",
                            ),
                            class_name="flex gap-1 items-center mt-14",
                        ),
                        class_name="border-solid border w-60 h-52 p-3 mt-2 rounded-md border-[#6b7280]/12",
                    ),
                    xt.box(
                        xt.text(
                            PROJECTS[3]["name"],
                            class_name="font-bold",
                            font_size="1.2em",
                        ),
                        xt.text(
                            PROJECTS[3]["description"],
                            class_name="max-w-[200px]",
                            font_size="1em",
                        ),
                        xt.box(
                            xt.text(
                                "Side Project",
                                class_name="font-medium bg-[#f3f4f6] px-2 text-sm rounded-md",
                            ),
                            xt.text(
                                "Next.js",
                                class_name="font-medium bg-[#f3f4f6] px-2 text-sm rounded-md",
                            ),
                            class_name="flex gap-1 items-center mt-4",
                        ),
                        xt.text(
                            "Puppeteer",
                            class_name="font-medium bg-[#f3f4f6] w-24 text-center mt-2 text-sm rounded-md",
                        ),
                        class_name="border-solid border w-60 h-52 p-3 mt-2 rounded-md border-[#6b7280]/12",
                    ),
                    class_name="grid lg:grid-cols-4 md:grid-cols-3 grid-cols-1 gap-2 md:gap-4 items-center",
                    # class_name="flex overflow-y-scroll lg:overflow-hidden	gap-2 md:gap-4",
                ),
                class_name="flex",
            ),
        ),
        class_name="mt-6",
    )
    return layout


def index() -> xt.Component:
    return xt.fragment(
        xt.box(
            basic_section(),
            about(),
            work_experience(),
            education(),
            skills(),
            projects(),
            class_name="mt-8 lg:mt-16 mx-4 md:mx-10 mb-8 lg:mx-80",
        ),
    )


app = xt.App()
app.add_page(index)
