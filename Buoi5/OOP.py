class StarCookie:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
    
    def cook(self):
        print("The StarCookie has been cooked")

star_cookie = StarCookie("15","red")
print("StarCookie: " + star_cookie.weight + " " + star_cookie.color)
star_cookie.cook()