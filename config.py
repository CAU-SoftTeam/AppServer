import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--database_user', type=str, default='root', help='name of database user')
parser.add_argument('--database_password', type=str, default='1234', help='password of database')
parser.add_argument('--database', type=str, default='userData', help='name of database')
parser.add_argument('--charset', type=str, default='utf8', help='type of character encode/decode on database')

def get_config():
    return parser.parse_args()
