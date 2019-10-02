from tkinter import *



class HGauge:

    def __init__(self, width, height, min_value, max_value, value):
        self.width = width
        self.height = height
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.bar_color = 'red'
        self.bg_color = 'black'
        self.border_color = 'white'

    def set_value(self, value):
        if value > self.max_value:
            self.value = self.max_value
        elif value < self.min_value:
            self.value = self.min_value
        else:
            self.value = value

    def show(self, parent):
        self.g = Canvas(width=self.width, height=self.height, bg=self.border_color, borderwidth=0)
        self.g.create_rectangle(3, 3, self.width, self.height, fill=self.bg_color, outline=self.bg_color)
        return self.g

    def update(self, value):
        self.set_value(value)
        self.g.delete('all')
        self.g.create_rectangle(3, 3, self.width, self.height, fill=self.bg_color, outline=self.bg_color)
        if self.value != 0:
            self.g.create_rectangle(4, 4, (self.width - 1) / self.max_value * self.value, self.height - 1,
                                    fill=self.bar_color, outline=self.bar_color)


class VGauge:

    def __init__(self, width, height, min_value, max_value, value):
        self.width = width
        self.height = height
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.bar_color = 'red'
        self.bg_color = 'black'
        self.border_color = 'white'
        self.g = None

    def set_value(self, value):
        if value > self.max_value:
            self.value = self.max_value
        elif value < self.min_value:
            self.value = self.min_value
        else:
            self.value = value

    def show(self, parent):
        self.g = Canvas(width=self.width, height=self.height, bg=self.border_color, borderwidth=0)
        self.g.create_rectangle(3, 3, self.width, self.height, fill=self.bg_color, outline=self.bg_color)
        return self.g

    def update(self, value):
        self.set_value(value)
        self.g.delete('all')
        self.g.create_rectangle(3, 3, self.width, self.height, fill=self.bg_color, outline=self.bg_color)
        if self.value != 0:
            self.g.create_rectangle(4, self.height - 1, self.width - 1,
                                    self.height - (self.height - 4) / self.max_value * self.value, fill=self.bar_color,
                                    outline=self.bar_color)


class VVuMeter:

    def __init__(self, min_value, max_value, value):
        self.width = 50
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.bar_on_color = 'red'
        self.bar_off_color = 'grey'
        self.bg_color = 'black'
        self.border_color = 'white'
        self.g = None
        self.bars = []
        self.interval = 3
        self.bar_height = 7
        self.bar_number = 10
        self.height = self.bar_number * (self.interval + self.bar_height) + 4
        self.num_bars_lit = 0

    def set_value(self, value):
        if value > self.max_value:
            self.value = self.max_value
        elif value < self.min_value:
            self.value = self.min_value
        else:
            self.value = value

    def update(self, value):
        self.bars = []
        for i in range(1, self.bar_number + 1):
            x = self.height - 2 - ((i - 1) * (self.bar_height + self.interval))
            y = x - self.bar_height
            self.bars.append((5, x, self.width - 2, y))
        self.set_value(value)
        self.g.delete('all')
        self.g.create_rectangle(3, 3, self.width, self.height, fill=self.bg_color, outline=self.bg_color)

        self.num_bars_lit = int(value / self.max_value * self.bar_number)
        current_bar = 1
        for bar in self.bars:
            if current_bar > self.num_bars_lit:
                self.g.create_rectangle(bar[0], bar[1], bar[2],
                                        bar[3], fill=self.bar_off_color,
                                        outline=self.bar_off_color)
            else:
                self.g.create_rectangle(bar[0], bar[1], bar[2],
                                        bar[3], fill=self.bar_on_color,
                                        outline=self.bar_on_color)
            current_bar += 1

    def show(self, parent):
        self.height = self.bar_number * (self.interval + self.bar_height) + 4
        self.g = Canvas(width=self.width, height=self.height, bg=self.border_color, borderwidth=0)
        self.g.create_rectangle(3, 3, self.width, self.height, fill=self.bg_color, outline=self.bg_color)
        return self.g
