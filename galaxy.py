from random import randrange
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, x = None, y = None, z = None):
        self.__x = x if x else randrange(1, 20)
        self.__y = y if y else randrange(1, 20)
        self.__z = z if z else randrange(1, 20)

    def coords(self):
        return (self.__x, self.__y, self.__z)

class Location:
    def __init__(self, coords=None, conns=None):
        self.__coords = coords if coords else Coordinate()
        self.__connects = []

    def coords(self):
        return self.__coords.coords()

    def gen_connects(self, num=None, origin=None):
        num_connects = num if num else randrange(start=1, stop=5)
        new_connects = []
        print('Generating %d connections from' % num_connects, origin.coords())
        for i in range(num_connects):
            loc = Location()
            loc.add_connect(origin)
            new_connects.append(loc)
        return new_connects
            
    def add_connect(self, location):
        self.__connects.append(location)
        
    def connects(self):
        return self.__connects

class Galaxy:
    def __init__(self, origin=None):
        self.__origin = origin if origin else Location()
        self.__levels = [[origin]] # galaxy contains a 2 dimensional list of levels
        
    def describe(self):
        #if self.__origin:
            #print('Origin =', self.__origin.coords())
        level = 0
        for loc in self.__levels:
            print('Level %d' % level)
            for l in loc:
                print(l)
            level += 1
            
    def list_all(self):
        for loc in self.__levels:
            for point in loc:
                print(point.coords())
            
    def build(self, levels):
        cur_level = 0
        # For each level, loop through levels
        # For each location:
        # 1. Generate number of connections
        # 2. For each connection:
        #    1. Create a location object with random coordinates
        #    2. Add connection back to original location
        #    3. Add to list of new connections
        #    4. Append list to master list
        for level in range(levels):
            print('Generating level %d' % (level+1))
            new_connects = []
            for loc in self.__levels[level]:
                #print('Generation connections for location', loc.coords())
                new_connects.extend(loc.gen_connects(num=2, origin=loc))
            self.__levels.append(new_connects)
            print(self.__levels)
            print("Level %d" % level, self.__levels[level])
        print(self.__levels)
                
    def add_location(self, location):
        self.__levels.append(location)

    def coords_x(self, axis = None):
        return [loc.coords()[0] for loc in self.__levels]

    def coords_y(self, axis = None):
        return [loc.coords()[1] for loc in self.__levels]

    def coords_z(self, axis = None):
        return [loc.coords()[2] for loc in self.__levels]

    def levels(self):
        return self.__levels

    def plot(self):
        points = []
        for level in self.__levels:
            for loc in level:
                points.append(loc.coords())
        print(points)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection = '3d')
        
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        z = [point[2] for point in points]
        
        ax.scatter(x, y, z, c = 'r', marker = 'o')
        
        for level in self.__levels:
            for loc in level:
                for connect in loc.connects():
                    print('Plotting', loc.coords(), 'to', connect.coords())
                    ax.plot([loc.coords()[0], connect.coords()[0]],
                            [loc.coords()[1], connect.coords()[1]],
                            [loc.coords()[2], connect.coords()[2]])
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()


origin = Location(Coordinate(x=2, y=3, z=1), conns=2)
galaxy = Galaxy(origin=origin)
galaxy.build(levels=3)
#galaxy = Galaxy()

galaxy.describe()
galaxy.list_all()

galaxy.plot()
#galaxy.add_location(start_loc)

#galaxy = Galaxy()
#levels = galaxy.levels()

#print(galaxy.coords_x())
#print(galaxy.coords_y())
#print(galaxy.coords_z())

"""
points = [(1, 1, 1),
          (2, 2, 2),
          (2, 3, 1)]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(x, y, z, c='r', marker='o')
ax.plot([1, 2], [1, 2], [1, 2])
ax.plot([1, 2], [1, 3], [1, 1])
plt.show()
"""

ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],VecEnd_y[i]],zs=[VecStart_z[i],VecEnd_z[i]])