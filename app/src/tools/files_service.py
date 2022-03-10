def generate_subscribers_file(subscribers):
    emails = [sub["email"] for sub in subscribers]
    with open("app/src/tools/tmp/subscribers.txt", "w+") as file:
        file.seek(0)
        file.truncate()
        file.writelines("\n".join(emails))
