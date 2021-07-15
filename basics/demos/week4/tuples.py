from math import pi

def students_marks():
  name = input("Enter students' name: ")
  mark = float(input(f"Enter the mark for {name}"))
  return name, mark


def area_and_circ(radius):
  area = pi*radius**2
  circ = 2*pi*radius
  return area,circ

def run():
    tuplex = area_and_circ(float(input("Enter radius of your circle: ")))
    print("The area of your circle is {:.2f} and circunferences is {:.2f}".format(tuplex[0], tuplex[1]))
run()
