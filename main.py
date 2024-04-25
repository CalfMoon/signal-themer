import os
import platform
import shutil

import asarPy


def theme_injector():
    asarPy.extract_asar(app_path(), "temp")

    shutil.copy("background.html", os.path.join("temp", "background.html"))

    shutil.rmtree(os.path.join("temp", "themes"))
    shutil.copytree("themes", os.path.join("temp", "themes"))

    themer_file = open(os.path.join("temp", "themer.css"), "w")
    themer_file.write("@import '" + os.path.join("themes", selected_theme()) + "';")
    themer_file.close()

    asarPy.pack_asar("temp", app_path())
    shutil.rmtree("temp")

def app_path():
    match platform.system():
        case "Linux":
            return "/usr/lib/signal-desktop/resources/app.asar"
        case "Windows":
            return os.path.join(os.getenv("LOCALAPPDATA"), r"Programs\signal-desktop\resources\app.asar")

def selected_theme():
    print("Which theme do you want to use?")
    print_theme_list()
    selected = input(">> ")
    
    while os.path.isfile(os.path.join("themes", selected)) == False:
        print("Error: The theme you have given doesn't exist in ./themes folder. Enter the correct one:")
        print_theme_list()
        selected = input(">> ")
    return selected

def print_theme_list():
    themes = os.listdir("./themes")
    for theme in themes:
        print("- " + theme)

theme_injector()
