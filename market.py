import argparse
from app import run_service, init_config


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('market_type', nargs='?', help='set market type (emart: 1, lotte:2, homeplus: 3)')
    parser.add_argument('market_name', nargs='?', help='search market name')
    args = parser.parse_args()
    print(args)

    if args.market_type is None:
        print("error!!")
        exit(1)

    init_config()
    run_service(args.market_type, args.market_name)

