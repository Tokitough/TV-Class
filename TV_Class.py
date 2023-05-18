# Create a TV class with the stated attributes
class TV:
    channel: int
    volume: int
    on: bool
    
    # Create methods for the default constructor
    def __init__ (self):
        self.channel: 1
        self.volume: 1
        self.on: False
        
    # Method for turning the tv on or off
    def turn_on (self) -> None:
        self.on = True
        
    def turn_off (self) -> None:
        self.off = False
    
    # A method for getting the channel
    def get_channel (self) -> int:
        return self.channel
    
    def set_channel (self, channel) -> None:
        # Conditional statements for the amount of channels available
        if channel <= 120 and channel >= 1:
            self.channel = channel 
        else:
            print("\u001b[31mThat Channel does not exist!\u001b[31m")

    # Method for getting the volume
    def get_volume (self) -> int:
        return self.volume
    
    def set_volume (self, volume) -> None:
        # Conditional statements for the range of volume
        if volume <= 7 and volume >= 1:
            self.volume = volume 
        else:
            print("\u001b[31mThat Volume does not exist!\u001b[31m")

    # Method for chagning the channel
    def channel_up (self) -> None:
        # Conditional statements for the amount of channels available
        if self.channel + 1 <= 120 and self.channel + 1 >= 1:
            self.channel = self.channel + 1
        else:
            print("\u001b[31mThat Channel does not exist!\u001b[31m")
            
    def channel_down (self) -> None:
        # Conditional statements for the amount of channels available
        if self.channel - 1 >= 1 and self.channel - 1 >= 1:
            self.channel = self.channel - 1
        else:
            print("\u001b[31mThat Channel does not exist!\u001b[31m")
            
    # Method for chagning the volume
    def volume_up (self) -> None:
        # Conditional statements for the range of volume
        if self.volume + 1 <= 7 and self.volume + 1 >= 1:
            self.volume = self.volume + 1
        else:
            print("\u001b[31mThat Volume does not exist!\u001b[31m")
            
    def volume_down (self) -> None:
        # Conditional statements for the range of volume
        if self.volume - 1 <= 7 and self.volume - 1 >= 1:
            self.volume = self.volume - 1
        else:
            print("\u001b[31mThat Volume does not exist!\u001b[31m")

    