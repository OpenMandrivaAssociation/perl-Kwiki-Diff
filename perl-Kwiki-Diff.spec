%define upstream_name	 Kwiki-Diff
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Display differences between the current wiki page and older revisions
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 403377
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-6mdv2009.0
+ Revision: 241585
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-4mdv2008.0
+ Revision: 86516
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-3mdv2007.0
- Rebuild

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Fri Nov 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdk
- New release 0.03
- %%mkrel
- make test in %%check

* Mon Apr 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdk 
- first mandriva release

