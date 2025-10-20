#nothing to build
%global debug_package %{nil}


Name:          nanofetch
Version:        1.0.0
Release:        1%{?dist}
Summary:      A lightweight system information tool written in C++.
License:        MIT
URL:           https://github.com/tinyopsec/nanofetch
Source0:    https://github.com/tinyopsec/nanofetch/archive/refs/heads/main.tar.gz

Requires:  glibc
BuildRequires: gcc

%description
A blazing-fast, highly customizable system info tool. Faster than neofetch, with extensive theming support. Display your system stats in style with endless customization options for colors, layout, and ASCII art. Perfect for Unix-like systems.

%prep
mv %{_sourcedir}/nanofetch-main.tar.gz %{_sourcedir}/main.tar.gz
%autosetup -n nanofetch-main

%build
g++ nanofetch/nanofetch-v0.1/nanofetch.cpp -O2 -o nanofetch-bin




%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

install -m 0755 nanofetch-bin %{buildroot}%{_bindir}/nanofetch
install -m 0755 nanofetch/nanofetch-v0.1/options.txt  %{buildroot}%{_datadir}/%{name}/options.txt
install -m 0755 nanofetch/nanofetch-v0.1/config.txt  %{buildroot}%{_datadir}/%{name}/config.txt
install -m 0755 nanofetch/nanofetch-v0.1/settings.txt %{buildroot}%{_datadir}/%{name}/settings.txt
install -m 0755 nanofetch/nanofetch-v0.1/logo.txt  %{buildroot}%{_datadir}/%{name}/logo.txt


%files
%license LICENSE
%{_bindir}/%{?name}
%{_datadir}/%{name}/options.txt
%{_datadir}/%{name}/config.txt
%{_datadir}/%{name}/settings.txt
%{_datadir}/%{name}/logo.txt
%changelog
* Mon Oct 20 2025  jakjasie1  - 1.3.0-1
- Initial RPM package



