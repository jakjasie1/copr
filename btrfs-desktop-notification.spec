#we are not building, there is nothing to compile. disable debug packages.
%global debug_package %{nil}


Name:           btrfs-desktop-notification
Version:        1.6.1
Release:        1%{?dist}
Summary:   Tool to send notifications when booting into read-only system or when BTRFS warnings/errors appear in kernel log.
License:        GPL-3.0
URL:           https://gitlab.com/Zesko/btrfs-desktop-notification
Source0:        https://gitlab.com/Zesko/btrfs-desktop-notification/-/archive/%{version}/btrfs-desktop-notification-%{version}.tar.gz

BuildRequires: git

Requires:  libnotify
Requires: systemd
Recommends: dunst



%description
BTRFS Desktop notification
It provides desktop notifications for the following events:

Booting into any read-only system or snapshot.
Btrfs warning or error messages appearing in the dmesg log.

%prep
%setup -q

#%build
#No build, this is a simple tar package with some assets.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}/
cp -r screenshots README.md CHANGELOG.md %{buildroot}/usr/share/doc/%{name}/
cp -r usr etc %{buildroot}/

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md

/etc/btrfs-desktop-notification.conf
/etc/xdg/autostart/btrfs-desktop-notification.desktop

/usr/bin/btrfs-desktop-notification
/usr/share/applications/btrfs-desktop-notification.desktop
/usr/share/doc/btrfs-desktop-notification/screenshots/{1,2}.jpg

%changelog
* Mon Mar 2 2026 jakjasie1
- Update to  1.6.1

* Wed Sep 24 2025 jakjasie1
- First release; version 1.3.1
- From the official AUR package
