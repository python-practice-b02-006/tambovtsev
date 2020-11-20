import body


def read_data(bodies):
    """
    This function reads data from the file "data.txt" line by line and initializes bodies.
    Each line contains information about one body. Lines, staring with '#' and empty lines are skipped.

    Format of the line:
    mass x y vx vy radius color(optional)
    """
    # Creates file if it didn't exist.
    inp = open("data.txt", 'a')
    inp.close()

    inp = open("data.txt", 'r')

    for line in inp:
        if len(line.strip()) == 0 or line[0] == '#':
            continue
        data = line.split()

        if len(data) > 6:
            color = data[6]
        else:
            color = 0

        data = [float(data[0]), [float(data[1]), float(data[2])], [float(data[3]), float(data[4])], int(data[5])]

        if color:
            data.append(color)

        body.Body(bodies, *data)

    inp.close()


def write_data(bodies):
    """
    This function writes information about the system into a file.
    """
    with open("data.txt", "w", encoding="utf8") as f:
        f.write("\n".join([" ".join(map(str,
                [b.mass, *b.pos, *b.vel, b.radius, b.color]))
                for b in bodies]))