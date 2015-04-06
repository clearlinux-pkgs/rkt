#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rkt
Version  : 0.5.5
Release  : 17
URL      : https://github.com/coreos/rkt/archive/v0.5.5.tar.gz
Source0  : https://github.com/coreos/rkt/archive/v0.5.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT
Requires: rkt-bin
Requires: rkt-config
Requires: rkt-data
BuildRequires : /usr/bin/ldd
BuildRequires : automake
BuildRequires : glibc-staticdev
BuildRequires : gnupg
BuildRequires : go
BuildRequires : gperf
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libcap-dev
BuildRequires : libgcrypt-dev
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : linux-container
BuildRequires : linux-container-lkvm
BuildRequires : m4
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : systemd-dev
BuildRequires : util-linux-bin
Patch1: build.patch
Patch2: fix-usr-build.patch
Patch3: 0001-Implement-kvm-containment-in-stage1.patch
Patch4: 0002-Add-p9-read-write-mounts-for-volumes.patch
Patch5: 0003-Update-go-systemd-unit-dependency.patch
Patch6: 0004-Mount-plan9-mounts-inside-the-guest.patch
Patch7: 0005-Switch-to-uncompressed-kernel.patch
Patch8: 0006-Use-our-ld.so-and-our-libraries.-lsof-output-will-be.patch
Patch9: 0007-Run-lkvm-in-debug-mode-when-debugging-is-requested.patch

%description
This directory tree is generated automatically by godep.
Please do not edit.
See https://github.com/tools/godep for more information.

%package bin
Summary: bin components for the rkt package.
Group: Binaries
Requires: rkt-data
Requires: rkt-config

%description bin
bin components for the rkt package.


%package config
Summary: config components for the rkt package.
Group: Default

%description config
config components for the rkt package.


%package data
Summary: data components for the rkt package.
Group: Data

%description data
data components for the rkt package.


%prep
%setup -q -n rkt-0.5.5
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/actool
/usr/bin/rkt
/usr/bin/stage1.aci

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/rkt-metadata.service
/usr/lib/systemd/system/rkt-metadata.socket

%files data
%defattr(-,root,root,-)
/usr/share/rkt/bridge
/usr/share/rkt/gc
/usr/share/rkt/host-local
/usr/share/rkt/init
/usr/share/rkt/macvlan
/usr/share/rkt/veth