import argparse
import sys

#
# def run():
#     if not hasattr(args, "name"):
#         print("Hello World")
#     elif not args.name:
#         print("Hello World")
#     else:
#         print(f"Hello {args.name}")
#
#
# def parse_args(args):
#     global_parser = argparse.ArgumentParser(
#         prog="klickbrick",
#         description="Some ClI app",
#         epilog="Thanks for using %(prog)s!"
#     )
#
#     subparsers = global_parser.add_subparsers(
#         title="subcommands", help="arithmetic operations"
#     )
#
#     name_parser = subparsers.add_parser("hello", help="say hello to somebody")
#     name_parser.add_argument("-n", "--name", help="User name")
#     name_parser.set_defaults(func=run)
#
#     return global_parser.parse_args(args)
#
#
# args = parse_args(sys.argv[1:])


def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument('hello',
                        type=str,
                        help="Friendly command that says hello")
    parser.add_argument('--name',
                        '-n',
                        type=str,
                        default="world",
                        help="Optional flag to be more personal")
    return parser.parse_args(args)


def construct_greeting(message, name):
    return f"{message} {name}"


def main():
    args = parse_args(sys.argv[1:])

    if args.hello == "hello":
        print(construct_greeting(args.hello, args.name))


if __name__ == '__main__':
    main()
