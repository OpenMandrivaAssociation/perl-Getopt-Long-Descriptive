%define upstream_name    Getopt-Long-Descriptive
%define upstream_version 0.093

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.093
Release:    2

Summary:    Getopt::Long with usage text and validation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Getopt/Getopt-Long-Descriptive-0.093.tar.gz

BuildRequires: perl(IO::Scalar)
BuildRequires: perl(List::Util)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel

BuildArch: noarch

%description
Convenient wrapper for Getopt::Long and program usage output

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 672848
- update to new version 0.090

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.89.0-2
+ Revision: 656917
- rebuild for updated spec-helper

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.89.0-1
+ Revision: 634270
- update to new version 0.089

* Thu Dec 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.87.0-1mdv2011.0
+ Revision: 604719
- update to new version 0.087

* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.86.0-1mdv2011.0
+ Revision: 596524
- update to new version 0.086

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.85.0-1mdv2011.0
+ Revision: 519952
- update to 0.085

* Mon Feb 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.84.0-1mdv2010.1
+ Revision: 506239
- update to 0.084

* Sun Dec 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.83.0-1mdv2010.1
+ Revision: 478056
- update to 0.083

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.82.0-1mdv2010.1
+ Revision: 473719
- update to 0.082

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.81.0-1mdv2010.1
+ Revision: 471046
- update to 0.081

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.79.0-1mdv2010.1
+ Revision: 470453
- update to 0.079

* Sat Aug 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.77.0-1mdv2010.0
+ Revision: 419688
- adding missing buildrequires:
- update to 0.077

* Wed Dec 03 2008 Jérôme Quelin <jquelin@mandriva.org> 0.074-1mdv2009.1
+ Revision: 309766
- import perl-Getopt-Long-Descriptive


* Wed Dec 03 2008 cpan2dist 0.074-1mdv
- initial mdv release, generated with cpan2dist


