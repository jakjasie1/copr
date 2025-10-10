%global debug_package %{nil}

Name:           selectdefaultapplication
Version:        20210812
Release:        2%{dist}
Summary:     an ugly hack to be able to select default applications in linux in a better way
License:        GPL-2.0-only
URL:         https://github.com/sandsmark/selectdefaultapplication
Source0:     https://github.com/sandsmark/selectdefaultapplication/archive/refs/heads/master.tar.gz

BuildRequires:  qt5-qtbase-devel
BuildRequires: make
Requires:       qt5-qtbase

%description
%{summary}

%prep
%autosetup -n selectdefaultapplication-master

%build
qmake-qt5
%make_build

%install
rm -rf %{buildroot}

# Install the binary
install -Dm0755 selectdefaultapplication \
    %{buildroot}%{_bindir}/selectdefaultapplication

# Install the desktop file
install -Dm0644 selectdefaultapplication.desktop \
    %{buildroot}%{_datadir}/applications/selectdefaultapplication.desktop

install -Dm0644 selectdefaultapplication.png \
   %{buildroot}%{_iconsdir}/hicolor/48x48/apps/selectdefaultapplication.png

%files
%license COPYING
%{_bindir}/selectdefaultapplication
%{_datadir}/applications/selectdefaultapplication.desktop
%{_iconsdir}/hicolor/48x48/apps/selectdefaultapplication.png

%changelog
* Sun Oct 10 2025  jakjasie1  - 20210812-1
- Initial RPM package
- Latest Git release (commit c752df6)
