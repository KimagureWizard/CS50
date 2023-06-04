def mtype(n):

    n = n.lstrip().lower()

    if n.find(".gif") >= 0:
        return print("image/gif")

    elif n.find(".jpg") >= 0:
        return print("image/jpeg")

    elif n.find("jpeg") >= 0:
        return print("image/jpeg")

    elif n.find(".png") >= 0:
        return print("image/png")

    elif n.find(".pdf") >= 0:
        return print("application/pdf")

    elif n.find(".txt") >= 0:
        return print("text/plain")

    elif n.find(".zip") >= 0:
        return print("application/zip")

    else:
        return print("application/octet-stream")

def main():

    name = input("")

    mtype(name)


main()