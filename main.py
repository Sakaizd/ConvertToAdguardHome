
#!/usr/bin/env python3
import yaml
from tld import get_tld, get_fld
import re
import argparse


def isIP(str):
    p = re.compile(
        '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False


def main(args):

    inputFile = args.inputFile
    outputFile = args.outputFile
    DNS = args.DNS
    with open(inputFile, encoding='utf-8') as f:

        data = yaml.load(f, Loader=yaml.FullLoader)
        items = data.items()

        # print(list(data.items())[0][1])
        servers = []
        serverList = open(outputFile, "w")

        for i in range(0, len(list(data.items())[0][1])):
            for item in data.items():

                url = item[1][i]['server']

                if isIP(url):
                    break

                print(url + " tld is " + get_fld(url, fix_protocol=True))
                servers.append(get_fld(url, fix_protocol=True))

        new_list = list(set(servers))

        for i in range(0, len(new_list)):
            
            serverList.writelines("[/" + new_list[i] + "/]"+DNS+"\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='将 clash proxy provider 的域名转换为用于 AdGuardHome 指定为特定域名的上游服务器列表')
    parser.add_argument('-i', '--inputFile', type=str)
    parser.add_argument('-o', '--outputFile', type=str,
                        default='serverlist.txt')
    parser.add_argument('-d', '--DNS', type=str,
                        default="https://dns.cloudflare.com/dns-query")
    args = parser.parse_args()
    main(args)
