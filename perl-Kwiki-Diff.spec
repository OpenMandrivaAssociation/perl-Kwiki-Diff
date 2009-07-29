%define upstream_name	 Kwiki-Diff
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Display differences between the current wiki page and older revisions
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Kwiki)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module requires that you be using Kwiki::Revisions. Please make sure
Kwiki::Revisions is in your plugins file.

This module adds a toolbar item, "Differences," when viewing past revisions of
wiki pages. When clicked, the user is shown a colorful side-by-side comparison
of that revision and the current revision.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm -f t/0-signature.t # debug files make it fails

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*
