Name:           risi-tweaks
Version:        0.1
Release:        4%{?dist}
Summary:        risiOS's Tweak Tool

License:        GPL v3
URL:            https://github.com/risiOS/risi-tweaks
Source0:        %{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:  python
Requires:       python
Requires:	python3-gobject, python3-yaml
Requires:	risi-adwaita-recolor

%description
The tweak tool for risiOS. Full alternative to GNOME Tweaks

%prep
%autosetup

%build
%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/risiOS/%{name}/tweaks
mkdir -p %{buildroot}%{_datadir}/applications/

cp %{_builddir}/%{name}-%{version}/%{name}/risi-tweaks %{buildroot}%{_bindir}/%{name}
cp %{_builddir}/%{name}-%{version}/%{name}/__main__.py %{buildroot}%{_libdir}/risiOS/%{name}
cp %{_builddir}/%{name}-%{version}/%{name}/__init__.py %{buildroot}%{_libdir}/risiOS/%{name}
cp %{_builddir}/%{name}-%{version}/%{name}/RtMainWindow.py %{buildroot}%{_libdir}/risiOS/%{name}
cp %{_builddir}/%{name}-%{version}/%{name}/RtBaseWidgets.py %{buildroot}%{_libdir}/risiOS/%{name}
cp %{_builddir}/%{name}-%{version}/%{name}/RtCustomWidgets.py %{buildroot}%{_libdir}/risiOS/%{name}
cp %{_builddir}/%{name}-%{version}/%{name}/RtExtensionWidgets.py %{buildroot}%{_libdir}/risiOS/%{name}
cp %{_builddir}/%{name}-%{version}/%{name}/RtSettingsToWidget.py %{buildroot}%{_libdir}/risiOS/%{name}
cp %{_builddir}/%{name}-%{version}/%{name}/RtUtils.py %{buildroot}%{_libdir}/risiOS/%{name}
cp -r %{_builddir}/%{name}-%{version}/%{name}/tweaks %{buildroot}%{_libdir}/risiOS/%{name}

%files
# %license add-license-file-here
# %doc add-docs-here
%dir %{_libdir}/risiOS/%{name}/
%{_bindir}/%{name}
%{_libdir}/risiOS/%{name}/__main__.py
%{_libdir}/risiOS/%{name}/__init__.py
%{_libdir}/risiOS/%{name}/RtMainWindow.py
%{_libdir}/risiOS/%{name}/RtBaseWidgets.py
%{_libdir}/risiOS/%{name}/RtCustomWidgets.py
%{_libdir}/risiOS/%{name}/RtExtensionWidgets.py
%{_libdir}/risiOS/%{name}/RtSettingsToWidget.py
%{_libdir}/risiOS/%{name}/RtUtils.py
%{_libdir}/risiOS/%{name}/tweaks/*/*

%changelog
* Tue Jul 13 2021 PizzaLovingNerd
- First spec file
