import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="MoloneyScript",
        description="A compiled language, not just for scripting (misleading I know)",
        epilog="Brought to you by OLIVER MOLONEY!"
    )
    parser.add_argument('script')
    # TODO: Add in relevant arguments.

    parser.parse_args()

if __name__ == "__main__":
    main()
