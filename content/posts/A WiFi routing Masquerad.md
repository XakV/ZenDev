Title: Masquerade of the Wifi Device
Date: 2018-10-30 23:20
Category: Posts
Tags: Linux, Firewall, libvirt
Slug: masquerade-your-wifi
Authors: Zach Villers
Summary: Do not brain this. It hurts. It's the magic config your laptop needs.

### Ever try to run libvirt on your laptop WiFi?

Please untie the noose, it will be ok....I think. The long and short of this is, libvirtd can't use a WiFi device. Which creates pain for me. Setting the wifi device to forward ipv4 and then using firewalld to masquerade packets between the laptop's wifi and ethernet device seems to work.

**Like This**

```
    firewall-cmd --direct --add-rule ipv4 nat POSTROUTING 0 -o wlp3s0 -j MASQUERADE
    firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -i enp0s25 -o wlp3s0 -j accept
    firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -i enp0s25 -o wlp3s0 -j ACCEPT
    firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -i wlp3s0 -o enp0s25 -m state --state RELATED,ESTABLISHED -j ACCEPT
    firewall-cmd --runtime-to-permanent
```

**DONT FORGET TO SET THE IPV4 SYSCTL Tunable**

```
    sysctl -p net.ipv4.blah.blah.thing
```

