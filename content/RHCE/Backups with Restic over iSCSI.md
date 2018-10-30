Title: Backup to an iSCSI share using Restic
Date: 2018-10-16 23:20
Category: RHCE
Tags: Restic, Backups, iSCSI
Slug: restic-via-iscsi
Authors: Zach Villers
Summary: Backup to an iSCSI share using Restic
---

# Backing up with Restic over iscsi:

## You do have backups, don't you?

Everyone has pictures, videos, books, life memories, documents, etc, that are irreplaceable. Baby's first steps, wedding videos, memories of  that
time you went to that place and did the thing. You want these to stay with you, right? Whether production or personal, you NEED backups of your
data.

## Why iscsi? What's restic?

I know I need a good, simple backup system. I've tried a few, but wasn't really happy with any of them, either the set-up was painful, or the
tooling was painful to use. I first learned about Restic from this [Fedora Magazine](https://fedoramagazine.org/use-restic-encrypted-backups/) article. Reading the Restic [docs](https://restic.readthedocs.io)_ you get lots of choices for storage backends, simple cli tools for scripting,
and an easy install. An ideal of the unix tradition is mixing and matching single-purpose tools to create useful systems and Restic lends itself well to this purpose. 

Using iscsi with Restic isn't necessary, in fact, since the machines I am using on my LAN have ssh access to each other, iscsi is just extra complexity. It's the first thing I thought of as a project, and it is working quite well, so I plan to stick with it. Linux iscsi tools allow you to share storage from one or more machines over the network. If you are familiar with a NAS (Network Attached Storage), this is similar, but different. 
My basic understanding is that with a NAS unit, you are exposing an appliance with storage and a file system over your LAN. Linux iscsi tooling creates a SAN (Storage Area Network) that exposes block devices to properly configured clients. The iscsi client is called an "initiator", while the server is called a "target." Why target/initiator? Ummm...good question.

-----------

## Ok, how do you do that? Part 1 - iscsi target

The iscsi "target" or server needs a CLI tool named **targetcli**. On CentOS 7, this is a simple yum command.

```sh
        yum -y install targetcli
```

Using targetcli is mostly straightforward, thanks to good examples in the man page and tab completion. The basic idea is as follows;

**Create or configure storage to share.** This can be an actual block device/partition/LVM or a large file backstore *think of a swap file, but for storage, not swap space*.

   ```sh
   [root@target-server ~]# targetcli
			   targetcli shell version 2.1.fb46
			   Copyright 2011-2013 by Datera, Inc and others.
			   For help on commands, type 'help'.
			   /> backstores/block/ create block1 /dev/vg/lv_iscsi
   ```

**Create a name for your share.** The name follows a sort of reverse DNS scheme, starting with the letters "iqn", and ending with a target name.

   ```sh
   /> iscsi/ create iqn.2018-06.local.target-server:target1
   
   Created target iqn.2018-06.local.target-server:target1.
   Created TPG 1.
   Global pref auto_add_default_portal=true
   Created default portal listening on all IPs (0.0.0.0), port 3260.
   ```

   In this case, I am using *.local* as the lan domain and *.target-server* as the machine name. The target name you want to create must be
   separated by a colon *":"*. The first two steps result in a "target portal group", abbreviated "TPG". The target/server offers a portal to connect to backstore.

**Create a LUN (logical unit number) for the named store under the new `iscsi/iqn.2018-06.local.target-server:target1/tpg1` directory.**

   ```sh
   /> cd iscsi/iqn.2018-06.local.target-server:target1/tpg1
   /iscsi/iqn.2018-06.local.target-server:target1/tpg1> luns/ create /backstores/block/block1
   ```

**Set up access for the initiator/client, known as an  ACL for the logical storage unit/**

   ```sh
   /iscsi/iqn.2018-06.local.target-server:target1/tpg1> acls/ create iqn.2018-06.local.target-server:client
   ```
 
  You can set a password for the share (I didn't). Make sure to copy the acl you've just created, this goes in your initiatorname.iscsi config file on the client. As always, `systemd enable --now target` will enable the target shares on reboot.

**Remember to open the appropriate firewall port (3260/tcp)**

   ```sh
   firewall-cmd --add-port=3260/tcp --permanent && firewall-cmd --runtime-to-permanent
   ```

-----------

## Ok, how do you do that? Part 2 - iscsi initiator

Moving to the client (aka initiator), we also need to install a bit of tooling.

```sh
       yum -y install iscsi-initiator-utils
```

This provides the `iscsiadm` command, which must be run as root or with sudo. There are three steps to connect to the shared storage on the server;

**Configure the initiatorname in `/etc/iscsi/initiatorname.iscsi`**

   ```sh
   [root@client.local]$ echo 'InitiatorName=iqn.2018-06.local.target-server:client' >> /etc/iscsi/initiatorname.iscsi
   ```

**Add the target server to the iscsi discovery database.**

   ```sh
   [root@client.local]$ iscsiadm --mode discovery --type sendtargets --portal 0.0.0.0
   ```

   *NOTE: instead of 0.0.0.0 - use the actual IP of the server.*

**Login to the target.**

   ```sh
   [root@client.local]$ iscsiadm --mode node --name iqn.2018-06.local.target-server:target1 --portal 0.0.0.0 --login
   ```

  After a successful login, you can mount the storage wherever you like and create a filesystem on it.

-------------

## Ok, how do you do that? Part 3 - Restic

Restic is easily installed, see the docs [here](https://restic.readthedocs.io/en/stable/020_installation.html) for distro/os specific 
directions. I am using the iscsi share I have mounted at /opt/Backups and again, following the docs by restic, you will;

* Initialize a "repo" for backups
* Create your first backup
* Learn how to check and restore from your backups

The final step I took is to schedule backups with cron (or a systemd timer), which I have done in my Ansible role for restic.

## And now to Ansiblize it

Since Ansible isn't the primary focus of this series, I will just link to my ansible repo [here](https://github.com/AffableZonkey/ChongoChingi.git). Hopefully this helps you get started with iscsi and restic. Feedback is appreciated!

