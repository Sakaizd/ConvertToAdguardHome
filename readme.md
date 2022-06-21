# ConvertToAdguardHome

 Use this program to convert the proxies server into a list for AdGuardHome specify upstreams:     

## Results
it converts this:
```
proxies:
  # Shadowsocks
  # The supported ciphers (encryption methods):
  #   aes-128-gcm aes-192-gcm aes-256-gcm
  #   aes-128-cfb aes-192-cfb aes-256-cfb
  #   aes-128-ctr aes-192-ctr aes-256-ctr
  #   rc4-md5 chacha20-ietf xchacha20
  #   chacha20-ietf-poly1305 xchacha20-ietf-poly1305
  - name: "ss1"
    type: ss
    server: ss.server.com
    port: 443
    cipher: chacha20-ietf-poly1305
    password: "password"
    # udp: true

  - name: "ss2"
    type: ss
    server: ss2.server.cn
    port: 443
    cipher: chacha20-ietf-poly1305
    password: "password"
    plugin: obfs
    plugin-opts:
      mode: tls # or http
      # host: bing.com

  - name: "ss3"
    type: ss
    server: ss3.server.hk
    port: 443
    cipher: chacha20-ietf-poly1305
    password: "password"
    plugin: v2ray-plugin
    plugin-opts:
      mode: websocket # no QUIC now
      # tls: true # wss
      # skip-cert-verify: true
      # host: bing.com
      # path: "/"
      # mux: true
      # headers:
      #   custom: value
```
 into

```
[/server.cn/]https://dns.cloudflare.com/dns-query
[/server.hk/]https://dns.cloudflare.com/dns-query
```
or list only:
```
server.com
server.hk
server.cn
```
or clash rule:
```
 - DOMAIN-SUFFIX,server.cn,DIRECT
 - DOMAIN-SUFFIX,server.com,DIRECT
 - DOMAIN-SUFFIX,server.hk,DIRECT
```
# usage
```
pip install requirements.txt
python ./main.py -i test.yaml -o serverlist.txt -d https://dns.cloudflare.com/dns-query
```


```
options:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputFile INPUTFILE
  -o OUTPUTFILE, --outputFile OUTPUTFILE，default='serverlist.txt'
  -d DNS, --DNS DNS     specify DNS server, default='https://dns.cloudflare.com/dns-query'
  --list                server list only
  --clashRule           convert to clash rule
  --verbose             verbose
  
  ```
