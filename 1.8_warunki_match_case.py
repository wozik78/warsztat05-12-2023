#match_case -instrukcja warunkowa

lang=input('prosze podaj znany ci jezyk programowania:')

match lang.lower().replace(" ",""):
    case "java":
        print("Java")
    case "python":
        print("python")
    case _: #domyslna wartosc

        print("domyslna")
