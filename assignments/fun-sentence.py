SENTENCE_START: str = "Panaversity is awesome! I learned to code and now I can "  

def main():
    adj = str(input("Enter a wacky adjective: "))
    noun = str(input("Enter a random noun: "))
    verb = str(input("Enter a super cool verb: "))
    print(f"{SENTENCE_START}{verb} a {adj} {noun}!")

if __name__ == "__main__":
    main()
