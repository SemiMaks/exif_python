from exif import Image

br = "-----------------------------"
with open('./image/foto1.jpg', 'rb') as f1_f:
    foto1 = Image(f1_f)

with open('./image/foto2.jpg', 'rb') as f2_f:
    foto2 = Image(f2_f)

images = [foto1, foto2]


def exif_status():
    for index, image in enumerate(images):
        if image.has_exif:
            status = f"содержит EXIF информацию (версия {image.exif_version})."
        else:
            status = "не содержит какой либо EXIF информации."
            print(f"Фото {index} {status}")
    return print(status, '\n')


def members():
    image_members = []

    for image in images:
        image_members.append(dir(image))

    for index, image_member_list in enumerate(image_members):
        print(f"Фото {index + 1} содержит {len(image_member_list)} значения:")
        print(f"{image_member_list}\n")


def model():
    for index, image in enumerate(images):
        print(f"Информация о камере - Фото {index + 1}:")
        print(br)
        print(f"Производитель: {image.make}")
        print(f"Модель: {image.model}")
        print(f"Фото снято: {image.datetime_original}.{image.subsec_time_original} {image.get('время', '')}\n")


def gps_func():
    def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
        decimal_degress = coordinates[0] + coordinates[1] / 60 + coordinates[2] / 3600
        if coordinates_ref == "S" or coordinates_ref == "W":
            decimal_degress = - decimal_degress

        return decimal_degress

    for index, image in enumerate(images):
        print(f"Координаты - Фото {index + 1}")
        print(br)
        print(f"Широта (DMS): {image.gps_latitude} {image.gps_latitude_ref}")
        print(f"Долгота (DVC): {image.gps_longitude} {image.gps_longitude_ref}\n ")
        print(f"Широта (DD): {dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)}")
        print(f"Долгота (DD): {dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)}\n")


exif_status()
members()
model()
gps_func()
