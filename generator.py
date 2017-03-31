import math

def write_point(x, y, f):
    f.writelines(str(x) + ',' + str(y) + ',' +'0.\n');
    # print("write a point")

def write_last(f):
    f.writelines("</coordinates>\n")
    f.writelines("</LineString>\n")
    f.writelines("</Placemark>\n")
    f.writelines("</Document>\n")
    f.writelines("</kml>\n")

def generator(f):
    R = 5; r = 1; a = 4
    x0 = R + r - a
    y0 = 0
    nRev = 10
    t = 0.0

    original_x = -118.289272
    original_y = 34.021311

    while t < (math.pi * nRev):
        x = (R+r)*math.cos((r/R)*t) - a*math.cos((1+r/R)*t);
        y = (R+r)*math.sin((r/R)*t) - a*math.sin((1+r/R)*t);
        x += original_x
        y += original_y
        write_point(x, y, f)
        t += 0.01

if __name__ == '__main__':
    output_file = 'spiro.kml'
    f = open(output_file, 'a', encoding='latin1')
    generator(f)
    write_last(f)
    f.close()