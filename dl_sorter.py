import os

uprofile = "USERPROFILE"
downloadsPath = os.path.join(os.getenv(uprofile), "Downloads")
picturesPath = os.path.join(os.getenv(uprofile), "Pictures")
documentsPath = os.path.join(os.getenv(uprofile), "Documents")
videosPath = os.path.join(os.getenv(uprofile), "Videos")
musicPath = os.path.join(os.getenv(uprofile), "Music")

documentExt = ["doc", "docx", "xls", "xlsx", "ppt", "pdf", "txt"]
videoExt = ["mp4", "avi", "mkv", "mov"]
pictureExt = ["png", "jpg", "jpeg", "webm"]
musicExt = ["mp3", "wav"]


file_list = os.listdir(downloadsPath)


def moveFilesFromDownloads(destPath, item):
    destPathItem = os.path.join(destPath, item)
    sourceItem = os.path.join(downloadsPath, item)

    if os.path.exists(destPathItem):
        print("ada duplikat " + item + " pada folder tujuan, melewati...")
    else:
        if os.path.exists(destPath):
            os.rename(sourceItem, destPathItem)
        else:
            print("path " + destPath + " tidak ditemukan")


print("Mulai sorting file dari folder Downloads")
for list in file_list:
    name, ext = os.path.splitext(list)
    ext = ext[1:].lower()
    if ext in pictureExt:
        print(
            "memindah "
            + list
            + " dari "
            + os.path.join(downloadsPath, list)
            + " ke "
            + os.path.join(picturesPath, list)
        )

        moveFilesFromDownloads(picturesPath, list)
    elif ext in documentExt:
        print(
            "memindah "
            + list
            + " dari "
            + os.path.join(downloadsPath, list)
            + " ke "
            + os.path.join(documentsPath, list)
        )
        moveFilesFromDownloads(documentsPath, list)
    elif ext in musicExt:
        print(
            "memindah "
            + list
            + " dari "
            + os.path.join(downloadsPath, list)
            + " ke "
            + os.path.join(musicPath, list)
        )
        moveFilesFromDownloads(musicPath, list)
    elif ext in videoExt:
        print(
            "memindah "
            + list
            + " dari "
            + os.path.join(downloadsPath, list)
            + " ke "
            + os.path.join(videosPath, list)
        )
        moveFilesFromDownloads(videosPath, list)
    else:
        print("terissa: " + list)
