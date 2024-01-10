type ParkingSystem struct {
	big, medium, small int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{
		big: big*1,
		medium: medium*2,
		small: small*3,
	}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	if carType == 1 {
		if this.big-1 >= 0 {
			this.big -= 1
			return true
		}
		return false
	} else if carType == 2 {
		if this.medium-2 >= 0 {
			this.medium -= 2
			return true
		}
		return false
	} else if carType == 3 {
		if this.small-3 >= 0 {
			this.small -= 3
			return true
		}
		return false
	}
	return false
}
