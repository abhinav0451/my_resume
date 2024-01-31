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
        class_name="border-solid border w-10 h-10 flex items-center p-2 rounded-md border-[#6b7280]/50",
    )


def basic_section():
    layout = xt.box(
        xt.box(
            xt.text(BASICS["name"], class_name="font-bold", font_size="2em"),
            xt.text(
                BASICS["label"],
                " focused on building products with extra attention to details",
                class_name="text-[#6b7280] text-lg max-w-md",
            ),
            xt.text(
                BASICS["location"]["address"], class_name="text-base text-[#6b7280]"
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
            xt.text("About", class_name="font-bold", font_size="1.5em"),
            xt.text(
                BASICS["summary"], class_name="text-base max-w-2xl mt-2 text-[#6b7280]"
            ),
        ),
        class_name="mt-6",
    )
    return layout


def work_experience():
    layout = xt.box(
        xt.box(
            xt.text("Work Experience", class_name="font-bold", font_size="1.5em"),
            xt.box(
                xt.box(
                    xt.text(
                        WORK_EXPERIENCE[0]["name"], class_name="text-base font-bold "
                    ),
                    xt.text(
                        "Remote", class_name="text-base px-3 bg-[#f3f4f6] rounded-md"
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
                WORK_EXPERIENCE[0]["summary"], class_name="text-base text-[#6b7280]"
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
                            class_name="text-base px-3 bg-[#f3f4f6] rounded-md",
                        ),
                        class_name="flex gap-4 mt-2 items-center",
                    ),
                    xt.box(
                        xt.text(
                            WORK_EXPERIENCE[1]["startDate"],
                            "-",
                        ),
                        xt.text(
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
                    WORK_EXPERIENCE[2]["summary"], class_name="text-base text-[#6b7280]"
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
                            "-",
                        ),
                        xt.text(
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
                    WORK_EXPERIENCE[1]["summary"], class_name="text-base text-[#6b7280]"
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
                            "-",
                        ),
                        xt.text(
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
                    WORK_EXPERIENCE[3]["summary"], class_name="text-base text-[#6b7280]"
                ),
                class_name="mt-2",
            ),
        ),
        class_name="mt-6 ",
    )
    return layout


def index() -> xt.Component:
    return xt.fragment(
        xt.box(
            basic_section(),
            about(),
            work_experience(),
            class_name="mt-16 mx-4 lg:mx-96 ",
        ),
    )


app = xt.App()
app.add_page(index)
