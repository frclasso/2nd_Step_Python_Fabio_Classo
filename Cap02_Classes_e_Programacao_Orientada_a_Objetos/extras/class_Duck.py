#!/usr/bin/env python3


class Duck:
    sound = "Quaaaaaaaack!!"
    movement = "Walking like a duck!"

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)


def main():
    donald = Duck()
    donald.quack()
    donald.move()


if __name__ == "__main__":main()