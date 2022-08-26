# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from ZoneMixer import zoneEater, zoneMaker, zoneWalker

if __name__ == '__main__':
    filename = "MTek.txt"

    # Read in the door list .txt file & generate rooms
    [Rooms, RoomCounts, door_descr, forcing] = zoneEater(filename)
    print('zoneEater complete!\n\n')

    # Say the results
    # totalCount = [0,0,0]
    # for R in Rooms.keys():
    #     print(R, ' Doors: ', Rooms[R], ', Count = ', RoomCounts[R])
    #     for i in range(3):
    #         totalCount[i] += RoomCounts[R][i]
    #
    # print('\nTotal door count: ', totalCount)

    # Connect rooms together to produce zones
    [map1, zones, zone_counts] = zoneMaker(Rooms, RoomCounts, forcing)
    print('zoneMaker complete!\n\n')
    print(map1)
    print(zones)
    print(zone_counts)


    [map2, walk] = zoneWalker(Rooms, zones, zone_counts, forcing)
    print('zoneWalker complete!\n\n')
    print('Final door mapping:')
    for m in map1:
        print('\t',m[0],' <-> ',m[1],':\t',door_descr[m[0]],' <-> ',door_descr[m[1]])
    print('Final trapdoor mapping:')
    for m in map2:
        print('\t',m[0],' --> ',m[1],':\t',door_descr[m[0]],' --> ',door_descr[m[1]])

    fullmap = [m for m in map1]
    fullmap.extend(map2)

    #print(walk)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
