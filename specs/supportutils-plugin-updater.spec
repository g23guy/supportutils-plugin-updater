#
# spec file for package supportutils-plugin-updater (Version 1.0-20)
#
# Copyright (C) 2011-2013 Novell, Inc.
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
Release:      21
Source:       %{name}-%{version}.tar.gz
Summary:      Supportutils Auto Update Client
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     bash
Requires:     grep
Requires:     coreutils

%description
Automatically downloads and updates the supportutils and supporting
supportutils plugin packages for detailed troubleshooting.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-updater/issues/list

Authors:
--------
    Jason Record <jrecord@suse.com>

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

%changelog
* Wed Apr 3 2013 jrecord@suse.com
- dynamically selects repository

* Mon Mar 25 2013 jrecord@suse.com
- changed to SLE11 SP2 repository

* Wed Sep 05 2012 jrecord@suse.com
- added suse cloud detection

* Thu Feb 16 2012 jrecord@suse.com
-removed wget dependency
-supports curl if wget missing
-added NetIQ Sentinel plugin

* Thu Jun 30 2011 jrecord@suse.com
-fixed network timeout

* Fri Jan 28 2011 jrecord@suse.com
-added message to run updateSupportutils after install

* Thu Dec 21 2010 jrecord@suse.com
-added plugin tags for idm,sentinel,ncs

* Fri Dec 10 2010 jrecord@suse.com
-added -p to exclude plugins
-interface enhancements

* Thu Dec 09 2010 jrecord@suse.com
-fixed longer update RPM version needing updates
-added -u to force RPM updates

* Wed Dec 09 2010 jrecord@suse.com
-initial build

