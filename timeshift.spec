Name:           timeshift
Version:        25.07.5
Release:        1%{?dist}
Summary:        System restore tool for Linux
Group:          Archiving/Backup
License:        GPLv3+
URL:            https://github.com/linuxmint/timeshift
Source0:        https://github.com/linuxmint/timeshift/archive/refs/tags/25.07.5.tar.gz

BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(xapp)

Requires:       cronie
Requires:       polkit
Requires:       psmisc
Requires:       rsync

%description
Timeshift for Linux is an application that provides functionality similar to
the System Restore feature in Windows and the Time Machine tool in Mac OS.
Timeshift protects your system by taking incremental snapshots of the file
system at regular intervals. These snapshots can be restored at a later date
to undo all changes to the system.

In RSYNC mode, snapshots are taken using rsync and hard-links. Common files
are shared between snapshots which saves disk space. Each snapshot is a full
system backup that can be browsed with a file manager.

In BTRFS mode, snapshots are taken using the in-built features of the BTRFS
filesystem. BTRFS snapshots are supported only on BTRFS systems having an
Ubuntu-type subvolume layout (with @ and @home subvolumes).


%lang_package

%prep
%autosetup -p1
# rpmlint
sed -i -e 's|/usr/bin/env bash|/usr/bin/bash|g' src/timeshift-launcher

%build
%meson -Dxapp=false
%meson_build

%install
%meson_install
#Cleanup rpath references
chrpath --delete %{buildroot}%{_bindir}/timeshift
chrpath --delete %{buildroot}%{_bindir}/timeshift-gtk
#Fix file permissions
chmod 0644 %{buildroot}%{_sysconfdir}/timeshift/default.json
chmod 0644 %{buildroot}%{_datadir}/metainfo/timeshift.appdata.xml
chmod 0644 %{buildroot}%{_datadir}/timeshift/images/*.svg
#Remove as we use rpm/dnf
rm -f %{buildroot}%{_bindir}/timeshift-uninstall
#Remove appdata in preference to metadinfo
rm -rf %{buildroot}%{_datadir}/appdata
#Manually add log directories, set mode to 0750 and owned by root (boo#1165805)
install -d %{buildroot}%{_localstatedir}/log/timeshift
install -d %{buildroot}%{_localstatedir}/log/timeshift-btrfs
#%%suse_update_desktop_file -r timeshift-gtk Utility Archiving
%find_lang %{name} %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%license LICENSES/*
%dir %{_sysconfdir}/timeshift
%config(noreplace) %{_sysconfdir}/timeshift/default.json
%{_bindir}/timeshift*
%{_datadir}/applications/timeshift-gtk.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/timeshift.1%{?ext_man}
%{_mandir}/man1/timeshift-gtk.1%{?ext_man}
%{_datadir}/metainfo/timeshift.appdata.xml
%{_datadir}/polkit-1/actions/in.teejeetech.pkexec.timeshift.policy
%{_datadir}/pixmaps/timeshift.png
%{_datadir}/timeshift/
%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift
%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift-btrfs

%files lang -f %{name}.lang



%changelog
* Mon Aug 18 2025 krzysiu
- Update to 25.07.5

* Tue Jun 3 2025 krzysiu
- First release
- Version 24.06.6
