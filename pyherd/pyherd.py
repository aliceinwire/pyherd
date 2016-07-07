#! /usr/bin/python
#
# Copyright(c) 2009 Gentoo Foundation
# Licensed under the GNU General Public License, v2
#
# Copyright: 2013 Alice Ferrazzi <alice.ferrazzi@gmail.com>
# License: GPL2/BSD
#

__version__ = '0.1'

from BeautifulSoup import BeautifulStoneSoup
import argparse
import ConfigParser
import logging
import sys
import os
import subprocess

logging.basicConfig(level=logging.DEBUG)
cwd = os.path.abspath(os.path.dirname(__file__))
rcwd = cwd + "/rsync/"

conf_parser = argparse.ArgumentParser(
    # Turn off help, so we print all options in response to -h
        add_help=False
        )
conf_parser.add_argument("-c", "--conf_file",
                         help="Specify config file", metavar="FILE")
args, remaining_argv = conf_parser.parse_known_args()
defaults = {
    "package" : "mail-client/mutt",
    "portdir" : rcwd,
    "newtree" : False
    }
if args.conf_file:
    config = ConfigParser.SafeConfigParser()
    config.read([args.conf_file])
    defaults = dict(config.items("Defaults"))

# Don't surpress add_help here so it will handle -h
parser = argparse.ArgumentParser(
    # Inherit options from config_parser
    parents=[conf_parser],
    # print script description with -h/--help
    description=__doc__,
    # Don't mess with format of description
    formatter_class=argparse.RawDescriptionHelpFormatter,
    )
parser.set_defaults(**defaults)
parser.add_argument("-package", "--package", help="package name foo/foo")
parser.add_argument("-portdir", "--portdir", help="portage directory")
parser.add_argument("-newtree", "--newtree", action='store_true', help="portage directory")
args = parser.parse_args(remaining_argv)
logging.info(args)

