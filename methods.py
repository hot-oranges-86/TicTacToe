def center(self, width, height) -> tuple[int, int]:

    screen_width = self.winfo_screenwidth()

    screen_height = self.winfo_screenheight()

    x = int((screen_width/2) - (width/2))

    y = int((screen_height/2) - (height/2))

    return x, y


def set_size(self, width, height) -> str:

    x, y = center(self, width, height)

    return f'{width}x{height}+{x}+{y}'
