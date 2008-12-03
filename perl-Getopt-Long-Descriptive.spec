
%define realname   Getopt-Long-Descriptive
%define version    0.074
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Getopt::Long with usage text and validation
Source:     http://www.cpan.org/modules/by-module/Getopt/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(List::Util)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
Convenient wrapper for Getopt::Long and program usage output





%prep
%setup -q -n %{realname}-%{version} 

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


