class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status: bool = False
        self.muted: bool = False
        self.volume: int = Television.MIN_VOLUME
        self.channel: int = Television.MIN_CHANNEL

    def power(self):
        """
        Powers the tv off and on
        """
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        """
        Mutes and unmutes the tv if it is powered on
        """
        if self.status:
            if self.muted:
                self.muted = False
            else:
                self.muted = True

    def channel_up(self):
        """
        Goes to the next channel if tv is on
        Goes to first channel if increasing beyond the last channel
        """
        if self.status:
            if self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        """
        Goes to the previous channel if tv is on
        Goes to last channel if lowering the channel below channel one
        """
        if self.status:
            if self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        """
        Increases the volume if the tv is on and does not go above max volume
        Unmutes the tv
        """
        self.muted = False
        if self.status:
            if self.volume != Television.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        """
        Decreases the volume if the tv is on and does not go below 0
        Unmutes the tv
        """
        self.muted = False
        if self.status:
            if self.volume != Television.MIN_VOLUME:
                self.volume -= 1

    def get_status(self):
        return self.status

    def get_muted(self):
        return self.muted

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume

    def __str__(self) -> str:
        """

        :return: Returns the formatted string for the object
        """
        final_volume: int = 0
        if self.muted:
            final_volume = 0
        else:
            final_volume = self.volume
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {final_volume}"
