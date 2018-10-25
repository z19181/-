import os
import yaml
import subprocess
def main():
    data = dict()
    with open('D:/TD/peizhi.yaml','r') as f:
        data = yaml.load(f)

    _env = os.environ.copy()
    for i in data['Env']:
        if i['mode'] == 'over':
            _env[i['name']] = i['value']

        elif i['mode'] == 'pre':
            _env[i['name']] = i['value']+';'+ os.environ.get(i['name'],'')

        else:
            pass

        subprocess.call(data['Exec'],env=_env)

main()
