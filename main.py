from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(10, 10), Point(300, 300))
    win.draw_line(line, "black")
    line = Line(Point(50, 100), Point(20, 300))
    win.draw_line(line, "blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()