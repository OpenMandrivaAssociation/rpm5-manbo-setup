Summary:	rpm5.org compatibility macros for Manbo
Name:		rpm5-manbo-setup
Version:	1
Release:	%manbo_mkrel 1
License:	GPL
Group:		System/Configuration/Packaging
Source0:	rpm5.org-manbo.macros
Source1:	convertrpmrc-optflags.sh
Requires:	rpm-manbo-setup
BuildRequires:	rpm-manbo-setup
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
This package contains manbo compatibility macros for rpm5.org.

%install
rm -rf %{buildroot}
install -m644 %{SOURCE0} -D %{buildroot}%{_sysconfdir}/rpm/macros.d/90rpm5.org-manbo.macros
install -m755 %{SOURCE1} -D %{buildroot}%{_prefix}/lib/rpm/manbo/convertrpmrc-optflags.sh
mkdir -p %{buildroot}%{_prefix}/lib/rpm/mandriva
%{buildroot}%{_prefix}/lib/rpm/manbo/convertrpmrc-optflags.sh \
	%{_prefix}/lib/rpm/manbo/rpmrc \
	%{buildroot}%{_prefix}/lib/rpm/mandriva

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/rpm/macros.d/90rpm5.org-manbo.macros
%{_prefix}/lib/rpm/manbo/convertrpmrc-optflags.sh
%dir %{_prefix}/lib/rpm/mandriva/*/
%{_prefix}/lib/rpm/mandriva/*/*

