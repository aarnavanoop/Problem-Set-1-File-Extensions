def check(saying):
    if saying.endswith(".gif"):
        print("image/gif")
    elif saying.endswith("jpg") or saying.endswith("jpeg"):
        print("image/jpeg")
    elif saying.endswith(".png"):
        print("image/png")
    elif saying.endswith(".pdf"):
        print("application/pdf")
    elif saying.endswith("txt"):
        print("text/plain")
    elif saying.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")



def main():
    file_name = input("What's the name of the file?: ").strip().lower()
    check(file_name)


main()