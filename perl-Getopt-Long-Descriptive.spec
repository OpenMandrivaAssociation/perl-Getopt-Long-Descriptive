%define upstream_name    Getopt-Long-Descriptive
%define upstream_version 0.097

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Getopt::Long with usage text and validation

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Getopt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Scalar)
BuildRequires: perl(Test::Warnings)
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
%{perl_vendorlib}/*



