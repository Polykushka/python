class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        if self.status:
            if self.muted:
                self.muted = False
            else:
                self.muted = True

    def channel_up(self):
        if self.status:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        if self.status:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        self.muted = False
        if self.status:
            if self.volume != Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        self.muted = False
        if self.status:
            if self.volume != Television.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        if self.muted:
            final_volume = 0
        else:
            final_volume = self.volume
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {final_volume}"
