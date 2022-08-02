
#!/usr/bin/env python3
import yaml
from tld import get_tld, get_fld
import re
import os
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
    server = args.server

    isExists = os.path.exists("output")
    if not isExists:
        os.mkdir("output")

    with open(inputFile, encoding='utf-8') as f:

        data = yaml.load(f, Loader=yaml.FullLoader)
        items = data.items()

        # print(list(data.items())[0][1])
        servers = []
        serverList = open("output/"+outputFile, "w")

        for i in range(0, len(list(data.items())[0][1])):
            for item in data.items():

                url = item[1][i]['server']

                if isIP(url):
                    break

                if args.verbose:
                    print(url + " tld is " + get_fld(url, fix_protocol=True))

                servers.append(get_fld(url, fix_protocol=True))

        new_list = list(set(servers))

        for i in range(0, len(new_list)):
            if args.list:
                serverList.writelines(new_list[i]+"\n")
            elif args.clash:
                serverList.writelines(
                    " - DOMAIN-SUFFIX," + new_list[i] + ",DIRECT" + "\n")
            elif args.mosdns:
                serverList.writelines(
                    "domain:" + new_list[i] + "\n")

            else:
                serverList.writelines("[/" + new_list[i] + "/]"+DNS+"\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='提取 clash proxy provider 的服务器域名，转换为用于 AdGuardHome 指定为特定域名的上游服务器列表等')
    parser.add_argument('-i', '--inputFile', type=str)
    parser.add_argument('-o', '--outputFile', type=str,
                        default='serverlist.txt', help="default='serverlist.txt'")
    parser.add_argument('-s', '--server', type=str,
                        default='https://dns.cloudflare.com/dns-query',
                        help="specify DNS server, default='https://dns.cloudflare.com/dns-query'"
                        )
    parser.add_argument("--list", help="server list only",
                        action="store_true")
    parser.add_argument("--clash", help="convert to clash rule",
                        action="store_true")
    parser.add_argument("--mosdns", help="convert to mosdns rule",
                        action="store_true")
    parser.add_argument("--verbose", help="verbose",
                        action="store_true")
    args = parser.parse_args()
    main(args)
