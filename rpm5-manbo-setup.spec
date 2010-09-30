Summary:	rpm5.org compatibility macros for Manbo
Name:		rpm5-manbo-setup
Version:	2
Release:	%manbo_mkrel 1
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0:	rpm5.org-manbo.macros
Source1:	rpm5.org-manbo-pre.macros
Requires:	rpm-manbo-setup
BuildRequires:	rpm-manbo-setup
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
This package contains manbo compatibility macros for rpm5.org.

%install
rm -rf %{buildroot}
install -m644 %{SOURCE0} -D %{buildroot}%{_sysconfdir}/rpm5/macros.d/90rpm5.org-manbo.macros
install -m644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/rpm5/premacros.d/90rpm5.org-manbo.macros


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/rpm5/macros.d/90rpm5.org-manbo.macros
%{_sysconfdir}/rpm5/premacros.d/90rpm5.org-manbo.macros
