Title: RHCE - Getting Started
Date: 2018-05-30 22:40:37
Category: RHCE
Tags: RHCE, Projects
Slug: RHCE-begin
Authors: Zach Villers
Summary: Beginning to Study for the RHCE
---

# RHCE Project Based Study

## Q. How do you study for a big test?

Do you read, take notes, and highlight? Do you practice all the exercises until they are second nature? Do you work by yourself or with a group?
Are you making flash cards right now? Those are all valid strategies for passing a test. If they work for you, great! Some of this works for me, 
if I read on a subject and write down a few notes, it's likely I will retain a good bit of the information. If the test is multiple-choice, essay style, I have a pretty good chance at passing. 

### What about a practical exam?

As someone who has trained in martial arts for several years, I've come to understand that an exam is a demonstration of understanding,
an exhibition of intent and interest. There is a big difference between someone who has memorized a set of techniques and a student who 
has examined, researched, and internalized concepts.

In every book and cert class I have taken, the requirements to pass the exam have been expertly covered in as much depth as possible in
the allotted time. It's a proper review of the concepts and application, however, the perfect world lab that you begin with generally lacks
two things;

1. Guidance on how to understand a thing that is broken and fix it in a time-pressured situation.
2. An honest assessment of your engagement with the tools your are being tested on. 

*The first time I was faced with a practical exam, sitting for the RHCSA, I failed because I studied for the exam, instead of learning the technology and how it is used.*

### A. Develop the ability to use and create meaningful tools with the subject matter being tested.

In one sense, I am studying for the Red Hat Certified Engineer exam. In another, I am developing my ability to act like, think as, and be an
engineer. I may be able to *study* for the first one, but without application, the knowledge will be quickly lost. Accordingly, I will be 
studying for this RHCE exam by creating, using, and maintaining the following projects;

| Project                                                    | Purpose                                | Objective                                  |
| :--------------------------                                | :------------------------------------- | :----------------------------------------- |
| [Simple Backups](/project/backups-with-restic-over-iscsi/) | Recovery - Data Safety                 | iscsi target and initiator configuration   |
| Apache Server                                              | CentOS 7 repos for VMs                 | *RHCSA objective* - useful for practice    |
| [Network Bond](/project/bonding-for-load-balancing/)       | "Optimize" network performance         | Configure link aggregation                 |
| LAN DNS server                                             | Speed website loading, host id         | Configure caching only nameserver          |
| Postfix server                                             | email monitoring reports               | Configure a system to send email           |
| ~~Wallabag app~~                                           | Wasn't super happy with this app       | Looking for a replacement atm              |
| LAN System Reports emailed                                 | Keep tabs on hosts                     | Configure System Reports                   |
| SAMBA Media Share                                          | Play Music on various devices          | Mounting Network File Systems              |
|                                                            |                                        | *What else?*                               |

#### What about the objectives I left out?

Good question. You can read up on the RHCE exam objectives at [redhat.com](https://www.redhat.com/en/services/training/ex300-red-hat-certified-engineer-rhce-exam). I will add to this project list in the next few weeks, but I also welcome suggestions from readers. I will post the ansible roles and playbooks I create as well as helpful details and suggestions I find along the way.

