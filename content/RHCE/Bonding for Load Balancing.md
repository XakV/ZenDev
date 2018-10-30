Title: Bonding for Load Balancing
Date: 2018-06-12 14:37:01
Category: RHCE
Tags: Networking
Slug: network-teaming
Authors: Zach Villers
Summary: How to set up a load balancing network interface bond
---

## I can't really claim to have a need for a load balancer at home, but...

Why should that stop us? My server was recovered from the ancient history section of Craigslist, but with a fresh install of [CentOS 7](www.centos.org) it gets the few jobs done I ask of it;

- DNS server for my LAN
- iSCSI share for backing up hosts
- Serving up a CentOS repo for VMs to use
- Hosting a webpage that is accessible only on our LAN

I had a two port 100G ethernet card stuck in it from a while back, which for a few days, helped it server as router connected only to an Rpi. Setting up a network bond device is easy and provides load balancing and failover. (It also is good practice for the RHCE exam)

## For this small project, the nmtui cli tool works well enough for me.

```sh
	yum -y install NetworkManager-tui
```

I only had one port left in the little switch near my server, so I used just two of the three interfaces available. We will create a new *bond* device, add two physical devices as "slaves" (seems like we could find a better word for that?), and then tell NetworkManager to apply the load-balancing configuration. I didn't want to spend a ton of time writing this, so I've cheated a bit and taken screenshots after.

This is nmtui;

![nmtui](/nmtui.png)

First, we will add a device;

![add interface](/addinterface.png)

In the interface screen, we'll create a bond;

![create a bond](/bondcreate.png)

To add the physical devices, we need to add "slaves";

![add slave](/addslave.png)

Once you have added the slave devices, tell NetworkManager how you want the bonded device to behave. In this case we'll choose "Adaptive LoadBalance".

![load balancing](/loadbalancing.png)

Finally, activate the connection. **Reminder, be sure you have physical access to the machine or can reboot it without a terminal if necessary.**

![activate](/activate.png)

![activate bond](/activatebond.png)

That's it folks...load balancing over a bonded pair of network devices.



