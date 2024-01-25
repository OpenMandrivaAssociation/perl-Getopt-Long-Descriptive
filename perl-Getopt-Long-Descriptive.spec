%define module Getopt-Long-Descriptive
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	0.114
Release:	1
Summary:	Getopt::Long, but simpler and more powerful
URL:		https://metacpan.org/pod/Getopt::Long::Descriptive
Source:		https://cpan.org/modules/by-module/Getopt/%{module}-%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildRequires:	perl
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
Getopt::Long, but simpler and more powerful

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

# We're currently missing dependencies
# perl(Meta::CPAN::Check)
#check
#make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/*/*
%{_mandir}/man3/*.3pm*
