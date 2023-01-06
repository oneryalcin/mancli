import argparse
import sys


def parse_args(args):
    global_parser = argparse.ArgumentParser()
    subparsers = global_parser.add_subparsers(
        title="subcommands", help="Subcommand help"
    )

    # create the parser for the "hello" command
    hello = subparsers.add_parser('hello', help="Friendly command that says hello")
    hello.add_argument('--name', '-n', type=str, default="world", help="Optional flag to be more personal")

    return global_parser.parse_args()


def construct_greeting(name):
    return f"Hello {name}"


def main():
    args = parse_args(sys.argv[1:])

    if hasattr(args, "name"):
        print(construct_greeting(args.name))


if __name__ == '__main__':
    main()
