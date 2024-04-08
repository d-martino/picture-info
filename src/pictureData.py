import exiftool

files = ["pic.jpg"]
with exiftool.ExifToolHelper() as et:
    metadata = et.get_metadata(files)
    print(metadata)
    dateTimeOriginal = et.get_tags(files, "EXIF:DateTimeOriginal")
    print(dateTimeOriginal)
    print(et.get_tags(files, "File:FileModifyDate"))
    et.set_tags(files, {"File:FileModifyDate": dateTimeOriginal[0]['EXIF:DateTimeOriginal']})
    print(et.get_tags(files, "File:FileModifyDate"))
    for d in metadata:

        print("{:20.20} {:20.20}".format(d["SourceFile"],
                                         d["EXIF:DateTimeOriginal"]))
