def number_of_files(file_size, file_unit, drive_size_gb):


    Total_Bytes =  drive_size_gb * 1_000_000_000

    file_size_in_bytes = 0

    if file_unit == "KB":
        file_size_in_bytes = file_size * 1000
      
    elif file_unit == "MB":
        file_size_in_bytes = file_size * 1_000_000

    else:
        file_size_in_bytes = file_size

    if file_size_in_bytes == 0:
        return 0
    

    number_of_files = int(Total_Bytes / file_size_in_bytes)

    return number_of_files

print(number_of_files(500, "KB", 1))
