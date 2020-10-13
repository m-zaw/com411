def climb_ladder(s_r, s_c):
    if (s_r > s_c):
        print("Still some way to go!")
    elif (s_r < s_c):
        print("We are almost there!")

climb_ladder(5, 2)
climb_ladder(2, 5)