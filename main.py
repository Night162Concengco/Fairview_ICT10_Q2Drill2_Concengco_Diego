from js import document
from pyodide.ffi import create_proxy

club_members = [
    "Athena Aria",
    "Matt Nicolas",
    "Lily Cawthon",
    "Jenny Parker",
    "kelly bridge"
]

def add_member(event):
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()
    full_name = f"{first_name} {last_name}".strip()
    club_members.append(full_name)
    document.getElementById("result").innerText = f"Congratulations {full_name}! You are now part of the ICT club."
    document.getElementById("members-list").innerText = ", ".join(club_members)
    document.getElementById("member-count").innerText = f"Official Club Members: {len(club_members)} STUDENTS"
    document.getElementById("fname").value = ""
    document.getElementById("lname").value = ""
def setup(event=None):
    document.getElementById("members-list").innerText = ", ".join(club_members)
    document.getElementById("member-count").innerText = f"Official Club Members: {len(club_members)} STUDENTS"
    button = document.getElementById("btn-submit")
    button.addEventListener("click", create_proxy(add_member))
setup()
