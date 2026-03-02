Name:           timeshift
Version:       25.12.4
Release:        1%{?dist}
Summary:        System restore tool for Linux
License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/timeshift
Source0:        https://github.com/linuxmint/timeshift/archive/refs/tags/%{version}.tar.gz

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

%prep
%autosetup -p1
# rpmlint
sed -i -e 's|/usr/bin/env bash|/usr/bin/bash|g' src/timeshift-launcher

%build
%meson -Dxapp=false
%meson_build

%install
%meson_install

# Remove duplicate
rm -rf %{buildroot}%{_datadir}/appdata

%find_lang %{name}


#Fix file permissions
chmod 0644 %{buildroot}%{_sysconfdir}/timeshift/default.json
chmod 0644 %{buildroot}%{_datadir}/timeshift/images/*.svg
#Remove as we use rpm/dnf
rm -f %{buildroot}%{_bindir}/timeshift-uninstall

#Manually add log directories, set mode to 0750 and owned by root
install -d %{buildroot}%{_localstatedir}/log/timeshift
install -d %{buildroot}%{_localstatedir}/log/timeshift-btrfs


%files -f %{name}.lang
%license LICENSES/*
%doc AUTHORS README.md
%{_bindir}/*
%{_metainfodir}/*.metainfo.xml
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-gtk.1.*
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/default.json
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/%{name}-boot
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/%{name}-hourly
%ghost %attr(664, root, root) %{_sysconfdir}/%{name}.json

%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift
%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift-btrfs


%changelog
* Mon Mar 2 2026 jakjasie1
- Update to 25.12.4

* Sat Sep 13 2025 jakjasie1
- Update to 25.07.7 patch

* Mon Aug 18 2025 jakjasie1
- Update to 25.07.5

* Tue Jun 3 2025 jakjasie1
- First release
- Version 24.06.6
