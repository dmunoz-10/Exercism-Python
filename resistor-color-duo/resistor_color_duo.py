def value(colors):
    COLORS = ["black", "brown", "red", "orange", "yellow",
              "green", "blue", "violet", "grey", "white"]

    return int("{}{}".format(COLORS.index(colors[0]), COLORS.index(colors[1])))
