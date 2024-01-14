import tkinter as tk


class RoundedButton(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, width=300, height=30, bg='white', highlightthickness=0)
        self.text = kwargs.get('text', '')
        self.command = kwargs.get('command', None)
        self.font = kwargs.get('font', ("Changa", 12))
        self.fg = kwargs.get('fg', "#080F17")
        self.bg = kwargs.get('bg', "#F7FAFC")

        self.button_rectangle = self._create_rounded_rect(0, 0, 300, 30, 10, fill=self.bg)

        self.button_label = tk.Label(self, text=self.text, font=self.font, bg=self.bg, fg=self.fg)
        self.button_label.place(x=150, y=15, anchor="center")

        self.bind("<Button-1>", self._execute_command)

    def _create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [x1+r, y1,
                  x1+r, y1,
                  x2-r, y1,
                  x2-r, y1,
                  x2, y1,
                  x2, y1+r,
                  x2, y1+r,
                  x2, y2-r,
                  x2, y2-r,
                  x2, y2,
                  x2-r, y2,
                  x2-r, y2,
                  x1+r, y2,
                  x1+r, y2,
                  x1, y2,
                  x1, y2-r,
                  x1, y2-r,
                  x1, y1+r,
                  x1, y1+r,
                  x1, y1]
        return self.create_polygon(points, **kwargs, smooth=True)

    def _execute_command(self, event):
        if self.command is not None:
            self.command()


