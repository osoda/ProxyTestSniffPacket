# ProxyTestSniffPacket

# Configuration

Enviroment:
- Window machine whit the software (WM)
    - IP:192.168.0.87
- Linux machine in Virtualbox conect at same network (LVB)
    - IP:192.168.0.11

Execution:
1. (LVB) Run this project in a virtual machine linux
2. (WM) Create spoofing for public ip to capturate through proxy (software). It's do making a red fake like the public ip because we need redirect the trafic to the same pc transforming that ip like loop-back ip (https://serverfault.com/a/1069202). 
    
    2.1. following the tutorial link.. add a ip public software 
    ```
    IP [172.x.x.x] 
    Mascara [255.255.255.255]
    ```
3. (WM) Configurate port forwadding (https://woshub.com/port-forwarding-in-windows/). in order to redirect the trafict to the new loop-back ip [172.x.x.x] to the [(VM)] proxy . Using the next command
    ```
    netsh interface portproxy add v4tov4 listenaddress=172.x.x.x listenport=5555 connectaddress=192.168.0.11 connectport=80
    ```

4. Run the software
