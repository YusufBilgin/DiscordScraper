from datetime import datetime

def save_content_to_txt(data):
    with open("Discord info %s.txt" % datetime.now().strftime(f"%d-%m-%Y"), "w", encoding = "utf-8") as f:
        f.write(data + "\n\n\n" + datetime.now() \
            .strftime(f"Data created on: %d.%m.%Y  %H:%M"))