# Write your code here :-)
class Information:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return "Info (%s, %s)" % (self.a, self.b)

i1 = Information(1, 2)
i2 = Information(3, 4)
name = "tim"
dns = {
    "google.com" : "8.8.8.8",
    "timgolden.me.uk" : ["192.168.0.1", "1.2.3.4"],
    "tommypujol.him" : "123.456.67.78",
    "www.timgolden.me.uk" : "192.168.0.1",
    "tomasreyna.com" : [i1, i2],
    name : "192.3.4.5"
}
print(name)
print(dns['tomasreyna.com'])
print(dns['tim'])