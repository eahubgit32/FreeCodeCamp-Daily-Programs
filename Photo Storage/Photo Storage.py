def number_of_photos(photo_size_mb, drive_size_gb):

    Number_of_Photos = int((drive_size_gb * 1000)/photo_size_mb)

    return Number_of_Photos

print(number_of_photos(1, 1))
