#!/usr/bin/env python3

import sys


def hello(who: str = 'world'):
    return f'Hello {who}! Hi!'


if __name__ == '__main__':
    print(hello())
