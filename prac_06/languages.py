from prac_06.programming_language import ProgrammingLanguage


def main():
    language_list = []

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    language_list.append(ruby)
    language_list.append(python)
    language_list.append(visual_basic)

    for language in language_list:
        print(language)

    print("The dynamically typed langages are:")
    for language in language_list:
        if language.is_dynamic():
            print(language.language_name)


main()
