import os


def Renamer():
    i = 0
    path ="E:/Governer Generative AI Course/GIAIC Q3/growth_mindset_challenge/assignment-4/assign-01/06_bulk_file_renamer/images/"
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".png"
        my_sourse = path + filename
        my_dest = path + my_dest
        os.rename(my_sourse, my_dest)
        i += 1

if __name__ == "__main__":
    Renamer()