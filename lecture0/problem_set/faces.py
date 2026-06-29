def main():
    face = input()
    print(convert(face))

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()