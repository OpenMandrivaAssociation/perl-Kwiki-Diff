%define module	Kwiki-Diff
%define name	perl-%{module}
%define version 0.03
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Display differences between the current wiki page and older revisions
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
License:	GPL
Group:		Development/Perl
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Kwiki)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module requires that you be using Kwiki::Revisions. Please make sure
Kwiki::Revisions is in your plugins file.

This module adds a toolbar item, "Differences," when viewing past revisions of
wiki pages. When clicked, the user is shown a colorful side-by-side comparison
of that revision and the current revision.

%prep
%setup -q -n %{module}-%{version}
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

