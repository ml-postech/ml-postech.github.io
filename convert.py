# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "beautifulsoup4",
#     "pydantic",
#     "pyyaml",
# ]
# ///
from __future__ import annotations
from bs4 import BeautifulSoup
from pathlib import Path
from pydantic import BaseModel
from typing import Iterator
import base64
import yaml


class Profile(BaseModel):
    name: str
    role: str
    email: str
    webpage: str | None = None
    category: str
    image_base64_url: str

    def save(self, directory: Path) -> None:
        directory.mkdir(parents=True, exist_ok=True)
        filename = self.category + "-" + self.name.replace(" ", "-").lower()

        if (directory / f"{filename}.md").exists():
            raise FileExistsError(f"{directory / f'{filename}.md'} already exists")

        data = self.model_dump(
            exclude_none=True,
        )
        data.pop("image_base64_url", None)  # Exclude image data from YAML

        if "jpg" in self.image_base64_url or "jpeg" in self.image_base64_url:
            image_extension = "jpg"
        elif "png" in self.image_base64_url:
            image_extension = "png"
        else:
            raise ValueError("Unsupported image format in base64 URL")
        image_data = self.image_base64_url.split(",")[1]
        (directory / f"{filename}.{image_extension}").write_bytes(
            base64.urlsafe_b64decode(image_data)
        )
        data["image"] = f"{filename}.{image_extension}"
        (directory / f"{filename}.md").write_text(f"""---
{yaml.dump(data, sort_keys=False)}---
""")


class Professor(Profile): ...


class Professors(list[Professor]):
    @staticmethod
    def from_people_html_string(html_string: str) -> Iterator[Profile]:
        soup = BeautifulSoup(html_string, "html.parser")
        divs = soup.select("div.profile-info-prof")
        for div in divs:
            name: str = div.h4.contents[0].strip()
            webpage: str = div.h4.a["href"] if div.h4.a else None
            assert webpage is not None
            role: str = div.select_one("p.sub-text").contents[0].strip()
            email: str = (
                div.select_one("p.sub-text").contents[2].strip().replace(" (at) ", "@")
            )
            img_tag = div.find_previous_sibling("div").img
            assert img_tag is not None
            image_base64_url = _base64_url_from_img_tag(img_tag)

            yield Profile(
                name=name,
                role=role,
                email=email,
                webpage=webpage,
                category="advisor",
                image_base64_url=image_base64_url,
            )


class Student(Profile):
    enrollment_year: int
    graduation_year: int | None = None
    areas_of_interest: list[str]


class Students(list[Student]):
    @staticmethod
    def from_people_html_string(html_string: str) -> Iterator[Student]:
        soup = BeautifulSoup(html_string, "html.parser")
        divs = soup.select("div.profile-info-stud")
        for div in divs:
            course_info: str = div.select_one("p.sub-text-course").contents[0].strip()
            if "Administrative Officer" in course_info:
                continue

            enrollment_year = int("20" + course_info.split("'")[1].split(" ")[0])
            if "Combined" in course_info:
                degree = "Ph.D./M.S."
            elif "Ph.D." in course_info:
                degree = "Ph.D."
            elif "Master" in course_info:
                degree = "M.S."

            name: str = div.h4.contents[0].strip()
            webpage: str = div.h4.a["href"] if div.h4.a else None
            sub_text_contents = [
                content.strip()
                for content in div.select_one("p.sub-text").stripped_strings
                if content.strip() and content.strip() != "<br/>"
            ]
            email: str = sub_text_contents[0].replace(" (at) ", "@")
            areas_of_interest: list[str] = (
                [area.strip() for area in sub_text_contents[1].split(",")]
                if len(sub_text_contents) > 1
                else []
            )
            img_tag = div.find_previous_sibling("div").img
            assert img_tag is not None
            image_base64_url = _base64_url_from_img_tag(img_tag)

            yield Student(
                name=name,
                role=degree,
                email=email,
                webpage=webpage,
                category="student",
                image_base64_url=image_base64_url,
                enrollment_year=enrollment_year,
                areas_of_interest=areas_of_interest,
            )


