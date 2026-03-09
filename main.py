from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)

    """c = Cell(win)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)"""

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100) # x1, y1, x2, y2

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(200, 50, 250, 100) # x1, y1, x2, y2

    c1.draw_move(c2)

    win.wait_for_close()

if __name__ == "__main__":
    main()