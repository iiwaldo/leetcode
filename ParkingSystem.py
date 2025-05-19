class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small
        self.parking_dict = {"big":0 , "medium":0 , 'small':0}
    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            avalbile_space = self.parking_dict['big'] < self.big
            self.parking_dict['big'] = self.parking_dict['big'] + 1
            return avalbile_space
        elif carType == 2:
            avalbile_space = self.parking_dict['medium'] < self.medium
            self.parking_dict['medium'] = self.parking_dict['medium'] + 1
            return avalbile_space
        elif carType==3:
            avalbile_space = self.parking_dict['small'] < self.small
            self.parking_dict['small'] = self.parking_dict['small'] + 1
            return avalbile_space

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)