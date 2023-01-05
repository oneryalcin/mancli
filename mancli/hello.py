import argparse


def run():
    if not hasattr(args, "name"):
        print("Hello World")
    elif not args.name:
        print("Hello World")
    else:
        print(f"Hello {args.name}")


global_parser = argparse.ArgumentParser(
    prog="klickbrick",
    description="Some ClI app",
    epilog="Thanks for using %(prog)s!"
)

subparsers = global_parser.add_subparsers(
    title="subcommands", help="arithmetic operations"
)

name_parser = subparsers.add_parser("hello", help="say hello to somebody")
name_parser.add_argument("-n", "--name", help="User name")
name_parser.set_defaults(func=run)

args = global_parser.parse_args()