class herd(object):
    def __init__(self):
        if args.newtree:
            cwd = os.path.abspath(os.path.dirname(__file__))
            print cwd
            rcwd = (cwd + "/rsync/")
            if not os.path.isdir(rcwd):
                os.makedirs(rcwd)
            rsync = "rsync -a -v --progress rsync://rsync.jp.gentoo.org/gentoo-portage . --include '*/' --include '**metadata.xml' --include '**herds.xml' --exclude '*' \n"
            conn = subprocess.Popen(rsync, stdout=subprocess.PIPE, shell=True, cwd="" + rcwd + "")
            for line in conn.stdout:
                print line.strip('\n')

        self.pherd = {"accessibility":"accessibility@gentoo.org",
        "ada":"ada@gentoo.org",
        "afterstep":"afterstep@gentoo.org",
        "alpha":"alpha@gentoo.org",
        "alsa":"alsa-bugs@gentoo.org",
        "amd64":"amd64@gentoo.org",
        "antivirus":"antivirus@gentoo.org",
        "app-backup":"app-backup@gentoo.org",
        "app-dicts":"app-dicts@gentoo.org",
        "app-doc":"app-doc@gentoo.org",
        "arm":"arm@gentoo.org",
        "ayatana":"ayatana-bugs@gentoo.org",
        "base-system":"base-system@gentoo.org",
        "bazaar":"bazaar@gentoo.org",
        "benchmarks":"benchmarks@gentoo.org",
        "bsd":"bsd@gentoo.org",
        "chromium":"chromium@gentoo.org",
        "cjk":"cjk@gentoo.org",
        "cluster":"cluster@gentoo.org",
        "common-lisp":"common-lisp@gentoo.org",
        "cpp":"cpp@gentoo.org",
        "cron":"cron-bugs@gentoo.org",
        "crypto":"crypto@gentoo.org",
        "cvs-utils":"cvs-utils@gentoo.org",
        "deb-tools":"deb-tools@gentoo.org",
        "desktop-dock":"desktop-dock@gentoo.org",
        "desktop-effects":"desktop-effects@gentoo.org",
        "desktop-misc":"desktop-misc@gentoo.org",
        "desktop-wm":"desktop-wm@gentoo.org",
        "dev-embedded":"dev-embedded@gentoo.org",
        "dev-tools":"dev-tools@gentoo.org",
        "dotnet":"dotnet@gentoo.org",
        "emacs":"emacs@gentoo.org",
        "embedded":"embedded@gentoo.org",
        "enlightenment":"enlightenment@gentoo.org",
        "fonts":"fonts@gentoo.org",
        "forensics":"forensics@gentoo.org",
        "freedesktop":"freedesktop-bugs@gentoo.org",
        "games":"games@gentoo.org",
        "gdesklets":"gdesklets@gentoo.org",
        "gnome":"gnome@gentoo.org",
        "gnome-accessibility":"gnome-accessibility@gentoo.org",
        "gnome-mm":"gnome-mm@gentoo.org",
        "gnome-office":"gnome-office@gentoo.org",
        "gnustep":"gnustep@gentoo.org",
        "gpe":"gpe@gentoo.org",
        "graphics":"graphics@gentoo.org",
        "gstreamer":"gstreamer@gentoo.org",
        "hardened":"hardened@gentoo.org",
        "haskell":"haskell@gentoo.org",
        "hppa":"hppa@gentoo.org",
        "ia64":"ia64@gentoo.org",
        "java":"java@gentoo.org",
        "kde":"kde@gentoo.org",
        "kerberos":"kerberos@gentoo.org",
        "kernel":"kernel@gentoo.org",
        "kernel-misc":"kernel-misc@gentoo.org",
        "lang-misc":"lang-misc@gentoo.org",
        "ldap":"ldap-bugs@gentoo.org",
        "leechcraft":"leechcraft@gentoo.org",
        "livecd":"livecd@gentoo.org",
        "lxde":"lxde@gentoo.org",
        "media-optical":"media-optical@gentoo.org",
        "media-tv":"media-tv@gentoo.org",
        "mips":"mips@gentoo.org",
        "ml":"ml@gentoo.org",
        "mobile-phone":"mobile-phone@gentoo.org",
        "mozilla":"mozilla@gentoo.org",
        "mysql":"mysql-bugs@gentoo.org",
        "mythtv":"mythtv@gentoo.org",
        "net-dialup":"net-dialup@gentoo.org",
        "net-fs":"net-fs@gentoo.org",
        "net-ftp":"net-ftp@gentoo.org",
        "net-im":"net-im@gentoo.org",
        "net-irc":"net-irc@gentoo.org",
        "net-mail":"net-mail@gentoo.org",
        "net-news":"net-news@gentoo.org",
        "net-p2p":"net-p2p@gentoo.org",
        "net-proxy":"net-proxy@gentoo.org",
        "netmon":"netmon@gentoo.org",
        "nx":"nx@gentoo.org",
        "openoffice":"openoffice@gentoo.org",
        "openrc":"openrc@gentoo.org",
        "pam":"pam-bugs@gentoo.org",
        "pda":"pda@gentoo.org",
        "perl":"perl@gentoo.org",
        "php":"php-bugs@gentoo.org",
        "postgresql":"pgsql-bugs@gentoo.org",
        "ppc":"ppc@gentoo.org",
        "ppc64":"ppc64@gentoo.org",
        "prefix":"prefix@gentoo.org",
        "printing":"printing@gentoo.org",
        "proaudio":"proaudio@gentoo.org",
        "prolog":"prolog@gentoo.org",
        "proxy-maintainers":"proxy-maint@gentoo.org",
        "python":"python@gentoo.org",
        "qemu":"qemu@gentoo.org",
        "qmail":"qmail-bugs@gentoo.org",
        "qt":"qt@gentoo.org",
        "radio":"radio@gentoo.org",
        "rox":"rox@gentoo.org",
        "ruby":"ruby@gentoo.org",
        "s390":"s390@gentoo.org",
        "samba":"samba@gentoo.org",
        "scheme":"scheme@gentoo.org",
        "sci":"sci@gentoo.org",
        "sci-astronomy":"sci-astronomy@gentoo.org",
        "sci-biology":"sci-biology@gentoo.org",
        "sci-chemistry":"sci-chemistry@gentoo.org",
        "sci-electronics":"sci-electronics@gentoo.org",
        "sci-geosciences":"sci-geosciences@gentoo.org",
        "sci-mathematics":"sci-mathematics@gentoo.org",
        "sci-physics":"sci-physics@gentoo.org",
        "selinux":"selinux@gentoo.org",
        "sgml":"sgml@gentoo.org",
        "sh":"sh@gentoo.org",
        "shell-tools":"shell-tools@gentoo.org",
        "sound":"sound@gentoo.org",
        "sparc":"sparc@gentoo.org",
        "suse":"suse@gentoo.org",
        "sysadmin":"sysadmin@gentoo.org",
        "tcltk":"tcltk@gentoo.org",
        "tex":"tex@gentoo.org",
        "theology":"theology@gentoo.org",
        "toolchain":"toolchain@gentoo.org",
        "tools-portage":"tools-portage@gentoo.org",
        "video":"media-video@gentoo.org",
        "vim":"vim@gentoo.org",
        "virtualization":"virtualization@gentoo.org",
        "vmware":"vmware@gentoo.org",
        "voip":"voip@gentoo.org",
        "vserver":"vserver-devs@gentoo.org",
        "web-apps":"web-apps@gentoo.org",
        "wine":"wine@gentoo.org",
        "wxwidgets":"wxwidgets@gentoo.org",
        "x11":"x11@gentoo.org",
        "x11-drivers":"x11-drivers@gentoo.org",
        "x86":"x86@gentoo.org",
        "xbox":"xbox@gentoo.org",
        "xemacs":"xemacs@gentoo.org",
        "xen":"xen@gentoo.org",
        "xfce":"xfce@gentoo.org"}

    def run(self, file):
        soup = self.soup(file)
        try:
            maint = self.maint(soup[1])
        except:
            maint = None
        try:
            herd = self.herd(soup[0])
        except:
            herd = None

        email = self.mail(maint, herd)
        return email

    def list(self):
        return self.pherd

    def soup(self, file):
        try:
            xml = open(file, 'r')
        except:
            sys.exit('we cannot find the package: ' + args.package )
        soup = BeautifulStoneSoup(xml)
        logging.info(soup)
        try:
            hsoup = soup.findAll('herd')
        except:
            hsoup = None
        try:
            msoup = soup.findAll('email')
        except:
            msoup = None
        logging.debug("hsoup: "+ str(hsoup))
        logging.debug("msoup: "+ str(msoup))
        return hsoup, msoup

    def maint(self, msoup):
        q = 0
        mail_number = len(msoup)
        if msoup:
            for i in msoup:
                if q == 0 and len(msoup) > 1:
                    maint = '%s:' % (i.string)
                    logging.debug("maint1: "+ str(maint))
                    q += 1
                elif q == 0 and len(msoup) == 1:
                    maint = '%s:' % (i.string)
                    logging.debug("maint1: "+ str(maint))
                    q += 1
                elif q == 1 or q == len(msoup):
                    maint = '%s%s' % (maint, i.string)
                    logging.debug("maint2: "+ str(maint))
                    q += 1
                else:
                    logging.debug("maint3: "+ str(maint))
                    maint = '%s,%s' % (maint, i.string)
        logging.debug("maint: "+ str(maint))
        print "found " + str(mail_number) + " mail."
        return maint

    def herd(self, hsoup):
        q = 0
        for i in hsoup:
            if i.string in self.pherd.keys():
                if q == 0:
                    herd = self.pherd.get(i.string)
                    q += 1
                else:
                    herd = herd + ',' + self.pherd.get(i.string)
        logging.debug("herd: "+ str(herd))
        return herd

    def mail(self, maint, herd):
        if maint and herd:
            email = maint + '' + herd
        elif maint:
            email = maint
        elif herd:
            email = herd
        else:
            print("this dont have to happen")
        return email

def main():
    import pyherd
    herd = pyherd.herd()
    print herd.run(args.portdir + args.package +'/metadata.xml')

if __name__ == '__main__':
        sys.exit(main())
