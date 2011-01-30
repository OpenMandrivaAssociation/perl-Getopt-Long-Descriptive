%define upstream_name    Getopt-Long-Descriptive
%define upstream_version 0.089

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Getopt::Long with usage text and validation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Getopt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Scalar)
BuildRequires: perl(List::Util)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
