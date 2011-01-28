#
# spec file for package supportutils-plugin-updater (Version 1.0-13)
#
# Copyright (C) 2011 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-updater
URL:          https://code.google.com/p/supportutils-plugin-updater/
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      1.0
Release:      13
Source:       %{name}-%{version}.tar.gz
Summary:      Supportutils Auto Update Client
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     bash
Requires:     wget
Requires:     grep
Requires:     coreutils

%description
Automatically downloads and updates the supportutils and supporting
supportutils plugin packages for detailed troubleshooting.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-updater/issues/list

Authors:
--------
    Jason Record <jrecord@novell.com>

%prep
%setup -q
%build
gzip -9f updateSupportutils.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0544 updateSupportutils $RPM_BUILD_ROOT/sbin/updateSupportutils
install -m 0644 updateSupportutils.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/updateSupportutils.8.gz

%post
echo
echo "Now run updateSupportutils"
echo

%files
%defattr(-,root,root)
/sbin/updateSupportutils
/usr/share/man/man8/updateSupportutils.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-updater

