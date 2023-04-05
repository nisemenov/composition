# Composition

## Description:

The program presented in the lesson has a number of shortcomings and incomplete features. It is necessary to correct and improve it according to the following plan:

1. When calculating the surface area to be wallpapered, we do not "ruin" the self.square field. It remains the full wall area. After all, it may be needed if the composition of the wd list changes and the wallpapered area needs to be calculated again.
2. However, the class does not provide for the storage of side lengths, although they may also be required. For example, if you need to change one of the parameters of an existing object. The area of the room can always be calculated if the original parameters are stored. Therefore, it is not necessary to store the area itself in the field.
3. Fix the code so that Room objects have only four fields - `width`, `length`, `height`, and `wd`. The areas (full and wallpapered) should be calculated only when necessary by calling the methods.
4. The program calculates the area under the wallpaper but says nothing about how many wallpaper rolls are needed. Add a method that takes the length and width of one roll as arguments and returns the required number based on the wallpapered area.
5. Develop a program interface. Let it request data from the user and output the wallpapered surface area and the required number of wallpaper rolls.

## Script from the lesson:
```python
class Room:
     def __init__(self, x, y, z):
         self.square = 2 * z * (x + y)
         self.wd = []
     def add_wd(self, w, h):
         self.wd.append(WinDoor(w, h))
     def work_surface(self):
         new_square = self.square
         for i in self.wd:
             new_square -= i.square
         return new_square
 r1 = Room(6, 3, 2.7)
 print(r1.square)  #output 48.6
 r1.add_wd(1, 1)
 r1.add_wd(1, 1)
 r1.add_wd(1, 2)
 print(r1.work_surface())  #output 44.6
 ```
 
 ## Example of main.py implementation:
 ```python
 Enter dimensions of the room (LxWxH): 4x3x5
Enter dimensions of the one wallpaper (LxW): 30x1.25
Enter dimensions of the window/door (LxW) or input "next": 2x0.5
Enter dimensions of the window/door (LxW) or input "next": 1x1
Enter dimensions of the window/door (LxW) or input "next": 1.5x1
Enter dimensions of the window/door (LxW) or input "next": next
Area will be covered by wallpaper 66.5
Quantity of wallpapers: 2
```

---

Task 7 from course: <https://younglinux.info/oopython/course>
