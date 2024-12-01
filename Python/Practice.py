class Human:
  def work(self):
    print("I can work.")
  def flirt(self):
    print("I can flirt.")
class child(Human):
  def eat(self):
    print("I can eat.")
  def work(self):
    super().work()
    print("I cannot work.")
res = child()
res.work()