class Alumni(Profile):
    enrollment_year: int = None
    graduation_year: int
    current_position: str | None = None


class Alumnis(list[Alumni]):
    """
    <div class="col-sm-2">
      <div class="profile-image-alumni">
        <img src="img/bckoh_profile.jpg" alt=""  />
      </div>
      <div class="profile-info-alumni">
        <p class="sub-text-course">'22 MS, Nalbi</p>
        <h5 class="name-alumni">ByungChan Ko</h5>
        <p class="sub-text">
          kbc6723 (at) postech.ac.kr <br/>
        </p>
      </div>
    </div>
    """

    @staticmethod
    def from_people_html_string(html_string: str) -> Iterator[Alumni]:
        soup = BeautifulSoup(html_string, "html.parser")
        divs = soup.select("div.profile-info-alumni")
        for div in divs:
            course_info: str = div.select_one("p.sub-text-course").contents[0].strip()

            graduation_year = int("20" + course_info.split("'")[1].split(" ")[0])
            if "MS" in course_info:
                degree = "M.S."
            elif "Ph.D." in course_info:
                degree = "Ph.D."

            name: str = div.h5.contents[0].strip()
            webpage: str = div.h5.a["href"] if div.h5.a else None
            sub_text_contents = [
                content.strip()
                for content in div.select_one("p.sub-text").stripped_strings
                if content.strip() and content.strip() != "<br/>"
            ]
            email: str = sub_text_contents[0].replace(" (at) ", "@")
            current_position: str | None = (
                sub_text_contents[1] if len(sub_text_contents) > 1 else None
            )
            img_tag = div.find_previous_sibling("div").img
            assert img_tag is not None
            image_base64_url = _base64_url_from_img_tag(img_tag)

            yield Alumni(
                name=name,
                role=degree,
                email=email,
                webpage=webpage,
                category="alumni",
                image_base64_url=image_base64_url,
                graduation_year=graduation_year,
                current_position=current_position,
            )


class Officer(Profile): ...


class Officers(list[Officer]):
    @staticmethod
    def from_people_html_string(html_string: str) -> Iterator[Officer]:
        soup = BeautifulSoup(html_string, "html.parser")
        divs = soup.select("div.profile-info-stud")
        for div in divs:
            course_info: str = div.select_one("p.sub-text-course").contents[0].strip()
            if "Administrative Officer" not in course_info:
                continue

            role = "Administrative Officer"

            name: str = div.h4.contents[0].strip()
            webpage: str = div.h4.a["href"] if div.h4.a else None
            sub_text_contents = [
                content.strip()
                for content in div.select_one("p.sub-text").stripped_strings
                if content.strip() and content.strip() != "<br/>"
            ]
            email: str = sub_text_contents[0].replace(" (at) ", "@")

            img_tag = div.find_previous_sibling("div").img
            assert img_tag is not None
            image_base64_url = _base64_url_from_img_tag(img_tag)

            yield Officer(
                name=name,
                role=role,
                email=email,
                webpage=webpage,
                category="officer",
                image_base64_url=image_base64_url,
            )


def _base64_url_from_img_tag(
    img_tag, base_directory: Path = Path(__file__).parent
) -> str:
    img_path = base_directory / img_tag["src"]
    img_data = img_path.read_bytes()
    img_base64 = base64.urlsafe_b64encode(img_data).decode("utf-8")

    if img_path.suffix.lower() in [".jpg", ".jpeg"]:
        return f"data:image/jpeg;base64,{img_base64}"
    elif img_path.suffix.lower() == ".png":
        return f"data:image/png;base64,{img_base64}"
    else:
        raise ValueError(f"Unsupported image format: {img_path.suffix}")


def export_profiles():
    people_html_string = (Path(__file__).parent / "people.html").read_text()

    professors = Professors.from_people_html_string(people_html_string)
    students = Students.from_people_html_string(people_html_string)
    alumnis = Alumnis.from_people_html_string(people_html_string)
    officers = Officers.from_people_html_string(people_html_string)

    for person in list(professors) + list(students) + list(alumnis) + list(officers):
        person.save(Path(__file__).parent / "people")


if __name__ == "__main__":
    export_profiles()
