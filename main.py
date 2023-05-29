from Game import Game


def main():
    while True:
        tetris = Game()
        tetris.init_param()
        tetris.run()


if __name__ == '__main__':
    main()
