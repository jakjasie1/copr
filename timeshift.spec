Name:           timeshift
Version:        25.07.5
Release:        1%{?dist}
Summary:        System restore tool for Linux
Group:          Archiving/Backup
License:        GPLv3+
URL:            https://github.com/linuxmint/timeshift
Source0:        https://github.com/linuxmint/timeshift/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  help2man
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(xapp)
BuildRequires:  vala

Requires:       cronie
Requires:       hicolor-icon-theme
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

%build
%meson -Dxapp=false
%meson_build

%install
%meson_install
# Remove duplicate
rm -rf %{buildroot}%{_datadir}/appdata

%find_lang %{name}

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc AUTHORS README.md
%{_bindir}/*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/timeshift-gtk.1.*
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/timeshift-boot
%ghost %attr(644, root, root) %{_sysconfdir}/cron.d/timeshift-hourly
%ghost %attr(664, root, root) %{_sysconfdir}/timeshift.json
%config %{_sysconfdir}/timeshift/default.json


%changelog
* Mon Aug 18 2025 krzysiu
- Update to 25.07.5

* Tue Jun 3 2025 krzysiu
- First release
- Version 24.06.6
