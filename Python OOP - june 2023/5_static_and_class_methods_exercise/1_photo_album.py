import math
from typing import List


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for row in range(self.pages)]
        self.current_row_index = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        if len(self.photos[self.current_row_index]) == 4:
            self.current_row_index += 1

        try:
            self.photos[self.current_row_index].append(label)
        except IndexError:
            return "No more free slots"
        return f"{label} photo added successfully on page {self.current_row_index + 1}" \
               f" slot {self.photos[self.current_row_index].index(label) + 1}"

    def display(self):
        # similar but not the same result
        # result = "\n".join([f"-----------\n{len(page) * '[]'}" for page in self.photos])
        result = 11 * "-" + "\n"
        for page in self.photos:
            result += " ".join(["[]" for photo_name in page]) + "\n"
            result += 11 * "-" + "\n"
        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())



