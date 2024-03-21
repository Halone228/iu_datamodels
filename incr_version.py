from click import command, option, Choice
from toml import load, dump


@command()
@option(
    '--typo',
    default='patch',
    type=Choice(
        ['major', 'minor', 'patch'],
        case_sensitive=False)
)
def main(typo):
    with open('pyproject.toml', 'r', encoding='utf-8') as f:
        toml = load(f)
    version = toml['tool']['poetry']['version']
    raw_version = version.split('.')
    if typo == 'patch':
        raw_version[2] = str(int(raw_version[2])+1)
    if typo == 'minor':
        raw_version[1] = str(int(raw_version[1])+1)
        raw_version[2] = '0'
    if typo == 'major':
        raw_version[0] = str(int(raw_version[0])+1)
        raw_version[1] = '0'
        raw_version[2] = '0'
    toml['tool']['poetry']['version'] = '.'.join(raw_version)
    with open('pyproject.toml', 'w', encoding='utf-8') as f:
        dump(toml, f)


if __name__ == '__main__':
    main()
